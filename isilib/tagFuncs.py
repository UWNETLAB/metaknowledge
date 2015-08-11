from .constants import tagNameConverter, monthDict
from .citation import Citation

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

def editors(val):
    """

    ED
    """
    return val

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

def language(val):
    """
    returns the languages of the Record as a string with languages seperated by ', ', usually there is only one language
    LA tag
    """
    return ', '.join(val)

def docType(val):
    """
    returns the type of document the Record contains
    DT tag
    """
    return val[0]

def confTitle(val):
    """
    returns the title of the conference associated with the Record
    CT tag
    """
    return ' '.join(val)

def confDate(val):
    """
    returns the date string of the conference associated with the Record
    CY tag
    """
    return val[0]

def confSponsors(val):
    """
    returns a list of sponsors for the conference associated with the record
    SP tag
    """
    return ', '.join(val).split(', ')

def wosTimesCited(val):
    """
    returns the number of times the Record has been cited byr records in WOS
    TC tag
    """
    return int(val[0])

def authAddress(val):
    """

    C1 tag
    """
    return val

def confLocation(val):
    """
    returns the sting giving the confrence's location
    CL tag
    """
    return ' '.join(val)

def j9(val):
    """
    returns the J9 (29-Character Source Abbreviation) of the publication
    J9 tag
    """
    return val[0]

def funding(val):
    """
    Returns a list of the groups funding the Record
    FU tag
    """
    return ' '.join(val).split('; ')

def subjectCategory(val):
    """
    returns a list of the subjects associated with the Record
    SC tag
    """
    return ' '.join(val).split('; ')

def citations(val):
    """
    returns a list of all the citations in the record
    CR tag
    """
    retCites = []
    for c in val:
        retCites.append(Citation(c))
    return retCites

def publisherCity(val):
    """
    Returns the city the publisher is in
    PI tag
    """
    return ' '.join(val).upper()

def ISSN(val):
    """
    returns the ISSN of the Record
    SN tag
    """
    return val[0]

def articleNumber(val):
    """
    returns a string giving the article number, not all are integers
    AR tag
    """
    return val[0]

def issue(val):
    """
    returns a string giving the issue or range of issues the Record was in
    IS tag
    """
    return val[0]

def email(val):
    """
    returns a list of emails given by the authors of the Record
    EM tag
    """
    return ' '.join(val).split('; ')

def eISSN(val):
    """
    returns the EISSN of the Record
    EI tag
    """
    return val[0]

def DOI(val):
    """
    return the DOI number of the record
    DI tag
    """
    return val[0]

def wosString(val):
    """
    returns the WOS number of the record as a string preceded by "WOS:""
    UT tag
    """
    return val[0]

def orcID(val):
    """
    returns a list of orc IDs of the Record
    OI tag
    """
    return ' '.join(val).split('; ')

def meetingAbstract(val):
    """
    returns the ID of the meeting abstract prefixed by 'EPA-'
    MA tag
    """
    return val[0]

def isoAbbreviation(val):
    """
    returns the iso abbreviation of the journal
    JI tag
    """
    return ' '.join(val).upper()

def pageCount(val):
    """
    returns an interger giving the number of pages of the Record
    PG tag
    """
    return int(val[0])

def publisher(val):
    """
    returns the publisher of the Record
    PU tag
    """
    return ' '.join(val).upper()

def ISBN(val):
    """
    returns a list of ISBNs assocaited with the Record
    BN tag
    """
    return ' '.join(val).split('; ')

def month(val):
    """
    returns the month the record was published in as an int with January as 1, February 2, ...
    PD tag
    """
    return getMonth(val[0])

def fundingText(val):
    """
    Returns a string of the funding thank you
    FX tag
    """
    return ' '.join(val)

def bookDOI(val):
    """
    returns the book DOI of the Record
    D2 tag
    """
    return val[0]

def volume(val):
    """
    return the volume the record is in as a string not an int
    VL tag
    """
    return val[0].strip()

def ResearcherIDnumber(val):
    """
    returns a lsit of the research ids of the Record
    RI tag
    """
    return ' '.join(val).split('; ')

def citedRefsCount(val):
    """
    returns the numer citations, length of CR list
    NR tag
    """
    return int(val[0])

def beginningPage(val):
    """
    returns the first page the record occurs on as a string not an int
    BP tag
    """
    return val[0].strip()

def abstract(val):
    """
    return abstract of the record, with newlines hopefully in the correct places
    AB tag
    """
    return '\n'.join(val)

def supplement(val):
    """
    returns the supplemtn number
    SU tag
    """
    return ' '.join(val)

def confHost(val):
    """
    returns the host of the conference
    HO tag
    """
    return ' '.join(val)

def publisherAddress(val):
    """
    returns the publishers address
    PA tag
    """
    return ' '.join(val)

def endingPage(val):
    """
    return the last page the record occurs on as a string not an int
    EP tag
    """
    return val[0].strip()

def year(val):
    """
    returns the year the record was published in as an int
    PY tag
    """
    yearField = val[0]
    if len(yearField) == 4:
        return int(yearField)
    else:
        raise ValueError("Incorrectly formatted PY tag")

def authKeyWords(val):
    """
    returns the keywords assigned by the author of the Record
    DE tag
    """
    return ' '.join(val).split('; ')

def reprintAddress(val):
    """
    returns the reprint address string
    RP tag
    """
    return val[0]

def totalTimesCited(val):
    """
    returns the total number of citations of the record
    Z9 tag
    """
    return int(val[0])

def partNumber(val):
    """
    return an integer giving the part of the issue the Record is in
    PN tag
    """
    return int(val[0])

def specialIssue(val):
    """
    returns the special issue value
    SI tag
    """
    return val[0]

def subjects(val):
    """
    returns a lsit of subjects as assigned by WOS
    WC tag
    """
    return ' '.join(val).split('; ')

def keyWords(val):
    """
    returns the WOS keywords of the Record
    ID tag
    """
    return ' '.join(val).split('; ')

def pubMedID(val):
    """
    returns the pubmed idof the record
    PM tag
    """
    return val[0]

def documentDeliveryNumber(val):
    """
    returns the document delivery number of the Record
    GA tag
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
            'ED' : editors,
            'TI' : title,
            'SO' : journal,
            'SE' : seriesTitle,
            'BS' : seriesSubtitle,
            'LA' : language,
            'DT' : docType,
            'CT' : confTitle,
            'CY' : confDate,
            'HO' : confHost,
            'CL' : confLocation,
            'SP' : confSponsors,
            'DE' : authKeyWords,
            'ID' : keyWords,
            'AB' : abstract,
            'C1' : authAddress,
            'RP' : reprintAddress,
            'EM' : email,
            'RI' : ResearcherIDnumber,
            'OI' : orcID,
            'FU' : funding,
            'FX' : fundingText,
            'CR' : citations,
            'NR' : citedRefsCount,
            'TC' : wosTimesCited,
            'Z9' : totalTimesCited,
            'PU' : publisher,
            'PI' : publisherCity,
            'PA' : publisherAddress,
            'SC' : subjectCategory,
            'SN' : ISSN,
            'EI' : eISSN,
            'BN' : ISBN,
            'J9' : j9,
            'JI' : isoAbbreviation,
            'PD' : month,
            'PY' : year,
            'VL' : volume,
            'IS' : issue,
            'PN' : partNumber,
            'SU' : supplement,
            'SI' : specialIssue,
            'MA' : meetingAbstract,
            'BP' : beginningPage,
            'EP' : endingPage,
            'AR' : articleNumber,
            'PG' : pageCount,
            'WC' : subjects,
            'DI' : DOI,
            'D2' : bookDOI,
            'GA' : documentDeliveryNumber,
            'UT' : wosString,
            'PM' : pubMedID,
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
