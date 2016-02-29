import csv
import os.path

def isNSERCfile(fileName, useFileName = True):
    if useFileName and not os.path.basename(fileName).startswith('NSERC_'):
        return False
    try:
        with open(fileName, 'r', encoding = 'latin-1') as openfile:
            reader = csv.DictReader(openfile, fieldnames=None, dialect='excel')
            for row in reader:
                if 'Cle' not in row:
                    return False
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return True
