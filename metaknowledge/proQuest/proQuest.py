from ..record import BadISIFile, Record

import collections
import csv
import os

proTagTable = {
    "Name" : 'TI',
    "Author" : 'AF',
    "url" : '',
    "Abstract" : 'AB',
    "Links" : '',
    "Advisor" : '',
    "Classification" : 'ID',
    "Committee member" : '',
    "Copyright" : '',
    "Country of publication" : '',
    "Database" : '',
    "Degree" : '',
    "Degree date" : '',
    "Department" : '',
    "Dissertation/thesis number" : '',
    "Document type" : 'DC',
    "ISBN" : 'BN',
    "Identifier / keyword" : 'DE',
    "Language" : 'LA',
    "Number of pages" : 'PG',
    "Place of publication" : 'PA',
    "ProQuest document ID" : '',#'UT',
    "Publication year" : 'PY',
    "School code" : '',
    "Source" : '',
    "Source type" : '',
    "Subject" : '',
    "Title" : 'TI',
    "University location" : 'PI',
    "University/institution" : '',
    "Pages" : '',
    "Publication subject" : '',
    "People" : ''
}


def proParser(targetFileName):
    entries = set()
    with open(targetFileName, mode = 'r', encoding = 'utf-8') as f:
        currentLine = f.readline()
        while currentLine != "Bibliography\n":
            currentLine = f.readline()
            if currentLine == '':
                raise BadISIFile("{} does not have a correctly formatted Bibliography".format(targetFileName))
        else:
            if f.readline() != "\n" or f.readline() != "____________________________________________________________\n":
                raise BadISIFile("{} does not have a correctly formatted Bibliography".format(targetFileName))
        while True:
            try:
                entries.add(dictTranslator(entryReader(f)))
            except RuntimeError:
                break
    return entries

def entryReader(f):
    entryDict = collections.OrderedDict()
    currentEntry = 'Name'
    if f.readline() != '\n' or not f.readline().startswith("Document ") or f.readline() != '\n':
            raise RuntimeError("not the start of an entry")
    for line in f:
        if line == '____________________________________________________________\n':
            return entryDict
        elif line == '\n':
            pass
        elif currentEntry is 'Name' or currentEntry is 'url':
            entryDict[currentEntry] = [line.rstrip()]
            currentEntry = None
        elif ':' in line and not line.startswith('http://'):
            splitLine = line.split(': ')
            currentEntry = splitLine[0]
            entryDict[currentEntry] = [': '.join(splitLine[1:]).rstrip()]
            if currentEntry == 'Author':
                currentEntry = 'url'
        else:
            entryDict[currentEntry].append(line.rstrip())
    raise BadISIFile("File ran out before the entry was over")

def dictTranslator(entryDict):
    translatedDict = collections.OrderedDict()
    translatedDict['UT'] = ['PRO:{}'.format(entryDict['ProQuest document ID'][0])]
    for k, v in entryDict.items():
        if k in proTagTable and proTagTable[k] != '':
            translatedDict[proTagTable[k]] = v
        else:
            translatedDict[k.upper()] = v
    return Record(translatedDict)
