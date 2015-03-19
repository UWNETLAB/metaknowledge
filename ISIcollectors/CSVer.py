#!/usr/bin/env python2
#Written by Reid McIlroy-Young for John McLevey

import os
import sys
import csv

isiList = ['SOURCEAUTHORNAME', 'SOURCETYPE','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']
outfile = "CompiledData.csv"  #Name of output file
stringOfThreeSpaces = '   ' #What it says on the tin

"""
ignoreotherfiles = True
isiList = ['SOURCEAUTHORNAME', 'SOURCETYPE','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']
outfile = "CompiledData.csv"  #Name of output file

ignoreotherfiles = False #produce two csvs
isiList = ['Filesname','AU', 'AF', 'TI', 'SO','ID', 'AB', 'C1', 'RP', 'CR', 'DE', 'TC', 'SC', 'J9', 'JI', 'PY', 'UT', 'FU', 'FX']
outfile = "CompiledData.csv"  #Name of output file
"""

class BadPaper(Exception):
    pass
        
def readPaper(index, flines, rowDict, csvOut):
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
        raise BadPaper("bad paper at line " + str(loc + 1) + " " + flines[loc][:-1])
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

def csvPaperList(paperls, csvout):
    """
    csvPaperList goes through the list of files checks if their headers meet the
    isi format. If they do it runs readPaper on each line that is not the
    header, footer(ER) or whitespace.
    """
    for fname in flist:
        namesplit = fname[:-4].split('_')
        if len(namesplit) < 3:
            print fname + " is not a valid file name, it will be skipped"
        else:
            fdict = {}
            fdict[isiList[0]] = namesplit[0] + '_' + namesplit[1]
            fdict[isiList[1]] = ''.join(namesplit[2:])
            readisi = open(fname,"r").readlines()
            if len(readisi) < 2:
                print fname + " is one line long it will be skipped"
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
                            fileIndex = readPaper(fileIndex, readisi, fdict, csvout)
                        except BadPaper as e:
                            print e
                            print "skipping the rest of " + fname
                            break
                        except Exception as e:
                            raise type(e)(e.message + " Exception in " + fname + " at line " + str(fileIndex + 1))

if __name__ == "__main__":
    if (os.path.isfile(outfile)):
        #Checks if the output already exists and terminates if it does
        print outfile +  " already exists"
        sys.exit()
    flist = [f for f in os.listdir(".") if f.endswith(".txt")] #Creates list of all .txt in the directory
    if len(flist) == 0:
        #checks for any valid files
        print "No txt Files"
        sys.exit()
    else:
        #Tells how many files were found
        print "Found " + str(len(flist)) + " txt files"
    print "Creating " + outfile
    of = open(outfile, 'wb') #creates output file and puts header on it
    ocsv = csv.DictWriter(of, isiList, quotechar='"', quoting=csv.QUOTE_ALL) #makes the file into csv type with header isiList
    ocsv.writeheader() #Gives ocsv a header of isiList
    try:
        print "Starting reads"
        csvPaperList(flist, ocsv)
    except Exception as e:
        #If any exceptions are raised cleans up and prints them
        of.close()
        print 'Exception:'
        print e
        print "Deleting " + outfile
        os.remove(outfile)
        raise
    else:
        of.close()
    finally:
        print "Exiting"