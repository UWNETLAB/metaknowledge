"""`Record` is the base of various objects in mk, it is intended to be used with things that have some sort of key-value relationship and is basiclly a hashable python dict. It also has a few extra attributes intead to make debugging and record keeping easier.

+ `bad` cand be set to `True` to indcate something is wrong with the issue being saved in `error` the exact details are left to designer

+ `_sourceFile` and `_sourceLine` store the original file name and line number and are mostly for improving error messages

+ `_id` should be a unique string, that preferably can be used to identify the record from its source, although the latter is not always possible to do so, do your best. It is also what is used for hashing and comparison

+ `_fieldDict` contains the base mapping of keys to values, it is the dictionary


`ExtendedRecord` is what WOSRecord and its ilk inherit from and extends `Record` by adding memoizing and processing of the fields. `ExtendedRecord` cannot be invoked directly as it has many abstract (virtual) methods that define how the tags are to be proccesed what they are called, what encoding to use when writing to disk, etc.
"""

import abc
try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections
import copy

from .mkExceptions import BadRecord

from .WOS.journalAbbreviations.wosCitations import WOSCitation

class Record(collections.abc.Mapping, collections.abc.Hashable):
    """A dictionary with error handling and an id string.

    `Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

    The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

    # Customizations

    `Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

    In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

    # \_\_Init\_\_

    _fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

    # Parameters

    _fieldDict_ : `dict[str:]`

    > A dictionary that maps from strings to values

    _idValue_ : `str`

    > A unique identifier string for the `Record`

    _bad_ : `bool`

    > `True` if there are issues with the `Record`, otherwise `False`

    _error_ : `Exception`

    > The `Exception` that caused whatever error made the record be marked as bad or `None`

    _sFile_ : `str`

    > A string that gives the source file of the original records

    _sLine_ : `int`

    > The first line the original record is found on in the source file
    """

    #This is for the documentation generation, it doesn't do anything on its own
    _documented = ['__hash__', '__eq__', '__str__', '__repr__']

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
        """Gives a hash of the id or if `bad` returns a hash of the fields combined with the error messages, either of these could be blank

        `bad` Records are more likely to cause hash collisions due to their lack of entropy when created.

        # Returns

        `int`

        > A hopefully unique random number
        """
        if self.bad:
            return hash(str(self._fieldDict.values()) + str(self.error))
        else:
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
        """Compares `Records` using their hashes if their hashes are the same then `True` is returned.

        # Parameters

        _other_ : `Record`

        > Another `Record` to be compared against

        # Returns

        `bool`

        > If the `records` are the same then `True` is returned
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.__hash__() == other.__hash__()

    #Other niceties

    def __str__(self):
        """Makes a string with the title of the file as given by self.title, if there is not one it returns "Untitled record"

        # Returns

        `str`

        > The title of the `Record`
        """
        #This is instead of than redefining for the subclasses
        return "{}({})".format(type(self).__name__, self.get('title', self.id))

    def __repr__(self):
        """Makes a string with the id of the file and its type

        # Returns

        `str`

        > The representation of the `Record`
        """
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
            return bytes(''.join(strLst), self.encoding())

    def __getstate__(self):
        #Makes a slightly smaller object than __dict__
        d = self.__dict__.copy()
        #Make copy.copy() produce a shallow copy
        d['_fieldDict'] = d['_fieldDict'].copy()
        return d

    def __setstate__(self, state):
        self.__dict__ = state

    def copy(self):
        """Correctly copies the `Record`

        # Returns

        `Record`

        > A completely decoupled copy of the original
        """
        c = copy.copy(self)
        c._fieldDict = c._fieldDict.copy()
        return c

    #Making these immutable

    @property
    def id(self):
        return self._id

    @property
    def sourceFile(self):
        return self._sourceFile

    @property
    def sourceLine(self):
        return self._sourceLine

class ExtendedRecord(Record, metaclass = abc.ABCMeta):

    #Overwriting the Record attribute
    _documented = ['encoding', 'getAltName', 'specialFuncs', 'tagProccessingFunc', 'writeRecord']

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
                        raise KeyError("'{}' could not be found in the Record".format(key)) from BaseException
                #Both refer to the same object, computedVal
                self._computedFields[key] = computedVal
                alt = self.getAltName(key)
                if alt is not None:
                    self._computedFields[alt] = computedVal
                return computedVal
            else:
                raise TypeError("Keys to Records must be strings they cannot be of the type '{}'.".format(type(key).__name__)) from BaseException

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

    #these need a slight tweak over Record's thanks to `_computedFields`

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
            #No j9 means its probably book so using the books title/leaving blank
            valsLst.append(self.get('title', ''))
        if self.get("volume", False):
            valsLst.append('V' + str(self.get('volume')))
        if self.get("beginningPage", False):
            valsLst.append('P' + str(self.get('beginningPage')))
        if self.get("DOI", False):
            valsLst.append('DOI ' + self.get('DOI'))
        if multiCite and len(auths) > 0:
            return(tuple((WOSCitation(', '.join([a] + valsLst)) for a in auths)))
        elif multiCite:
            return WOSCitation(', '.join(valsLst)),
        else:
            return WOSCitation(', '.join(valsLst))
