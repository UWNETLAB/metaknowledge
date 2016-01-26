#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

from ..mkExceptions import BadPubmedRecord
from ..record import Record

class PubmedRecord(Record):
    def __init__(self, inRecord, sFile = "", sLine = 0):
        """See help on [Record](#Record.Record) for details"""
        bad = False
        error = None
        fieldDict = None
        self._unComputedTags = set()
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, itertools.chain):
                fieldDict = pubRecordParser(inRecord)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = pubRecordParser(enumerate(inRecord))
            elif isinstance(inRecord, str):
                def addChartoEnd(lst):
                    for s in lst:
                        yield s + '\n'
                fieldDict = pubRecordParser(enumerate(addChartoEnd(inRecord.split('\n')), start = 1))
                #string io
            else:
                raise TypeError("Unsupported input type '{}', PubmedRecords cannot be created from '{}'".format(inRecord, type(inRecord)))
        except BadPubmedRecord as b:
            self.bad = True
            self.error = b
            fieldDict = collections.OrderedDict()
        if fieldDict is not None:
            if 'PMID' in fieldDict:
                self._pubNum = fieldDict['PMID'][0]
            else:
                self._pubNum = None
                bad = True
                error = BadPubmedRecord("Missing WOS number")
    @property
    def encoding(self):
        return 'latin-1'

    @staticmethod
    def getAltName(tag):
        return tagNameConverterDict.get(tag)
