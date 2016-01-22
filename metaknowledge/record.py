import abc
import collections.abc

from .mkExceptions import BadRecord

class Record(collections.abc.Mapping, collections.abc.Hashable, metaclass = abc.ABCMeta):
    def __init__(self, fieldDict, idValue, titleKey, bad, error, strEncoding = 'utf-8', sFile = "", sLine = 0, altNames = None, proccessingFuncs = None):
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
        """

        #File stuff for debug/error messages
        self._sourceFile = sFile
        self._sourceLine = sLine

        #Error message stuff
        self.bad = bad
        self.error = error

        #Important data
        self._id = idValue
        self._fieldDict = fieldDict
        self.encoding = strEncoding

        #Memoizing stuff
        #I have done some testing
        #altNames and proccessingFuncs are not usually replicated for each Record
        #This is memory effient
        self._computedFields = {}
        self._altNames = altNames
        if proccessingFuncs is None:
            proccessingFuncs = {}
        self._proccessingFuncs = proccessingFuncs

        #Give it a title
        title = self.get(titleKey)
        if isinstance(title, str):
            self.title = title
        else:
            self.title = "Untitled record"

    #collections.abc.Hashable method

    def __hash__(self):
        """returns a hash of the ID or if `bad` returns a hash of the fields combined with the error messages, either of these could be blank

        `bad` Records are more likely to cause hash collisions due to their lack of entropy when created.
        """
        if self.bad:
            return hash(str(self._fieldDict.values()) + str(self.error))
        return hash(self._id)

    #collections.abc.Mapping methods
    #All but keys() are custom

    def __getitem__(self, key):
        """Proccesses the tag requested with _key_ and memoize it.

        Allows long names, but will still raise a KeyError if the tag is missing, regardless of name used.
        """
        try:
            return self._computedFields[key]
        except KeyError:
            if isinstance(key, str):
                if key in self._fieldDict:
                    computedVal = self._proccessingFuncs.get(key, lambda x : x)(self._fieldDict[key])
                elif self._altNames.get(key) in self._fieldDict:
                    key = self._altNames.get(key)
                    computedVal = self._proccessingFuncs[key](self._fieldDict[key])
                else:
                    raise KeyError("'{}' could not be found in the Record".format(key)) from None
                #Both refer to the same object, computedVal
                self._computedFields[key] = computedVal
                self._computedFields[self._altNames.get(key)] = computedVal
                return computedVal
            else:
                raise TypeError("Keys to Records must be strings they cannot be of the type: {}.".format(type(key)))

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
        if not isinstance(other, Record):
            return NotImplemented
        else:
            return self.__hash__() == other.__hash__()

    def get(self, tag, default = None, raw = False):
        """Allows access to the raw values or is wrapper to __getitem__.

        Does not raise KeyError, will just return `None` if _tag_ cannot be found.
        """
        if raw:
            if tag in self._fieldDict:
                return self._fieldDict[tag]
            elif self._altNames.get(tag) in self._fieldDict:
                return self._fieldDict[self._altNames.get(tag)]
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

    #Other niceties

    def __str__(self):
        """returns a string with the title of the file as given by self.title, if there is not one it returns "Untitled record"
        """
        return "{}({})".format(type(self).__name__, self.title)

    def __repr__(self):
        if self.bad:
            return "< metaknowledge.{} object BAD >".format(type(self).__name__)
        else:
            return "< metaknowledge.{} object {} >".format(type(self).__name__, self.UT)

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
        d['_computedFields'] = []
        return d

    def __setstate__(self, state):
        self.__dict__ = state

    @property
    def id(self):
        """the ID of the record, not overwritable
        """
        return self._id

    @abc.abstractmethod
    def writeRecord(self, infile):
        pass

    def subDict(self, tags, raw = True):
        """returns a dict of values of _tags_ from the Record. The tags are the keys and the values are the values

        _raw_ can be used to make the the retuned values  unproccesed
        """
        retDict = {}
        for tag in tags:
            retDict[tag] = self.get(tag, raw = raw)
        return retDict
