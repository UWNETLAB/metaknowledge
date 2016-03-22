from ..mkExceptions import BadProQuestFile

from .recordProQuest import ProQuestRecord

def isProQuestFile(infile, checkedLines = 2):
    try:
        with open(infile, 'r', encoding='utf-8') as openfile:
            f = enumerate(openfile, start = 0)
            for i in range(checkedLines):
                #This seems like enough checking
                #The next line is the date meaning it is not constant
                #More checking could be done
                if f.__next__()[1] == "_" * 60 + "\n" and f.__next__()[1] == '\n' and f.__next__()[1] == 'Report Information from ProQuest\n':
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False

def proQuestParser(proFile):
    #assumes the file is ProQuest
    nameLst = []
    recSet = set()
    error = None
    lineNum = 0
    try:
        with open(proFile, 'r', encoding = 'utf-8') as openfile:
            f = enumerate(openfile, start = 1)
            for i in range(12):
                lineNum, line = next(f)
            while True:
                lineNum, line = next(f)
                lineNum, line = next(f)
                if line == 'Bibliography\n':
                    for i in range(3):
                        lineNum, line = next(f)
                    break
                else:
                    s = line.split('. ')
                    nameLst.append((int(s[0]), '. '.join(s[1:])[:-1]))
            while True:
                #import pdb; pdb.set_trace()
                lineNum, line = next(f)
                if line == 'Bibliography\n':
                    break
                elif line.startswith('Document '):
                    n = int(line[9:].split(' of ')[0])
                    recSet.add(ProQuestRecord(f, recNum = n, sFile = proFile, sLine = lineNum))
                else:
                    #Parsing failed
                    error = BadProQuestFile("The file '{}' has parts of it that are unparsable starting at line: {}. It is likely that the seperators between the records are incorrect".format(pubFile, lineNum))
                    raise StopIteration
    except (UnicodeDecodeError, StopIteration, ValueError) as e:
        if error is None:
            error = BadProQuestFile("The file '{}' has parts of it that are unparsable starting at line: {}.\nThe error was: '{}'".format(pubFile, lineNum, e))
    except KeyboardInterrupt as e:
        #ctrl-c still should work
        error = e
    finally:
        if isinstance(error, KeyboardInterrupt):
            raise error
        return recSet, error
