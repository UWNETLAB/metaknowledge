#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015

import itertools
import io
import collections

from .citation import Citation

monthDict = {'SPR': 3, 'SUM': 6, 'FAL': 9, 'WIN': 12, 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6 , 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12}


class BadISIRecord(Warning):
    """
    Exception thrown by recordParser for mis-formated papers
    """
    pass

def lazy(f):
    """
    A decorator that makes the function be only evaluated once.
    It does this by creating an attribute in the class with the same name as the function and referencing that on successive calls.
    """

    def wrapper(self, *arg, **kwargs):
        if self.bad:
            return None
        if not hasattr(self, "_" + f.__name__):
            setattr(self, "_" + f.__name__, f(self, *arg, **kwargs))
        return getattr(self, "_" + f.__name__)
    return wrapper

class Record(object):
    """
    class for containig full ISI records
    It requires that the record contains a WOS number and have tags for each field.
    """
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
                self._fieldDict = recordParser(enumerate(addChartoEnd(inRecord.split('\n')), start = 1))
                #string io
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
        """
        returns a string with the title of the file as given by self.title(), if there is not one it returns "Untitled record"
        """
        if self.title():
            return self.title()
        else:
            return "Untitled record"

    def __eq__(self, other):
        """
        returns true if the WOS numbers of both Records are identical.
        if either is bad False is returned
        """
        if self.bad or other.bad:
            return False
        else:
            return self.wosString() == other.wosString()

    def __ne__(self, other):
        """
        returns the opposite of __eq__
        """
        return not self == other

    def __hash__(self):
        """
        returns a hash of the WOS number.
        If bad returns a hash of the fields, these could be blank
        bad Records are likely to cause hash collisions
        """
        if self.bad:
            return hash(self._fieldDict.values())
        return hash(self._wosNum)

    def __getstate__(self):
        """
        returns the minimum amount of information to recreate a Record
        """
        sDict = self.__dict__
        for k in sDict:
            if k not in ['bad', 'error', '_sourceFile', '_sourceLine', '_fieldDict', '_wosNum']:
                del sDict[k]
        return sDict

    def __setstate__(self, state):
        self.__dict__ = state

    @lazy
    def authors(self, full = True):
        """
        returns a list of authors
        The optional argument full(defaults to True) if True will cause the AF field to be checked first if False AU is used
        AF or AU tag
        """
        if 'AF' in self._fieldDict and full:
            return self._fieldDict['AF']
        elif 'AU' in self._fieldDict:
            return self._fieldDict['AU']
        else:
            return None

    @lazy
    def year(self):
        """
        returns the year the record was published in as an int
        PY tag
        """
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
        """
        returns the month the record was published in as an int with January as 1, February 2, ...
        PD tag
        """
        if 'PD' in self._fieldDict:
            return getMonth(self._fieldDict['PD'][0])
        else:
            return None
    @lazy
    def title(self):
        """
        returns the title of the record
        TI tag
        """
        if 'TI' in self._fieldDict:
            return ' '.join(self._fieldDict['TI'])
        else:
            return None
    @lazy
    def citations(self):
        """
        returns a list of all the citations in the record
        CR tag
        """
        if 'CR' in self._fieldDict:
            retCites = []
            for c in self._fieldDict['CR']:
                retCites.append(Citation(c))
            return retCites
        else:
            return None

    @lazy
    def journal(self):
        """
        returns the full name of the publication
        SO tag
        """
        if 'SO' in self._fieldDict:
            return ' '.join(self._fieldDict['SO'])
        else:
            return None

    @lazy
    def j9(self):
        """
        returns the J9 (29-Character Source Abbreviation) of the publication
        J9 tag
        """
        if 'J9' in self._fieldDict:
            return self._fieldDict['J9'][0]
        else:
            return None

    @lazy
    def beginningPage(self):
        """
        returns the first page the record occurs on
        BP tag
        """
        if 'BP' in self._fieldDict:
            return int(self._fieldDict['BP'][0])
        else:
            return None

    @lazy
    def endingPage(self):
        """
        return the last page the record occurs on
        EP tag
        """
        if 'EP' in self._fieldDict:
            return int(self._fieldDict['EP'][0])
        else:
            return None

    @lazy
    def volume(self):
        """
        return the volume the record is in
        VL tag
        """
        if 'VL' in self._fieldDict:
            return int(self._fieldDict['VL'][0])
        else:
            return None

    @lazy
    def getTag(self, tag):
        """
        returns a list containing the raw data of the record assocaited ith tag.
        Each line of the record is one string in the list.
        """
        if tag in self._fieldDict:
            return self._fieldDict[tag]
        else:
            return None

    @lazy
    def DOI(self):
        """
        return the DOI number of the record
        DI tag
        """
        if 'DI' in self._fieldDict:
            return self._fieldDict['DI'][0]
        else:
            return None

    def createCitation(self):
        valsLst = []
        if self.authors():
            valsLst.append(self.authors(full = False)[0])
        if self.year():
            valsLst.append(str(self.year()))
        if self.j9():
            valsLst.append(self.j9())
        if self.volume():
            valsLst.append('V' + str(self.volume()))
        if self.beginningPage():
            valsLst.append('P' + str(self.beginningPage()))
        if self.DOI():
            valsLst.append('DOI ' + self.DOI())
        return Citation(', '.join(valsLst))

    def getTagsList(self, taglst):
        """"
        returns a list of the results of getTag for each tag in taglist, it has the same order as the original.
        """
        retList = []
        for tag in taglst:
            retList.append(self.getTag(tag))
        return retList

    def getTagsDict(self, taglst):
        """"
        returns a dict of the results of getTag, with the elements of taglist as the keys and the results as the values.
        """
        retDict = {}
        for tag in taglst:
            retDict[tag] = self.getTag(tag)
        return retDict

    def wosString(self):
        """
        returns the WOS number of the record as a string preceeded by "WOS:""
        UT tag
        """
        return self._wosNum

    def writeRecord(self, infile):
        """
        writes to infile the origninal contents of the Record
        """
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
    tagList = []
    for l in paper:
        if len(l[1]) < 3:
            raise BadISIRecord("Missing field on line " + str(l[0]) + " : " + l[1])
        elif 'ER' in l[1][:2]:
            return  collections.OrderedDict(tagList)
        elif '   ' in l[1][:3]: #the string is three spaces in row
            tagList[-1][1].append(l[1][3:-1])
        elif l[1][2] == ' ':
            tagList.append((l[1][:2], [l[1][3:-1]]))
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
