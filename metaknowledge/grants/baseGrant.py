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

class DefaultGrant(Grant):
    #Making it a subclass so that Grant is never used raw
    #Also make interface simpler
    def __init__(self, original, grantdDict, sFile = "", sLine = 0):
        Grant.__init__(self, original, grantdDict, hash(original), False, None, sFile = sFile, sLine = sLine)

def isDefaultGrantFile(fileName, encoding = 'latin-1', dialect = 'excel'):
    try:
        print(fileName)
        #Try ISO-8859
        with open(fileName, 'r', encoding = encoding) as openfile:
            reader = csv.DictReader(openfile, fieldnames = None, dialect = dialect)
            for row in reader:
                if set(row.keys()) != set(reader.fieldnames):
                    return False
    except (StopIteration, UnicodeDecodeError, csv.Error):
        return False
    else:
        return True

def parserDefaultGrantFile(fileName, encoding = 'latin-1', dialect = 'excel'):
    grantSet = set()
    error = None
    try:
        with open(fileName, 'r', encoding = encoding) as openfile:
            f = enumerate(openfile, start = 1)
            reader = csvAndLinesReader(f, fieldnames = None, dialect = dialect)
            for lineNum, lineString, lineDict in reader:
                grantSet.add(DefaultGrant(lineString, lineDict, sFile = fileName, sLine = lineNum))
    except UnicodeDecodeError:
        if error is None:
            error = BadGrant("The file '{}' is having decoding issues. It may have been modifed since it was downloaded or not be a CIHR grant file.".format(fileName))
    return grantSet, error
