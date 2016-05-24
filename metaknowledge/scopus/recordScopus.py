#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import collections
import csv
import re

from .tagProcessing.tagFunctions import scopusTagToFunction

from ..mkRecord import ExtendedRecord
from ..mkExceptions import RCTypeError, BadScopusFile, BadScopusRecord

scopusHeader = ['Authors', 'Title', 'Year', 'Source title', 'Volume', 'Issue', 'Art. No.', 'Page start', 'Page end', 'Page count', 'Cited by', 'DOI', 'Link', 'Affiliations', 'Authors with affiliations', 'Abstract', 'Author Keywords', 'Index Keywords', 'Molecular Sequence Numbers', 'Chemicals/CAS', 'Tradenames', 'Manufacturers', 'Funding Details', 'References', 'Correspondence Address', 'Editors', 'Sponsors', 'Publisher', 'Conference name', 'Conference date', 'Conference location', 'Conference code', 'ISSN', 'ISBN', 'CODEN', 'PubMed ID', 'Language of Original Document', 'Abbreviated Source Title', 'Document Type', 'Source', 'EID']

class ScopusRecord(ExtendedRecord):

    def __init__(self, inRecord, sFile = "", sLine = 0):
        bad = False
        error = None
        fieldDict = None
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, str):
                fieldDict = scopusRecordParser(inRecord)
            else:
                raise RCTypeError("Unsupported input type '{}', ScopusRecords cannot be created from '{}'".format(inRecord, type(inRecord)))
        except BadScopusRecord as b:
            self.bad = True
            self.error = b
            fieldDict = collections.OrderedDict()
        if fieldDict is not None:
            if 'EID' in fieldDict:
                self._scopusNum = "EID:{}".format(fieldDict['EID'])
            else:
                self._scopusNum = None
                bad = True
                error = BadScopusRecord("Missing EID")
        ExtendedRecord.__init__(self, fieldDict, self._scopusNum, bad, error, sFile = sFile, sLine = sLine)

    def encoding(self):
        return 'utf-8'

    @staticmethod
    def getAltName(tag):
        return None

    @staticmethod
    def tagProcessingFunc(tag):
        return scopusTagToFunction[tag]

    def specialFuncs(self, key):
        raise KeyError

    def writeRecord(self, f):
        raise Exception
firstQuotingRegex = re.compile(r'("")*"([^"]|"$)')
innerQuotingRegex = re.compile(r'("")*"([^"|$])')

def scopusRecordParser(record):
    splitRecord = record[:-1].split(',')
    tagDict = {}
    quoted = False
    for key in reversed(scopusHeader):
        currentVal = splitRecord.pop()
        if currentVal == '':
            pass
        elif currentVal[-1] == '"':
            if re.match(firstQuotingRegex, currentVal) is None:
                valString = ',' + currentVal[:-1]
                currentVal = splitRecord.pop()
                #double quotes (") are escaped by proceeding them with another double quote
                #So an entry contatining:
                #',"stuff,""quoted"",more stuff,""more quoted""",'
                # whould be a single string belonging to 1 column that looks like:
                #'stuff,"quoted",more stuff,"more quoted"'
                #We are not going to unescape the quotation marks but we do have to deal with them
                while re.match(innerQuotingRegex, currentVal) is None:
                    valString = ',' + currentVal + valString
                    currentVal = splitRecord.pop()
                valString = currentVal[1:] + valString
            else:
                try:
                    valString = int(currentVal[1:-1])
                except ValueError:
                    valString = currentVal[1:-1]
            tagDict[key] = valString
        else:
            tagDict[key] = currentVal
    return tagDict
