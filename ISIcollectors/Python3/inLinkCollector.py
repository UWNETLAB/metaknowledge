#Written by Reid McIlroy-Young for John McLevey

import isi_scrape
import csv
import sys
import os
import argparse

#output files extension
outputExt = '.txt'

#Controls if each author get their own directory
makeSeparateDirs = False

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
    print("Getting: " + pap[2])
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
        query.rip(fname)
    except Warning as w:
        raise w
    if makeSeparateDirs:
        os.chdir('..')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("login", help="File containing login information: first line is user name, second line is bar code")
    parser.add_argument("inputcsv", help="csv of all the papers for inlinks to be extracted from")
    args = parser.parse_args()
    print("Reading " + args.inputcsv)
    papersList = getPapers(args.inputcsv)
    userDat = getLogin(args.login)
    print("Logging in as " + userDat[0].split(' ')[0])
    S = isi_scrape.AnonymizedUWISISession()
    S.login(userDat[0], userDat[1])
    for p in papersList:
        try:
            exportInLinks(p, S)
        except Warning as w:
            print(w)
    print("done")
