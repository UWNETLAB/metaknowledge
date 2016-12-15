import csv
import os.path

from .baseGrant import Grant, csvAndLinesReader
from ..mkExceptions import BadGrant

class NSERCGrant(Grant):
    def __init__(self, original, grantdDict, sFile, sLine):
        bad = False
        error = None
        if grantdDict.get('Cle', '') == '':
            bad = True
            error = BadGrant("Missing 'CLE'")
            idValue = "NSERC:{}".format(hash(original))
        else:
            idValue = "NSERC:{}".format(grantdDict.get('Cle', ''))
        Grant.__init__(self, original, grantdDict, idValue, bad, error, sFile = sFile, sLine = sLine)

    def update(self, other):
        for field, value in other._fieldDict.items():
            if value == '':
                continue
            elif self._fieldDict.get(field, '') == '':
                self._fieldDict[field] = value
            else:
                self._fieldDict[field] += "; {}".format(value)

    def getInvestigators(self, tags = None, seperator = ";", _getTag = False):
        """Returns a list of the names of investigators. The optional arguments are ignored.

        # Returns

        `list [str]`

        > A list of all the found investigator's names
        """
        if tags is None:
            tags = []
        elif isinstance(tags, str):
            tags = [tags]
        for k in self.keys():
            if 'name-' in k.lower() and k not in tags:
                tags.append(k)
        return super().getInvestigators(tags = tags, seperator = seperator, _getTag = _getTag)

    def getInstitutions(self, tags = None, seperator = ";", _getTag = False):
        """Returns a list with the names of the institution. The optional arguments are ignored

        # Returns

        `list [str]`

        > A list with 1 entry the name of the institution
        """
        if tags is None:
            tags = []
        elif isinstance(tags, str):
            tags = [tags]
        for k in self.keys():
            if 'institution' in k.lower() and k not in tags:
                tags.append(k)
        return super().getInvestigators(tags = tags, seperator = seperator, _getTag = _getTag)

def isNSERCfile(fileName, useFileName = True):
    if useFileName and not os.path.basename(fileName).startswith('NSERC_'):
        return False
    try:
        with open(fileName, 'r', encoding = 'latin-1') as openfile:
            reader = csv.DictReader(openfile, fieldnames=None, dialect='excel')
            length = 0
            for row in reader:
                length += 1
                if set(row.keys()) != set(reader.fieldnames):
                    return False
            if length < 1:
                return False
    except (StopIteration, UnicodeDecodeError, KeyError):
        return False
    else:
        return True

def parserNSERCfile(fileName):
    grantSet = set()
    error = None
    try:
        with open(fileName, 'r', encoding = 'latin-1') as openfile:
            f = enumerate(openfile, start = 1)
            reader = csvAndLinesReader(f, fieldnames = None, dialect = 'excel')
            for lineNum, lineString, lineDict in reader:
                G = NSERCGrant(lineString, lineDict, sFile = fileName, sLine = lineNum)
                if G in grantSet:
                    for Gin in grantSet:
                        if Gin == G:
                            Gin.update(G)
                            break
                else:
                    grantSet.add(G)
    except Exception:
        if error is None:
            error = BadGrant("The file '{}' is having decoding issues. It may have been modifed since it was downloaded or not be a NSERC grant file.".format(fileName))
    except KeyboardInterrupt as e:
        error = e
    finally:
        if isinstance(error, KeyboardInterrupt):
            raise error
        return grantSet, error
