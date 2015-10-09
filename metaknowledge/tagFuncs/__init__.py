"""The functions used by metaknowledge to handle WOS tags

Each of the functions in tagFuncs is named after the long name of its tag and is responsible for taking the raw data from a WOS file and returning usable information. The raw data is a list containing each line associated with the tag as a string. So the section of a record:

    TI The Motion Behind the Symbols: A Vital Role for Dynamism in the
      Conceptualization of Limits and Continuity in Expert Mathematics

would be the list:

    ["The Motion Behind the Symbols: A Vital Role for Dynamism in the",
    "Conceptualization of Limits and Continuity in Expert Mathematics"
    ]

The function to process it is called [`title()`](#tagFuncs.title) which is determined by looking up the tag in the `tagFuncs.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`](#metaknowledge.metaknowledge).

The full list of tags and their long names is provided below followed by the descriptions of the functions:

| tag | Name |
|:---|:---|
| `'EM'` |[email]({{ site.baseurl }}{{ page.url }}#tagFuncs.email)
| `'BS'` |[seriesSubtitle]({{ site.baseurl }}{{ page.url }}#tagFuncs.seriesSubtitle)
| `'VL'` |[volume]({{ site.baseurl }}{{ page.url }}#tagFuncs.volume)
| `'SO'` |[journal]({{ site.baseurl }}{{ page.url }}#tagFuncs.journal)
| `'PM'` |[pubMedID]({{ site.baseurl }}{{ page.url }}#tagFuncs.pubMedID)
| `'RP'` |[reprintAddress]({{ site.baseurl }}{{ page.url }}#tagFuncs.reprintAddress)
| `'PU'` |[publisher]({{ site.baseurl }}{{ page.url }}#tagFuncs.publisher)
| `'GP'` |[group]({{ site.baseurl }}{{ page.url }}#tagFuncs.group)
| `'J9'` |[j9]({{ site.baseurl }}{{ page.url }}#tagFuncs.j9)
| `'CR'` |[citations]({{ site.baseurl }}{{ page.url }}#tagFuncs.citations)
| `'EP'` |[endingPage]({{ site.baseurl }}{{ page.url }}#tagFuncs.endingPage)
| `'C1'` |[authAddress]({{ site.baseurl }}{{ page.url }}#tagFuncs.authAddress)
| `'UT'` |[wosString]({{ site.baseurl }}{{ page.url }}#tagFuncs.wosString)
| `'Z9'` |[totalTimesCited]({{ site.baseurl }}{{ page.url }}#tagFuncs.totalTimesCited)
| `'ID'` |[keyWords]({{ site.baseurl }}{{ page.url }}#tagFuncs.keyWords)
| `'PY'` |[year]({{ site.baseurl }}{{ page.url }}#tagFuncs.year)
| `'RI'` |[ResearcherIDnumber]({{ site.baseurl }}{{ page.url }}#tagFuncs.ResearcherIDnumber)
| `'EI'` |[eISSN]({{ site.baseurl }}{{ page.url }}#tagFuncs.eISSN)
| `'BF'` |[bookAuthorFull]({{ site.baseurl }}{{ page.url }}#tagFuncs.bookAuthorFull)
| `'BN'` |[ISBN]({{ site.baseurl }}{{ page.url }}#tagFuncs.ISBN)
| `'BP'` |[beginningPage]({{ site.baseurl }}{{ page.url }}#tagFuncs.beginningPage)
| `'AR'` |[articleNumber]({{ site.baseurl }}{{ page.url }}#tagFuncs.articleNumber)
| `'SU'` |[supplement]({{ site.baseurl }}{{ page.url }}#tagFuncs.supplement)
| `'NR'` |[citedRefsCount]({{ site.baseurl }}{{ page.url }}#tagFuncs.citedRefsCount)
| `'LA'` |[language]({{ site.baseurl }}{{ page.url }}#tagFuncs.language)
| `'BA'` |[bookAuthor]({{ site.baseurl }}{{ page.url }}#tagFuncs.bookAuthor)
| `'SN'` |[ISSN]({{ site.baseurl }}{{ page.url }}#tagFuncs.ISSN)
| `'CA'` |[groupName]({{ site.baseurl }}{{ page.url }}#tagFuncs.groupName)
| `'D2'` |[bookDOI]({{ site.baseurl }}{{ page.url }}#tagFuncs.bookDOI)
| `'PA'` |[publisherAddress]({{ site.baseurl }}{{ page.url }}#tagFuncs.publisherAddress)
| `'TC'` |[wosTimesCited]({{ site.baseurl }}{{ page.url }}#tagFuncs.wosTimesCited)
| `'OI'` |[orcID]({{ site.baseurl }}{{ page.url }}#tagFuncs.orcID)
| `'GA'` |[documentDeliveryNumber]({{ site.baseurl }}{{ page.url }}#tagFuncs.documentDeliveryNumber)
| `'AU'` |[authorsShort]({{ site.baseurl }}{{ page.url }}#tagFuncs.authorsShort)
| `'PG'` |[pageCount]({{ site.baseurl }}{{ page.url }}#tagFuncs.pageCount)
| `'SI'` |[specialIssue]({{ site.baseurl }}{{ page.url }}#tagFuncs.specialIssue)
| `'WC'` |[subjects]({{ site.baseurl }}{{ page.url }}#tagFuncs.subjects)
| `'CL'` |[confLocation]({{ site.baseurl }}{{ page.url }}#tagFuncs.confLocation)
| `'SP'` |[confSponsors]({{ site.baseurl }}{{ page.url }}#tagFuncs.confSponsors)
| `'PT'` |[pubType]({{ site.baseurl }}{{ page.url }}#tagFuncs.pubType)
| `'AB'` |[abstract]({{ site.baseurl }}{{ page.url }}#tagFuncs.abstract)
| `'BE'` |[editedBy]({{ site.baseurl }}{{ page.url }}#tagFuncs.editedBy)
| `'PI'` |[publisherCity]({{ site.baseurl }}{{ page.url }}#tagFuncs.publisherCity)
| `'HO'` |[confHost]({{ site.baseurl }}{{ page.url }}#tagFuncs.confHost)
| `'DI'` |[DOI]({{ site.baseurl }}{{ page.url }}#tagFuncs.DOI)
| `'AF'` |[authorsFull]({{ site.baseurl }}{{ page.url }}#tagFuncs.authorsFull)
| `'TI'` |[title]({{ site.baseurl }}{{ page.url }}#tagFuncs.title)
| `'SC'` |[subjectCategory]({{ site.baseurl }}{{ page.url }}#tagFuncs.subjectCategory)
| `'FX'` |[fundingText]({{ site.baseurl }}{{ page.url }}#tagFuncs.fundingText)
| `'DT'` |[docType]({{ site.baseurl }}{{ page.url }}#tagFuncs.docType)
| `'CT'` |[confTitle]({{ site.baseurl }}{{ page.url }}#tagFuncs.confTitle)
| `'IS'` |[issue]({{ site.baseurl }}{{ page.url }}#tagFuncs.issue)
| `'PD'` |[month]({{ site.baseurl }}{{ page.url }}#tagFuncs.month)
| `'JI'` |[isoAbbreviation]({{ site.baseurl }}{{ page.url }}#tagFuncs.isoAbbreviation)
| `'CY'` |[confDate]({{ site.baseurl }}{{ page.url }}#tagFuncs.confDate)
| `'DE'` |[authKeyWords]({{ site.baseurl }}{{ page.url }}#tagFuncs.authKeyWords)
| `'FU'` |[funding]({{ site.baseurl }}{{ page.url }}#tagFuncs.funding)
| `'PN'` |[partNumber]({{ site.baseurl }}{{ page.url }}#tagFuncs.partNumber)
| `'ED'` |[editors]({{ site.baseurl }}{{ page.url }}#tagFuncs.editors)
| `'SE'` |[seriesTitle]({{ site.baseurl }}{{ page.url }}#tagFuncs.seriesTitle)
| `'MA'` |[meetingAbstract]({{ site.baseurl }}{{ page.url }}#tagFuncs.meetingAbstract)

"""

from .tagFuncs import *
