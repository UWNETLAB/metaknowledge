import csv
import os

from .record import Record
from .recordCollection import RecordCollection

knownGrantOrgs = ['NSERC', 'SSHRC', 'CIHR']

equivalentFields = {
    'Name-Nom' : 'PI Names',
    'CoApplicantName-NomCoApplicant' : 'CO Names',
}

def grantDirReader(dirName):
    retRC = RecordCollection()
    nsercFiles = []
    nsercDict = {}
    for fname in os.listdir(dirName):
        org = fname.split('_')[0].upper()
        fullF = os.path.join(os.path.abspath(dirName), fname)
        if org == 'NSERC':
            nsercFiles.append(fullF)
        elif org in knownGrantOrgs:
            retRC += grantFileParser(fullF)
    for fname in nsercFiles:
        for rec in grantFileParser(fname, nsercMode = True):
            updateNsercDict(rec, nsercDict, fname)
    for recDict in nsercDict.values():
        retRC.addRec(Record(recDict, sFile = recDict['sourceFile'][0]))
    retRC._repr = 'files-from-{}'.format(dirName)
    return retRC

def grantFileParser(fileName, nsercMode = False):
    orgName = os.path.basename(fileName).split('_')[0].upper()
    recs = []
    with open(fileName, encoding = 'latin1') as f:
        if orgName == 'CIHR':
            f.readline()
            f.readline()
            f.readline()
        reader = csv.DictReader(f)
        for i in range(len(reader.fieldnames)):
            if reader.fieldnames[i] in equivalentFields:
                reader.fieldnames[i] = equivalentFields[reader.fieldnames[i]]
        for row in reader:
            if nsercMode:
                recs.append(grantToRec(row, orgName, fileName, nsercMode = True))
            else:
                recs.append(grantToRec(row, orgName, fileName, nsercMode = False))
    if nsercMode:
        return recs
    else:
        return RecordCollection(recs)

def grantToRec(rowDict, org, fileName, nsercMode = False):
    recDict = {k.replace(' ', '')[:5] : [s.strip() for s in v.split(';')] for k,v in rowDict.items()}
    recDict['org'] = [org]
    recDict['UT'] = ["{0}:{1}".format(org, hash(''.join(rowDict.values())))]
    if nsercMode:
        recDict['sourceFile'] = [fileName]
        return recDict
    else:
        Rec = Record(recDict, sFile = fileName)
        return Rec

def updateNsercDict(recDict, targetDict, fileName):
    try:
        cle = recDict['Cle'][0]
    except KeyError:
        raise RuntimeError("The file {} does not have a Cle column it cannot be proccessed correctly".format(fileName))
    else:
        if cle in targetDict:
            for k,v in recDict.items():
                for val in v:
                    try:
                        if val not in targetDict[cle][k]:
                            targetDict[cle][k].append(val)
                    except KeyError:
                        targetDict[cle][k] = [val]
        else:
            targetDict[cle] = recDict
