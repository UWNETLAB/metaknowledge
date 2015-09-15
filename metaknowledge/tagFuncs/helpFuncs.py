from ..constants import tagNameConverter, monthDict

def makeReversed(d):
    """
    Simple function for reversing a dictionary
    """
    dTmp = d.copy()
    for k in d.keys():
        try:
            dTmp[tagNameConverter[k]] = dTmp[k]
        except KeyError:
            raise Exception("Something is wrong with the tag to full name mappings")
    return dTmp

def getMonth(s):
    """
    Known formats:
    Month ("%b")
    Month Day ("%b %d")
    Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
    Season ("%s") --- this gets coerced to use the first month of the given season
    Month Day Year ("%b %d %Y")
    Month Year ("%b %Y")
    """
    monthOrSeason = s.split(' ')[0].split('-')[0].upper()
    if monthOrSeason in monthDict:
        return monthDict[monthOrSeason]
    else:
        raise ValueError("Month format not recognized: " + s)
