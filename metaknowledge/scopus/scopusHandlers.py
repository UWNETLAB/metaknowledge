#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016

import csv

from .recordScopus import ScopusRecord, scopusHeader

from ..mkExceptions import BadScopusFile

def isScopusFile(infile, checkedLines = 2):
    """Determines if _infile_ is the path to a Scopus csv file. A file is considerd to be a Scopus file if it has the correct encoding (`utf-8` with BOM (Byte Order Mark)) and within the first _checkedLines_ a line contains the complete header, the list of all header entries in order is found in [`scopus.scopusHeader`](#metaknowledge.scopus).

    **Note** this is for csv files _not_ plain text files from scopus, plain text files are not complete.

    # Parameters

    _infile_ : `str`

    > The path to the targets file

    _checkedLines_ : `optional [int]`

    > default 2, the number of lines to check for the header

    # Returns

    `bool`

    > `True` if the file is a Scopus csv file
    """
    try:
        with open(infile, 'r', encoding='utf-8') as openfile:
            if openfile.read(1) != "\ufeff":
                return False
            for i in range(checkedLines):
                if openfile.readline()[:-1].split(',') == scopusHeader:
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False

def scopusParser(scopusFile):
    """Parses a scopus file, _scopusFile_, to extract the individual lines as [`ScopusRecords`](#metaknowledge.ScopusRecord).

    A Scopus file is a csv (Comma-separated values) with a complete header, see [`scopus.scopusHeader`](#metaknowledge.scopus) for the entries, and each line after it containing a record's entry. The string valued entries are quoted with double quotes which means double quotes inside them can cause issues, see [`scopusRecordParser()`](#metaknowledge.scopusRecordParser) for more information.

    # Parameters

    _scopusFile_ : `str`

    > A path to a valid scopus file, use [`isScopusFile()`](#metaknowledge.isScopusFile) to verify

    # Returns

    `set[ScopusRecord]`

    > Records for each of the entries
    """
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
