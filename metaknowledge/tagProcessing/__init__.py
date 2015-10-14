"""The functions used by metaknowledge to handle WOS tags

Each of the functions in tagProcessing is named after the long name of its tag and is responsible for taking the raw data from a WOS file and returning usable information. The raw data is a list containing each line associated with the tag as a string. So the section of a record:

    TI The Motion Behind the Symbols: A Vital Role for Dynamism in the
      Conceptualization of Limits and Continuity in Expert Mathematics

would be the list:

    ["The Motion Behind the Symbols: A Vital Role for Dynamism in the",
    "Conceptualization of Limits and Continuity in Expert Mathematics"
    ]

The function to process it is called [`title()`](#tagProcessing.title) which is determined by looking up the tag in the `tagProcessing.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`](#metaknowledge.metaknowledge).

The full list of tags and their long names is provided below followed by the descriptions of the functions:

| tag | Name |
|:---|:---|
| `'EM'` |[email]({{ site.baseurl }}{{ page.url }}#tagProcessing.email)
| `'BS'` |[seriesSubtitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.seriesSubtitle)
| `'VL'` |[volume]({{ site.baseurl }}{{ page.url }}#tagProcessing.volume)
| `'SO'` |[journal]({{ site.baseurl }}{{ page.url }}#tagProcessing.journal)
| `'PM'` |[pubMedID]({{ site.baseurl }}{{ page.url }}#tagProcessing.pubMedID)
| `'RP'` |[reprintAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.reprintAddress)
| `'PU'` |[publisher]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisher)
| `'GP'` |[group]({{ site.baseurl }}{{ page.url }}#tagProcessing.group)
| `'J9'` |[j9]({{ site.baseurl }}{{ page.url }}#tagProcessing.j9)
| `'CR'` |[citations]({{ site.baseurl }}{{ page.url }}#tagProcessing.citations)
| `'EP'` |[endingPage]({{ site.baseurl }}{{ page.url }}#tagProcessing.endingPage)
| `'C1'` |[authAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.authAddress)
| `'UT'` |[wosString]({{ site.baseurl }}{{ page.url }}#tagProcessing.wosString)
| `'Z9'` |[totalTimesCited]({{ site.baseurl }}{{ page.url }}#tagProcessing.totalTimesCited)
| `'ID'` |[keyWords]({{ site.baseurl }}{{ page.url }}#tagProcessing.keyWords)
| `'PY'` |[year]({{ site.baseurl }}{{ page.url }}#tagProcessing.year)
| `'RI'` |[ResearcherIDnumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.ResearcherIDnumber)
| `'EI'` |[eISSN]({{ site.baseurl }}{{ page.url }}#tagProcessing.eISSN)
| `'BF'` |[bookAuthorFull]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookAuthorFull)
| `'BN'` |[ISBN]({{ site.baseurl }}{{ page.url }}#tagProcessing.ISBN)
| `'BP'` |[beginningPage]({{ site.baseurl }}{{ page.url }}#tagProcessing.beginningPage)
| `'AR'` |[articleNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.articleNumber)
| `'SU'` |[supplement]({{ site.baseurl }}{{ page.url }}#tagProcessing.supplement)
| `'NR'` |[citedRefsCount]({{ site.baseurl }}{{ page.url }}#tagProcessing.citedRefsCount)
| `'LA'` |[language]({{ site.baseurl }}{{ page.url }}#tagProcessing.language)
| `'BA'` |[bookAuthor]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookAuthor)
| `'SN'` |[ISSN]({{ site.baseurl }}{{ page.url }}#tagProcessing.ISSN)
| `'CA'` |[groupName]({{ site.baseurl }}{{ page.url }}#tagProcessing.groupName)
| `'D2'` |[bookDOI]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookDOI)
| `'PA'` |[publisherAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisherAddress)
| `'TC'` |[wosTimesCited]({{ site.baseurl }}{{ page.url }}#tagProcessing.wosTimesCited)
| `'OI'` |[orcID]({{ site.baseurl }}{{ page.url }}#tagProcessing.orcID)
| `'GA'` |[documentDeliveryNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.documentDeliveryNumber)
| `'AU'` |[authorsShort]({{ site.baseurl }}{{ page.url }}#tagProcessing.authorsShort)
| `'PG'` |[pageCount]({{ site.baseurl }}{{ page.url }}#tagProcessing.pageCount)
| `'SI'` |[specialIssue]({{ site.baseurl }}{{ page.url }}#tagProcessing.specialIssue)
| `'WC'` |[subjects]({{ site.baseurl }}{{ page.url }}#tagProcessing.subjects)
| `'CL'` |[confLocation]({{ site.baseurl }}{{ page.url }}#tagProcessing.confLocation)
| `'SP'` |[confSponsors]({{ site.baseurl }}{{ page.url }}#tagProcessing.confSponsors)
| `'PT'` |[pubType]({{ site.baseurl }}{{ page.url }}#tagProcessing.pubType)
| `'AB'` |[abstract]({{ site.baseurl }}{{ page.url }}#tagProcessing.abstract)
| `'BE'` |[editedBy]({{ site.baseurl }}{{ page.url }}#tagProcessing.editedBy)
| `'PI'` |[publisherCity]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisherCity)
| `'HO'` |[confHost]({{ site.baseurl }}{{ page.url }}#tagProcessing.confHost)
| `'DI'` |[DOI]({{ site.baseurl }}{{ page.url }}#tagProcessing.DOI)
| `'AF'` |[authorsFull]({{ site.baseurl }}{{ page.url }}#tagProcessing.authorsFull)
| `'TI'` |[title]({{ site.baseurl }}{{ page.url }}#tagProcessing.title)
| `'SC'` |[subjectCategory]({{ site.baseurl }}{{ page.url }}#tagProcessing.subjectCategory)
| `'FX'` |[fundingText]({{ site.baseurl }}{{ page.url }}#tagProcessing.fundingText)
| `'DT'` |[docType]({{ site.baseurl }}{{ page.url }}#tagProcessing.docType)
| `'CT'` |[confTitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.confTitle)
| `'IS'` |[issue]({{ site.baseurl }}{{ page.url }}#tagProcessing.issue)
| `'PD'` |[month]({{ site.baseurl }}{{ page.url }}#tagProcessing.month)
| `'JI'` |[isoAbbreviation]({{ site.baseurl }}{{ page.url }}#tagProcessing.isoAbbreviation)
| `'CY'` |[confDate]({{ site.baseurl }}{{ page.url }}#tagProcessing.confDate)
| `'DE'` |[authKeyWords]({{ site.baseurl }}{{ page.url }}#tagProcessing.authKeyWords)
| `'FU'` |[funding]({{ site.baseurl }}{{ page.url }}#tagProcessing.funding)
| `'PN'` |[partNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.partNumber)
| `'ED'` |[editors]({{ site.baseurl }}{{ page.url }}#tagProcessing.editors)
| `'SE'` |[seriesTitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.seriesTitle)
| `'MA'` |[meetingAbstract]({{ site.baseurl }}{{ page.url }}#tagProcessing.meetingAbstract)
"""

from .tagFunctions import *
from .funcDicts import *
