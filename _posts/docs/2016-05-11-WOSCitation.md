---
layout: doc
title: WOSCitation
categories: docs
excerpt: A Citation that supports the WOS journal abbreviations
tags: [class]
weight: 2
---
<a name="WOSCitation"></a>
<a name="WOSCitation"></a><small></small>**[<ins>WOSCitation</ins>]({{ site.baseurl }}{{ page.url }}#WOSCitation)**(_<a href="#Citation"><u style="border-bottom: .5px dashed gray;">Citation</u></a>_):

<a name="WOSCitation.__init__"></a><small></small>**[<ins>WOSCitation.__init__</ins>]({{ site.baseurl }}{{ page.url }}#WOSCitation.__init__)**(_cite_):

A class to hold citation strings and allow for comparison between them.

The initializer takes in a string representing a WOS citation in the form:

    Author, Year, Journal, Volume, Page, DOI

`Author` is the author's name in the form of first last name first initial sometimes followed by a period.
`Year` is the year of publication.
`Journal` being the 29-Character Source Abbreviation of the journal.
`Volume` is the volume number(s) of the publication preceded by a V
`Page` is the page number the record starts on
`DOI` is the DOI number of the cited record preceeded by the letters `'DOI'`
Combined they look like:

    Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

**Note**: any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpreted as any of these it is put in the `misc` attribute. That is the reason to use this class, it gracefully handles missing information while still allowing for  comparison between WOS citation strings.

##### Customizations

Citation's hashing and equality checking are based on [`ID()`]({{ site.baseurl }}{{ page.url }}#ID) and use the values of `author`, `year` and `journal`.

When converted to a string a Citation will return the original string.

##### Attributes

As noted above, citations are considered to be divided into six distinct fields (`Author`, `Year`, `Journal`, `Volume`, `Page` and `DOI`) with a seventh `misc` for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a `Citation` created from the string: `'Nunez R., 1998, MATH COGNITION'` would have `author`, `year` and `journal` defined. While one from `'Nunez R.'` would have only the attribute `misc`.

If the parsing of a citation string fails the attribute `bad` is set to `True` and the attribute `error` is created to contain said error, which is a [BadCitation]({{ site.baseurl }}{{ page.url }}#BadCitation) object. If no errors occur `bad` is `False`.

The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

##### \_\_Init\_\_

Citations can be created by [Records]({{ site.baseurl }}{{ page.url }}#Record) or by giving the initializer a string containing a WOS style citation.

##### Parameters

_cite_ : `str`

 A str containing a WOS style citation.


<h3>
The WOSCitation class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#FullJournalName"><b>FullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
<li><article><a href="#isJournal"><b>isJournal</b>(<i>dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="FullJournalName"></a><small>WOSCitation.</small>**[<ins>FullJournalName</ins>]({{ site.baseurl }}{{ page.url }}#FullJournalName)**():

Returns the full name of the Citation's journal field. Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

###### Returns

`str`

 The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then `None` is returned


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addToDB"></a><small>WOSCitation.</small>**[<ins>addToDB</ins>]({{ site.baseurl }}{{ page.url }}#addToDB)**(_manualName=None, manaulDB='manualj9Abbreviations', invert=False_):

Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()]({{ site.baseurl }}{{ page.url }}#isJournal) to return `True` for this Citation and all others with its `journal`.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

###### Parameters

_manualName_ : `optional [str]`

 Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

_manaulDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_invert_ : `optional [bool]`

 Default `False`, if `True` the journal will be removed instead of added


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isJournal"></a><small>WOSCitation.</small>**[<ins>isJournal</ins>]({{ site.baseurl }}{{ page.url }}#isJournal)**(_dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False_):

Returns `True` if the `Citation`'s `journal` field is a journal abbreviation from the WOS listing found at [http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html), i.e. checks if the citation is citing a journal.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

**Note**: All parameters are used for getting the data base with  [**getj9dict**()]({{ site.baseurl }}{{ page.url }}#getj9dict).

###### Parameters

_dbname_ : `optional [str]`

 The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

_manaulDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_returnDict_ : `optional [str]`

 default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.

###### Returns

`bool`

 `True` if the `Citation` is for a journal



{% include docsFooter.md %}