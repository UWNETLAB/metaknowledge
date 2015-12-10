from ..record import BadISIFile, Record

import collections
import csv
import os

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
                print(entries)
                entries.add(dictTranslator(entryReader(f)))
            except RuntimeError:
                for i in range(10):
                    print(f.readline(), end = '')
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
    entryDict['UT'] = ['PRO:{}'.format(entryDict['ProQuest document ID'][0])]
    del entryDict['ProQuest document ID']
    print(entryDict['UT'])
    return Record(entryDict)

def csver(entriesLst, fName):
    headers = []
    for entry in entriesLst:
        fieldsLst = [f for f in entry.keys() if f not in headers]
        headers += fieldsLst
    with open(fName, 'w', encoding = 'utf-8') as f:
        csvFile = csv.DictWriter(f, headers, restval='', extrasaction='raise', dialect=csv.unix_dialect)
        csvFile.writeheader()
        for entry in entriesLst:
            csvFile.writerow(entry)

def getFiles(target):
    retList = []
    if os.path.isdir(target):
        for fileName in os.listdir(target):
            if os.path.isfile(os.path.join(target, fileName)):
                retList.append(os.path.join(target, fileName))
    elif os.path.isfile(target):
        retList = [target]
    else:
        raise RuntimeError("{} is not a file or directory".format(target))
    return retList

def main():
    entries = []
    filesLst = getFiles(targetFileOrDir)
    print("Found {} files".format(len(filesLst)))
    for i, fileName in enumerate(filesLst):
        print("{} of {} files analyzed".format(i, len(filesLst)), end = '\r')
        entries += proQuestReader(fileName)
    print("{0} of {0} files analyzed, writing to file '{1}'".format(len(filesLst), outputFileName))
    csver(entries, outputFileName)

if __name__ == '__main__':
    main()
