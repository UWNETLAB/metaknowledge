class Record(object):
    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0, altNames = None, proccessingFuncs = None):
        """Base constructor for Records

        _fieldDict_ : is the unpared entry dict with tags as keys and their lines as a list of strings

        _idValue_ : is the unique ID of the Record, e.g. the WOS number

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
        self._computedFields = {}
        self._altNames = altNames
        if proccessingFuncs is None:
            proccessingFuncs = {}
        self._proccessingFuncs = proccessingFuncs

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
                    raise KeyError("'{}' could not be found in the Record".format(key))
                self._computedFields[key] = computedVal
                self._computedFields[self._altNames.get(key)] = computedVal
                return computedVal
            else:
                raise TypeError("Keys to Records must be strings they cannot be of the type: {}.".format(type(key)))

    def getTag(tag, raw = False):
        """Allows access to the raw values or is wrapper to __getitem__.

        Does not raise KeyError, will just return `None` if _tag_ cannot be found.
        """
        if raw:
            if tag in self._fieldDict:
                return self._fieldDict[tag]
            elif self._altNames.get(tag) in self._fieldDict:
                return self._fieldDict[self._altNames.get(tag)]
            else:
                return None
        else:
            try:
                return self[tag]
            except KeyError:
                return None
