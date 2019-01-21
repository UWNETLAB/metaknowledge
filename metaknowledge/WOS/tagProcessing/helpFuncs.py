#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
monthDict = {'SPR': 3, 'SUM': 6, 'FAL': 9, 'WIN': 12, 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6 , 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12}

def getMonth(s):
    """
    Known formats:
    Month ("%b")
    Month Day ("%b %d")
    Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
    Season ("%s") --- this gets coerced to use the first month of the given season
    Month Day Year ("%b %d %Y")
    Month Year ("%b %Y")
    Year Month Day ("%Y %m %d")
    """
    monthOrSeason = s.split('-')[0].upper()
    if monthOrSeason in monthDict:
        return monthDict[monthOrSeason]
    else:
        monthOrSeason = s.split('-')[1].upper()
        if monthOrSeason.isdigit():
            return monthOrSeason
        else:
            return monthDict[monthOrSeason]

    raise ValueError("Month format not recognized: " + s)

def makeBiDirectional(d):
    """
    Helper for generating tagNameConverter
    Makes dict that maps from key to value and back
    """
    dTmp = d.copy()
    for k in d:
        dTmp[d[k]] = k
    return dTmp

def reverseDict(d):
    """
    Helper for generating fullToTag
    Makes dict of value to key
    """
    retD = {}
    for k in d:
        retD[d[k]] = k
    return retD
