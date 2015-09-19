---
layout: page
title: journalAbbreviations
categories: docs
excerpt: The journalAbbreviations Module
tags: [module]
weight: 3
---
<a name="journalAbbreviations"></a>





- - -

<a name="journalAbbreviations.addToDB"></a>journalAbbreviations.**addToDB**(_abbr=None, dbname='manualj9Abbreviations'_):

Adds _abbr_ to the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manaulDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

##### Parameters

_abbr_ : `optional [str or dict[str : str]]`

 The journal abbreviation to be added to the database, it can either be a single string in which case that string will be added with its self as the full name, or a dict can be given with the abbreviations as keys and their names as strings, use pipes ('|') to separate multiple names. Note, if the empty string is given as a name the abbreviation will be considered manually __excluded__, i.e. having excludeFromDB() run on it.

_dbname_ : `optional [str]`

 The name of the database file, default is `metaknowledge.journalAbbreviations.manaulDBname`.


- - -

<a name="journalAbbreviations.excludeFromDB"></a>journalAbbreviations.**excludeFromDB**(_abbr=None, dbname='manualj9Abbreviations'_):

Marks _abbr_ to be excluded the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manaulDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

##### Parameters

_abbr_ : `optional [str or tuple[str] or list[str]`

 The journal abbreviation to be excluded from the database, it can either be a single string in which case that string will be exclude or a list/tuple of strings can be given with the abbreviations.

_dbname_ : `optional [str]`

 The name of the database file, default is `metaknowledge.journalAbbreviations.manaulDBname`.


- - -

<a name="journalAbbreviations.getj9dict"></a>journalAbbreviations.**getj9dict**(_dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'_):

Returns the dictionary of journal abbreviations to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

##### Parameters

_dbname_ : `optional [str]`

 The name of the database file


- - -

<a name="journalAbbreviations.updatej9DB"></a>journalAbbreviations.**updatej9DB**(_dbname='j9Abbreviations', saveRawHTML=False_):

Updates the database of Journal Title Abbreviations. Requires an internet connection. The data base is saved relative to the source file not the working directory.

##### Parameters

_dbname_ : `optional [str]`

 The name of the database file, default is "j9Abbreviations.db"

_saveRawHTML_ : `optional [bool]`

 Determines if the original HTML of the pages is stored, default `False`. If `True` they are saved in a directory inside j9Raws begining with todays date.



{% include docsFooter.md %}