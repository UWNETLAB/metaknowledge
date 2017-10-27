#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import collections
import csv
import re

from .tagProcessing.tagFunctions import scopusTagToFunction
from .tagProcessing.specialFunctions import scopusSpecialTagToFunc

from ..mkRecord import ExtendedRecord
from ..mkExceptions import RCTypeError, BadScopusFile, BadScopusRecord

scopusHeader = ['Authors', 'Title', 'Year', 'Source title', 'Volume', 'Issue', 'Art. No.', 'Page start', 'Page end', 'Page count', 'Cited by', 'DOI', 'Link', 'Affiliations', 'Authors with affiliations', 'Abstract', 'Author Keywords', 'Index Keywords', 'Molecular Sequence Numbers', 'Chemicals/CAS', 'Tradenames', 'Manufacturers', 'Funding Details', 'References', 'Correspondence Address', 'Editors', 'Sponsors', 'Publisher', 'Conference name', 'Conference date', 'Conference location', 'Conference code', 'ISSN', 'ISBN', 'CODEN', 'PubMed ID', 'Language of Original Document', 'Abbreviated Source Title', 'Document Type', 'Source', 'EID']

class ScopusRecord(ExtendedRecord):
    """Class for full Scopus entries.

    This class is an [`ExtendedRecord`](#metaknowledge.ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [`scopusParser()`](#metaknowledge.scopusParser) on a scopus **CSV** file.
    """
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
        except (BadScopusRecord, IndexError) as b:
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
        return scopusSpecialTagToFunc[key](self)

    def writeRecord(self, f):
        if self.bad:
            raise BadScopusRecord("This record cannot be converted to a file as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        else:
            f.write(','.join(('"{}"'.format(self._fieldDict.get(k, '')) for k in scopusHeader)))

firstQuotingRegex = re.compile(r'("")*"([^"]|"$)')
innerQuotingRegex = re.compile(r'("")*"([^"|$])')

def scopusRecordParser(record):
    """The parser [`ScopusRecords`](#metaknowledge.ScopusRecord) use. This takes a line from [`scopusParser()`](#metaknowledge.scopusParser) and parses it as a part of the creation of a `ScopusRecord`.

    **Note** this is for csv files downloaded from scopus _not_ the text records as those are less complete. Also, Scopus uses double quotes (`"`) to quote strings, such as abstracts, in the csv so double quotes in the string must be escaped. For reasons not fully understandable by mortals they choose to use two double quotes in a row (`""`) to represent an escaped double quote. This parser does not unescape these quotes, but it does correctly handle their interacts with the outer double quotes.

    # Parameters

    _record_ : `str`

    > string ending with a newline containing the record's entry

    # Returns

    `dict`

    > A dictionary of the key-vaue pairs in the entry
    """
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
                #So an entry containing:
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
                    valString = currentVal[1:-1]
                except ValueError:
                    valString = currentVal[1:-1]
            tagDict[key] = valString
        else:
            tagDict[key] = currentVal
    return tagDict
