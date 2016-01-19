class Record(object):
    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0):
        self._sourceFile = sFile
        self._sourceLine = sLine
        self.bad = bad
        self.error = error
        self._id = idValue
        self._fieldDict = fieldDict

    def __getitem__(self, key):
        try:
            return self._fieldDict[key]
        except KeyError:
            if isinstance(key, str):
                KeyError("'{}' could not be found in the Record".format(key))
            else:
                raise TypeError("Keys to Records cannot be of the type: {}".format(type(key)))


    def getTag(tag, raw = False):
