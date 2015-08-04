def isInteractive():
    """
    A basic check of if the program is running in interactive mode
    """
    import sys
    try:
        s = sys.ps1 #pylint: disable=all
        if isinstance(s, str) and sys.stdout.isatty():
            return True
        else:
            return False
    except AttributeError:
        return False


VERBOSE_MODE = isInteractive()

#maps three letter combinations to numbers for use in Record.month
monthDict = {'SPR': 3, 'SUM': 6, 'FAL': 9, 'WIN': 12, 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6 , 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12}

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

"""
Converts WOS tags to more descriptive names
This is all tags known about and is mostly likely not a complete list
The names are not official and are added by the author
"""
tagToFull = {

            'PT' : "pubType",
            'AF' : "authorsFull",
            #'GA' : "groupAuthors", Old usage
            'GP' : "group",
            'BE' : "editedBy",
            'AU' : "authorsShort",
            'BA' : "bookAuthor",
            'BF' : "bookAuthorFull",
            'CA' : "groupName",
            'TI' : "title",
            'ED' : "editors",
            'SO' : "journal",
            'SE' : "seriesTitle",
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
            }

fullToTag = reverseDict(tagToFull) #Reverses tagToFull

tagNameConverter = makeBiDirectional(tagToFull) #tagToFull made reversible

tagsAndNames = set(tagNameConverter.keys()) #set of WOS tags ad their names

knownTagsList = list(tagToFull.keys()) #list of all the known tags
