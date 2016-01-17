import itertools

from .recordWOS import WOSRecord
from ..mkExceptions import cacheError, BadWOSFile, BadWOSRecord


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
        openfile = open(isifile, 'r', encoding='utf-8-sig')
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    f = enumerate(openfile, start = 0)
    try:
        linesChecked = 3
        for i in range(linesChecked):
            if "VR 1.0" in f.__next__()[1]:
                break
            if i == linesChecked - 1:
                openfile.close()
                raise BadWOSFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
    except StopIteration as e:
        openfile.close()
        raise BadWOSFile("File ends before EF found")
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    notEnd = True
    plst = []
    while notEnd:
        try:
            line = f.__next__()
        except StopIteration as e:
            raise BadWOSFile("The file '{}' ends before EF was found".format(isifile))
        if not line[1]:
            raise BadWOSFile("No ER found in " + isifile)
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
        raise BadWOSFile("EF not at end of " + isifile)
    except StopIteration as e:
        pass
    finally:
        openfile.close()
    return plst
