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

    The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [tags()](./CollectionWithIDs.html#metaknowledge.CollectionWithIDs.tags) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

    # Customizations

    The `Record`'s hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with `'WOS:'` and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

    When converted to a string the records title is used so for a record `R`, `R.TI == R.title == str(R)` and its representation uses the WOS number instead of memory location.

    # Attributes

    When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

    Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [citations()](../modules/WOS.html#metaknowledge.WOS.tagProcessing.tagFunctions.citations) from the the [tagProcessing](../modules/WOS.html#module-metaknowledge.WOS.tagProcessing.helpFuncs) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](../modules/WOS.html#metaknowledge.WOS.tagProcessing.funcDicts.tagToFull)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

    The attribute `authors` is also defined as a convenience and returns the same as 'AF' or if that is not found 'AU'.

    # \_\_Init\_\_

    Records are generally created as collections in  [Recordcollections](./RecordCollection.html#metaknowledge.RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

    # Parameters

    _inRecord_: `files stream, dict, str or itertools.chain`

    > If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

    > If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](../modules/WOS.html#metaknowledge.WOS.recordWOS.recordParser) returns.

    > For a string the input must be the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in `'ER'`.

    > itertools.chain is treated identically to a file stream and is used by [RecordCollections](./RecordCollection.html#metaknowledge.RecordCollection).

    _sFile_ : `optional [str]`

    > Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

    _sLine_ : `optional [int]`

    > Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.
    """

    def __init__(self, inRecord, sFile = "", sLine = 0):
        """See help on [Record](./Record.html#metaknowledge.Record) for details"""
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

    def encoding(self):
        return 'utf-8'

    @staticmethod
    def getAltName(tag):
        return tagNameConverterDict.get(tag)

    @staticmethod
    def tagProcessingFunc(tag):
        return tagToFunc.get(tag, lambda x: x)

    def specialFuncs(self, key):
        if key == 'selfCitation':
            #this cannot be computed until after the Record is created
            return self.createCitation()
        elif key == 'id':
            return self.id
        elif key == 'grants':
            return []
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
        """Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections](./RecordCollection.html#metaknowledge.RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file (if utf-8 is used). No newline is inserted above the write but the last character is a newline.

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

def recordParser(paper):
    """This is function that is used to create [Records](../classes/Record.html#metaknowledge.Record) from files.

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
