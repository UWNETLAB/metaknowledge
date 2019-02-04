import itertools

from ..mkExceptions import BadPubmedFile

from .recordMedline import MedlineRecord

def isMedlineFile(infile, checkedLines = 2):
    """Determines if _infile_ is the path to a Medline file. A file is considerd to be a Medline file if it has the correct encoding (`latin-1`) and within the first _checkedLines_ a line starts with `"PMID- "`.

    # Parameters

    _infile_ : `str`

    > The path to the targets file

    _checkedLines_ : `optional [int]`

    > default 2, the number of lines to check for the header

    # Returns

    `bool`

    > `True` if the file is a Medline file
    """
    try:
        with open(infile, 'r', encoding='latin-1') as openfile:
            f = enumerate(openfile, start = 0)
            for i in range(checkedLines):
                if f.__next__()[1].startswith("PMID- "):
                    #Only indicator I could find
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False

def medlineParser(pubFile):
    """Parses a medline file, _pubFile_, to extract the individual entries as [MedlineRecords](#metaknowledge.medline.recordMedline.MedlineRecord).

    A medline file is a series of entries, each entry is a series of tags. A tag is a 2 to 4 character string each tag is padded with spaces on the left to make it 4 characters which is followed by a dash and a space (`'- '`). Everything after the tag and on all lines after it not starting with a tag is considered associated with the tag. Each entry's first tag is `PMID`, so a first line looks something like `PMID- 26524502`. Entries end with a single blank line.

    # Parameters

    _pubFile_ : `str`

    > A path to a valid medline file, use [isMedlineFile](#metaknowledge.medline.medlineHandlers.isMedlineFile) to verify

    # Returns

    `set[MedlineRecord]`

    > Records for each of the entries
    """
    #assumes the file is MEDLINE
    recSet = set()
    error = None
    lineNum = 0
    try:
        with open(pubFile, 'r', encoding = 'latin-1') as openfile:
            f = enumerate(openfile, start = 1)
            lineNum, line = next(f)
            try:
                while True:
                    if line.startswith("PMID- "):
                        try:
                            r = MedlineRecord(itertools.chain([(lineNum, line)], f), sFile = pubFile, sLine = lineNum)
                            recSet.add(r)
                        except BadPubmedFile as e:
                            badLine = lineNum
                            try:
                                lineNum, line = next(f)
                                while not line.startswith("PMID- "):
                                    lineNum, line = next(f)
                            except (StopIteration, UnicodeDecodeError) as e:
                                if error is None:
                                    error = BadPubmedFile("The file '{}' becomes unparsable after line: {}, due to the error: {} ".format(pubFile, badLine, e))
                                raise e
                    elif line != '\n':
                        if error is None:
                            error = BadPubmedFile("The file '{}' has parts of it that are unparsable starting at line: {}.".format(pubFile, lineNum))
                    lineNum, line = next(f)
            except StopIteration:
                #End of the file has been reached
                pass
    except UnicodeDecodeError:
        if error is None:
            error = BadPubmedFile("The file '{}' has parts of it that are unparsable starting at line: {}.".format(pubFile, lineNum))
    return recSet, error
