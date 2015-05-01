#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015

import itertools
import io

class BadISIRecord(Warning):
    """
    Exception thrown by recordParser for mis-formated papers
    """
    pass

class BadISIFile(Warning):
    """
    Exception thrown by isiParser for mis-formated files
    """
    pass

def lazy(f):
    def wrapper(self, *arg, **kwargs):
        if self.bad:
            return None
        if not hasattr(self, "_" + f.__name__):
            setattr(self, "_" + f.__name__, f(self, *arg, **kwargs))
        return getattr(self, "_" + f.__name__)
    return wrapper

class Record(object):
    def __init__(self, inRecord, sFile = '', sLine = 0):
        self.bad = False
        self.error = None
        self._sourceFile = sFile
        self._sourceLine = sLine
        if isinstance(inRecord, dict):
            self._fieldDict = inRecord
        elif isinstance(inRecord, io.IOBase) or isinstance(inRecord, itertools.chain):
            try:
                self._fieldDict = recordParser(inRecord)
            except BadISIRecord as b:
                self.bad = True
                self.error = b
        else:
            raise TypeError
    @lazy
    def authors(self):
        if 'AF' in self._fieldDict:
            return self._fieldDict['AF']
        elif 'AU' in self._fieldDict:
            return self._fieldDict['AU']
        else:
            return None

    @lazy
    def year(self):
        if 'PY' in self._fieldDict:
            return self._fieldDict['PY'][0]
        else:
            return None
    @lazy
    def month(self):
        if 'PD' in self._fieldDict:
            return self._fieldDict['PD'][0]
        else:
            return None
    @lazy
    def title(self):
        if 'TI' in self._fieldDict:
            return ' '.join(self._fieldDict['TI'])
        else:
            return None
    @lazy
    def citations(self):
        if 'CR' in self._fieldDict:
            return self._fieldDict['CR']
        else:
            return None

def recordParser(paper):
    """
    recordParser() reads the file paper until it reaches 'EF'.
    For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line seperately
    """
    tdict = {}
    currentTag = ''
    for l in paper:
        if 'ER' in l[1][:2]:
            return tdict
        elif '   ' in l[1][:3]: #the string is three spaces in row
            tdict[currentTag].append(l[1][3:-1])
        elif l[1][2] == ' ':
            currentTag = l[1][:2]
            tdict[currentTag] = [l[1][3:-1]]
        else:
            raise BadISIRecord("Field tag not formed correctly on line " + str(l[0]) + " : " + l[1])
    raise BadISIRecord("End of file reached before EF on line " + str(l[0]))
