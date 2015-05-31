def isInteractive():
    import sys
    try:
        s = sys.ps1
        if isinstance(s, str):
            return True
        else:
            return False
    except AttributeError:
        return False

VERBOSE_MODE = isInteractive()

monthDict = {'SPR': 3, 'SUM': 6, 'FAL': 9, 'WIN': 12, 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6 , 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12}

tagToFull = {
            'PT' : "pubType",
            'AF' : "authorsFull",
            #'GA' : "groupAuthors",
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
