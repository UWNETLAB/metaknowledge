#Written by Reid McIlroy-Young for John McLevey

import os
import sys



#List of tags in isi files ored based on their occurence in other isi files
tags = ['PT', 'AU', 'AF', 'TI', 'SO', 'LA', 'DT', 'DE', 'ID', 'AB', 'C1', 'RP', 'CR', 'NR', 'TC', 'Z9', 'PU', 'PI', 'PA', 'SN', 'J9', 'JI', 'PD', 'PY', 'VL', 'IS', 'BP', 'EP', 'PG', 'WC', 'SC', 'GA', 'UT', 'PM']


#Set false to produce one file per year in each input
oneFilePerYear = True


#If true the progarm will quit whenever it thinks there is duplication
aggresiveExiting = True

#The suffix of the isi files
inputSuffix = '.txt'

class BadPaper(Warning):
    """
    Exception thrown by paperParser and isiParser for mis-formated papers
    """
    pass

def paperParser(paper):
    """
    paperParser reads paper until it reaches 'EF' for each field tag it adds an
    entry to the returned dict with the tag as the key and a list of the entries
    for the tag as the value, the list has each line as an entry.
    """
    tdict = {}
    currentTag = ''
    for l in paper:
        if 'ER' in l[:2]:
            return tdict
        elif '   ' in l[:3]: #the string is three spaces in row
            tdict[currentTag].append(l[3:-1])
        elif l[2] == ' ':
            currentTag = l[:2]
            tdict[currentTag] = [l[3:-1]]
        else:
            raise BadPaper("Field tag not formed correctly: " + l)
    raise BadPaper("End of file reached before EF")

def isiParser(isifile):
    """
    isiParser reads a file, checks that the header is correct then reads each
    paper returning a list of of dicts keyed with the field tags.
    """
    f = open(isifile, 'r')
    if "VR 1.0" not in f.readline() and "VR 1.0" not in f.readline():
        raise BadPaper(isifile + " Does not have a valid header")
    notEnd = True
    plst = []
    while notEnd:
        try:
            l = f.next()
        except StopIteration as e:
            raise BadPaper("File ends before EF found")
        if not l:
            raise BadPaper("No ER found in " + isifile)
        elif l.isspace():
            continue
        elif 'EF' in l[:2]:
            notEnd = False
            continue
        else:
            try:
                if l[:2] != 'PT':
                    raise BadPaper("Paper does not start with PT tag")
                plst.append(paperParser(f))
                plst[-1][l[:2]] = l[3:-1]
            except Warning as w:
                raise BadPaper(str(w.message) + "In " + isifile)
            except Exception as e:
                 raise e
    try:
        f.next()
        print "EF not at end of " + isifile
    except StopIteration as e:
        pass
    finally:
        return plst

def getFiles(suffix):
    """
    getFiles reads the current directory and returns all files ending with
    suffix. Terminates the program if none are found, no exceptions thrown.
    """
    fls = sys.argv[1:] if sys.argv[1:] else [f for f in os.listdir(".") if f.endswith(suffix)]
    if len(fls) == 0:
        #checks for any valid files
        print "No " + suffix + " Files"
        sys.exit()
    return fls

def nameMatchCheck(n, nlst):
    """
    checks if the n is in the list of strings, if it is ouputs the string,
    if not ouputs False
    """
    for name in nlst:
        if n in name:
            return name
    return False

def writeISI(f, paper):
    """
    Writes a paper to f tags are ordered by the tags valaible with extra ones
    put afterword
    """
    for t in tags:
        if t in paper:
            val = paper[t]
            f.write(t + ' ' + val[0] + '\n')
            if len(val) > 1:
                for line in val[1:]:
                    f.write('   ' + line + '\n')
            del paper[t]
    for t in paper.keys():
        val = paper[t]
        f.write(t + ' ' + val[0])
        if len(val) > 1:
            for line in val[1:]:
                f.write(line + '\n')
        del paper[t]
    f.write('ER\n\n')

def makeFilesPerPaper(pDat, name):
    """
    Creates files for each year found and writes the corresponding
    """
    print "Writing files for " + name
    newFiles = {}
    for p in pDat:
        if 'PY' in p:
            year = p['PY'][0]
            if len(year) != 4:
                print "Badly formated Year field " + year + ' ' + p['UT'][0] + " will be skipped"
            if year in newFiles:
                writeISI(newFiles[year], p)
            else:
                newFiles[year] = open(year + '-' + name + inputSuffix, 'w')
                newFiles[year].write("FN Thomson Reuters Web of Science\nVR 1.0\n")
                writeISI(newFiles[year], p)
    for newF in newFiles.values():
        newF.write('EF')
        newF.close()

def makeFilesPerYear(pDat, name, yDict):
    """
    For each paper in pdat writes it to the corresponding year in the dict of
    files yDict. If the year is missing it creates it with the name of the file
    currently being read
    """
    for p in pDat:
        if 'PY' in p:
            year = p['PY'][0]
            if len(year) != 4:
                print "Badly formated Year field " + year + ' ' + p['UT'][0] + " will be skipped"
            if year in yDict:
                writeISI(yDict[year], p)
            else:
                print year + '-' + name + inputSuffix + " created"
                yDict[year] = open(year + '-' + name + inputSuffix, 'w')
                yDict[year].write("FN Thomson Reuters Web of Science\nVR 1.0\n")
                writeISI(yDict[year], p)


if __name__ == "__main__":
    fileNameList = os.listdir(".")
    flist = getFiles(inputSuffix)
    if oneFilePerYear:
        yearFiles = {}
    for isi in flist:
        localName = isi.split('/')[-1]
        if isi in fileNameList:
            fileNameList.remove(localName)
        nameCheck = nameMatchCheck(localName[:-len(inputSuffix)], fileNameList)
        if nameCheck:
            print nameCheck + " found " + localName +  " already split,",
            if oneFilePerYear and aggresiveExiting:
                print "quitting"
                sys.exit()
            else:
                print "skipping"
        else:
            try:
                paperDat = isiParser(isi)
                if oneFilePerYear:
                    makeFilesPerYear(paperDat, localName[:-len(inputSuffix)], yearFiles)
                makeFilesPerPaper(paperDat, localName[:-len(inputSuffix)])
            except BadPaper as b:
                print b
            except Exception as e:
                print 'Major Exception:'
                print e
                raise
    if oneFilePerYear:
            for newF in yearFiles.values():
                newF.write('EF')
                newF.close()
    print "Done"
