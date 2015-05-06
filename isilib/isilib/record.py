#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015

import itertools
import io

monthDict = {'SPR': 3, 'SUM': 6, 'FAL': 9, 'WIN': 12, 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6 , 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12}


class BadISIRecord(Warning):
    """
    Exception thrown by recordParser for mis-formated papers
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
        elif isinstance(inRecord, itertools.chain):
            try:
                self._fieldDict = recordParser(inRecord)
            except BadISIRecord as b:
                self.bad = True
                self.error = b
            finally:
                if 'UT' in self._fieldDict:
                    self._wosNum = self._fieldDict['UT'][0]
                else:
                    self._wosNum = None
                    self.bad = True
                    self.error = BadISIRecord("Missing WOS number")
        elif isinstance(inRecord, io.IOBase):
            try:
                self._fieldDict = recordParser(enumerate(inRecord))
            except BadISIRecord as b:
                self.bad = True
                self.error = b
                self._fieldDict = {}
            finally:
                if 'UT' in self._fieldDict:
                    self._wosNum = self._fieldDict['UT'][0]
                else:
                    self._wosNum = None
                    self.bad = True
                    self.error = BadISIRecord("Missing WOS number")
        elif isinstance(inRecord, str):
            try:
                def addChartoEnd(lst):
                    for s in lst:
                        yield s + '\n'
                self._fieldDict = recordParser(enumerate(addChartoEnd(inRecord.split('\n'))))
            except BadISIRecord as b:
                self.bad = True
                self.error = b
                self._fieldDict = {}
            finally:
                if 'UT' in self._fieldDict:
                    self._wosNum = self._fieldDict['UT'][0]
                else:
                    self._wosNum = None
                    self.bad = True
                    self.error = BadISIRecord("Missing WOS number")


        else:
            raise TypeError

    def __str__(self):
        if self.title():
            return self.title()
        else:
            return "Untitled record"

    def __eq__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return self.wosString() == other.wosString()

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        if self.bad:
            return hash(self._fieldDict.values())
        return hash(self._wosNum)

    def __getstate__(self):
        return (self.bad, self.error, self._sourceFile, self._sourceLine, self._fieldDict)

    def __setstate__(self, state):
        self.bad = state[0]
        self.error = state[1]
        self._sourceFile = state[2]
        self._sourceLine = state[3]
        self._fieldDict = state[4]

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
            yearField = self._fieldDict['PY'][0]
            if len(yearField) == 4:
                return int(yearField)
            else:
                raise Exception
        else:
            return None
    @lazy
    def month(self):
        if 'PD' in self._fieldDict:
            return getMonth(self._fieldDict['PD'][0])
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

    def wosString(self):
        return self._wosNum

    def writeRecord(self, infile):
        if self.bad:
            raise exception
        else:
            for tag in self._fieldDict.keys():
                for i, value in enumerate(self._fieldDict[tag]):
                    if i == 0:
                        infile.write(tag + ' ')
                    else:
                        infile.write('   ')
                    infile.write(value + '\n')
            infile.write("ER\n")

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

def getMonth(s):
    """

    Known formats:
    Month ("%b")
    Month Day ("%b %d")
    Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
    Season ("%s") --- this gets coerced to use the first month of the given season
    Month Day Year ("%b %d %Y")
    Month Year ("%b %Y")

    """
    monthOrSeason = s.split(' ')[0].split('-')[0].upper()
    if monthOrSeason in monthDict:
        return monthDict[monthOrSeason]
    else:
        raise ValueError("Month format not recognized: " + s)
