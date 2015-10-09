#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""This file contains the Record class for metaknowledge and one helper function for parsing WOS records, recordParser. The record class is used to represent a single records meta-data from WOS.
"""
import itertools
import io
import collections

from .citation import Citation
from .constants import tagNameConverter, tagsAndNames, fullToTag
from .tagFuncs import tagToFunc

class BadISIRecord(Warning):
    """Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

        * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

        * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

        * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

        * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

    Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.
    """
    pass

class BadISIFile(Warning):
    """
    Exception thrown by isiParser for mis-formated files
    """
    pass

class Record(object):
    """
    Class for full WOS records

    It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored in a private dictionary.

    The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [getTag()](#Record.getTag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

    # Customizations

    The Record's hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with "WOS:" and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

    When converted to a string the records title is used so for a record `R`, R.TI == R.title == str(R).

    # Attributes

    When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

    Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [citations()](#tagFuncs.citations) from the the [tagFuncs](#tagFuncs.tagFuncs) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](#metaknowledge.metaknowledge)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

    The attribute `authors` is also defined as a convience and returns the same as 'AF' or if that is not found 'AU'.

    # \_\_Init\_\_

    Records are generally create as collections in  [Recordcollections](#RecordCollection.RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

    # Parameters

    _inRecord_: `files stream, dict, str or itertools.chain`

    > If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

    > If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](#metaknowledge.recordParser) returns.

    > For a str the input is the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in 'ER'.

    > itertools.chain is treated identically to a file stream and is used by [RecordCollections](#RecordCollection.RecordCollection).

    _sFile_ : `optional [str]`

    > Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

    _sLine_ : `optional [int]`

    > Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.
    """

    def __init__(self, inRecord, taglist = (), sFile = "", sLine = 0):
        """See help on [Record](#Record.Record) for details"""
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
                self._fieldDict = {}
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
        if hasattr(self, "_fieldDict"):
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
        """
        Hack to get the attributes correct, read the Record help for more information
        """
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
        if not isinstance(other, Record):
            raise RuntimeError("Equality checking between Records and non-Records is not implemented")
        if self.bad or other.bad:
            return False
        else:
            return self.wosString == other.wosString

    def __ne__(self, other):
        """returns the opposite of \_\_eq\_\_"""
        return not self == other

    def __hash__(self):
        """returns a hash of the WOS number or if `bad` returns a hash of the fields combined with the error messages, either of these could be blank

        `bad` Records are more likely to cause hash collisions due to their lack of entropy when created.
        """
        if self.bad:
            return hash(str(self._fieldDict.values()) + str(self.error))
        return hash(self._wosNum)

    def __getstate__(self):
        """gets the __dict__ of the Record"""
        return self.__dict__

    def __setstate__(self, state):
        """This is necessary because __getattribute__ is overwritten, but works like \_\_setstate\_\_ usually does"""
        for k in state:
            object.__setattr__(self, k, state[k])

    @property
    def wosString(self):
        """Returns the WOS number (UT tag) of the record"""
        return self._wosNum

    @property
    def UT(self):
        """Returns the UT tag (WOS number) of the record"""
        return self._wosNum

    @property
    def authors(self):
        """Returns the full names of the authors (AF tag) if available otherwise attempts to use their shorter names (AU tag) if that fails None is returned
        Usually another way of calling authorsFull or AF
        """
        auth = self.authorsFull
        if auth is None:
            return self.authorsShort
        else:
            return auth

    def getTag(self, tag, clean = False):
        """Returns a list containing the raw data of the record associated with _tag_. Each line of the record is one string in the list.

        # Parameters

        _tag_ : `str`

        > _tag_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag](#metaknowledge). If the string is not found in the original record or after being translated through [fullToTag](#metaknowledge), `None` is returned.

        # Returns

        `List [str]`

        > Each string in the list is a line from the record associated with _tag_ or None if not found.
        """

        #tag = tag.upper()
        #TODO Figure out why this causes issues
        if clean:
            return getattr(self, tag.upper(), None)
        if tag in self._fieldDict:
            return self._fieldDict[tag]
        elif tag in fullToTag and fullToTag[tag] in self._fieldDict:
            return self._fieldDict[fullToTag[tag]]
        else:
            return None

    def createCitation(self):
        """Creates a citation string, using the same format as other WOS citations, for the [Record](#Record.Record) by reading the relevant tags (year, J9, volume, beginningPage, DOI) and using it to start a [Citation](#Citation.Citation) object.

        # Returns

        `Citation`

        > A [Citation](#Citation.Citation) object containing a citation for the Record.
        """
        valsLst = []
        if self.authorsShort:
            valsLst.append(self.authorsShort[0].replace(',', ''))
        if getattr(self, "year", False):
            valsLst.append(str(self.year))
        if getattr(self, "j9", False):
            valsLst.append(self.j9)
        elif getattr(self, "TI", False):
            valsLst.append(self.TI)
        if getattr(self, "volume", False):
            valsLst.append('V' + str(self.volume))
        if getattr(self, "beginningPage", False):
            valsLst.append('P' + str(self.beginningPage))
        if getattr(self, "DOI", False):
            valsLst.append('DOI ' + self.DOI)
        return Citation(', '.join(valsLst))

    def getTagsList(self, taglst, cleaned = False):
        """Returns a list of the results of [`getTag()`](#Record.getTag) for each tag in _taglist_, the return has the same order as the original.

        # Parameters
        _taglst_ : `List[str]`

        > Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag](#metaknowledge.metaknowledge). If the string is not found in the original record before or after being translated through [fullToTag](#metaknowledge.metaknowledge), `None` is used instead. Same as in [`getTag()`](#Record.getTag)

        > Then they are compiled into a list in the same order as _taglst_

        # Returns

        `List[str]`

        > a list of the values for each tag in _taglst_, in the same order
        """
        retList = []
        for tag in taglst:
            retList.append(self.getTag(tag), clean = cleaned)
        return retList

    def getTagsDict(self, taglst, cleaned = False):
        """returns a dict of the results of getTag, with the elements of _taglst_ as the keys and the results as the values.

        # Parameters
        _taglst_ : `List[str]`

        > Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag](#metaknowledge.metaknowledge). If the string is not found in the oriagnal record before or after being translated through [fullToTag](#metaknowledge), `None` is used instead. Same as in [`getTag()`](#Record.getTag)

        # Returns

        `dict[str : List [str]]`

        > a dictionary with keys as the original tags in _taglst_ and the values as the results
        """
        retDict = {}
        for tag in taglst:
            retDict[tag] = self.getTag(tag, clean = cleaned)
        return retDict

    def activeTags(self):
        """Returns a list of all the tags the original WOS record had. These are all the tags that ['getTag()'](#Record.getTag) will not return `None` for.

        # Returns

        `List[str]`

        > a list of WOS tags in the Record
        """
        return list(self._fieldDict.keys())

    def writeRecord(self, infile):
        """Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections](#RecordCollection.RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file. No newline is inserted above the write but the last character is a newline.

        # Parameters

        _infile_ : `file stream`

        > An open utf-8 encoded file
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
    """Reads the file _paper_ until it reaches 'ER'.

    For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

    "AF BREVIK, I

        ANICIN, B"

    The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

    [Record](#metaknowledge.Record) objects can be created with these dictionaries as the initializer.

    # Parameters

    _paper_ : `file stream`

    > An open file, with the current line at the beginning of the record.

    # Returns

    `dict[str : List[str]]`

    > A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.
    """
    tagList = []
    doneReading = False
    for l in paper:
        if len(l[1]) < 3:
            #Line too short
            raise BadISIRecord("Missing field on line " + str(l[0]) + " : " + l[1])
        elif 'ER' in l[1][:2]:
            #Reached the end of the record
            doneReading = True
            break
        elif l[1][2] != ' ':
            #Field tag longer than 2 or offset in some way
            raise BadISIFile("Field tag not formed correctly on line " + str(l[0]) + " : " + l[1])
        elif '   ' in l[1][:3]: #the string is three spaces in row
            #No new tag append line to current tag (last tag in tagList)
            tagList[-1][1].append(l[1][3:-1])
        else:
            #New tag create new entry at the end of tagList
            tagList.append((l[1][:2], [l[1][3:-1]]))
    if not doneReading:
        raise BadISIRecord("End of file reached before ER: " + l[1])
    else:
        retdict = collections.OrderedDict(tagList)
        if len(retdict) == len(tagList):
            return retdict
        else:
            dupSet = set()
            for tupl in tagList:
                if tupl[0] in retdict:
                    dupSet.add(tupl[0])
            raise BadISIRecord("Duplicate tags (" + ', '.join(dupSet) + ") in record")
