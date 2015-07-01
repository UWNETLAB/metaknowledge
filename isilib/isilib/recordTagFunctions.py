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

def pubType(val):
    """
    retunrs the type of publication as a character: conference, book, journal, book in series, or patent
    PT tag
    """
    return val[0]


def authorsFull(val):
    """
    returns a list of authors full names
    AF tag
    """
    return val

def group(val):
    """
    returns the group associated with the Record
    GP tag
    """
    return val[0]

def editedBy(val):
    """
    returns a list of the editors of the Record
    BE tag
    """
    return val

def authorsShort(val):
    """
    returns a list of authors shortened names
    AU tag
    """
    return val

def bookAuthor(val):
    """
    returns a list of the short names of the authors of a book Record
    BA tag
    """
    return val

def bookAuthorFull(val):
    """
    returns a list of the long names of the authors of a book Record
    BF tag
    """
    return val

def groupName(val):
    """
    returns the name of the group associated with the Record
    CA tag
    """
    return val[0]

def title(val):
    """
    returns the title of the record
    TI tag
    """
    return ' '.join(val)

def journal(val):
    """
    returns the full name of the publication
    SO tag
    """
    return ' '.join(val)

def seriesTitle(val):
    """
    returns the title of the series the Record is in
    SE tag
    """
    return val[0]

def seriesSubtitle(val):
    """
    returns the title of the series the Record is in
    BS tag
    """
    return val[0]

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


def citations(val):
    """
    returns a list of all the citations in the record
    CR tag
    """
    retCites = []
    for c in val:
        retCites.append(Citation(c))
    return retCites



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
            'PT' : pubType,
            'AF' : authorsFull,
            'GP' : group,
            'BE' : editedBy,
            'AU' : authorsShort,
            'BA' : bookAuthor,
            'BF' : bookAuthorFull,
            'CA' : groupName,
            'TI' : title,
            'SO' : journal,
            'SE' : seriesTitle,
            'BS' : seriesSubtitle,
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



"""
TODO:
'ED' : "editors",
'BS' : "seriesSubtitle",

'LA' : "language",
'DT' : "docType",
'CT' : "confTitle",
'CY' : "confDate",
'HO' : "confHost",
'CL' : "confLocation",
'SP' : "confSponsors",
'DE' : "authKeyWords",
'ID' : "keyWords",
'AB' : "abstract",
'C1' : "authAddress",
'RP' : "reprintAddress",
'EM' : "email",
'RI' : "ResearcherIDnumber",
'OI' : "orcID",
'FU' : "funding",
'FX' : "fundingText",
'CR' : "citations",
'NR' : "citedRefsCount",
'TC' : "wosTimesCited",
'Z9' : "totalTimesCited",
'PU' : "publisher",
'PI' : "publisherCity",
'PA' : "publisherAddress",
'SC' : "subjectCategory",
'SN' : "ISSN",
'EI' : "eISSN",
'BN' : "ISBN",
'J9' : "j9",
'JI' : "isoAbbreviation",
'PD' : "month",
'PY' : "year",
'VL' : "volume",
'IS' : "issue",
'PN' : "partNumber",
'SU' : "supplement",
'SI' : "specialIssue",
'MA' : "meetingAbstract",
'BP' : "beginningPage",
'EP' : "endingPage",
'AR' : "articleNumber",
'PG' : "pageCount",
'WC' : "subjects",
'DI' : "DOI",
'D2' : "bookDOI",
'GA' : "documentDeliveryNumber",
'UT' : "wosString",
'PM' : "pubMedID",

"""
