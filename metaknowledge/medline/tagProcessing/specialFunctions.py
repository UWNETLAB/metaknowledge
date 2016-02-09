from ...WOS.tagProcessing.helpFuncs import getMonth

def year(R):
    return R['DP'].split(' ')[0]

def month(R):
    try:
        m = R['DP'].split(' ')[1]
    except IndexError:
        raise KeyError
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

medlineSpecialTagToFunc = {
    'year' : year,
    'month' : month,
    'volume' : volume,
    'beginningPage' : beginningPage,
    'DOI' : DOI,
    'authorsShort' : lambda R: R['AU'], #just remaps to the correct name
    'authorsFull' : lambda R : R['FAU'], #just remaps to the correct name
    'title' : lambda R : R['TI'], #just remaps to the correct name
    'j9' : lambda R : R['TA'], #remaps to the closests name TA is not quite J9
}
