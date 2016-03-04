import collections.abc
import csv
import os

from ..mkRecord import Record

class Grant(Record, collections.abc.MutableMapping):
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

    def update(self, other):
        if type(self) != type(other):
            return NotImplemented
        else:
            if other.bad:
                self.error = otehr.error
                self.bad = True
            self._fieldDict.update(other._fieldDict)

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
        #We do not known anyhting about the structure of the grant so there is nothing to check about causing an error
        #The id needs to be unique so hashing the original will always give us that
        idValue = "{}-l:{}-{:0=20}".format(os.path.basename(sFile), sLine, hash(original))
        Grant.__init__(self, original, grantdDict, idValue, False, None, sFile = sFile, sLine = sLine)

def isDefaultGrantFile(fileName, useFileName = True, encoding = 'latin-1', dialect = 'excel'):
    try:
        #Try to open it
        with open(fileName, 'r', encoding = encoding) as openfile:
            #See if csv likes it
            reader = csv.DictReader(openfile, fieldnames = None, dialect = dialect)
            #Check that every row can be read
            length = 0
            for row in reader:
                length += 1
                #Just wanted to put something here that analysis the row
                #There is probably a better check
                if set(row.keys()) != set(reader.fieldnames):
                    return False
            #Check that there are rows to read
            if length < 1:
                return False
    except (StopIteration, UnicodeDecodeError, csv.Error):
        #If any of theses exceptions are raised the nit is defintly not as csv file
        #We do not want to catch everything though as there could be an issue with the code
        return False
    else:
        #IF nothing caused an issue return True
        return True

def parserDefaultGrantFile(fileName, encoding = 'latin-1', dialect = 'excel'):
    #Declare the returns out side of the block to show they are accessible everywhere inside it and so if there are issues with their creation it will no cause a problem with returning them
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
    finally:
        return grantSet, error
