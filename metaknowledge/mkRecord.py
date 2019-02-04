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

from .constants import commonRecordFields

from .mkExceptions import BadRecord

from .genders.nameGender import recordGenders

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
    """A subclass of `Record` that adds processing to the dictionary. It also cannot be use directly and must be subclassed.

    The `ExtendedRecord` class is a extension of `Record` that is intended for use with the records on scientific papers provided by different organizations such as WOS or Pubmed. The 5 abstract (virtual) methods must be defined for each subclass and define how the data in the different fields is processed and how the record can be rewritten to a file.

    # Processing fields

    When an `ExtendedRecord` is created a dictionary, _fieldDict_, must be provided this contains the raw data from the file reader, usually as lists of strings. `tagProcessingFunc` is a `staticmethod` function that takes in a tag string an returns another function to process it.

    Each tag may also be given a second name, as usually what the they are called in the raw data are not very easy to understand (e.g. `'SO'` is the journal name for WOs records). The mapping from the raw tag (`'SO'`) to the human friendly string (`'journal'`)  is done with the `getAltName` `staticmethod`. `getAltName` takes in a tag string and returns either `None` or the other name for that string. Note, `getAltName` must go both directions `WOSRecord.getAltName(WOSRecord.getAltName('SO')) == 'SO'`.

    The last method for processing entries is `specialFuncs` The following are the special keys for `ExtendedRecords`. These must be the alternate names of tags or strings accepted by the `specialFuncs` method.

    + `'authorsFull'`
    + `'keywords'`
    + `'grants'`
    + `'j9'`
    + `'authorsShort'`
    + `'volume'`
    + `'selfCitation'`
    + `'citations'`
    + `'address'`
    + `'abstract'`
    + `'title'`
    + `'month'`
    + `'year'`
    + `'journal'`
    + `'beginningPage'`
    + `'DOI'`

    `specialFuncs` when given one of these must raise a `KeyError` or return an object of the same type as that returned by the `MedlineRecord` or `WOSRecord`. e.g. `'title'` would return a string giving the title of the record.

    For an example of how this works lets first look at the `'SO'` tag on a `WOSRecord` accessed with the alternate name `'journal'`.

        t = R['journal']

    First the private dictionary `_computedFields` is checked for the key `'title'`, which will fail if this is the first time `'journal'` or `'SO'` has been requested, after this the results will be added to the dictionary to speed up future requests.

    Then the _fieldDict_ will be checked for the key and when that fails the key will go through `getAltName` and be checked again. If the record had a journal entry this will succeed and the raw data will be given to the `tagProcessingFunc` using the same key as _fieldDict_, in this case `SO`.

    The results will then be written to `_computedFields` and returned.

    If the requested key was instead `'grants'` (`g = R['grants']`)the both lookups to _fieldDict_ would have failed and the string `'grants'` would have been given to `specialFuncs` which would return a list of all the grants in the `WOSRecord` (this is always `[]` as WOS does not provided grant information).

    What if the key were not present anywhere? Then the `specialFuncs` should raise a `KeyError` which will be caught then re-raised like a dictionary would with an invalid key look up.

    # File Handling fields

    The two other required methods `encoding` and `writeRecord` define how the records can be rewritten to a file. `encoding` is should return a string giving the encoding python would use, e.g. `'utf-8'` or `'latin-1'`. This is the same encoding that the files written by `writeRecord` should have, `writeRecord` when called should write the original record to the provided open file, _infile_. The opening, closing, header and footer of the file will be handled by `RecordCollection`'s `writeFile` function which should me modified accordingly. If the order of the fields in a record is important you can use a [collections.OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) for _fieldDict_.

    # \_\_Init\_\_

    The `__init__` of `ExtendedRecord` takes the same arguments as [Record](./Record.html#metaknowledge.Record)
    """
    #Overwriting the Record attribute
    _documented = ['encoding', 'getAltName', 'specialFuncs', 'tagProcessingFunc', 'writeRecord']

    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0):
        """Base constructor for Records

        _fieldDict_ : is the unpared entry dict with tags as keys and their lines as a list of strings

        _idValue_ : is the unique ID of the Record, e.g. the WOS number

        _titleKey_ : is the tag giving the title of the Record, e.g. the WOS tag is `'TI'`

        _bad_ : is the bool to flag the Record as having encountered an errror

        _error_ : is the error that bad indicates

        _sFile_ : is the name of the source file

        _sLine_ : is the line number of the start of the Record entry

        _altNames_ : is a dict that maps the names of tags to an alternative name, i.e. the long names dict. It **must** be bidirectional: map long to short and short to long

        _proccessingFuncs_ : is a dict of functions to proccess the tags. It has the short names as keys and their proccessing fucntions as values. Missing tags will result in the unparsed value to be returned.

        The Records inheting from this must implement, calling the implementations in Record with super() will not cause errors:
        + writeRecord
        + tagProcessingFunc
        + encoding
        + titleTag
        + getAltName
        """
        Record.__init__(self, fieldDict, idValue, bad, error, sFile = sFile, sLine = sLine)

        #Memoizing stuff
        self._computedFields = {}

    def __contains__(self, item):
        """Checks if the tag _item_ is in the Record"""
        #Check all the dicts
        #They are ordered assuming people are checking fresh Records not ones with full _computedFields
        if item in self._fieldDict or self.getAltName(item) in self._fieldDict or item in self._computedFields:
            return True
        else:
            try:
                computedVal = self.specialFuncs(item)
            except KeyError:
                return False
            self._computedFields[item] = computedVal
            alt = self.getAltName(item)
            if alt is not None:
                self._computedFields[alt] = computedVal
            return True


    def __getitem__(self, key):
        """Processes the tag requested with _key_ and memoize it.

        Allows long names, but will still raise a KeyError if the tag is missing, regardless of name used.
        """
        try:
            return self._computedFields[key]
        except KeyError:
            if isinstance(key, str):
                if key in self._fieldDict:
                    computedVal = self.tagProcessingFunc(key)(self._fieldDict[key])
                elif self.getAltName(key) in self._fieldDict:
                    key = self.getAltName(key)
                    computedVal = self.tagProcessingFunc(key)(self._fieldDict[key])
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
        """Allows access to the raw values or is an Exception safe wrapper to `__getitem__`.

        # Parameters

        _tag_ : `str`

        > The requested tag

        _default_ : `optional [Object]`

        > Default `None`, the object returned when _tag_ is not found

        _raw_ : `optional [bool]`

        > Default `False`, if `True` the unprocessed value of _tag_ is returned

        # Returns

        `Object`

        > The processed value of _tag_ or _default_
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
        """Like `values` for dicts but with a `raw` option

        # Parameters

        _raw_ : `optional [bool]`

        > Default `False`, if `True` the `ValuesView` contains the raw values

        # Returns

        `ValuesView`

        > The values of the record
        """
        if raw:
            return self._fieldDict.values()
        else:
            return collections.abc.Mapping.values(self)

    #Keys given by the mixin

    def items(self, raw = False):
        """Like `items` for dicts but with a `raw` option

        # Parameters

        _raw_ : `optional [bool]`

        > Default `False`, if `True` the `KeysView` contains the raw values as the values

        # Returns

        `KeysView`

        > The key-value pairs of the record
        """
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
        """An `abstractmethod`, writes the record in its original form to _infile_

        # Parameters

        _infile_ : `writable file`

        > The file to be written to
        """
        pass

    @abc.abstractmethod
    def encoding(self):
        """An `abstractmethod`, gives the encoding string of the record.

        # Returns

        `str`

        > The encoding
        """
        return 'utf-8' #Most likely to be the encoding

    @staticmethod
    def getAltName(tag):
        """An `abstractmethod`, gives the alternate name of _tag_ or `None`

        # Parameters

        _tag_ : `str`

        > The requested tag

        # Returns

        `str`

        > The alternate name of _tag_ or `None`
        """
        return None #Default to Null case

    @staticmethod
    @abc.abstractmethod
    def tagProcessingFunc(tag):
        """An `abstractmethod`, gives the function for processing _tag_

        # Parameters

        _tag_ : `optional [str]`

        > The tag in need of processing

        # Returns

        `function`

        > The function to process the raw tag
        """
        #Should not raise an exception
        return lambda x: x

    @abc.abstractmethod
    def specialFuncs(self, key):
        """An `abstractmethod`, process the special tag, _key_ using the whole `Record`

        # Parameters

        _key_ : `str`

        > One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

        # Returns

        > The processed value of _key_
        """
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

    def getCitations(self, field = None, values = None, pandasFriendly = True):
        """Creates a pandas ready dict with each row a different citation and columns containing the original string, year, journal and author's name.

        There are also options to filter the output citations with _field_ and _values_

        # Parameters

        _field_ : `optional str`

        > Default `None`, if given all citations missing the named field will be dropped.

        _values_ : `optional str or list[str]`

        > Default `None`, if _field_ is also given only those citations with one of the strings given in _values_ will be included.

        > e.g. to get only citations from 1990 or 1991: `field = year, values = [1991, 1990]`

        _pandasFriendly_ : `optional bool`

        > Default `True`, if `False` a list of the citations will be returned instead of the more complicated pandas dict

        # Returns

        `dict`

        > A pandas ready dict with all the citations
        """
        retCites = []
        if values is not None:
            if isinstance(values, (str, int, float)) or not isinstance(values, collections.abc.Container):
                values = [values]
        if field is not None:
            for cite in self.get('citations', []):
                try:
                    targetVal = getattr(cite, field)
                    if values is None or targetVal in values:
                        retCites.append(cite)
                except AttributeError:
                    pass
        else:
            retCites = self.get('citations', [])
        if pandasFriendly:
            return _pandasPrep(retCites, False)
        return retCites

    def subDict(self, tags, raw = False):
        """Creates a dict of values of _tags_ from the Record. The tags are the keys and the values are the values. If the tag is missing the value will be `None`.

        # Parameters

        _tags_ : `list[str]`

        > The list of tags requested

        _raw_ : `optional [bool]`

        >default `False` if `True` the retuned values of the dict will be unprocessed

        # Returns

        `dict`

        > A dictionary with the keys _tags_ and the values from the record
        """
        retDict = {}
        for tag in tags:
            retDict[tag] = self.get(tag, raw = raw)
        return retDict

    def createCitation(self, multiCite = False):
        """Creates a citation string, using the same format as other WOS citations, for the [Record](./Record.html#metaknowledge.Record) by reading the relevant special tags (`'year'`, `'J9'`, `'volume'`, `'beginningPage'`, `'DOI'`) and using it to create a [Citation](./Citation.html#metaknowledge.citation.Citation) object.

        # Parameters

        _multiCite_ : `optional [bool]`

        > Default `False`, if `True` a tuple of Citations is returned with each having a different one of the records authors as the author

        # Returns

        `Citation`

        > A [Citation](./Citation.html#metaknowledge.citation.Citation) object containing a citation for the Record.
        """
        #Need to put the import here to avoid circular import issues
        from .citation import Citation
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
            return(tuple((Citation(', '.join([a] + valsLst)) for a in auths)))
        elif multiCite:
            return Citation(', '.join(valsLst)),
        else:
            return Citation(', '.join(valsLst))

    def authGenders(self, countsOnly = False, fractionsMode = False, _countsTuple = False):
        """Creates a dict mapping `'Male'`, `'Female'` and `'Unknown'` to lists of the names of all the authors.

        # Parameters

        _countsOnly_ : `optional bool`

        > Default `False`, if `True` the counts (lengths of the lists) will be given instead of the lists of names

        _fractionsMode_ : `optional bool`

        > Default `False`, if `True` the fraction counts (lengths of the lists divided by the total  number of authors) will be given instead of the lists of names. This supersedes _countsOnly_

        # Returns

        `dict[str:str or int]`

        > The mapping of genders to author's names or counts
        """

        authDict = recordGenders(self)
        if _countsTuple or countsOnly or fractionsMode:
            rawList = list(authDict.values())
            countsList = []
            for k in ('Male','Female','Unknown'):
                countsList.append(rawList.count(k))
            if fractionsMode:
                tot = sum(countsList)
                for i in range(3):
                    countsList.append(countsList.pop(0) / tot)
            if _countsTuple:
                return tuple(countsList)
            else:
                return {'Male' : countsList[0], 'Female' : countsList[1], 'Unknown' : countsList[2]}
        else:
            return authDict

    def bibString(self, maxLength = 1000, WOSMode = False, restrictedOutput = False, niceID = True):
        """Makes a string giving the Record as a bibTex entry. If the Record is of a journal article (`PT J`) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

        **Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier.

        **Note** Record entries that are lists have their values seperated with the string `' and '`

        # Parameters

        _maxLength_ : `optional [int]`

        > default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

        _WOSMode_ : `optional [bool]`

        > default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

        _restrictedOutput_ : `optional [bool]`

        > default `False`, if `True` the tags output will be limited to tose found in `metaknowledge.commonRecordFields`

        _niceID_ : `optional [bool]`

        > default `True`, if `True` the ID used will be derived from the authors, publishing date and title, if `False` it will be the UT tag

        # Returns

        `str`

        > The bibTex string of the Record
        """
        keyEntries = []
        if self.bad:
            raise BadRecord("This record cannot be converted to a bibtex entry as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        if niceID:
            if self.get('authorsFull'):
                bibID = self['authorsFull'][0].title().replace(' ', '').replace(',', '').replace('.','')
            else:
                bibID = ''
            if self.get('year', False):
                bibID += '-' + str(self['year'])
            if self.get('month', False):
                bibID += '-' + str(self['month'])
            if self.get('title', False):
                tiSorted = sorted(self.get('title').split(' '), key = len)
                bibID += '-' + tiSorted.pop().title()
                while len(bibID) < 35 and len(tiSorted) > 0:
                    bibID += '-' + tiSorted.pop().title() #Title Case
            if len(bibID) < 30:
                bibID += str(self.id)
        elif WOSMode:
            bibID = 'ISI:{}'.format(self.id[4:])
        else:
            bibID = str(self.id)
        keyEntries.append("author = {{{{{}}}}},".format(' and '.join(self.get('authorsFull', ['None']))))
        if restrictedOutput:
            tagsIter = ((k, self[k]) for k in commonRecordFields if k in self)
        else:
            tagsIter = self.items()
        if WOSMode:
            for tag, value in tagsIter:
                if isinstance(value, list):
                    keyEntries.append("{} = {{{{{}}}}},".format(tag,'\n   '.join((str(v) for v in value))))
                else:
                    keyEntries.append("{} = {{{{{}}}}},".format(tag, value))
            s = """@{0}{{ {1},\n{2}\n}}""".format('misc', bibID, '\n'.join(keyEntries))
        else:
            for tag, value in tagsIter:
                keyEntries.append("{} = {},".format(tag, _bibFormatter(value, maxLength)))
            s = """@{0}{{ {1},\n    {2}\n}}""".format('misc', bibID, '\n    '.join(keyEntries))
        return s

def _bibFormatter(s, maxLength):
    """Formats a string, list or number to make it good for a bib file by:
        * if too long splits up the string correctly
        * tries to use the best quoting characters
        * expands lists into ' and ' seperated values, as per spec for authors field
    Note, this does not escape characters. LaTeX may have issues with the output
    Max length splitting derived from https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html
    """
    if isinstance(s, list):
        s = ' and '.join((str(v) for v in s))
    elif not isinstance(s, str):
        s = str(s)
    if len(s) > maxLength:
        s = s.replace('"', '')
        s = [s[i * maxLength: (i + 1) * maxLength] for i in range(len(s) // maxLength )]
        s = '"{}"'.format('" # "'.join(s))
    elif '"' not in s:
        s = '"{}"'.format(s)
    else:
        s = s.replace('{', '\\{').replace('}', '\\}')
        s = '{{{}}}'.format(s)
    return s

def _pandasPrep(cites, addcounts):
    mainValues = ['year', 'journal', 'author']
    retDict = {'citeString' : []}
    for s in mainValues:
        retDict[s] = []
    if addcounts:
        retDict.update({'num-cites' : [], 'fraction-cites-overall' : [], 'fraction-cites-year' : []})
        countsDict = {}
        totCites = 0
        for cite in cites:
            totCites += 1
            try:
                countsDict[cite] += 1
            except KeyError:
                countsDict[cite] = 1
            try:
                cYear = cite.year
            except AttributeError:
                continue
            else:
                try:
                    countsDict[cYear] += 1
                except KeyError:
                    countsDict[cYear] = 1

    for cite in set(cites):
        retDict['citeString'].append(str(cite))
        for s in mainValues:
            try:
                retDict[s].append(getattr(cite, s))
            except AttributeError:
                retDict[s].append(None)
        if addcounts:
            count = countsDict[cite]
            retDict['num-cites'].append(count)
            retDict['fraction-cites-overall'].append(count / totCites)
            try:
                retDict['fraction-cites-year'].append(count / countsDict[cite.year])
            except AttributeError:
                retDict['fraction-cites-year'].append(None)
    return retDict
