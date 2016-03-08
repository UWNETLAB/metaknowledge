#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""This file contains the Record class for metaknowledge and one helper function for parsing WOS records, recordParser. The record class is used to represent a single records meta-data from WOS.
"""
import itertools
import io
import collections

from ..mkRecord import ExtendedRecord

from ..WOS.tagProcessing.funcDicts import tagNameConverterDict, tagToFull
from ..WOS.tagProcessing.tagFunctions import tagToFunc
from ..mkExceptions import BadWOSFile, BadWOSRecord

class WOSRecord(ExtendedRecord):
    """Class for full WOS records

    It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored privately.

    The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [**Tag**()](#Record.Tag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

    # Customizations

    The `Record`'s hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with `'WOS:'` and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

    When converted to a string the records title is used so for a record `R`, `R.TI == R.title == str(R)` and its representation uses the WOS number instead of memory location.

    # Attributes

    When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

    Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [**citations**()](#tagProcessing.citations) from the the [tagProcessing](#tagProcessing.tagProcessing) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](#metaknowledge.metaknowledge)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

    The attribute `authors` is also defined as a connivence and returns the same as 'AF' or if that is not found 'AU'.

    # \_\_Init\_\_

    Records are generally create as collections in  [Recordcollections](#RecordCollection.RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

    # Parameters

    _inRecord_: `files stream, dict, str or itertools.chain`

    > If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

    > If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](#metaknowledge.recordParser) returns.

    > For a string the input must be the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in `'ER'`.

    > itertools.chain is treated identically to a file stream and is used by [RecordCollections](#RecordCollection.RecordCollection).

    _sFile_ : `optional [str]`

    > Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

    _sLine_ : `optional [int]`

    > Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.
    """

    def __init__(self, inRecord, sFile = "", sLine = 0):
        """See help on [Record](#Record.Record) for details"""
        bad = False
        error = None
        fieldDict = None
        try:
            if isinstance(inRecord, dict) or isinstance(inRecord, collections.OrderedDict):
                fieldDict = collections.OrderedDict(inRecord)
            elif isinstance(inRecord, itertools.chain):
                fieldDict = recordParser(inRecord)
            elif isinstance(inRecord, io.IOBase):
                fieldDict = recordParser(enumerate(inRecord))
            elif isinstance(inRecord, str):
                def addChartoEnd(lst):
                    for s in lst:
                        yield s + '\n'
                fieldDict = recordParser(enumerate(addChartoEnd(inRecord.split('\n')), start = 1))
                #string io
            else:
                raise TypeError("Unsupported input type '{}', WOSRecords cannot be created from '{}'".format(inRecord, type(inRecord)))
        except BadWOSRecord as b:
            self.bad = True
            self.error = b
            fieldDict = collections.OrderedDict()
        if fieldDict is not None:
            if 'UT' in fieldDict:
                self._wosNum = fieldDict['UT'][0]
            else:
                self._wosNum = 'WOS:Missing'
                bad = True
                error = BadWOSRecord("Missing WOS number")
        ExtendedRecord.__init__(self, fieldDict, self._wosNum, bad, error, sFile = sFile, sLine = sLine)

    @property
    def encoding(self):
        return 'utf-8'

    @staticmethod
    def getAltName(tag):
        return tagNameConverterDict.get(tag)

    @staticmethod
    def tagProccessingFunc(tag):
        return tagToFunc.get(tag, lambda x: x)

    def specialFuncs(self, key):
        if key == 'selfCitation':
            #this cannot be computed until after the Record is created
            return self.createCitation()
        elif key == 'grants':
            return None
        else:
            raise KeyError("WOS Records do not have any special functions besides 'grants', they are what the special functions are mostly based on.")

    @property
    def wosString(self):
        """Returns the WOS number (UT tag) of the record"""
        return self._wosNum

    @property
    def UT(self):
        """Returns the UT tag (WOS number) of the record"""
        return self._wosNum

    def writeRecord(self, infile):
        """Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections](#RecordCollection.RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file (if utf-8 is used). No newline is inserted above the write but the last character is a newline.

        # Parameters

        _infile_ : `file stream`

        > An open utf-8 encoded file
        """
        if self.bad:
            raise BadWOSRecord("This record cannot be converted to a file as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        else:
            for tag in self._fieldDict.keys():
                for i, value in enumerate(self._fieldDict[tag]):
                    if i == 0:
                        infile.write(tag + ' ')
                    else:
                        infile.write('   ')
                    infile.write(value + '\n')
            infile.write("ER\n")

    def bibString(self, maxLength = 1000, WOSMode = False, restrictedOutput = False, niceID = True):
        """Makes a string giving the Record as a bibTex entry. If the Record is of a journal article (`PT J`) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

        **Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier.

        **Note** Record entries that are lists have their values seperated with the string `' and '`

        # Parameters

        _maxLength_ : `optional [int]`

        > default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

        _WOSMode_ : `optional [bool]`

        > default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

        _restrictedOutput_ : `optional [bool]`

        > default `False`, if `True` the tags output will be limited to: `'AF'`, `'BF'`, `'ED'`, `'TI'`, `'SO'`, `'LA'`, `'NR'`, `'TC'`, `'Z9'`, `'PU'`, `'J9'`, `'PY'`, `'PD'`, `'VL'`, `'IS'`, `'SU'`, `'PG'`, `'DI'`, `'D2'`, and `'UT'`

        _niceID_ : `optional [bool]`

        > default `True`, if `True` the ID used will be derived from the authors, publishing date and title, if `False` it will be the UT tag

        # Returns

        `str`

        > The bibTex string of the Record
        """
        restrictedTags = ['AF', 'BF', 'ED', 'TI', 'SO', 'LA', 'NR', 'TC','Z9','PU','J9','PY','PD','VL','IS','SU','PG', 'DI','D2','UT']
        keyEntries = []
        if self.bad:
            raise BadWOSRecord("This record cannot be converted to a bibtex entry as the input was malformed.\nThe original line number (if any) is: {} and the original file is: '{}'".format(self._sourceLine, self._sourceFile))
        texType = self.bibTexType()
        if niceID:
            if self.get('authorsFull'):
                bibID = self['authorsFull'][0].title().replace(' ', '').replace(',', '').replace('.','')
            else:
                bibID = ''
            if self.get('year'):
                bibID += '-' + str(self['year'])
            if self.get('month'):
                bibID += '-' + str(self['month'])
            if self.get('title'):
                tiSorted = sorted(self['title'].split(' '), key = len)
                bibID += '-' + tiSorted.pop().title()
                while len(bibID) < 35 and len(tiSorted) > 0:
                    bibID += '-' + tiSorted.pop().title() #Title Case
            if len(bibID) < 30:
                bibID += str(self.id)
        elif WOSMode:
            bibID = 'ISI:{}'.format(self.id[4:])
        else:
            bibID = str(self.id)
        if WOSMode:
            for tag, value in self.items():
                if restrictedOutput and tag not in restrictedTags:
                    pass
                elif tag == 'AF':
                    keyEntries.append("{} = {{{{{}}}}},".format('author',' and '.join(value)))
                elif isinstance(value, list):
                    keyEntries.append("{} = {{{{{}}}}},".format(tagToFull(tag),'\n   '.join(value)))
                else:
                    keyEntries.append("{} = {{{{{}}}}},".format(tagToFull(tag), value))
            s = """@{0}{{ {1},\n{2}\n}}""".format(texType, bibID, '\n'.join(keyEntries))
        else:
            tagsList = []
            for tag in self.keys():
                try:
                    if restrictedOutput and tag not in restrictedTags:
                        pass
                    else:
                        tagsList.append(tagToFull(tag))
                except KeyError:
                    tagsList.append(tag)
            for tagName in tagsList:
                keyEntries.append("{} = {},".format(tagName, _bibFormatter(self.get(tagName), maxLength)))
            s = """@{0}{{ {1},\n    {2}\n}}""".format(texType, bibID, '\n    '.join(keyEntries))
        return s

    def bibTexType(self):
        """Returns the bibTex type corresonding to the record

        # Returns

        `str`

        > The bibTex type string
        """
        mappingDict = {
            'Article' : 'article',
            'Proceedings Paper' : 'proceedings',
            'Meeting Abstract' : 'inproceedings',
            'Book' : 'book',
        }
        if self['DT'] in mappingDict:
            return mappingDict[self['DT']]
        else:
            return 'misc'

def _bibFormatter(s, maxLength):
    """Formats a string, list or number to make it good for a bib file by:
        * if too long splits up the string correctly
        * tries to use the best quoting characters
        * expands lists into ' and ' seperated values, as per spec for authors field
    Note, this does not escape characters. LaTeX may have issues with the output
    Max length splitting derived from https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html
    """
    if isinstance(s, list):
        s = ' and '.join((str(v) for v in s))
    elif not isinstance(s, str):
        s = str(s)
    if len(s) > maxLength:
        s = s.replace('"', '')
        s = [s[i * maxLength: (i + 1) * maxLength] for i in range(len(s) // maxLength )]
        s = '"{}"'.format('" # "'.join(s))
    elif '"' not in s:
        s = '"{}"'.format(s)
    else:
        s = s.replace('{', '\\{').replace('}', '\\}')
        s = '{{{}}}'.format(s)
    return s

def recordParser(paper):
    """This is function that is used to create [`Records`](#metaknowledge.Record) from files.

    **recordParser**() reads the file _paper_ until it reaches 'ER'. For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following two lines in a record:

        AF BREVIK, I
           ANICIN, B

    The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

    `Record` objects can be created with these dictionaries as the initializer.

    # Parameters

    _paper_ : `file stream`

    > An open file, with the current line at the beginning of the WOS record.

    # Returns

    `OrderedDict[str : List[str]]`

    > A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.
    """
    tagList = []
    doneReading = False
    l = (0, '')
    for l in paper:
        if len(l[1]) < 3:
            #Line too short
            raise BadWOSRecord("Missing field on line {} : {}".format(l[0], l[1]))
        elif 'ER' in l[1][:2]:
            #Reached the end of the record
            doneReading = True
            break
        elif l[1][2] != ' ':
            #Field tag longer than 2 or offset in some way
            raise BadWOSFile("Field tag not formed correctly on line " + str(l[0]) + " : " + l[1])
        elif '   ' in l[1][:3]: #the string is three spaces in row
            #No new tag append line to current tag (last tag in tagList)
            tagList[-1][1].append(l[1][3:-1])
        else:
            #New tag create new entry at the end of tagList
            tagList.append((l[1][:2], [l[1][3:-1]]))
    if not doneReading:
        raise BadWOSRecord("End of file reached before ER: {}".format(l[1]))
    else:
        retdict = collections.OrderedDict(tagList)
        if len(retdict) == len(tagList):
            return retdict
        else:
            dupSet = set()
            for tupl in tagList:
                if tupl[0] in retdict:
                    dupSet.add(tupl[0])
            raise BadWOSRecord("Duplicate tags (" + ', '.join(dupSet) + ") in record")
