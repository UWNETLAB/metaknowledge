import itertools

from .recordWOS import WOSRecord
from ..mkExceptions import cacheError, BadWOSFile, BadWOSRecord

def isWOSFile(infile, checkedLines = 3):
    """Checks if _infile_ has the right header in the first _checkedLines_ lines
    """
    try:
        with open(isifile, 'r', encoding='utf-8-sig') as openfile:
            f = enumerate(openfile, start = 0)
            for i in range(checkedLines):
                if "VR 1.0" in f.__next__()[1]:
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False

def wosParser(isifile):
    """This is function that is used to create [`RecordCollections`](#metaknowledge.RecordCollection) from files.

    **wosParser**() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [**recordParser**()](#metaknowledge.recordParser) and converted into [`Records`](#metaknowledge.Record). A list of these `Records` is returned.

    `BadWOSFile` is raised if an issue is found with the file.

    # Parameters

    _isifile_ : `str`

    > The path to the target file

    # Returns

    `List[Record]`

    > All the `Records` found in _isifile_
    """
    try:
        with open(isifile, 'r', encoding='utf-8-sig') as openfile:
            f = enumerate(openfile, start = 0)
            while "VR 1.0" not in f.__next__()[1]:
                pass
            notEnd = True
            plst = []
            while notEnd:
                line = f.__next__()
                if line[1] == '':
                    raise BadWOSFile("'{}' does not have an 'EF', lines 1 to {} were checked".format(isifile, line[0] + 1))
                elif line[1].isspace():
                    continue
                elif 'EF' in line[1][:2]:
                    notEnd = False
                    continue
                else:
                    try:
                        plst.append(WOSRecord(itertools.chain([line], f), sFile = isifile, sLine = line[0]))
                    except BadWOSFile as e:
                        try:
                            s = f.__next__()[1]
                            while s[:2] != 'ER':
                                s = f.__next__()[1]
                        except:
                            raise BadWOSFile("The file {} was not terminated corrrectly caused the following error:\n{}".format(isifile, str(e)))
            try:
                f.__next__()
            except StopIteration:
                return plst
            else:
                raise BadWOSFile("EF not at end of " + isifile)
    except UnicodeDecodeError:
        try:
            raise BadWOSFile("'{}' has a unicode issue on line: {}.".format(isifile, f.__next__()[0]))
        except:
            raise BadWOSFile("'{}' has a unicode issue".format(isifile))
    except StopIteration:
        raise BadWOSFile("The file '{}' ends before EF was found".format(isifile))
