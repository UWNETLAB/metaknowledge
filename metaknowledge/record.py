class Record(object):
    def __init__(self, fieldDict, idValue, bad, error, sFile = "", sLine = 0):
        self._sourceFile = sFile
        self._sourceLine = sLine
        self.bad = bad
        self.error = error
        self._id = idValue
        self._fieldDict = fieldDict
