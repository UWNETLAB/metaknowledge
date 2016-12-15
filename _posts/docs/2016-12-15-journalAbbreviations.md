---
layout: doc
title: journalAbbreviations
categories: docs
excerpt: Handles the abbreviated journal names used by WOS
tags: [module]
weight: 3
---
<a name="journalAbbreviations"></a>

# [journalAbbreviations]({{ site.baseurl }}{{ page.url }}#journalAbbreviations)

This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in WOS Records and for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function [**updatej9DB**()]({{ site.baseurl }}{{ page.url }}#getj9dict) is used to scape and parse the pages, it must be run without error before the other features can be used. _metaknowledge_. If the database is requested by `getj9dict()`, which is what [`Citations`]({{ site.baseurl }}{{ page.url }}#Citation) use, and the database is not found or is corrupted then [`updatej9DB()`]({{ site.baseurl }}{{ page.url }}#updatej9DB) will be run to download the database if this fails an `mkException` will be raised, the download and parsing usually takes less than a second on a good internet connection.

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool `metaknowledge` instead of with a script.




<h3><a name="journalAbbreviations">The <a href="#journalAbbreviations"><u>journalAbbreviations</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#getj9dict"><b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getj9dict"></a><small>journalAbbreviations.</small>**[<ins>getj9dict</ins>]({{ site.baseurl }}{{ page.url }}#getj9dict)**(_dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'_):

Returns the dictionary of journal abbreviations mapping to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

###### Parameters

_dbname_ : `optional [str]`

 The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

_manualDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_returnDict_ : `optional [str]`

 default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addToDB"></a><small>journalAbbreviations.</small>**[<ins>addToDB</ins>]({{ site.baseurl }}{{ page.url }}#addToDB)**(_abbr=None, dbname='manualj9Abbreviations'_):

Adds _abbr_ to the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manualDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

###### Parameters

_abbr_ : `optional [str or dict[str : str]]`

 The journal abbreviation to be added to the database, it can either be a single string in which case that string will be added with its self as the full name, or a dict can be given with the abbreviations as keys and their names as strings, use pipes (`'|'`) to separate multiple names. Note, if the empty string is given as a name the abbreviation will be considered manually __excluded__, i.e. having excludeFromDB() run on it.

_dbname_ : `optional [str]`

 The name of the database file, default is `metaknowledge.journalAbbreviations.manualDBname`.



{% include docsFooter.md %}