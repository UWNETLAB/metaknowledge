import itertools
import io

class BadISIRecord(Warning):
    """
    Exception thrown by paperParser and isiParser for mis-formated papers
    """
    pass

class BadISIFile(Warning):
    """
    Exception thrown by paperParser and isiParser for mis-formated papers
    """
    pass

class Record(object):
    def __init__(self, inRecord):
        self.bad = False
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

class RecordCollection(object):
    def __init__(self, inCollection):
        if type(inCollection) == str:
            try:
                self._Records = isiParser(inCollection)
            except:
                raise
        else:
            raise TypeError

"""
    def authors(self):
        Uses AF then AU fields

        print "SEGDRDGGFGDFGD"
        if 'AF' in self._fieldDict:
            self._authors = self._fieldDict['AF']
        elif 'AU' in self._fieldDict:
            self._authors = self._fieldDict['AU']
        else:
            self._authors = None
        return self._authors
"""

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

def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reachs EF.
    Each it finds is used to initilize a Record then all Record are returned as a list.
    """
    f = enumerate(open(isifile, 'r'), start = 0)
    if "VR 1.0" not in f.__next__()[1] and "VR 1.0" not in f.__next__()[1]:
        raise BadISIFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
    notEnd = True
    plst = []
    while notEnd:
        try:
            line = f.__next__()
        except StopIteration as e:
            raise BadISIFile("File ends before EF found")
        if not line[1]:
            raise BadISIFile("No ER found in " + isifile)
        elif line[1].isspace():
            continue
        elif 'EF' in line[1][:2]:
            notEnd = False
            continue
        else:
            try:
                plst.append(Record(itertools.chain([line], f)))
            except Exception as e:
                 raise e
    try:
        f.next()
        raise BadISIFile("EF not at end of " + isifile)
    except StopIteration as e:
        pass
    finally:
        return plst
