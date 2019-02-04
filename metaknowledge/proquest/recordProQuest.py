import collections
import io
import itertools

from ..mkExceptions import BadProQuestRecord, RecordsNotCompatible
from ..mkRecord import ExtendedRecord

from .tagProcessing.specialFunctions import proQuestSpecialTagToFunc
from .tagProcessing.tagFunctions import proQuestTagToFunc

class ProQuestRecord(ExtendedRecord):
    """Class for full ProQuest entries.

    This class is an [ExtendedRecord](./ExtendedRecord.html#metaknowledge.ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [proQuestParser()](../modules/proquest.html#metaknowledge.proquest.proQuestHandlers.proQuestParser) on a ProQuest file.
    """
    def __init__(self, inRecord, recNum = None, sFile = "", sLine = 0):
        bad = False
        error = None
        fieldDict = None
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, enumerate) or isinstance(inRecord, itertools.chain):
                #Already enumerated
                #itertools.chain is for the parser upstream to insert stuff into the stream
                fieldDict = proQuestRecordParser(inRecord, recNum)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = proQuestRecordParser(enumerate(inRecord), recNum)
            elif isinstance(inRecord, str):
                #Probaly a better way to do this but it isn't going to be used much, so no need to improve it
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
        try:
            self._proID = "PROQUEST:{}".format(fieldDict["ProQuest document ID"][0])
        except KeyError:
            self._proID = "PROQUEST:MISSING"
            bad = True
            error = BadProQuestRecord("Missing ProQuest document ID")
        ExtendedRecord.__init__(self, fieldDict, self._proID, bad, error, sFile =sFile, sLine = sLine)

    def encoding(self):
        return 'utf-8'

    @staticmethod
    def getAltName(tag):
        return None

    @staticmethod
    def tagProcessingFunc(tag):
        #Should not raise an exception
        #It might be faster to do this as a class attribute
        return proQuestTagToFunc(tag)

    def specialFuncs(self, key):
        return proQuestSpecialTagToFunc[key](self)
        #raise KeyError("There are no special functions given by default.")

    def writeRecord(self, infile):
        raise RecordsNotCompatible("ProQuest's data format cannot be written back to file. You can still write out a csv with writeCSV().")

def proQuestRecordParser(enRecordFile, recNum):
    """The parser [ProQuestRecords](../classes/ProQuestRecord.html#metaknowledge.proquest.ProQuestRecord) use. This takes an entry from [proQuestParser()](#metaknowledge.proquest.proQuestHandlers.proQuestParser) and parses it a part of the creation of a `ProQuestRecord`.

    # Parameters

    _enRecordFile_ : `enumerate object`

    > a file wrapped by `enumerate()`

    _recNum_ : `int`

    > The number given to the entry in the first section of the ProQuest file

    # Returns

    `collections.OrderedDict`

    > An ordered dictionary of the key-vaue pairs in the entry
    """
    tagDict = collections.OrderedDict()
    currentEntry = 'Name'
    while True:
        lineNum, line = next(enRecordFile)
        if line == '_' * 60 + '\n':
            break
        elif line == '\n':
            pass
        elif currentEntry is 'Name' or currentEntry is 'url':
            tagDict[currentEntry] = [line.rstrip()]
            currentEntry = None
        elif ':' in line and not line.startswith('http://'):
            splitLine = line.split(': ')
            currentEntry = splitLine[0]
            tagDict[currentEntry] = [': '.join(splitLine[1:]).rstrip()]
            if currentEntry == 'Author':
                currentEntry = 'url'
        else:
            tagDict[currentEntry].append(line.rstrip())
    return tagDict
