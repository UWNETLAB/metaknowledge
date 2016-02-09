#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import collections
import itertools
import io

from ..mkExceptions import BadPubmedRecord
from ..record import Record
from .tagProcessing.tagNames import tagNameConverterDict, authorBasedTags
from .tagProcessing.tagFunctions import medlineTagToFunc
from .tagProcessing.specialFunctions import medlineSpecialTagToFunc

class MedlineRecord(Record):
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
                fieldDict = medlineRecordParser(inRecord)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = medlineRecordParser(enumerate(inRecord))
            elif isinstance(inRecord, str):
                def addChartoEnd(lst):
                    for s in lst:
                        yield s + '\n'
                fieldDict = medlineRecordParser(enumerate(addChartoEnd(inRecord.split('\n')), start = 1))
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
        Record.__init__(self, fieldDict, self._pubNum, bad, error, sFile = sFile, sLine = sLine)


    @property
    def encoding(self):
        return 'latin-1'

    @staticmethod
    def getAltName(tag):
        return tagNameConverterDict.get(tag)

    @staticmethod
    def tagProccessingFunc(tag):
        return medlineTagToFunc[tag]

    def specialFuncs(self, key):
        #This will usually raise a key error that needs to be caught higher up
        #Catching it here would require unnecessary overhead
        return medlineSpecialTagToFunc[key](self)

    def writeRecord(self, f):
        pass

def medlineRecordParser(record):
    tagDict = {}
    tag = 'PMID'
    mostRecentAuthor = None
    for lineNum, line in record:
        tmptag = line[:4].rstrip()
        contents = line[6:-1]
        if tmptag.isalpha() and line[4] == '-':
            tag = tmptag
            if tag == 'AU':
                mostRecentAuthor = contents
            if tag in authorBasedTags:
                contents = "{} : {}".format(mostRecentAuthor, contents)
            try:
                tagDict[tag].append(contents)
            except KeyError:
                tagDict[tag] = [contents]
        elif line[:6] == '      ':
            tagDict[tag][-1] += '\n' + line[6:-1]
        elif line == '\n':
            break
        else:
            raise BadPubmedRecord("Tag not formed correctly on line {}: '{}'".format(lineNum, line))
    return tagDict
