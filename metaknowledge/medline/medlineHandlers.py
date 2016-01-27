import itertools

from .recordMedline import MedlineRecord

def isMedlineFile(infile, checkedLines = 2):
    """Checks if _infile_ has the right header in the first _checkedLines_ lines
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
    #assumes the file is MEDLINE
    recSet = set()
    error = None
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
                                    error = BadPubmedFile("The file '{}' becomes unparsable after line: {}, due to the error: ".format(pubFile, badLine, e))
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
    finally:
        return recSet, error
