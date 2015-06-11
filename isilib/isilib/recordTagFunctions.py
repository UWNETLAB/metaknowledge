from .constants import tagNameConverter, monthDict
from .citation import Citation

class tagWrapper(object):
    def __init__(self, parent, tag):
        self.tag = tag
        self.data = None
        try:
            self.name = tagNameConverter[tag]
            setattr(parent, self.name, self)
        except KeyError:
            pass
        except AttributeError:
            pass

    def __get__(self, instance, owner):
        if self.data == None:
            try:
                self.data = tagToFunc[self.tag](instance._fieldDict[self.tag])
            except KeyError:
                self.data = instance._fieldDict[self.tag]
        return self.data

def authorsFull(val):
    """
    returns a list of authors full names
    AF tag
    """
    return val

def authorsShort(val):
    """
    returns a list of authors shortened names
    AU tag
    """
    return val

def year(val):
    """
    returns the year the record was published in as an int
    PY tag
    """
    yearField = val[0]
    if len(yearField) == 4:
        return int(yearField)
    else:
        raise Exception


def month(val):
    """
    returns the month the record was published in as an int with January as 1, February 2, ...
    PD tag
    """
    return getMonth(val[0])


def title(val):
    """
    returns the title of the record
    TI tag
    """
    return ' '.join(val)

def citations(val):
    """
    returns a list of all the citations in the record
    CR tag
    """
    retCites = []
    for c in val:
        retCites.append(Citation(c))
    return retCites

def journal(val):
    """
    returns the full name of the publication
    SO tag
    """
    return ' '.join(val)

def j9(val):
    """
    returns the J9 (29-Character Source Abbreviation) of the publication
    J9 tag
    """
    return val[0]


def beginningPage(val):
    """
    returns the first page the record occurs on as a string not an int
    BP tag
    """

    return val[0].strip()


def endingPage(val):
    """
    return the last page the record occurs on as a string not an int
    EP tag
    """
    return val[0].strip()


def volume(val):
    """
    return the volume the record is in as a string not an int
    VL tag
    """

    return val[0].strip()


def DOI(val):
    """
    return the DOI number of the record
    DI tag
    """
    return val[0]

def abstract(val):
    """
    return abstract of the record, with newlines hopefully in the correct places
    AB tag
    """
    return '\n'.join(val)


def wosString(val):
    """
    returns the WOS number of the record as a string preceded by "WOS:""
    UT tag
    """
    return val[0]




def makeReversed(d):
    dTmp = d.copy()
    for k in d.keys():
        try:
            dTmp[tagNameConverter[k]] = dTmp[k]
        except KeyError:
            raise Exception("Something is wrong with the tag to full name mappings")
    return dTmp

tagToFunc = makeReversed( {
            'AF' : authorsFull,
            'TI' : title,
            'SO' : journal,
            'AB' : abstract,
            'CR' : citations,
            'J9' : j9,
            'PD' : month,
            'PY' : year,
            'VL' : volume,
            'BP' : beginningPage,
            'EP' : endingPage,
            'DI' : DOI,
            #'UT' : wosString,
            })


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
