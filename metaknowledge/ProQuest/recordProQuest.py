import collections
import io
import itertools

from ..mkExceptions import BadProQuestRecord
from ..mkRecord import ExtendedRecord


class ProQuestRecord(ExtendedRecord):
    def __init__(self, inRecord, recNum = None, sFile = "", sLine = 0):
        bad = False
        error = None
        fieldDict = None
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, enumerate) or isinstance(inRecord, itertools.chain):
                #Already enumerated
                fieldDict = proQuestRecordParser(inRecord, recNum)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = proQuestRecordParser(enumerate(inRecord), recNum)
            elif isinstance(inRecord, str):
                def addCharToEnd(lst):
                    for s in lst:
                        yield s + '\n'
                fieldDict = proQuestRecordParser(enumerate(addCharToEnd(inRecord.split('\n')), start = 1), recNum)
                #string io
            else:
                raise TypeError("Unsupported input type '{}', ProQuestRecords cannot be created from '{}'".format(inRecord, type(inRecord)))
        except BadProQuestRecord as b:
            self.bad = True
            self.error = b
            fieldDict = collections.OrderedDict()
        ExtendedRecord.__init__(self, fieldDict, idValue, bad, error, sFile =sFile, sLine = sLine)

    def encoding(self):
        return 'utf-8'

    @staticmethod
    def getAltName(tag):
        return None

    @staticmethod
    def tagProccessingFunc(tag):
        #Should not raise an exception
        return lambda x: x

    def specialFuncs(self, key):
        raise KeyError("There are no special functions given by default.")

    def writeRecord(self):
        raise RuntimeError("This needs to be written")



def proQuestRecordParser(record, recNum):
    tagDict = collections.OrderedDict()
    for lineNum, line in record:
        print(line[:-1])
        if line == '_' * 60 + '\n':
            break
    print(next(record))
    print(next(record))
    return tagDict
