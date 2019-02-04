try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections
import csv
import os

from ..mkRecord import Record
from ..mkExceptions import BadGrant



class Grant(Record, collections.abc.MutableMapping):

    #Overwriting Record's attribute
    _documented = []

    def __init__(self, original, grantdDict, idValue, bad, error, sFile = "", sLine = 0):
        self.original = original
        Record.__init__(self, grantdDict, idValue, bad, error, sFile = sFile, sLine = sLine)

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self._fieldDict.__setitem__(key, value)
        else:
            raise KeyError("{} is not a valid key, all keys must be strings.".format(key))

    def __delitem__(self, key):
        self._fieldDict.__delitem__(key)

    def getInvestigators(self, tags = None, seperator = ";", _getTag = False):
        """Returns a list of the names of investigators. This is done by looking (in order) for any of fields in _tags_ and splitting the strings on _seperator_. If no strings are found an empty list will be returned.

        *Note* for some Grants `getInvestigators` has been overwritten and will ignore the arguments and simply provide the investigators.

        # Parameters

        _tags_ : `optional list[str]`

        > A list of the tags to look for investigators in

        _seperator_ : `optional str`

        > The string that separators each investigators name  within the column

        # Returns

        `list [str]`

        > A list of all the found investigator's names
        """
        #By default we don't know which field has the investigators
        investVal = []
        retTag = None
        if tags is not None:
            if not isinstance(tags, list):
                tags = [tags]
            for tag in tags:
                try:
                    tval = self[tag].split(seperator)
                    if _getTag:
                        investVal += [(t.strip(), tag) for t in tval]
                    else:
                        investVal += [t.strip() for t in tval]
                except KeyError:
                    pass
                except AttributeError:
                    tval = [auth.split(seperator)[0] for auth in self[tag]]
                    if _getTag:
                        investVal += [(t.strip(), tag) for t in tval]
                    else:
                        investVal += [t.strip() for t in tval]
        return investVal

    def getInstitutions(self, tags = None, seperator = ";", _getTag = False):
        """Returns a list of the names of institutions. This is done by looking (in order) for any of fields in _tags_ and splitting the strings on _seperator_ (in case of multiple institutions). If no strings are found an empty list will be returned.

        *Note* for some Grants `getInstitutions` has been overwritten and will ignore the arguments and simply provide the investigators.

        # Parameters

        _tags_ : `optional list[str]`

        > A list of the tags to look for institutions in

        _seperator_ : `optional str`

        > The string that separators each institutions name within the column

        # Returns

        `list [str]`

        > A list of all the found institution's names
        """
        return self.getInvestigators(tags = tags, seperator = seperator, _getTag = _getTag)

    def update(self, other):
        """Adds all the tag-entry pairs from _other_ to the `Grant`. If there is a conflict _other_ takes precedence.

        # Parameters

        _other_ : `Grant`

        > Another `Grant` of the same type as _self_
        """
        if type(self) != type(other):
            return NotImplemented
        else:
            if other.bad:
                self.error = other.error
                self.bad = True
            self._fieldDict.update(other._fieldDict)

def csvAndLinesReader(enumeratedFile, *csvArgs, **csvKwargs):
    currentData = {
    'currentLineNum' : -1,
    'currentLineString' : '',
    }
    def readerWithSideEffects(target, datDict):
        while True:
            datDict['currentLineNum'], datDict['currentLineString'] = next(target)
            yield datDict['currentLineString']
    reader = csv.DictReader(readerWithSideEffects(enumeratedFile, currentData), *csvArgs, **csvKwargs)
    readerIter = reader.__iter__()
    while True:
        row = next(readerIter)
        yield currentData['currentLineNum'], currentData['currentLineString'], row

class FallbackGrant(Grant):
    """A subclass of [Grant](./grants.html#metaknowledge.grants.Grant), it has the same attributes and is returned from the fall back constructor for grants.
    """
    #Making it a subclass so that Grant is never used raw
    #Also make interface simpler
    def __init__(self, original, grantdDict, sFile = "", sLine = 0):
        #We do not known anything about the structure of the grant so there is nothing to check about causing an error
        #The id needs to be unique so hashing the original will always give us that
        idValue = "{}-l:{}-{:0=20}".format(os.path.basename(sFile), sLine, hash(original))
        Grant.__init__(self, original, grantdDict, idValue, False, None, sFile = sFile, sLine = sLine)

def isFallbackGrantFile(fileName, useFileName = True, encoding = 'latin-1', dialect = 'excel'):
    if useFileName:
        if not fileName.endswith('csv'):
            return False
    try:
        #Try to open it
        with open(fileName, 'r', encoding = encoding) as openfile:
            #See if csv likes it
            reader = csv.DictReader(openfile, fieldnames = None, dialect = dialect)

            #Check that it is not a scopus file
            if len(set(reader.fieldnames) & {'Conference location', 'Conference code', 'ISSN', 'ISBN', 'CODEN', 'PubMed ID', 'Language of Original Document', 'Abbreviated Source Title', 'Document Type', 'Source', 'EID'}) == 11:
                return False
            #Check that every row can be read
            length = 0
            for row in reader:
                length += 1
                #Just wanted to put something here that analysis the row
                #There is probably a better check
                if set(row.keys()) != set(reader.fieldnames):
                    return False
            #Check that there are rows to read
            if length < 1:
                return False
    except (StopIteration, UnicodeDecodeError, csv.Error, TypeError):
        #If any of theses exceptions are raised the nit is defintly not as csv file
        #We do not want to catch everything though as there could be an issue with the code
        return False
    else:
        #IF nothing caused an issue return True
        return True

def parserFallbackGrantFile(fileName, encoding = 'latin-1', dialect = 'excel'):
    #Declare the returns out side of the block to show they are accessible everywhere inside it and so if there are issues with their creation it will no cause a problem with returning them
    grantSet = set()
    error = None
    try:
        with open(fileName, 'r', encoding = encoding) as openfile:
            f = enumerate(openfile, start = 1)
            reader = csvAndLinesReader(f, fieldnames = None, dialect = dialect)
            for lineNum, lineString, lineDict in reader:
                grantSet.add(FallbackGrant(lineString, lineDict, sFile = fileName, sLine = lineNum))
    except Exception:
        if error is None:
            error = BadGrant("The file '{}' is having decoding issues. It may have been modifed since it was downloaded or not be a CIHR grant file.".format(fileName))
    except KeyboardInterrupt as e:
        error = e
    finally:
        if isinstance(error, KeyboardInterrupt):
            raise error
        return grantSet, error
