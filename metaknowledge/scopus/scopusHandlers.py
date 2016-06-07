#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import csv

from .recordScopus import ScopusRecord, scopusHeader

from ..mkExceptions import BadScopusFile

def isScopusFile(infile, checkedLines = 2):
    try:
        with open(infile, 'r', encoding='utf-8') as openfile:
            if openfile.read(1) != "\ufeff":
                return False
            if openfile.readline()[:-1].split(',') != scopusHeader:
                return False
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return True

def scopusParser(scopusFile):
    #assumes the file is Scopus
    recSet = set()
    error = None
    lineNum = 0
    try:
        with open(scopusFile, 'r', encoding = 'utf-8') as openfile:
            #Get rid of the BOM
            openfile.readline()
            lineNum = 0
            try:
                for line, row in enumerate(openfile, start = 2):
                    lineNum = line
                    recSet.add(ScopusRecord(row, sFile = scopusFile, sLine = line))
            except BadScopusFile as e:
                if error is None:
                    error = BadScopusFile("The file '{}' becomes unparsable after line: {}, due to the error: {} ".format(scopusFile, lineNum, e))
    except (csv.Error, UnicodeDecodeError):
        if error is None:
            error = BadScopusFile("The file '{}' has parts of it that are unparsable starting at line: {}.".format(scopusFile, lineNum))
    return recSet, error
