from ...WOS.tagProcessing.helpFuncs import getMonth

import re

def year(R):
    try:
        return int(R['DP'].split(' ')[0])
    except ValueError:
        yVal = re.search(r'-?\d{1,4}', R['DP'].split(' ')[0])
        if yVal is None:
            return 0
        else:
            return(int(yVal.group(0)))

def month(R):
    try:
        m = R['DP'].split(' ')[1]
    except IndexError:
        raise KeyError("Unable to extract a month")
    else:
        return getMonth(m)

def volume(R):
    """Returns the first number/word of the volume field, hopefully trimming something like: `'49 Suppl 20'` to `49`"""
    return R['VI'].split(' ')[0]

def beginningPage(R):
    """As pages may not be given as numbers this is the most accurate this function can be"""
    p = R['PG']
    if p.startswith('suppl '):
        p = p[6:]
    return p.split(' ')[0].split('-')[0].replace(';', '')


def DOI(R):
    ids = R['AID']
    for a in ids:
        if a.endswith(' [doi]'):
            return a[:-6]
    raise KeyError("No DOI number found")

def address(R):
    """Gets the first address of the first author"""
    return R['AD'][R['AU'][0]][0]

medlineSpecialTagToFunc = {
    'year' : year,
    'month' : month,
    'volume' : volume,
    'beginningPage' : beginningPage,
    'DOI' : DOI,
    'address' : address,

    'j9' : lambda R : R['TA'], #remaps to the closests field TA, but J9 != TA

    #'citations' : lambda R: None, #Medline does not have citations

    'grants' : lambda R: R['GR'],#This is the basis for the 'grants' special function

    'selfCitation' : lambda R: R.createCitation(), #just remaps to the correct function
    'authorsShort' : lambda R: R['AU'], #just remaps to the correct name
    'authorsFull' : lambda R : R['FAU'], #just remaps to the correct name
    'title' : lambda R : R['TI'], #just remaps to the correct name
    'journal' : lambda R : R['JT'], #just remaps to the correct name
    'keywords' : lambda R : R['OT'], #just remaps to the correct name
    'abstract' : lambda R : R['AB'], #just remaps to the correct name
    'id' : lambda R : R.id, #just remaps to the correct name
}
