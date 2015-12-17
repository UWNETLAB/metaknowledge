#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""The functions used by metaknowledge to handle WOS tags

Each of the functions in tagProcessing is named after the long name of its tag and is responsible for taking the raw data from a WOS file and returning usable information. The raw data is a list containing each line associated with the tag as a string. So the section of a record:

    TI The Motion Behind the Symbols: A Vital Role for Dynamism in the
      Conceptualization of Limits and Continuity in Expert Mathematics

would be the list:

    ["The Motion Behind the Symbols: A Vital Role for Dynamism in the",
    "Conceptualization of Limits and Continuity in Expert Mathematics"
    ]

The function to process it is called [`title()`](#tagProcessing.title) which is determined by looking up the tag in the `tagProcessing.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`](#metaknowledge.metaknowledge).

The objects `tagToFullDict`, `fullToTagDict`, `tagNameConverterDict`, `tagsAndNameSet` and `knownTagsList` are also provided. They are the objects used by metaknowledge to keep track of tag names. `tagToFullDict` and `fullToTagDict` are dictionaries that convert from tags to full names and vice versa, respectively, while `tagNameConverterDict` goes both ways. `tagsAndNameSet` is a set of all full names and tags, while `knownTagsList` contains only tags and is a list. For a less raw interface look the functions provided by the base metaknowledge module, e.g. [`tagToFull()`](#metaknowledge.tagToFull).

The full list of tags and their long names is provided below followed by the descriptions of the functions, they are ordered by their occurrence in WOS records:

| tag | Name |
|:---|:---|
| [`'PT'`]({{ site.baseurl }}{{ page.url }}#pubType) | [pubType]({{ site.baseurl }}{{ page.url }}#pubType) |
| [`'AF'`]({{ site.baseurl }}{{ page.url }}#authorsFull) | [authorsFull]({{ site.baseurl }}{{ page.url }}#authorsFull) |
| [`'GP'`]({{ site.baseurl }}{{ page.url }}#group) | [group]({{ site.baseurl }}{{ page.url }}#group) |
| [`'BE'`]({{ site.baseurl }}{{ page.url }}#editedBy) | [editedBy]({{ site.baseurl }}{{ page.url }}#editedBy) |
| [`'AU'`]({{ site.baseurl }}{{ page.url }}#authorsShort) | [authorsShort]({{ site.baseurl }}{{ page.url }}#authorsShort) |
| [`'BA'`]({{ site.baseurl }}{{ page.url }}#bookAuthor) | [bookAuthor]({{ site.baseurl }}{{ page.url }}#bookAuthor) |
| [`'BF'`]({{ site.baseurl }}{{ page.url }}#bookAuthorFull) | [bookAuthorFull]({{ site.baseurl }}{{ page.url }}#bookAuthorFull) |
| [`'CA'`]({{ site.baseurl }}{{ page.url }}#groupName) | [groupName]({{ site.baseurl }}{{ page.url }}#groupName) |
| [`'ED'`]({{ site.baseurl }}{{ page.url }}#editors) | [editors]({{ site.baseurl }}{{ page.url }}#editors) |
| [`'TI'`]({{ site.baseurl }}{{ page.url }}#title) | [title]({{ site.baseurl }}{{ page.url }}#title) |
| [`'SO'`]({{ site.baseurl }}{{ page.url }}#journal) | [journal]({{ site.baseurl }}{{ page.url }}#journal) |
| [`'SE'`]({{ site.baseurl }}{{ page.url }}#seriesTitle) | [seriesTitle]({{ site.baseurl }}{{ page.url }}#seriesTitle) |
| [`'BS'`]({{ site.baseurl }}{{ page.url }}#seriesSubtitle) | [seriesSubtitle]({{ site.baseurl }}{{ page.url }}#seriesSubtitle) |
| [`'LA'`]({{ site.baseurl }}{{ page.url }}#language) | [language]({{ site.baseurl }}{{ page.url }}#language) |
| [`'DT'`]({{ site.baseurl }}{{ page.url }}#docType) | [docType]({{ site.baseurl }}{{ page.url }}#docType) |
| [`'CT'`]({{ site.baseurl }}{{ page.url }}#confTitle) | [confTitle]({{ site.baseurl }}{{ page.url }}#confTitle) |
| [`'CY'`]({{ site.baseurl }}{{ page.url }}#confDate) | [confDate]({{ site.baseurl }}{{ page.url }}#confDate) |
| [`'HO'`]({{ site.baseurl }}{{ page.url }}#confHost) | [confHost]({{ site.baseurl }}{{ page.url }}#confHost) |
| [`'CL'`]({{ site.baseurl }}{{ page.url }}#confLocation) | [confLocation]({{ site.baseurl }}{{ page.url }}#confLocation) |
| [`'SP'`]({{ site.baseurl }}{{ page.url }}#confSponsors) | [confSponsors]({{ site.baseurl }}{{ page.url }}#confSponsors) |
| [`'DE'`]({{ site.baseurl }}{{ page.url }}#authKeyWords) | [authKeyWords]({{ site.baseurl }}{{ page.url }}#authKeyWords) |
| [`'ID'`]({{ site.baseurl }}{{ page.url }}#keyWords) | [keyWords]({{ site.baseurl }}{{ page.url }}#keyWords) |
| [`'AB'`]({{ site.baseurl }}{{ page.url }}#abstract) | [abstract]({{ site.baseurl }}{{ page.url }}#abstract) |
| [`'C1'`]({{ site.baseurl }}{{ page.url }}#authAddress) | [authAddress]({{ site.baseurl }}{{ page.url }}#authAddress) |
| [`'RP'`]({{ site.baseurl }}{{ page.url }}#reprintAddress) | [reprintAddress]({{ site.baseurl }}{{ page.url }}#reprintAddress) |
| [`'EM'`]({{ site.baseurl }}{{ page.url }}#email) | [email]({{ site.baseurl }}{{ page.url }}#email) |
| [`'RI'`]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber) | [ResearcherIDnumber]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber) |
| [`'OI'`]({{ site.baseurl }}{{ page.url }}#orcID) | [orcID]({{ site.baseurl }}{{ page.url }}#orcID) |
| [`'FU'`]({{ site.baseurl }}{{ page.url }}#funding) | [funding]({{ site.baseurl }}{{ page.url }}#funding) |
| [`'FX'`]({{ site.baseurl }}{{ page.url }}#fundingText) | [fundingText]({{ site.baseurl }}{{ page.url }}#fundingText) |
| [`'CR'`]({{ site.baseurl }}{{ page.url }}#citations) | [citations]({{ site.baseurl }}{{ page.url }}#citations) |
| [`'NR'`]({{ site.baseurl }}{{ page.url }}#citedRefsCount) | [citedRefsCount]({{ site.baseurl }}{{ page.url }}#citedRefsCount) |
| [`'TC'`]({{ site.baseurl }}{{ page.url }}#wosTimesCited) | [wosTimesCited]({{ site.baseurl }}{{ page.url }}#wosTimesCited) |
| [`'Z9'`]({{ site.baseurl }}{{ page.url }}#totalTimesCited) | [totalTimesCited]({{ site.baseurl }}{{ page.url }}#totalTimesCited) |
| [`'PU'`]({{ site.baseurl }}{{ page.url }}#publisher) | [publisher]({{ site.baseurl }}{{ page.url }}#publisher) |
| [`'PI'`]({{ site.baseurl }}{{ page.url }}#publisherCity) | [publisherCity]({{ site.baseurl }}{{ page.url }}#publisherCity) |
| [`'PA'`]({{ site.baseurl }}{{ page.url }}#publisherAddress) | [publisherAddress]({{ site.baseurl }}{{ page.url }}#publisherAddress) |
| [`'SC'`]({{ site.baseurl }}{{ page.url }}#subjectCategory) | [subjectCategory]({{ site.baseurl }}{{ page.url }}#subjectCategory) |
| [`'SN'`]({{ site.baseurl }}{{ page.url }}#ISSN) | [ISSN]({{ site.baseurl }}{{ page.url }}#ISSN) |
| [`'EI'`]({{ site.baseurl }}{{ page.url }}#eISSN) | [eISSN]({{ site.baseurl }}{{ page.url }}#eISSN) |
| [`'BN'`]({{ site.baseurl }}{{ page.url }}#ISBN) | [ISBN]({{ site.baseurl }}{{ page.url }}#ISBN) |
| [`'J9'`]({{ site.baseurl }}{{ page.url }}#j9) | [j9]({{ site.baseurl }}{{ page.url }}#j9) |
| [`'JI'`]({{ site.baseurl }}{{ page.url }}#isoAbbreviation) | [isoAbbreviation]({{ site.baseurl }}{{ page.url }}#isoAbbreviation) |
| [`'PD'`]({{ site.baseurl }}{{ page.url }}#month) | [month]({{ site.baseurl }}{{ page.url }}#month) |
| [`'PY'`]({{ site.baseurl }}{{ page.url }}#year) | [year]({{ site.baseurl }}{{ page.url }}#year) |
| [`'VL'`]({{ site.baseurl }}{{ page.url }}#volume) | [volume]({{ site.baseurl }}{{ page.url }}#volume) |
| [`'IS'`]({{ site.baseurl }}{{ page.url }}#issue) | [issue]({{ site.baseurl }}{{ page.url }}#issue) |
| [`'PN'`]({{ site.baseurl }}{{ page.url }}#partNumber) | [partNumber]({{ site.baseurl }}{{ page.url }}#partNumber) |
| [`'SU'`]({{ site.baseurl }}{{ page.url }}#supplement) | [supplement]({{ site.baseurl }}{{ page.url }}#supplement) |
| [`'SI'`]({{ site.baseurl }}{{ page.url }}#specialIssue) | [specialIssue]({{ site.baseurl }}{{ page.url }}#specialIssue) |
| [`'MA'`]({{ site.baseurl }}{{ page.url }}#meetingAbstract) | [meetingAbstract]({{ site.baseurl }}{{ page.url }}#meetingAbstract) |
| [`'BP'`]({{ site.baseurl }}{{ page.url }}#beginningPage) | [beginningPage]({{ site.baseurl }}{{ page.url }}#beginningPage) |
| [`'EP'`]({{ site.baseurl }}{{ page.url }}#endingPage) | [endingPage]({{ site.baseurl }}{{ page.url }}#endingPage) |
| [`'AR'`]({{ site.baseurl }}{{ page.url }}#articleNumber) | [articleNumber]({{ site.baseurl }}{{ page.url }}#articleNumber) |
| [`'PG'`]({{ site.baseurl }}{{ page.url }}#pageCount) | [pageCount]({{ site.baseurl }}{{ page.url }}#pageCount) |
| [`'WC'`]({{ site.baseurl }}{{ page.url }}#subjects) | [subjects]({{ site.baseurl }}{{ page.url }}#subjects) |
| [`'DI'`]({{ site.baseurl }}{{ page.url }}#DOI) | [DOI]({{ site.baseurl }}{{ page.url }}#DOI) |
| [`'D2'`]({{ site.baseurl }}{{ page.url }}#bookDOI) | [bookDOI]({{ site.baseurl }}{{ page.url }}#bookDOI) |
| [`'GA'`]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber) | [documentDeliveryNumber]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber) |
| [`'UT'`]({{ site.baseurl }}{{ page.url }}#wosString) | [wosString]({{ site.baseurl }}{{ page.url }}#wosString) |
| [`'PM'`]({{ site.baseurl }}{{ page.url }}#pubMedID) | [pubMedID]({{ site.baseurl }}{{ page.url }}#pubMedID) |
"""

from .tagFunctions import *
from .funcDicts import tagToFullDict, fullToTagDict, tagNameConverterDict, tagsAndNameSet, knownTagsList
