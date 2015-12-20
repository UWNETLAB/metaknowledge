---
layout: doc
title: tagProcessing
categories: docs
excerpt: All the tags and how they are handled
tags: [module]
weight: 3
---
<a name="tagProcessing"></a>

# [tagProcessing]({{ site.baseurl }}{{ page.url }}#tagProcessing)

The functions used by metaknowledge to handle WOS tags

Each of the functions in tagProcessing is named after the long name of its tag and is responsible for taking the raw data from a WOS file and returning usable information. The raw data is a list containing each line associated with the tag as a string. So the section of a record:

    TI The Motion Behind the Symbols: A Vital Role for Dynamism in the
      Conceptualization of Limits and Continuity in Expert Mathematics

would be the list:

    ["The Motion Behind the Symbols: A Vital Role for Dynamism in the",
    "Conceptualization of Limits and Continuity in Expert Mathematics"
    ]

The function to process it is called [**title**()]({{ site.baseurl }}{{ page.url }}#title) which is determined by looking up the tag in the `tagProcessing.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`]({{ site.baseurl }}{{ page.url }}#metaknowledge).

The objects `tagToFullDict`, `fullToTagDict`, `tagNameConverterDict`, `tagsAndNameSet` and `knownTagsList` are also provided. They are the objects used by _metaknowledge_ to keep track of tag names. `tagToFullDict` and `fullToTagDict` are dictionaries that convert from tags to full names and vice versa, respectively, while `tagNameConverterDict` goes both ways. `tagsAndNameSet` is a set of all full names and tags, while `knownTagsList` contains only tags and is a list. For a less raw interface look the functions provided by the base _metaknowledge_ module, e.g. [**tagToFull**()]({{ site.baseurl }}{{ page.url }}#tagToFull).

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




<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubType"></a><small>tagProcessing.</small>**[<ins>pubType</ins>]({{ site.baseurl }}{{ page.url }}#pubType)**(_val_):

######The PT Tag

extracts the type of publication as a character: conference, book, journal, book in series, or patent

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsFull"></a><small>tagProcessing.</small>**[<ins>authorsFull</ins>]({{ site.baseurl }}{{ page.url }}#authorsFull)**(_val_):

######The AF Tag

extracts a list of authors full names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="group"></a><small>tagProcessing.</small>**[<ins>group</ins>]({{ site.baseurl }}{{ page.url }}#group)**(_val_):

######The GP Tag

extracts the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the name of the group


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editedBy"></a><small>tagProcessing.</small>**[<ins>editedBy</ins>]({{ site.baseurl }}{{ page.url }}#editedBy)**(_val_):

######The BE Tag

extracts a list of the editors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of editors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsShort"></a><small>tagProcessing.</small>**[<ins>authorsShort</ins>]({{ site.baseurl }}{{ page.url }}#authorsShort)**(_val_):

######The AU Tag

extracts a list of authors shortened names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthor"></a><small>tagProcessing.</small>**[<ins>bookAuthor</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthor)**(_val_):

######The BA Tag

extracts a list of the short names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthorFull"></a><small>tagProcessing.</small>**[<ins>bookAuthorFull</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthorFull)**(_val_):

######The BF Tag

extracts a list of the long names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="groupName"></a><small>tagProcessing.</small>**[<ins>groupName</ins>]({{ site.baseurl }}{{ page.url }}#groupName)**(_val_):

######The CA Tag

extracts the name of the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The group's name


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editors"></a><small>tagProcessing.</small>**[<ins>editors</ins>]({{ site.baseurl }}{{ page.url }}#editors)**(_val_):

###### Needs Work

currently not well understood, returns _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="title"></a><small>tagProcessing.</small>**[<ins>title</ins>]({{ site.baseurl }}{{ page.url }}#title)**(_val_):

######The TI Tag

extracts the title of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="journal"></a><small>tagProcessing.</small>**[<ins>journal</ins>]({{ site.baseurl }}{{ page.url }}#journal)**(_val_):

######The SO Tag

extracts the full name of the publication and normalizes it to uppercase

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The name of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesTitle"></a><small>tagProcessing.</small>**[<ins>seriesTitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesTitle)**(_val_):

######The SE Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesSubtitle"></a><small>tagProcessing.</small>**[<ins>seriesSubtitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesSubtitle)**(_val_):

######The BS Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The subtitle of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="language"></a><small>tagProcessing.</small>**[<ins>language</ins>]({{ site.baseurl }}{{ page.url }}#language)**(_val_):

######The LA Tag

extracts the languages of the Record as a string with languages separated by ', ', usually there is only one language

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The language(s) of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="docType"></a><small>tagProcessing.</small>**[<ins>docType</ins>]({{ site.baseurl }}{{ page.url }}#docType)**(_val_):

######The DT Tag

extracts the type of document the Record contains

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The type of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confTitle"></a><small>tagProcessing.</small>**[<ins>confTitle</ins>]({{ site.baseurl }}{{ page.url }}#confTitle)**(_val_):

######The CT Tag

extracts the title of the conference associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confDate"></a><small>tagProcessing.</small>**[<ins>confDate</ins>]({{ site.baseurl }}{{ page.url }}#confDate)**(_val_):

######The CY Tag

extracts the date string of the conference associated with the Record, the date is not normalized

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The data of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confHost"></a><small>tagProcessing.</small>**[<ins>confHost</ins>]({{ site.baseurl }}{{ page.url }}#confHost)**(_val_):

######The HO Tag

extracts the host of the conference

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The host


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confLocation"></a><small>tagProcessing.</small>**[<ins>confLocation</ins>]({{ site.baseurl }}{{ page.url }}#confLocation)**(_val_):

######The CL Tag

extracts the sting giving the conference's location

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The conferences address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confSponsors"></a><small>tagProcessing.</small>**[<ins>confSponsors</ins>]({{ site.baseurl }}{{ page.url }}#confSponsors)**(_val_):

######The SP Tag

extracts a list of sponsors for the conference associated with the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the list of of sponsors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authKeyWords"></a><small>tagProcessing.</small>**[<ins>authKeyWords</ins>]({{ site.baseurl }}{{ page.url }}#authKeyWords)**(_val_):

######The DE Tag

extracts the keywords assigned by the author of the Record. The WOS description is:

    Author keywords are included in records of articles from 1991 forward. They are also include in conference proceedings records.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of keywords


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="keyWords"></a><small>tagProcessing.</small>**[<ins>keyWords</ins>]({{ site.baseurl }}{{ page.url }}#keyWords)**(_val_):

######The ID Tag

extracts the WOS keywords of the Record. The WOS description is:

    KeyWords Plus are index terms created by Thomson Reuters from significant, frequently occurring words in the titles of an article's cited references.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The keyWords list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="abstract"></a><small>tagProcessing.</small>**[<ins>abstract</ins>]({{ site.baseurl }}{{ page.url }}#abstract)**(_val_):

######The AB Tag

return abstract of the record, with newlines hopefully in the correct places

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The abstract


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authAddress"></a><small>tagProcessing.</small>**[<ins>authAddress</ins>]({{ site.baseurl }}{{ page.url }}#authAddress)**(_val_):

###### The C1 Tag

extracts the address of the authors as given by WOS. **Warning** the mapping of author to address is not very good and is given in multiple ways.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of addresses


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="reprintAddress"></a><small>tagProcessing.</small>**[<ins>reprintAddress</ins>]({{ site.baseurl }}{{ page.url }}#reprintAddress)**(_val_):

######The RP Tag

extracts the reprint address string

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The reprint address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="email"></a><small>tagProcessing.</small>**[<ins>email</ins>]({{ site.baseurl }}{{ page.url }}#email)**(_val_):

######The EM Tag

extracts a list of emails given by the authors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of emails


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ResearcherIDnumber"></a><small>tagProcessing.</small>**[<ins>ResearcherIDnumber</ins>]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber)**(_val_):

######The RI Tag

extracts a list of the research IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of the research IDs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="orcID"></a><small>tagProcessing.</small>**[<ins>orcID</ins>]({{ site.baseurl }}{{ page.url }}#orcID)**(_val_):

######The OI Tag

extracts a list of orc IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The orc ID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="funding"></a><small>tagProcessing.</small>**[<ins>funding</ins>]({{ site.baseurl }}{{ page.url }}#funding)**(_val_):

######The FU Tag

extracts a list of the groups funding the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of funding groups


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="fundingText"></a><small>tagProcessing.</small>**[<ins>fundingText</ins>]({{ site.baseurl }}{{ page.url }}#fundingText)**(_val_):

######The FX Tag

extracts a string of the funding thanks

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The funding thank-you


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citations"></a><small>tagProcessing.</small>**[<ins>citations</ins>]({{ site.baseurl }}{{ page.url }}#citations)**(_val_):

######The CR Tag

extracts a list of all the citations in the record, the citations are the [metaknowledge.Citation]({{ site.baseurl }}{{ page.url }}#Citation) class.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

` list[metaknowledge.Citation]`

 A list of Citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citedRefsCount"></a><small>tagProcessing.</small>**[<ins>citedRefsCount</ins>]({{ site.baseurl }}{{ page.url }}#citedRefsCount)**(_val_):

######The NR Tag

extracts the number citations, length of CR list

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of CRs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosTimesCited"></a><small>tagProcessing.</small>**[<ins>wosTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#wosTimesCited)**(_val_):

######The TC Tag

extracts the number of times the Record has been cited by records in WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of time the Record has been cited


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="totalTimesCited"></a><small>tagProcessing.</small>**[<ins>totalTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#totalTimesCited)**(_val_):

######The Z9 Tag

extracts the total number of citations of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The total number of citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisher"></a><small>tagProcessing.</small>**[<ins>publisher</ins>]({{ site.baseurl }}{{ page.url }}#publisher)**(_val_):

######The PU Tag

extracts the publisher of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherCity"></a><small>tagProcessing.</small>**[<ins>publisherCity</ins>]({{ site.baseurl }}{{ page.url }}#publisherCity)**(_val_):

######The PI Tag

extracts the city the publisher is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The city of the publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherAddress"></a><small>tagProcessing.</small>**[<ins>publisherAddress</ins>]({{ site.baseurl }}{{ page.url }}#publisherAddress)**(_val_):

######The PA Tag

extracts the publishers address

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjectCategory"></a><small>tagProcessing.</small>**[<ins>subjectCategory</ins>]({{ site.baseurl }}{{ page.url }}#subjectCategory)**(_val_):

######The SC Tag

extracts a list of the subjects associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of the subjects associated with the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISSN"></a><small>tagProcessing.</small>**[<ins>ISSN</ins>]({{ site.baseurl }}{{ page.url }}#ISSN)**(_val_):

######The SN Tag

extracts the ISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The ISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="eISSN"></a><small>tagProcessing.</small>**[<ins>eISSN</ins>]({{ site.baseurl }}{{ page.url }}#eISSN)**(_val_):

######The EI Tag

extracts the EISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The EISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISBN"></a><small>tagProcessing.</small>**[<ins>ISBN</ins>]({{ site.baseurl }}{{ page.url }}#ISBN)**(_val_):

######The BN Tag

extracts a list of ISBNs associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list`

 The ISBNs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="j9"></a><small>tagProcessing.</small>**[<ins>j9</ins>]({{ site.baseurl }}{{ page.url }}#j9)**(_val_):

######The J9 Tag

extracts the J9 (29-Character Source Abbreviation) of the publication

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The 29-Character Source Abbreviation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isoAbbreviation"></a><small>tagProcessing.</small>**[<ins>isoAbbreviation</ins>]({{ site.baseurl }}{{ page.url }}#isoAbbreviation)**(_val_):

######The JI Tag

extracts the iso abbreviation of the journal

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The iso abbreviation of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="month"></a><small>tagProcessing.</small>**[<ins>month</ins>]({{ site.baseurl }}{{ page.url }}#month)**(_val_):

######The PD Tag

extracts the month the record was published in as an int with January as 1, February 2, ...

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 A integer giving the month


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="year"></a><small>tagProcessing.</small>**[<ins>year</ins>]({{ site.baseurl }}{{ page.url }}#year)**(_val_):

######The PY Tag

extracts the year the record was published in as an int

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The year


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="volume"></a><small>tagProcessing.</small>**[<ins>volume</ins>]({{ site.baseurl }}{{ page.url }}#volume)**(_val_):

######The VL Tag

return the volume the record is in as a string, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The volume number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="issue"></a><small>tagProcessing.</small>**[<ins>issue</ins>]({{ site.baseurl }}{{ page.url }}#issue)**(_val_):

######The IS Tag

extracts a string giving the issue or range of issues the Record was in, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The issue number/range


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="partNumber"></a><small>tagProcessing.</small>**[<ins>partNumber</ins>]({{ site.baseurl }}{{ page.url }}#partNumber)**(_val_):

######The PN Tag

return an integer giving the part of the issue the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The part of the issue of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="supplement"></a><small>tagProcessing.</small>**[<ins>supplement</ins>]({{ site.baseurl }}{{ page.url }}#supplement)**(_val_):

######The SU Tag

extracts the supplement number

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The supplement number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialIssue"></a><small>tagProcessing.</small>**[<ins>specialIssue</ins>]({{ site.baseurl }}{{ page.url }}#specialIssue)**(_val_):

######The SI Tag

extracts the special issue value

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The special issue value


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="meetingAbstract"></a><small>tagProcessing.</small>**[<ins>meetingAbstract</ins>]({{ site.baseurl }}{{ page.url }}#meetingAbstract)**(_val_):

######The MA Tag

extracts the ID of the meeting abstract prefixed by 'EPA-'

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The meeting abstract prefixed


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="beginningPage"></a><small>tagProcessing.</small>**[<ins>beginningPage</ins>]({{ site.baseurl }}{{ page.url }}#beginningPage)**(_val_):

######The BP Tag

extracts the first page the record occurs on, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The first page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="endingPage"></a><small>tagProcessing.</small>**[<ins>endingPage</ins>]({{ site.baseurl }}{{ page.url }}#endingPage)**(_val_):

######The EP Tag

return the last page the record occurs on as a string, not aall are intergers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The final page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="articleNumber"></a><small>tagProcessing.</small>**[<ins>articleNumber</ins>]({{ site.baseurl }}{{ page.url }}#articleNumber)**(_val_):

######The AR Tag

extracts a string giving the article number, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The article number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pageCount"></a><small>tagProcessing.</small>**[<ins>pageCount</ins>]({{ site.baseurl }}{{ page.url }}#pageCount)**(_val_):

######The PG Tag

returns an integer giving the number of pages of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The page count


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjects"></a><small>tagProcessing.</small>**[<ins>subjects</ins>]({{ site.baseurl }}{{ page.url }}#subjects)**(_val_):

######The WC Tag

extracts a list of subjects as assigned by WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The subjects list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DOI"></a><small>tagProcessing.</small>**[<ins>DOI</ins>]({{ site.baseurl }}{{ page.url }}#DOI)**(_val_):

######The DI Tag

return the DOI number of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookDOI"></a><small>tagProcessing.</small>**[<ins>bookDOI</ins>]({{ site.baseurl }}{{ page.url }}#bookDOI)**(_val_):

######The D2 Tag

extracts the book DOI of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="documentDeliveryNumber"></a><small>tagProcessing.</small>**[<ins>documentDeliveryNumber</ins>]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber)**(_val_):

######The GA Tag

extracts the document delivery number of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The document delivery number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosString"></a><small>tagProcessing.</small>**[<ins>wosString</ins>]({{ site.baseurl }}{{ page.url }}#wosString)**(_val_):

######The UT Tag

extracts the WOS number of the record as a string preceded by "WOS:"

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The WOS number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubMedID"></a><small>tagProcessing.</small>**[<ins>pubMedID</ins>]({{ site.baseurl }}{{ page.url }}#pubMedID)**(_val_):

######The PM Tag

extracts the pubmed ID of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The pubmed ID



{% include docsFooter.md %}