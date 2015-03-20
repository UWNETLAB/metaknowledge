#Written by Reid McIlroy-Young for John McLevey
import os
import sys
import csv

#output file name
outputFile = "SubjectList.csv"

#The title of the csv's header
csvHeader = ['Article', 'Subject']

#Tag in the second column
subjectTag = 'SC'

#Fields in first column
articleTags = ['TI', 'SO', 'UT']

#Type of file the script looks for
inputSuffix = ".txt"

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
        l = f.next()
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
    else:
        #Tells how many files were found
        print "Found " + str(len(fls)) + suffix + "  files"
    return fls

def getRowsfromFile(f, csvFile):
    """
    getRowsfromFile uses isiParser to parse the file f, then it adds every field
    in articleTags it can find to the first column of csvFile. For each separate
    tag in subjectTag it creates an entry in csvFile with the tag in the second
    column.
    """
    plst = isiParser(f)
    for p in plst:
        pdict = {}
        for tag in articleTags:
            if csvHeader[0] in pdict:
                if tag in p:
                    pdict[csvHeader[0]] += '|' + ' '.join(p[tag])
            else:
                if tag in p:
                    pdict[csvHeader[0]] =' '.join(p[tag])
        if subjectTag in p:
            for sub in '; '.join(p[subjectTag]).split('; '): 
                #The join is in case the field is spans multiple lines
                if 'NA'
                pdict[csvHeader[1]] = sub
                csvFile.writerow(pdict)
        else:
            print "No " + subjectTag + " field in " + f,
            print "paper number " + p['UT'][0]
            pdict[csvHeader[1]] = ''

if __name__ == '__main__':
    if os.path.isfile(outputFile):
        #Checks if the output outputFile already exists and terminates if so
        print outputFile +  " already exists\nexisting"
        sys.exit()
        #os.remove(outputFile)
    flist = getFiles(inputSuffix)
    csvOut = csv.DictWriter(open(outputFile, 'w'), csvHeader, quotechar='"', quoting=csv.QUOTE_ALL)
    csvOut.writeheader()
    try:
        for isi in flist:
                try:
                    print "Reading " + isi
                    getRowsfromFile(isi, csvOut)
                except BadPaper as b:
                    print b
                except Exception, e:
                    print type(e)
    except Exception, e:
        #IF any exceptions are raised cleans up and prints them
        print 'Exception:'
        print e
        print "Deleting " + outputFile
        os.remove(outputFile)
    finally:
        print "Exiting"