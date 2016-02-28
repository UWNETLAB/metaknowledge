import abc
import collections.abc
import copy

from .mkExceptions import BadRecord

from .citation import Citation

class Record(collections.abc.Mapping, collections.abc.Hashable):
    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0):
        #File stuff for debug/error messages
        self._sourceFile = sFile
        self._sourceLine = sLine

        #Error message stuff
        self.bad = bad
        self.error = error

        #Important data
        self._id = idValue
        self._fieldDict = fieldDict

    #collections.abc.Hashable method

    def __hash__(self):
        """returns a hash of the ID or if `bad` returns a hash of the fields combined with the error messages, either of these could be blank

        `bad` Records are more likely to cause hash collisions due to their lack of entropy when created.
        """
        if self.bad:
            return hash(str(self._fieldDict.values()) + str(self.error))
        return hash(self._id)

    #collections.abc.Mapping methods

    def __getitem__(self, key):
        """This is redfined as something interesting for ExtendedRecord"""
        try:
            return self._fieldDict[key]
        except KeyError:
            raise KeyError("'{}' could not be found in the Record".format(key))

    def __iter__(self):
        """Iterates over the tags in the Record"""
        for t in self._fieldDict:
            yield t

    def __len__(self):
        """Returns the number of tags"""
        return len(self._fieldDict)

    def __contains__(self, item):
        """Checks if the tag _item_ is in the Record"""
        return item in self._fieldDict

    def __eq__(self, other):
        """
        returns true if the hashes of both Records are identical.

        if either is bad False is returned
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.__hash__() == other.__hash__()

    #Other niceties

    def __str__(self):
        """returns a string with the title of the file as given by self.title, if there is not one it returns "Untitled record"
        """
        #This is instead of than redefining for the subclasses
        return "{}({})".format(type(self).__name__, self.get('title', self.id))


    def __repr__(self):
        if self.bad:
            return "<metaknowledge.{} object BAD>".format(type(self).__name__)
        else:
            return "<metaknowledge.{} object {}>".format(type(self).__name__, self.id)

    def __bytes__(self):
        """Returns the binary form of the original"""
        if self.bad:
            raise BadRecord("This record cannot be converted to binary as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        else:
            strLst = []
            for tag in self._fieldDict.keys():
                for i, value in enumerate(self._fieldDict[tag]):
                    if i == 0:
                        strLst.append(tag + ' ')
                    else:
                        strLst.append('   ')
                    strLst.append(value + '\n')
            strLst.append("ER\n")
            return bytes(''.join(strLst), self.encoding)

    def __getstate__(self):
        #Makes a slightly smaller object than __dict__
        d = self.__dict__.copy()
        #Make copy.copy() produce a shallow copy
        d['_fieldDict'] = d['_fieldDict'].copy()
        return d

    def __setstate__(self, state):
        self.__dict__ = state

    def copy(self):
        #This is a method of dict and many other builtins
        #So it seems reasonable to included
        return copy.copy(self)

    @property
    def id(self):
        """the ID of the record, not overwritable
        """
        return self._id

class ExtendedRecord(Record, metaclass = abc.ABCMeta):
    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0):
        """Base constructor for Records

        _fieldDict_ : is the unpared entry dict with tags as keys and their lines as a list of strings

        _idValue_ : is the unique ID of the Record, e.g. the WOS number

        _titleKey_ : is the tag giving the title of the Record, e.g. the WOS tag is `'TI'`

        _bad_ : is the bool tto flag the Record as having encountered an errror

        _error_ : is the error that bad indicates

        _sFile_ : is the name of the source file

        _sLine_ : is the line number of the start of the Record entry

        _altNames_ : is a dict that maps the names of tags to an alternative name, i.e. the long names dict. It **must** be bidirectional: map long to short and short to long

        _proccessingFuncs_ : is a dict of functions to proccess the tags. It has the short names as keys and their proccessing fucntions as values. Missing tags will result in the unparsed value to be returned.

        The Records inheting from this must implement, calling the implementations in Record with super() will not cause errors:
        + writeRecord
        + tagProccessingFunc
        + encoding
        + titleTag
        + getAltName
        """
        Record.__init__(self, fieldDict, idValue, bad, error, sFile = sFile, sLine = sLine)

        #Memoizing stuff
        self._computedFields = {}

    def __getitem__(self, key):
        """Proccesses the tag requested with _key_ and memoize it.

        Allows long names, but will still raise a KeyError if the tag is missing, regardless of name used.
        """
        try:
            return self._computedFields[key]
        except KeyError:
            if isinstance(key, str):
                if key in self._fieldDict:
                    computedVal = self.tagProccessingFunc(key)(self._fieldDict[key])
                elif self.getAltName(key) in self._fieldDict:
                    key = self.getAltName(key)
                    computedVal = self.tagProccessingFunc(key)(self._fieldDict[key])
                else:
                    try:
                        computedVal = self.specialFuncs(key)
                    except KeyError:
                        raise KeyError("'{}' could not be found in the Record".format(key)) from None
                #Both refer to the same object, computedVal
                self._computedFields[key] = computedVal
                alt = self.getAltName(key)
                if alt is not None:
                    self._computedFields[alt] = computedVal
                return computedVal
            else:
                raise TypeError("Keys to Records must be strings they cannot be of the type '{}'.".format(type(key).__name__)) from None

    #Extra options added to the defaults to make access to raw data easier

    def get(self, tag, default = None, raw = False):
        """Allows access to the raw values or is wrapper to __getitem__.

        Does not raise KeyError, will just return `None` if _tag_ cannot be found.
        """
        if raw:
            if tag in self._fieldDict:
                return self._fieldDict[tag]
            elif self.getAltName(tag) in self._fieldDict:
                return self._fieldDict[self.getAltName(tag)]
            else:
                return default
        else:
            try:
                return self[tag]
            except KeyError:
                return default

    def values(self, raw = False):
        if raw:
            return self._fieldDict.values()
        else:
            return collections.abc.Mapping.values(self)

    #Keys given by the mixin

    def items(self, raw = False):
        if raw:
            return self._fieldDict.items()
        else:
            return collections.abc.Mapping.items(self)

    #This needs a slight tweak over Record's

    def __getstate__(self):
        #Makes a slightly smaller object than __dict__
        d = self.__dict__.copy()
        d['_computedFields'] = {}
        #Make copy.copy() produce a shallow copy
        d['_fieldDict'] = d['_fieldDict'].copy()
        return d

    #Making the 'virtual' methods

    @abc.abstractmethod
    def writeRecord(self, infile):
        pass

    @property
    @abc.abstractmethod
    def encoding(self):
        return 'utf-8' #Most likely to be the encoding

    @staticmethod
    @abc.abstractmethod
    def getAltName(tag):
        #Should not raise an exception
        return None #Default to Null case

    @staticmethod
    @abc.abstractmethod
    def tagProccessingFunc(tag):
        #Should not raise an exception
        return lambda x: x

    @abc.abstractmethod
    def specialFuncs(self, key):
        raise KeyError("There are no special functions given by default.")

    @property
    def title(self):
        return self.get('title', default = "Untitled record")

    @property
    def authors(self):
        auth = self.get('authorsFull')
        if auth is None:
            return self.get('authorsShort')
        else:
            return auth

    def subDict(self, tags, raw = True):
        """returns a dict of values of _tags_ from the Record. The tags are the keys and the values are the values

        _raw_ can be used to make the the retuned values  unproccesed
        """
        retDict = {}
        for tag in tags:
            retDict[tag] = self.get(tag, raw = raw)
        return retDict

    def createCitation(self, multiCite = False):
        """Creates a citation string, using the same format as other WOS citations, for the [Record](#Record.Record) by reading the relevant tags (`year`, `J9`, `volume`, `beginningPage`, `DOI`) and using it to create a [`Citation`](#Citation.Citation) object.

        # Parameters

        _multiCite_ : `optional [bool]`

        > Default `False`, if `True` a tuple of Citations is returned with each having a different one of the records authors as the author

        # Returns

        `Citation`

        > A [`Citation`](#Citation.Citation) object containing a citation for the Record.
        """
        valsLst = []
        if multiCite:
            auths = []
            for auth in self.get("authorsShort", []):
                auths.append(auth.replace(',', ''))
        else:
            if self.get("authorsShort", False):
                valsLst.append(self['authorsShort'][0].replace(',', ''))
        if self.get("year", False):
            valsLst.append(str(self.get('year')))
        if self.get("j9", False):
            valsLst.append(self.get('j9'))
        elif self.get("title", False):
            #Get no j9 means its a book so using the books title
            valsLst.append(self.get('title'))
        if self.get("volume", False):
            valsLst.append('V' + str(self.get('volume')))
        if self.get("beginningPage", False):
            valsLst.append('P' + str(self.get('beginningPage')))
        if self.get("DOI", False):
            valsLst.append('DOI ' + self.get('DOI'))
        if multiCite and len(auths) > 0:
            return(tuple((Citation(', '.join([a] + valsLst)) for a in auths)))
        elif multiCite:
            return Citation(', '.join(valsLst)),
        else:
            return Citation(', '.join(valsLst))
