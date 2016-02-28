import collections.abc

from ..mkRecord import Record

class Grant(Record, collections.abc.Mapping):
    def __init__(self, original, grantdDict, idValue, bad, error, sFile = "", sLine = 0):
        self.original = original
        Record.__init__(self, grantdDict, idValue, bad, error, sFile = sFile, sLine = sLine)

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self._fieldDict.__setitem__(key, value)
        else:
            raise KeyError("{} is not a valid key, all keys must be strings.".format(key))

    def __delitem__(self, key):
        self._fieldDict.__delitem__(key)
