from .helpFuncs import getMonth, makeReversed
from ..citation import Citation


def pubType(val):
    """
    #The PT Tag

    returns the type of publication as a character: conference, book, journal, book in series, or patent

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > A string

    """
    return val[0]


def authorsFull(val):
    """
    #The AF Tag

    returns a list of authors full names

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of author's names

    """
    return val

def group(val):
    """
    #The GP Tag

    returns the group associated with the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > A the name of the group

    """
    return val[0]

def editedBy(val):
    """
    #The BE Tag

    returns a list of the editors of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of editors

    """
    return val

def authorsShort(val):
    """
    #The AU Tag

    returns a list of authors shortened names

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of shortened author's names

    """
    return val

def bookAuthor(val):
    """
    #The BA Tag

    returns a list of the short names of the authors of a book Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of shortened author's names

    """
    return val

def bookAuthorFull(val):
    """
    #The BF Tag

    returns a list of the long names of the authors of a book Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of author's names

    """
    return val

def groupName(val):
    """
    #The CA Tag

    returns the name of the group associated with the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The group's name

    """
    return val[0]

def title(val):
    """
    #The TI Tag

    returns the title of the record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The title of the record

    """
    return ' '.join(val)

def editors(val):
    """
    # Needs Work

    currently not well understood, returns _val_
    """
    return val

def journal(val):
    """
    #The SO Tag

    returns the full name of the publication

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The name of the journal

    """
    return ' '.join(val)

def seriesTitle(val):
    """
    #The SE Tag

    returns the title of the series the Record is in

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The title of the series

    """
    return ' '.join(val)

def seriesSubtitle(val):
    """
    #The BS Tag

    returns the title of the series the Record is in

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The subtitle of the series

    """
    return ' '.join(val)

def language(val):
    """
    #The LA Tag

    returns the languages of the Record as a string with languages separated by ', ', usually there is only one language

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The language(s) of the record

    """
    return ', '.join(val)

def docType(val):
    """
    #The DT Tag

    returns the type of document the Record contains

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The type of the Record

    """
    return val[0]

def confTitle(val):
    """
    #The CT Tag

    returns the title of the conference associated with the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The title of the conference

    """
    return ' '.join(val)

def confDate(val):
    """
    #The CY Tag

    returns the date string of the conference associated with the Record, the date is not normalized

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The data of the conference

    """
    return val[0]

def confSponsors(val):
    """
    #The SP Tag

    returns a list of sponsors for the conference associated with the record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > A the list of of sponsors

    """
    return ', '.join(val).split(', ')

def wosTimesCited(val):
    """
    #The TC Tag

    returns the number of times the Record has been cited by records in WOS

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The number of time the Record has been cited

    """
    return int(val[0])

def authAddress(val):
    """
    # The C1 Tag

    Returns the address of the authors as given by WOS. **Warning** the mapping of author to address is not very good and is given in multiple ways.

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of addresses

    """
    ret = []
    for a in val:
        if a[0] == '[':
            ret.append('] '.join(a.split('] ')[1:]))
        else:
            ret.append(a)
    return ret

def confLocation(val):
    """
    #The CL Tag

    returns the sting giving the conference's location

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The conferences address

    """
    return ' '.join(val)

def j9(val):
    """
    #The J9 Tag

    returns the J9 (29-Character Source Abbreviation) of the publication

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The 29-Character Source Abbreviation

    """
    return val[0]

def funding(val):
    """
    #The FU Tag

    Returns a list of the groups funding the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of funding groups

    """
    return ' '.join(val).split('; ')

def subjectCategory(val):
    """
    #The SC Tag

    returns a list of the subjects associated with the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of the subjects associated with the Record

    """
    return ' '.join(val).split('; ')

def citations(val):
    """
    #The CR Tag

    returns a list of all the citations in the record, the citations are the [metaknowledge.Citation](#Citation.Citation) class.

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    ` list[metaknowledge.Citation]`

    > A list of Citations

    """
    retCites = []
    for c in val:
        retCites.append(Citation(c))
    return retCites

def publisherCity(val):
    """
    #The PI Tag

    Returns the city the publisher is in

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The city of the publisher

    """
    return ' '.join(val).upper()

def ISSN(val):
    """
    #The SN Tag

    returns the ISSN of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The ISSN string

    """
    return val[0]

def articleNumber(val):
    """
    #The AR Tag

    returns a string giving the article number, not all are integers

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The article number

    """
    return val[0]

def issue(val):
    """
    #The IS Tag

    returns a string giving the issue or range of issues the Record was in, not all are integers

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The issue number/range

    """
    return val[0]

def email(val):
    """
    #The EM Tag

    returns a list of emails given by the authors of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > A list of emails

    """
    return ' '.join(val).split('; ')

def eISSN(val):
    """
    #The EI Tag

    returns the EISSN of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The EISSN string

    """
    return val[0]

def DOI(val):
    """
    #The DI Tag

    return the DOI number of the record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The DOI number string

    """
    return val[0]

def wosString(val):
    """
    #The UT Tag

    returns the WOS number of the record as a string preceded by "WOS:"

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The WOS number

    """
    return val[0]

def orcID(val):
    """
    #The OI Tag

    returns a list of orc IDs of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The orc ID

    """
    return ' '.join(val).split('; ')

def meetingAbstract(val):
    """
    #The MA Tag

    returns the ID of the meeting abstract prefixed by 'EPA-'

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The meeting abstract prefixed

    """
    return val[0]

def isoAbbreviation(val):
    """
    #The JI Tag

    returns the iso abbreviation of the journal

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The iso abbreviation of the journal

    """
    return ' '.join(val).upper()

def pageCount(val):
    """
    #The PG Tag

    returns an integer giving the number of pages of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The page count

    """
    return int(val[0])

def publisher(val):
    """
    #The PU Tag

    returns the publisher of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The publisher

    """
    return ' '.join(val).upper()

def ISBN(val):
    """
    #The BN Tag

    returns a list of ISBNs associated with the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list`

    > The ISBNs

    """
    return ' '.join(val).split('; ')

def month(val):
    """
    #The PD Tag

    returns the month the record was published in as an int with January as 1, February 2, ...

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > A integer giving the month

    """
    return getMonth(val[0])

def fundingText(val):
    """
    #The FX Tag

    Returns a string of the funding thanks

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The funding thank-you

    """
    return ' '.join(val)

def bookDOI(val):
    """
    #The D2 Tag

    returns the book DOI of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The DOI number

    """
    return val[0]

def volume(val):
    """
    #The VL Tag

    return the volume the record is in as a string, not all are integers

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The volume number

    """
    return val[0].strip()

def ResearcherIDnumber(val):
    """
    #The RI Tag

    returns a list of the research IDs of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > The list of the research IDs

    """
    return ' '.join(val).split('; ')

def citedRefsCount(val):
    """
    #The NR Tag

    returns the number citations, length of CR list

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The number of CRs

    """
    return int(val[0])

def beginningPage(val):
    """
    #The BP Tag

    returns the first page the record occurs on, not all are integers

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The first page number

    """
    return val[0].strip()

def abstract(val):
    """
    #The AB Tag

    return abstract of the record, with newlines hopefully in the correct places

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The abstract

    """
    return '\n'.join(val)

def supplement(val):
    """
    #The SU Tag

    returns the supplement number

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The supplement number

    """
    return ' '.join(val)

def confHost(val):
    """
    #The HO Tag

    returns the host of the conference

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The host

    """
    return ' '.join(val)

def publisherAddress(val):
    """
    #The PA Tag

    returns the publishers address

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The publisher address

    """
    return ' '.join(val)

def endingPage(val):
    """
    #The EP Tag

    return the last page the record occurs on as a string, not aall are intergers

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The final page number

    """
    return val[0].strip()

def year(val):
    """
    #The PY Tag

    returns the year the record was published in as an int

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The year

    """
    yearField = val[0]
    if len(yearField) == 4:
        return int(yearField)
    else:
        raise ValueError("Incorrectly formatted PY tag")

def authKeyWords(val):
    """
    #The DE Tag

    returns the keywords assigned by the author of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > The list of keywords

    """
    return ' '.join(val).split('; ')

def reprintAddress(val):
    """
    #The RP Tag

    returns the reprint address string

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The reprint address

    """
    return val[0]

def totalTimesCited(val):
    """
    #The Z9 Tag

    returns the total number of citations of the record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The total number of citations

    """
    return int(val[0])

def partNumber(val):
    """
    #The PN Tag

    return an integer giving the part of the issue the Record is in

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `int`

    > The part of the issue of the Record

    """
    return val[0]

def specialIssue(val):
    """
    #The SI Tag

    returns the special issue value

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The special issue value

    """
    return val[0]

def subjects(val):
    """
    #The WC Tag

    returns a list of subjects as assigned by WOS

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > The subjects list

    """
    return ' '.join(val).split('; ')

def keyWords(val):
    """
    #The ID Tag

    returns the WOS keywords of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `list[str]`

    > The keyWords list

    """
    return ' '.join(val).split('; ')

def pubMedID(val):
    """
    #The PM Tag

    returns the pubmed ID of the record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The pubmed ID

    """
    return val[0]

def documentDeliveryNumber(val):
    """
    #The GA Tag

    returns the document delivery number of the Record

    # Parameters

    _val_: `list[str]`

    > The raw data from a WOS file

    # Returns

    `str`

    > The document delivery number

    """
    return val[0]

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
