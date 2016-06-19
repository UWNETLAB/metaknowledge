import xml.etree.ElementTree as ET

import os
import os.path

from .baseGrant import Grant
from ..mkExceptions import BadGrant

class NSFGrant(Grant):
    def __init__(self, grantdDict, sFile):
        bad = False
        error = None
        originalName = os.path.basename(sFile)
        if grantdDict.get('AwardID', '') == '':
            bad = True
            error = BadGrant("Missing 'AwardID'")
            idValue = "NSF:{}".format(originalName)
        else:
            idValue = "NSF:{}".format(grantdDict.get('AwardID'))
        Grant.__init__(self, originalName, grantdDict, idValue, bad, error, sFile = sFile, sLine = 1)

def isNSFfile(fileName, useFileName = True):
    if useFileName and not os.path.basename(fileName).endswith('.xml'):
        return False
    try:
        tree = ET.parse(fileName)
        root = tree.getroot()
        if len(root.findall('Award')) != 1:
            return False
        else:
            return True
    except (ET.ParseError, UnicodeError):
        return False

def parserNSFfile(fileName):
    error = None
    grantSet = set()
    grantDict = {}
    try:
        tree = ET.parse(fileName)
        top = tree.getroot().find('Award')
        #Organization is the only tag that goes 3 tags deep
        for org in top.findall('Organization'):
            directorate = org.find('Directorate')
            division = org.find('Division')
            if directorate is not None:
                directorateVal = []
                for subElement in directorate:
                    if subElement.text is not None:
                        directorateVal.append(subElement.text)
                if len(directorateVal) > 0:
                    if 'Directorate' not in grantDict:
                        grantDict['Directorate'] = []
                    grantDict['Directorate'].append('; '.join(directorateVal))
            if division is not None:
                divisionVal = []
                for subElement in division:
                    if subElement.text is not None:
                        divisionVal.append(subElement.text)
                if len(divisionVal) > 0:
                    if 'Division' not in grantDict:
                        grantDict['Division'] = []
                    grantDict['Division'].append('; '.join(divisionVal))
        for xmlElement in top:
            if xmlElement.tag == 'Organization':
                pass
            if len(xmlElement) < 1:
                grantDict[xmlElement.tag] = xmlElement.text
            else:
                if xmlElement.tag not in grantDict:
                    grantDict[xmlElement.tag] = []
                elmComps = []
                for subElement in xmlElement:
                    if subElement.text is not None:
                        elmComps.append(subElement.text)
                grantDict[xmlElement.tag].append('; '.join(elmComps))
        grantSet.add(NSFGrant(grantDict, fileName))
    except (ET.ParseError, UnicodeError):
        if error is None:
            error = BadGrant("The file '{}' is having decoding issues. It may have been modifed since it was downloaded or not be a NSF grant file.".format(fileName))
    return grantSet, error
