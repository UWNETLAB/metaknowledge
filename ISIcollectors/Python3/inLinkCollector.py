#Written by Reid McIlroy-Young for John McLevey

import isi_scrape
import csv
import sys
import os
import math
import time
import argparse

#output files extension
outputExt = '.txt'

#Controls if each author get their own directory
makeSeparateDirs = True

logFile = "inLinkCollectorLog.log"

testNumber = "WOS:000189249800003"

testFileName = "inLinkCollectorTestFile" + outputExt

def getLogin(s):
    """
    gets the login strings from a file, first line is name second is bar code
    """
    if os.path.isfile(s):
        f = open(args.login, 'r')
    else:
        print(s + " could not be found")
        sys.exit()
    try:
        return ([f.read(),f.read()])
    except Exception as e:
        print ("Not enough lines in " + s)
        sys.exit()

def getPapers(csvfile):
    """
    Reads the csv and produces a list of author name, paper name and WOS number triples for each row
    """
    if os.path.isfile(csvfile):
        csvF = csv.DictReader(open(csvfile, newline = ''),  quotechar='"')
    else:
        print(csvfile + " could not be found")
        sys.exit()
    paperlst = []
    for row in csvF:
        paperlst.append([row['SOURCEAUTHORNAME'], row['TI'], row['UT']])
    return paperlst

def exportInLinks(pap, session):
    """
    pap is a triple of author name, paper name and WOS number queries the database for all inlinks to that WOS number
    """
    writeToLog("Getting: " + pap[2])
    query = session.inlinks(pap[2])
    fname = pap[0] + "_cite_" + pap[1].replace('|', '-').replace(' ','-').replace('/', '') + outputExt
    if makeSeparateDirs:
        writeDir = pap[0] + "_cites"
        if not os.path.exists(writeDir):
            os.makedirs(writeDir)
            os.chdir(writeDir)
        else:
            os.chdir(writeDir)
    try:
        query.rip(fname[:200])
    except Warning as w:
        raise w
    if makeSeparateDirs:
        os.chdir('..')

def writeToLog(s):
    log = open(logFile, 'a')
    log.write(time.strftime("%Y-%m-%d %H:%M:%S: ") + s + '\n')
    log.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("login", help="File containing login information: first line is user name, second line is bar code")
    parser.add_argument("inputcsv", help="csv of all the papers for inlinks to be extracted from")
    args = parser.parse_args()
    print("Reading " + args.inputcsv)
    papersList = getPapers(args.inputcsv)
    userDat = getLogin(args.login)
    backOff = 0
    writeToLog("Starting Run")
    writeToLog("Reading " + args.inputcsv)
    totPapers = len(papersList)
    print(str(totPapers) + " papers found")
    writeToLog(str(totPapers) + " papers found")
    exceptionCount = 0
    warningCount = 0
    while papersList:
        writeToLog("Logging in as " + userDat[0].split('\n')[0])
        S = isi_scrape.AnonymizedUWISISession()
        S.login(userDat[0], userDat[1])
        try:
            query = S.inlinks(testNumber)
            query.rip(testFileName)
        except Exception:
            print("Login failed")
            writeToLog("Attempted to login failed, trying again")
            time.sleep(math.pow(2, backOff))
            backOff += 1
        else:
            writeToLog("Login successful")
            try:
                while papersList:
                    print (str((1 - len(papersList) / totPapers) * 100) + "% done " + str(len(papersList)) + " remaining")
                    try:
                        exportInLinks(papersList.pop(), S)
                    except Warning as w:
                        writeToLog("Warning: " + str(w))
                        warningCount += 1
            except Exception as e:
                print("Major Error")
                backOff = 0
                writeToLog("Exception")
                exceptionCount += 1
    writeToLog(str(totPapers - exceptionCount - warningCount) + " extracted, " + str(exceptionCount) + "Major issues, " + str(warningCount) + " Minor issues")
    writeToLog("Finished")
    print("done")
