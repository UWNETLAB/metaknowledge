#Written by Reid McIlroy-Young for John McLevey

import os
import sys
import csv

#The header for the output csv files, it also is the tags the script looks for
formattedList = ['SOURCEAUTHORNAME', 'SOURCETYPE','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']
#The list of journals looked for in the SO tag, map is to make upper case
journalsList = map(lambda x:x.upper(),["Philosophy of Science", "British Journal for the Philosophy of Science","Studies in History and Philosophy of Science","Synthese","European Journal for Philosophy of Science","Journal for General Philosophy of Science","International Studies in the Philosophy of Science"])

#File name of csv from authors in one of the journals
inCiteOut = "PhilJournalsCompiled.csv"

#File name of csv from authors not in one of the journals
notInCiteOut = "NonePhilJournalsCompiled.csv"

#Type of file the script looks for
inputSuffix = ".txt"

#Set True to list files as they are read
Displayfiles = False

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
        if 'ER' in l[1][:2]:
            return tdict
        elif '   ' in l[1][:3]: #the string is three spaces in row
            tdict[currentTag].append(l[1][3:-1])
        elif l[1][2] == ' ':
            currentTag = l[1][:2]
            tdict[currentTag] = [l[1][3:-1]]
        else:
            raise BadPaper("Field tag not formed correctly: " + l[1])
    raise BadPaper("End of file reached before EF")

def isiParser(isifile):
    """
    isiParser reads a file, checks that the header is correct then reads each
    paper returning a list of of dicts keyed with the field tags.
    """
    f = enumerate(open(isifile, 'r'), start = 0)
    if "VR 1.0" not in f.next()[1] and "VR 1.0" not in f.next()[1]:
        raise BadPaper(isifile + " Does not have a valid header")
    notEnd = True
    plst = []
    while notEnd:
        try:
            l = f.next()[1]
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
                    raise BadPaper("Paper does not start with PT tag at line " + str(f.next()[0]) + ' ')
                plst.append(paperParser(f))
                plst[-1][l[:2]] = l[3:-1]
            except Warning as w:
                raise BadPaper(str(w.message) + "in " + isifile)
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
    pubsPapers = []
    for fname in fls:
        if 'PUBS' in fname.upper() and len(fname[:-4].split('_')) > 2:
            pubsPapers.append(fname)
    else:
        #Tells how many files were found
        print str(len(pubsPapers)) + " PUBS files found."
    return pubsPapers

def authInJourn(adat):
    """
    Checks if any of the papers in adat have the SO tag equal to on of the
    journals in journalsList
    """
    for p in adat:
        if 'SO' in p:
            journ = ' '.join(p['SO']).upper()
            if any(journ in j for j in journalsList):
                return True
    return False

def makeCSV(adat, fileName, outCSV):
    """
    Writes all the papers in adat to outCSV using filename for the first two
    columns and writing empty string if a tag is missing
    """
    namesplit = fileName[:-4].split('_')
    if len(namesplit) < 3:
        raise BadPaper("PUBS name of " + fileName+ " is not correctly formatted")
    fdict = {}
    fdict[formattedList[0]] = namesplit[0] + '_' + namesplit[1]
    fdict[formattedList[1]] = ''.join(namesplit[2:])
    for p in adat:
        for isiTag in formattedList[2:]:
            if isiTag in p:
                fdict[isiTag] = '|'.join(p[isiTag]).replace('"', "'")
            else:
                fdict[isiTag] = ''
        outCSV.writerow(fdict)

if __name__ == "__main__":
    if os.path.isfile(notInCiteOut):
        #Checks if the output already exists and terminates if so
        print notInCiteOut +  " already exists\nexisting"
        sys.exit()
        #os.remove(notInCiteOut)
    if os.path.isfile(inCiteOut):
        #Checks if the output already exists and terminates if so
        print inCiteOut +  " already exists\nexisting"
        sys.exit()
        #os.remove(inCiteOut)
    flist = getFiles(inputSuffix)
    inCSV = csv.DictWriter(open(inCiteOut, 'w'), formattedList, quotechar='"', quoting=csv.QUOTE_ALL)
    notCSV = csv.DictWriter(open(notInCiteOut, 'w'), formattedList, quotechar='"', quoting=csv.QUOTE_ALL)
    inCSV.writeheader()
    notCSV.writeheader()
    for isi in flist:
        try:
            if Displayfiles:
                print isi,
            authDat = isiParser(isi)
            if authInJourn(authDat):
                if Displayfiles:
                    print "has a Philosophy Journal"
                makeCSV(authDat, isi, inCSV)
            else:
                if Displayfiles:
                    print "does not have a Philosophy Journal"
                makeCSV(authDat, isi, notCSV)
        except BadPaper as b:
            print b
        except Exception as e:
            print 'Major Exception:'
            print e
            print "Cleaning up, deleting outputs"
            os.remove(inCiteOut)
            os.remove(notInCiteOut)
            raise
    print "Exiting"
