import itertools

from .recordWOS import WOSRecord
from ..mkExceptions import cacheError, BadWOSFile, BadWOSRecord

def isWOSFile(infile, checkedLines = 3):
    """Determines if _infile_ is the path to a WOS file. A file is considerd to be a WOS file if it has the correct encoding (`utf-8` with a BOM) and within the first _checkedLines_ a line starts with `"VR 1.0"`.

    # Parameters

    _infile_ : `str`

    > The path to the targets file

    _checkedLines_ : `optional [int]`

    > default 2, the number of lines to check for the header

    # Returns

    `bool`

    > `True` if the file is a WOS file
    """
    try:
        with open(infile, 'r', encoding='utf-8-sig') as openfile:
            f = enumerate(openfile, start = 0)
            for i in range(checkedLines):
                if "VR 1.0" in f.__next__()[1]:
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False

def wosParser(isifile):
    """This is a function that is used to create [RecordCollections](../classes/RecordCollection.html#metaknowledge.RecordCollection) from files.

    **wosParser**() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [recordParser()](#metaknowledge.WOS.recordWOS.recordParser) and converted into [Records](../classes/Record.html#metaknowledge.Record). A list of these `Records` is returned.

    `BadWOSFile` is raised if an issue is found with the file.

    # Parameters

    _isifile_ : `str`

    > The path to the target file

    # Returns

    `List[Record]`

    > All the `Records` found in _isifile_
    """
    plst = set()
    error = None
    try:
        with open(isifile, 'r', encoding='utf-8-sig') as openfile:
            f = enumerate(openfile, start = 0)
            while "VR 1.0" not in f.__next__()[1]:
                pass
            notEnd = True
            while notEnd:
                line = f.__next__()
                if line[1] == '':
                    error =  BadWOSFile("'{}' does not have an 'EF', lines 1 to {} were checked".format(isifile, line[0] + 1))
                elif line[1].isspace():
                    continue
                elif 'EF' in line[1][:2]:
                    notEnd = False
                    continue
                else:
                    try:
                        plst.add(WOSRecord(itertools.chain([line], f), sFile = isifile, sLine = line[0]))
                    except BadWOSFile as e:
                        try:
                            s = f.__next__()[1]
                            while s[:2] != 'ER':
                                s = f.__next__()[1]
                        except:
                            error =  BadWOSFile("The file {} was not terminated corrrectly caused the following error:\n{}".format(isifile, str(e)))
            try:
                f.__next__()
            except StopIteration:
                pass
            else:
                error =  BadWOSFile("EF not at end of " + isifile)
    except UnicodeDecodeError:
        try:
            error =  BadWOSFile("'{}' has a unicode issue on line: {}.".format(isifile, f.__next__()[0]))
        except:
            #Fallback needed incase f.__next__() causes issues
            error =  BadWOSFile("'{}' has a unicode issue. Probably when being opened or possibly on the first line".format(isifile))
    except StopIteration:
        error =  BadWOSFile("The file '{}' ends before EF was found".format(isifile))
    except KeyboardInterrupt as e:
        error = e
    finally:
        if isinstance(error, KeyboardInterrupt):
            raise error
        return plst, error
