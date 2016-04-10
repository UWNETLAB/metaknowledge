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
    nameDict = {}
    recSet = set()
    error = None
    lineNum = 0
    try:
        with open(proFile, 'r', encoding = 'utf-8') as openfile:
            f = enumerate(openfile, start = 1)
            for i in range(12):
                lineNum, line = next(f)
            # f is file so it *should* end, or at least cause a parser error eventually
            while True:
                lineNum, line = next(f)
                lineNum, line = next(f)
                if line == 'Bibliography\n':
                    for i in range(3):
                        lineNum, line = next(f)
                    break
                else:
                    s = line.split('. ')
                    nameDict[int(s[0])] = '. '.join(s[1:])[:-1]
            while True:
                #import pdb; pdb.set_trace()
                lineNum, line = next(f)
                if line == 'Bibliography\n':
                    break
                elif line.startswith('Document '):
                    n = int(line[9:].split(' of ')[0])
                    R = ProQuestRecord(f, sFile = proFile, sLine = lineNum)
                    if R.get('Title') != nameDict[n]:
                        error = BadProQuestFile("The numbering of the titles at the beginning of the file does not match the records inside. Line {} has a record titled '{}' with number {}, the name should be '{}'.".format(lineNum, R.get('Title', "TITLE MISSING"), n, nameDict[n]))
                        raise StopIteration
                    recSet.add(R)
                    lineNum, line = next(f)
                else:
                    #Parsing failed
                    error = BadProQuestFile("The file '{}' has parts of it that are unparsable starting at line: {}. It is likely that the seperators between the records are incorrect".format(proFile, lineNum))
                    raise StopIteration
    except (UnicodeDecodeError, StopIteration, ValueError) as e:
        if error is None:
            error = BadProQuestFile("The file '{}' has parts of it that are unparsable starting at line: {}.\nThe error was: '{}'".format(proFile, lineNum, e))
    return recSet, error
