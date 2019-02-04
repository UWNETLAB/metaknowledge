#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import collections
import itertools
import io

from ..mkExceptions import BadPubmedRecord, RCTypeError
from ..mkRecord import ExtendedRecord
from .tagProcessing.tagNames import tagNameConverterDict, authorBasedTags
from .tagProcessing.tagFunctions import medlineTagToFunc
from .tagProcessing.specialFunctions import medlineSpecialTagToFunc

class MedlineRecord(ExtendedRecord):
    """Class for full Medline(Pubmed) entries.

    This class is an [ExtendedRecord](./ExtendedRecord.html#metaknowledge.ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [medlineParser()](../modules/medline.html#metaknowledge.medline.medlineHandlers.medlineParser) on a medline file.
    """
    def __init__(self, inRecord, sFile = "", sLine = 0):
        bad = False
        error = None
        fieldDict = None
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, itertools.chain):
                fieldDict = medlineRecordParser(inRecord)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = medlineRecordParser(enumerate(inRecord))
            elif isinstance(inRecord, str):
                def addCharToEnd(lst):
                    for s in lst:
                        yield s + '\n'
                fieldDict = medlineRecordParser(enumerate(addCharToEnd(inRecord.split('\n')), start = 1))
                #string io
            else:
                raise RCTypeError("Unsupported input type '{}', PubmedRecords cannot be created from '{}'".format(inRecord, type(inRecord)))
        except BadPubmedRecord as b:
            self.bad = True
            self.error = b
            fieldDict = collections.OrderedDict()
        if fieldDict is not None:
            if 'PMID' in fieldDict:
                self._pubNum = "PMID:{}".format(fieldDict['PMID'][0])
            else:
                self._pubNum = None
                bad = True
                error = BadPubmedRecord("Missing PMID")
        ExtendedRecord.__init__(self, fieldDict, self._pubNum, bad, error, sFile = sFile, sLine = sLine)

    def encoding(self):
        return 'latin-1'

    @staticmethod
    def getAltName(tag):
        return tagNameConverterDict.get(tag)

    @staticmethod
    def tagProcessingFunc(tag):
        return medlineTagToFunc[tag]

    def specialFuncs(self, key):
        #This will usually raise a key error that needs to be caught higher up
        #Catching it here would require unnecessary overhead
        return medlineSpecialTagToFunc[key](self)

    def writeRecord(self, f):
        """This is nearly identical to the original the FAU tag is the only tag not writen in the same place, doing so would require changing the parser and lots of extra logic.
        """
        if self.bad:
            raise BadPubmedRecord("This record cannot be converted to a file as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        else:
            authTags = {}
            for tag in authorBasedTags:
                for val in self._fieldDict.get(tag, []):
                    split = val.split(' : ')
                    try:
                        authTags[split[0]].append("{0}{1}- {2}\n".format(tag, ' ' * (4 - len(tag)),' : '.join(split[1:]).replace('\n', '\n      ')))
                    except KeyError:
                        authTags[split[0]] = ["{0}{1}- {2}\n".format(tag, ' ' * (4 - len(tag)),' : '.join(split[1:]).replace('\n', '\n      '))]
            for tag, value in self._fieldDict.items():
                if tag in authorBasedTags:
                    continue
                else:
                    for v in value:
                        f.write("{0}{1}- {2}\n".format(tag, ' ' * (4 - len(tag)), v.replace('\n', '\n      ')))
                        if tag == 'AU':
                            for authVal in authTags.get(v,[]):
                                f.write(authVal)

def medlineRecordParser(record):
    """The parser [`MedlineRecord`](../classes/MedlineRecord.html#metaknowledge.medline.MedlineRecord) use. This takes an entry from [medlineParser()](#metaknowledge.medline.medlineHandlers.medlineParser) and parses it a part of the creation of a `MedlineRecord`.

    # Parameters

    _record_ : `enumerate object`

    > a file wrapped by `enumerate()`

    # Returns

    `collections.OrderedDict`

    > An ordered dictionary of the key-vaue pairs in the entry
    """
    tagDict = collections.OrderedDict()
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
