import csv
import os

from .record import Record
from .recordCollection import RecordCollection

knownGrantOrgs = ['NSERC', 'SSHRC', 'CIHR']

def grantDirReader(dirName):
    retRC = RecordCollection()
    for fname in os.listdir(dirName):
        if fname.split('_')[0].upper() in knownGrantOrgs:
            fullF = os.path.join(os.path.abspath(dirName), fname)
            retRC += grantFileParser(fullF)
    retRC._repr = 'files-from-{}'.format(dirName)
    return retRC

def grantFileParser(fileName):
    orgName = fileName.split('_')[0].upper()
    recs = []
    with open(fileName, encoding = 'latin1') as f:
        if orgName == 'CIHR':
            f.readline()
            f.readline()
            f.readline()
        reader = csv.DictReader(f)
        for row in reader:
            recs.append(grantToRec(row, orgName, fileName))
    return RecordCollection(recs)

def grantToRec(rowDict, org, fileName):
    recDict = {k.replace(' ', '')[:5] : (s.strip() for s in v.split(';')) for k,v in rowDict.items()}
    recDict['org'] = org
    recDict['UT'] = ["{0}:{1}".format(org, hash(''.join(rowDict.values())))]
    Rec = Record(recDict, sFile = fileName)
    return Rec
