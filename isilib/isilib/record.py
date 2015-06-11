#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015

import itertools
import io
import collections

from .citation import Citation
from .constants import tagNameConverter, tagsAndNames
from .recordTagFunctions import tagToFunc

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
    class for containing full ISI records
    It requires that the record contains a WOS number and have tags for each field.
    """
    def __init__(self, inRecord, taglist = (), sFile = '', sLine = 0):
        self._unComputedTags = set()
        self.bad = False
        self.error = None
        self.tags = taglist
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
                if hasattr(self, '_fieldDict') and 'UT' in self._fieldDict:
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
                    self._wosNum = "NO WOS NUMBER"
                    self.bad = True
                    self.error = BadISIRecord("Missing WOS number")
        for tag in self._fieldDict:
            if tag != 'UT':
                self.__dict__[tag] = None
                self._unComputedTags.add(tag)
                try:
                    fullName = tagNameConverter[tag]
                except KeyError:
                    pass
                else:
                    self.__dict__[fullName] = None
                    self._unComputedTags.add(fullName)

    def __getattribute__(self, name):
        try:
            val = object.__getattribute__(self, name)
        except AttributeError:
            if name in tagsAndNames:
                return None
            else:
                raise
        else:
            if val != None:
                return val
            else:
                if name in self._unComputedTags:
                    try:
                        otherName = tagNameConverter[name]
                    except KeyError:
                        try:
                            tagVal = tagToFunc[name](self._fieldDict[name])
                        except KeyError:
                            tagVal = self._fieldDict[name]
                        setattr(self, name, tagVal)
                        self._unComputedTags.remove(name)
                    else:
                        try:
                            prossFunc = tagToFunc[name]
                        except KeyError:
                            try:
                                prossFunc = tagToFunc[otherName]
                            except KeyError:
                                prossFunc = lambda x: x
                        try:
                            tagVal = prossFunc(self._fieldDict[name])
                        except KeyError:
                            tagVal = prossFunc(self._fieldDict[otherName])
                        object.__setattr__(self, name, tagVal)
                        object.__setattr__(self, otherName, tagVal)
                        self._unComputedTags.remove(name)
                        self._unComputedTags.remove(otherName)
                return object.__getattribute__(self, name)


    def __str__(self):
        """
        returns a string with the title of the file as given by self.title(), if there is not one it returns "Untitled record"
        """
        if self.title:
            return self.title
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
            return self.wosString == other.wosString

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
        return self.__dict__

    def __setstate__(self, state):
        """
        This is nessary because __getattribute__ is overwritten
        """
        for k in state:
            object.__setattr__(self, k, state[k])

    @property
    def wosString(self):
        return self._wosNum

    @property
    def UT(self):
        return self._wosNum

    def getTag(self, tag):
        """
        returns a list containing the raw data of the record associated with tag.
        Each line of the record is one string in the list.
        """
        if tag in self._fieldDict:
            return self._fieldDict[tag]
        else:
            return None

    def createCitation(self):
        valsLst = []
        if self.authorsShort:
            valsLst.append(self.authorsShort[0].replace(',', ''))
        if getattr(self, "year", False):
            valsLst.append(str(self.year))
        if getattr(self, "j9", False):
            valsLst.append(self.j9)
        if getattr(self, "volume", False):
            valsLst.append('V' + str(self.volume))
        if getattr(self, "beginningPage", False):
            valsLst.append('P' + str(self.beginningPage))
        if getattr(self, "DOI", False):
            valsLst.append('DOI ' + self.DOI)
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

    def writeRecord(self, infile):
        """
        writes to infile the original contents of the Record
        """
        if self.bad:
            raise Exception
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
    For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately
    """
    tagList = []
    for l in paper:
        if len(l[1]) < 3:
            raise BadISIRecord("Missing field on line " + str(l[0]) + " : " + l[1])
        elif 'ER' in l[1][:2]:
            return  collections.OrderedDict(tagList)
        elif l[1][2] != ' ':
            raise BadISIFile("Field tag not formed correctly on line " + str(l[0]) + " : " + l[1])
        elif '   ' in l[1][:3]: #the string is three spaces in row
            tagList[-1][1].append(l[1][3:-1])
        else:
            tagList.append((l[1][:2], [l[1][3:-1]]))
    raise BadISIRecord("End of file reached before EF")
