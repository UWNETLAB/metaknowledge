import os.path
import csv

from .baseGrant import Grant, csvAndLinesReader
from ..mkExceptions import BadGrant

class CIHRGrant(Grant):
    def __init__(self, original, grantdDict, sFile, sLine):
        bad = False
        error = None
        if grantdDict.get('PI Names', '') == '':
            bad = True
            error = BadGrant("Missing 'PI Names'")

        #Source file - line number - 6 character long numeric hash
        idValue = "{}-l:{}-{:0=20}".format(os.path.basename(sFile), sLine, hash(original))

        Grant.__init__(self, original, grantdDict, idValue, bad, error, sFile = sFile, sLine = sLine)

def isCIHRfile(fileName, useFileName = True):
    if useFileName and not os.path.basename(fileName).startswith('cihr_'):
        return False
    try:
        with open(fileName, 'r', encoding = 'latin-1') as openfile:
            if not openfile.readline().startswith('Search Criteria'):
                return False
            elif not openfile.readline().endswith(',,,,,,,,,\n'):
                return False
            elif not openfile.readline().endswith(',,,,,,,,,\n'):
                return False
            reader = csv.DictReader(openfile, fieldnames = None, dialect = 'excel')
            for row in reader:
                if 'PI Names' not in row:
                    return False
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return True

def parserCIHRfile(fileName):
    grantSet = set()
    error = None
    try:
        with open(fileName, 'r', encoding = 'latin-1') as openfile:
            f = enumerate(openfile, start = 1)
            next(f)
            next(f)
            next(f)
            reader = csvAndLinesReader(f, fieldnames = None, dialect = 'excel')
            for lineNum, lineString, lineDict in reader:
                grantSet.add(CIHRGrant(lineString, lineDict, sFile = fileName, sLine = lineNum))
    except Exception:
        if error is None:
            error = BadGrant("The file '{}' is having decoding issues. It may have been modifed since it was downloaded or not be a CIHR grant file.".format(fileName))
    except KeyboardInterrupt as e:
        error = e
    finally:
        if isinstance(error, KeyboardInterrupt):
            raise error
        return grantSet, error
