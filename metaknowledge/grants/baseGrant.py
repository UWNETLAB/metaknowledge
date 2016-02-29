import collections.abc
import csv

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

def csvAndLinesReader(enumeratedFile, *csvArgs, **csvKwargs):
    currentData = {
    'currentLineNum' : -1,
    'currentLineString' : '',
    }
    def readerWithSideEffects(target, datDict):
        while True:
            datDict['currentLineNum'], datDict['currentLineString'] = next(target)
            yield datDict['currentLineString']
    reader = csv.DictReader(readerWithSideEffects(enumeratedFile, currentData), *csvArgs, **csvKwargs)
    readerIter = reader.__iter__()
    while True:
        row = next(readerIter)
        yield currentData['currentLineNum'], currentData['currentLineString'], row
