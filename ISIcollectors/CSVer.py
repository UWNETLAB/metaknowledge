#!/usr/bin/env python2
#Written by Reid McIlroy-Young for John McLevey

import os
import sys
import csv

formatedList = ['SOURCEAUTHORNAME', 'SOURCETYPE','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']

stringOfThreeSpaces = '   ' #What it says on the tin

#Output CITED csv name
citeOut = "CitedCompiled.csv"

#Output PUBS csv name
pubOut = "PubCompiled.csv"

#The file extension search for
fileType = '.txt' 

#set False to not create a third csv of of files that do not fit the FIRST_L_(PUBS/CITED) format
includeMisc = True
miscOut = "MiscCompiled.csv"
miscList = ['Filesname','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']

class BadPaper(Exception):
    pass
        
def readPaper(index, flines, rowDict, csvOut, isiList):
    """
    Reads flines starting at index and checks if the the first characters are not
    whitespace. If not then readPaper checks if they are in isiList if the lines
    4th character and onward get added to the rowDict under the isiList's values.
    If the character do not belong to isiList they get skipped. 
    If whitespace the 4th and onwards characters are added to the dict if they
    belong to the isiList otherwise they are ignored.
    Then the dict is written as line to csvOut.
    Exceptions are raised if the paper does not have the right terminator "ER"
    Exceptions are raised if the paper does not start with PT or have a space
    after its field tag these are printed and the rest of the file is skipped
    Exceptions raised by the operations are caught and raised with some
    debugging information added
    """
    loc = index
    currentVal = ''
    if 'PT' not in flines[loc]:
        raise BadPaper("bad first field at line " + str(loc + 1) + " " + flines[loc][:-1])
    try:
        while 'ER' not in flines[loc][:2]:
            if stringOfThreeSpaces not in flines[loc][:3]: #if the first three characters of flines[loc] are not three spaces
                if not flines[loc][2].isspace():
                    raise BadPaper("Bad field tag at line ")
                elif flines[loc][:2] in isiList:
                    currentVal = flines[loc][:2]
                    rowDict[currentVal] = flines[loc][3:-1].replace('"', "'")
                else:
                    currentVal = ''
            else:
                if currentVal != '':
                    rowDict[currentVal] += '|' + flines[loc][3:-1].replace('"', "'")
            loc += 1
    except BadPaper as e:
        raise type(e)(e.message + str(loc + 1) + ": " + flines[loc][:-1])
    except Exception as e:
        print "readPaper Exception:"
        print "currentVal = " + str(currentVal)
        print "loc = " + str(loc)
        print "flines[loc] = " + flines[loc],
        print rowDict
        raise type(e)(e.message + " While loop Exception.")
    if 'ER' not in flines[loc]:
        raise BadPaper("Paper terminator is not valid: " + flines[loc][:-1])
    loc += 1
    csvOut.writerow(rowDict)
    return loc

def csvFormatedPaperList(paperls, csvout):
    """
    csvPaperList goes through the list of files checks if their headers meet the
    isi format. If they do it runs readPaper on each line that is not the
    header, footer (EF) or whitespace.
    """
    for fname in paperls:
        namesplit = fname[:-4].split('_')
        if len(namesplit) < 3:
            print fname + " is not a valid file name, it will be skipped"
        else:
            fdict = {}
            fdict[formatedList[0]] = namesplit[0] + '_' + namesplit[1]
            fdict[formatedList[1]] = ''.join(namesplit[2:])
            readisi = open(fname,"r").readlines()
            if len(readisi) < 2:
                print fname + " is one or less lines long it will be skipped."
            elif "VR 1.0" not in readisi[1] and "VR 1.0" not in readisi[0]:
                #checks that the txt has the right header
                print "Wrong header in found in " + fname 
                print readisi[0],
                print readisi[1],
                print fname + " will be skipped"
            else:
                fileIndex = 2
                while fileIndex < len(readisi) - 1:
                    if readisi[fileIndex].isspace():
                        fileIndex += 1
                    elif 'EF' in readisi[fileIndex][:2]:
                        if fileIndex != len(readisi) - 1:
                            print fname + " does not end at ER"
                            print "EF is at " + str(fileIndex + 1)
                            print fname + " ends at " + str(len(readisi) + 1)
                            print "Papers after " + str(fileIndex + 1) + " will not be recorded"
                        break
                    else:
                        try:
                            fileIndex = readPaper(fileIndex, readisi, fdict, csvout, formatedList)
                        except BadPaper as e:
                            print e
                            print "skipping the rest of " + fname
                            break
                        except Exception as e:
                            raise type(e)(e.message + " Exception in " + fname + " at line " + str(fileIndex + 1))

def csvMiscPaperList(paperls, csvout):
    """
    csvPaperList goes through the list of files and runs readPaper on each line 
    that is not the header, footer (EF) or whitespace. Uses miscList as the csv header.
    """
    for fname in paperls:
        fdict = {}
        fdict[miscList[0]] = fname[:-len(fileType)]
        readisi = open(fname,"r").readlines()
        if len(readisi) < 2:
            print fname + " is one or less lines long it will be skipped."
        elif "VR 1.0" not in readisi[1] and "VR 1.0" not in readisi[0]:
            #checks that the txt has the right header
            print "Wrong header in found in " + fname 
            print readisi[0],
            print readisi[1],
            print fname + " will be skipped"
        else:
            fileIndex = 2
            while fileIndex < len(readisi) - 1:
                if readisi[fileIndex].isspace():
                    fileIndex += 1
                elif 'EF' in readisi[fileIndex][:2]:
                    if fileIndex != len(readisi) - 1:
                        print fname + " does not end at ER"
                        print "EF is at " + str(fileIndex + 1)
                        print fname + " ends at " + str(len(readisi) + 1)
                        print "Papers after " + str(fileIndex + 1) + " will not be recorded"
                    break
                else:
                    try:
                        fileIndex = readPaper(fileIndex, readisi, fdict, csvout, miscList)
                    except BadPaper as e:
                        print e
                        print "skipping the rest of " + fname
                        break
                    except Exception as e:
                        raise type(e)(e.message + " Exception in " + fname + " at line " + str(fileIndex + 1))

if __name__ == "__main__":
    if (os.path.isfile(pubOut)):
        #Checks if the output already exists and terminates if it does
        print pubOut +  " already exists"
        #os.remove(pubOut)
        sys.exit()
    if (os.path.isfile(citeOut)):
        #Checks if the output already exists and terminates if it does
        print citeOut +  " already exists"
        #os.remove(citeOut)
        sys.exit()
    if (os.path.isfile(miscOut)) and includeMisc:
        #Checks if the output already exists and terminates if it does
        print miscOut +  " already exists"
        #os.remove(miscOut)
        sys.exit()
    flist = [f for f in os.listdir(".") if f.endswith(fileType)] #Creates list of all fileType in the directory
    if len(flist) == 0:
        #checks for any valid files
        print "No txt Files"
        sys.exit()
    else:
        #Tells how many files were found
        print "Found " + str(len(flist)) + " txt files"
    pubFormatFiles = [] 
    citeFormatFiles = []
    miscFiles = []
    for fname in flist:
        slst = fname.split('_')
        if len(slst) < 3:
            miscFiles.append(fname)
        elif "cited" in slst[2].lower():
            citeFormatFiles.append(fname)
        elif "pubs" in slst[2][:4].lower():
            pubFormatFiles.append(fname)
        else:
            miscFiles.append(fname)
    print str(len(pubFormatFiles)) + " PUBS, " + str(len(citeFormatFiles)) + " CITED and " + str(len(miscFiles)) + " miscellaneous files found."
    if includeMisc:
        print "Creating " + pubOut + ", " + citeOut + " and " + miscOut
        csvMisc = csv.DictWriter(open(miscOut, 'w'), miscList, quotechar='"', quoting=csv.QUOTE_ALL)
        csvMisc.writeheader()
    else:
        print "Creating " + pubOut + " and " + citeOut
    csvPub = csv.DictWriter(open(pubOut, 'w'), formatedList, quotechar='"', quoting=csv.QUOTE_ALL)
    csvCite = csv.DictWriter(open(citeOut, 'w'), formatedList, quotechar='"', quoting=csv.QUOTE_ALL)
    csvPub.writeheader()
    csvCite.writeheader()
    try:
        print "Starting PUBS reads"
        csvFormatedPaperList(pubFormatFiles, csvPub)
        print "Starting CITES reads"
        csvFormatedPaperList(citeFormatFiles, csvCite)
        if includeMisc:
            print "Starting miscellaneous reads"
            csvMiscPaperList(miscFiles, csvMisc)
    except Exception as e:
        #If any exceptions are raised cleans up and prints them
        print 'Exception:'
        print e
        print "Cleaning up, deleting outputs"
        if includeMisc:
            os.remove(miscOut)
        os.remove(pubOut)
        os.remove(citeOut)
        raise
    finally:
        print "Exiting"