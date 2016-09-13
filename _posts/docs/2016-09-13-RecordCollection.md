---
layout: doc
title: RecordCollection
categories: docs
excerpt: A Collection of Records, this is what does most of the stuff on Records
tags: [class]
weight: 2
---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a><small></small>**[<ins>RecordCollection</ins>]({{ site.baseurl }}{{ page.url }}#RecordCollection)**(_<a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a>_):

<a name="RecordCollection.__init__"></a><small></small>**[<ins>RecordCollection.__init__</ins>]({{ site.baseurl }}{{ page.url }}#RecordCollection.__init__)**(_inCollection=None, name='', extension='', cached=False, quietStart=False_):

A container for a large number of indivual records.

`RecordCollection` provides ways of creating [`Records`]({{ site.baseurl }}{{ page.url }}#Record) from an isi file, string, list of records or directory containing isi files.

When being created if there are issues the Record collection will be declared bad, `bad` wil be set to `False`, it will then mostly return `None` or False. The attribute `error` contains the exception that occurred.

They also possess an attribute `name` also accessed accessed with **__repr__**(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred.

##### Customizations

The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur. The comparison operators `<`, `<=`, `>`, `>=` are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

##### \_\_Init\_\_

_inCollection_ is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

##### Parameters

_inCollection_ : `optional [str] or None`

 the name of the source of WOS records. It can be skipped to produce an empty collection.

 If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

 If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

_name_ : `optional [str]`

 The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

_extension_ : `optional [str]`

 The extension to search for when reading a directory for files. _extension_ is the suffix searched for when a directory is read for files, by default it is empty so all files are read.

_cached_ : `optional [bool]`

 Default `False`, if `True` and the _inCollection_ is a directory (a string giving the path to a directory) then the initialized `RecordCollection` will be saved in the directory as a Python pickle with the suffix `'.mkDirCache'`. Then if the `RecordCollection` is initialized a second time it will be recovered from the file, which is much faster than reprising every file in the directory.

 _metaknowledge_ saves the names of the parsed files as well as their last modification times and will check these when recreating the `RecordCollection`, so modifying existing files or adding new ones will result in the entire directory being reanalyzed and a new cache file being created. The extension given to **__init__**() is taken into account as well and each suffix is given its own cache.

 **Note** The pickle allows for arbitrary python code execution so only use caches that you trust.


<h3>
The RecordCollection class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#networkCoCitation"><b>networkCoCitation</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=True, detailedCoreAttributes=False, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#networkCitation"><b>networkCitation</b>(<i>dropAnon=False, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=True, detailedCoreAttributes=False, coreOnly=False, expandedCore=False, recordToCite=True</i>)</a></article></li>
<li><article><a href="#networkBibCoupling"><b>networkBibCoupling</b>(<i>weighted=True, fullInfo=False</i>)</a></article></li>
<li><article><a href="#yearSplit"><b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#localCiteStats"><b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
<li><article><a href="#dropNonJournals"><b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><b>writeCSV</b>(<i>fname=None, splitByTag=None, onlyTheseTags=None, numAuthors=True, genderCounts=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#writeBib"><b>writeBib</b>(<i>fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True</i>)</a></article></li>
<li><article><a href="#findProbableCopyright"><b>findProbableCopyright</b>()</a></article></li>
<li><article><a href="#forBurst"><b>forBurst</b>(<i>tag, outputFile=None, dropList=None, lower=True, removeNumbers=True, removeNonWords=True, removeWhitespace=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#forNLP"><b>forNLP</b>(<i>outputFile=None, extraColumns=None, dropList=None, lower=True, removeNumbers=True, removeNonWords=True, removeWhitespace=True, extractCopyright=False, stemmer=None</i>)</a></article></li>
<li><article><a href="#makeDict"><b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, raw=False, numAuthors=True, genderCounts=True</i>)</a></article></li>
<li><article><a href="#rpys"><b>rpys</b>(<i>minYear=None, maxYear=None, dropYears=None</i>)</a></article></li>
<li><article><a href="#genderStats"><b>genderStats</b>(<i>asFractions=False</i>)</a></article></li>
<li><article><a href="#getCitations"><b>getCitations</b>(<i>field=None, values=None, pandasFriendly=True, counts=True</i>)</a></article></li>
<li><article><a href="#networkCoAuthor"><b>networkCoAuthor</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCoCitation"></a><small>RecordCollection.</small>**[<ins>networkCoCitation</ins>]({{ site.baseurl }}{{ page.url }}#networkCoCitation)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=True, detailedCoreAttributes=False, coreOnly=False, expandedCore=False_):

Creates a co-citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{{ page.url }}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

_dropAnon_ : `optional [bool]`

 default `True`, if `True` citations labeled anonymous are removed from the network

_nodeInfo_ : `optional [bool]`

 default `True`, if `True` an extra piece of information is stored with each node. The extra inforamtion is detemined by _nodeType_.

_fullInfo_ : `optional [bool]`

 default `False`, if `True` the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

_weighted_ : `optional [bool]`

 default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

_dropNonJournals_ : `optional [bool]`

 default `False`, wether to drop citations of non-journals

_count_ : `optional [bool]`

 default `True`, causes the number of occurrences of a node to be counted

_keyWords_ : `optional [str] or [list[str]]`

 A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

_detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

 default `True`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.networkCoAuthor()`]({{ site.baseurl }}{{ page.url }}#networkCoAuthor)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

_expandedCore_ : `optional [bool]`

 default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

###### Returns

`Networkx Graph`

 A networkx graph with hashes as ID and co-citation as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCitation"></a><small>RecordCollection.</small>**[<ins>networkCitation</ins>]({{ site.baseurl }}{{ page.url }}#networkCitation)**(_dropAnon=False, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=True, detailedCoreAttributes=False, coreOnly=False, expandedCore=False, recordToCite=True_):

Creates a citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{{ page.url }}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

_dropAnon_ : `optional [bool]`

 default `True`, if `True` citations labeled anonymous are removed from the network

_nodeInfo_ : `optional [bool]`

 default `True`, wether an extra piece of information is stored with each node.

_fullInfo_ : `optional [bool]`

 default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

_weighted_ : `optional [bool]`

 default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

_dropNonJournals_ : `optional [bool]`

 default `False`, wether to drop citations of non-journals

_count_ : `optional [bool]`

 default `True`, causes the number of occurrences of a node to be counted

_keyWords_ : `optional [str] or [list[str]]`

 A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

_directed_ : `optional [bool]`

 Determines if the output graph is directed, default `True`

_detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

 default `True`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.networkCoAuthor()`]({{ site.baseurl }}{{ page.url }}#networkCoAuthor)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

_expandedCore_ : `optional [bool]`

 default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

###### Returns

`Networkx DiGraph or Networkx Graph`

 See _directed_ for explanation of returned type

 A networkx digraph with hashes as ID and citations as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkBibCoupling"></a><small>RecordCollection.</small>**[<ins>networkBibCoupling</ins>]({{ site.baseurl }}{{ page.url }}#networkBibCoupling)**(_weighted=True, fullInfo=False_):

Creates a bibliographic coupling network based on citations for the RecordCollection.

###### Parameters

_weighted_ : `optional bool`

 Default `True`, if `True` the weight of the edges will be added to the network

_fullInfo_ : `optional bool`

 Default `False`, if `True` the full citation string will be added to each of the nodes of the network.

###### Returns

`Networkx Graph`

 A graph of the bibliographic coupling


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="yearSplit"></a><small>RecordCollection.</small>**[<ins>yearSplit</ins>]({{ site.baseurl }}{{ page.url }}#yearSplit)**(_startYear, endYear, dropMissingYears=True_):

Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

###### Parameters

_startYear_ : `int`

 The smallest year to be included in the returned RecordCollection

_endYear_ : `int`

 The largest year to be included in the returned RecordCollection

_dropMissingYears_ : `optional [bool]`

 Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

###### Returns

`RecordCollection`

 A RecordCollection of Records from _startYear_ to _endYear_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCiteStats"></a><small>RecordCollection.</small>**[<ins>localCiteStats</ins>]({{ site.baseurl }}{{ page.url }}#localCiteStats)**(_pandasFriendly=False, keyType='citation'_):

Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

###### Parameters

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `'Citations'` is the citations the other is their occurrence counts as `'Counts'`.

_keyType_ : `optional [str]`

 default `'citation'`, the type of key to use for the dictionary, the valid strings are `'citation'`, `'journal'`, `'year'` or `'author'`. IF changed from `'citation'` all citations matching the requested option will be contracted and their counts added together.

###### Returns

`dict[str, int or Citation : int]`

 A dictionary with keys as given by _keyType_ and integers giving their rates of occurrence in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCitesOf"></a><small>RecordCollection.</small>**[<ins>localCitesOf</ins>]({{ site.baseurl }}{{ page.url }}#localCitesOf)**(_rec_):

Takes in a Record, WOS string, citation string or Citation and returns a RecordCollection of all records that cite it.

###### Parameters

_rec_ : `Record, str or Citation`

 The object that is being cited

###### Returns

`RecordCollection`

 A `RecordCollection` containing only those `Records` that cite _rec_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citeFilter"></a><small>RecordCollection.</small>**[<ins>citeFilter</ins>]({{ site.baseurl }}{{ page.url }}#citeFilter)**(_keyString='', field='all', reverse=False, caseSensitive=False_):

Filters `Records` by some string, _keyString_, in their citations and returns all `Records` with at least one citation possessing _keyString_ in the field given by _field_.

###### Parameters

_keyString_ : `optional [str]`

 Default `''`, gives the string to be searched for, if it is is blank then all citations with the specified field will be matched

_field_ : `optional [str]`

 Default `'all'`, gives the component of the citation to be looked at, it can be one of a few strings. The default is `'all'` which will cause the entire original `Citation` to be searched. It can be used to search across fields, e.g. `'1970, V2'` is a valid keystring
The other options are:

+ `'author'`, searches the author field
+ `'year'`, searches the year field
+ `'journal'`, searches the journal field
+ `'V'`, searches the volume field
+ `'P'`, searches the page field
+ `'misc'`, searches all the remaining uncategorized information
+ `'anonymous'`, searches for anonymous `Citations`, _keyString_ is not ignored
+ `'bad'`, searches for bad citations, keyString is not used

_reverse_ : `optional [bool]`

 Default `False`, being set to `True` causes all `Records` not matching the query to be returned

_caseSensitive_ : `optional [bool]`

 Default `False`, if `True` causes the search across the original to be case sensitive, **only** the `'all'` option can be case sensitive


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNonJournals"></a><small>RecordCollection.</small>**[<ins>dropNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#dropNonJournals)**(_ptVal='J', dropBad=True, invert=False_):

Drops the non journal type `Records` from the collection, this is done by checking _ptVal_ against the PT tag

###### Parameters

_ptVal_ : `optional [str]`

 Default `'J'`, The value of the PT tag to be kept, default is `'J'` the journal tag, other tags can be substituted.

_dropBad_ : `optional [bool]`

 Default `True`, if `True` bad `Records` will be dropped as well those that are not journal entries

_invert_ : `optional [bool]`

 Default `False`, Set `True` to drop journals (or the PT tag given by _ptVal_) instead of keeping them. **Note**, it still drops bad Records if _dropBad_ is `True`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeFile"></a><small>RecordCollection.</small>**[<ins>writeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeFile)**(_fname=None_):

Writes the `RecordCollection` to a file, the written file's format is identical to those download from WOS. The order of `Records` written is random.

###### Parameters

_fname_ : `optional [str]`

 Default `None`, if given the output file will written to _fanme_, if `None` the `RecordCollection`'s name's first 200 characters are used with the suffix .isi


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeCSV"></a><small>RecordCollection.</small>**[<ins>writeCSV</ins>]({{ site.baseurl }}{{ page.url }}#writeCSV)**(_fname=None, splitByTag=None, onlyTheseTags=None, numAuthors=True, genderCounts=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

Writes all the `Records` from the collection into a csv file with each row a record and each column a tag.

###### Parameters

_fname_ : `optional [str]`

 Default `None`, the name of the file to write to, if `None` it uses the collections name suffixed by .csv.

_splitByTag_ : `optional [str]`

 Default `None`, if a tag is given the output will be divided into different files according to the value of the tag, with only the records associated with that tag. For example if `'authorsFull'` is given then each file will only have the lines for `Records` that author is named in.

 The file names are the values of the tag followed by a dash then the normale name for the file as given by _fname_, e.g. for the year 2016 the file could be called `'2016-fname.csv'`.

_onlyTheseTags_ : `optional [iterable]`

 Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

 If you want to use all known tags pass [`metaknowledge.knownTagsList`]({{ site.baseurl }}{{ page.url }}#tagProcessing).

_numAuthors_ : `optional [bool]`

 Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.

_longNames_ : `optional [bool]`

 Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

_firstTags_ : `optional [iterable]`

 Default `None`, if `None` the iterable `['UT', 'PT', 'TI', 'AF', 'CR']` is used. The tags given by the iterable are the first ones in the csv in the order given.

 **Note** if tags are in _firstTags_ but not in _onlyTheseTags_, _onlyTheseTags_ will override _firstTags_

_csvDelimiter_ : `optional [str]`

 Default `','`, the delimiter used for the cells of the csv file.

_csvQuote_ : `optional [str]`

 Default `'"'`, the quote character used for the csv.

_listDelimiter_ : `optional [str]`

 Default `'|'`, the delimiter used between values of the same cell if the tag for that record has multiple outputs.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeBib"></a><small>RecordCollection.</small>**[<ins>writeBib</ins>]({{ site.baseurl }}{{ page.url }}#writeBib)**(_fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True_):

Writes a bibTex entry to _fname_ for each `Record` in the collection.

If the Record is of a journal article (PT J) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

**Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier only.

**Note** Record entries that are lists have their values separated with the string `' and '`, as this is the way bibTex understands

###### Parameters

_fname_ : `optional [str]`

 Default `None`, The name of the file to be written. If not given one will be derived from the collection and the file will be written to .

_maxStringLength_ : `optional [int]`

 Default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

_WOSMode_ : `optional [bool]`

 Default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

_restrictedOutput_ : `optional [bool]`

 Default `False`, if `True` the tags output will be limited to: `'AF'`, `'BF'`, `'ED'`, `'TI'`, `'SO'`, `'LA'`, `'NR'`, `'TC'`, `'Z9'`, `'PU'`, `'J9'`, `'PY'`, `'PD'`, `'VL'`, `'IS'`, `'SU'`, `'PG'`, `'DI'`, `'D2'`, and `'UT'`

_niceID_ : `optional [bool]`

 Default `True`, if `True` the IDs used will be derived from the authors, publishing date and title, if `False` it will be the UT tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="findProbableCopyright"></a><small>RecordCollection.</small>**[<ins>findProbableCopyright</ins>]({{ site.baseurl }}{{ page.url }}#findProbableCopyright)**():

Finds the (likely) copyright string from all abstracts in the `RecordCollection`

###### Returns

`list[str]`

 A deduplicated list of all the copyright strings


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="forBurst"></a><small>RecordCollection.</small>**[<ins>forBurst</ins>]({{ site.baseurl }}{{ page.url }}#forBurst)**(_tag, outputFile=None, dropList=None, lower=True, removeNumbers=True, removeNonWords=True, removeWhitespace=True, stemmer=None_):

Creates a pandas friendly dictionary with 2 columns one `'year'` and the other `'word'`. Each row is a word that occurred in the field given by _tag_ in a `Record` and the year of the record. Unfortunately getting the month or day with any type of accuracy has proved to be impossible so year is the only option.

###### Parameters

_tag_ : `str`

 The tag giving the field for the words to be extracted from.

_outputFile_ : `optional str`

 Default `None`, if a path is given a csv file will be created from the returned dictionary and written to that file

_dropList_ : `optional list[str]`

 Default `None`, if a list of strings is given each field will be checked for substrings, before any other processing, in the field, surrounded by spaces, matching those in _dropList_. The strings will only be dropped if they are surrounded on both sides with spaces (`' '`) so if `dropList = ['a']` then `'a cat'` will become `'cat'`.

_lower_ : `optional bool`

 default `True`, if `True` the output will made lower case

_removeNumbers_ : `optional bool`

 default `True`, if `True` all numbers will be removed

_removeNonWords_ : `optional bool`

 default `True`, if `True` all non-number non-number characters will be removed

_removeWhitespace_ : `optional bool`

 default `True`, if `True` all whitespace will be converted to a single space (`' '`)

_stemmer_ : `optional func`

 default `None`, if a function is provided it will be run on each individual word in the field and the output will replace it. For example to use the  `PorterStemmer` in the _nltk_ package you would give `nltk.PorterStemmer().stem`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="forNLP"></a><small>RecordCollection.</small>**[<ins>forNLP</ins>]({{ site.baseurl }}{{ page.url }}#forNLP)**(_outputFile=None, extraColumns=None, dropList=None, lower=True, removeNumbers=True, removeNonWords=True, removeWhitespace=True, extractCopyright=False, stemmer=None_):

Creates a pandas friendly dictionary with each row a `Record` in the `RecordCollection` and the columns fields natural language processing uses (id, title, publication year, keywords and the abstract). The abstract is by default is processed to remove non-word, non-space characters and the case is lowered.

###### Parameters

_outputFile_ : `optional str`

 default `None`, if a file path is given a csv of the returned data will be written

_extraColumns_ : `optional list[str]`

 default `None`, if a list of tags is given each of the tag's values for a `Record` will be added to the output(s)

_dropList_ : `optional list[str]`

 default `None`, if a list of strings is provided they will be dropped from the output's abstracts. The matching is case sensitive and done before any other processing. The strings will only be dropped if they are surrounded on both sides with spaces (`' '`) so if `dropList = ['a']` then `'a cat'` will become `'cat'`.

_lower_ : `optional bool`

 default `True`, if `True` the abstract will made to lower case

_removeNumbers_ : `optional bool`

 default `True`, if `True` all numbers will be removed

_removeNonWords_ : `optional bool`

 default `True`, if `True` all non-number non-number characters will be removed

_removeWhitespace_ : `optional bool`

 default `True`, if `True` all whitespace will be converted to a single space (`' '`)

_extractCopyright_ : `optional bool`

 default `False`, if `True` the copyright statement at the end of the abstract will be removed and added to a new column. Note this is heuristic based and will not work for all papers.

_stemmer_ : `optional func`

 default `None`, if a function is provided it will be run on each individual word in the abstract and the output will replace it. For example to use the  `PorterStemmer` in the _nltk_ package you would give `nltk.PorterStemmer().stem`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="makeDict"></a><small>RecordCollection.</small>**[<ins>makeDict</ins>]({{ site.baseurl }}{{ page.url }}#makeDict)**(_onlyTheseTags=None, longNames=False, raw=False, numAuthors=True, genderCounts=True_):

Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

When used with pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

###### Parameters

_onlyTheseTags_ : `optional [iterable]`

 Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

 If you want to use all known tags pass [`metaknowledge.knownTagsList`]({{ site.baseurl }}{{ page.url }}#tagProcessing).

_longNames_ : `optional [bool]`

 Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

_cleanedVal_ : `optional [bool]`

 Default `True`, if `True` the processed values for each `Record`'s field will be provided, otherwise the raw values are given.

_numAuthors_ : `optional [bool]`

 Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="rpys"></a><small>RecordCollection.</small>**[<ins>rpys</ins>]({{ site.baseurl }}{{ page.url }}#rpys)**(_minYear=None, maxYear=None, dropYears=None_):

This implements _Referenced Publication Years Spectroscopy_ a techinique for finding import years in citation data. The authors of the original papers have a website with more information, found [here](http://www.leydesdorff.net/software/rpys/).

This function computes the spectra of the `RecordCollection` and returns a dictionary mapping strings to lists of `ints`. Each list is ordered and the values of each with the same index form a row and each list a column. The strings are the names of the columns. This is intended to be read directly by pandas `DataFrames`.

The columns returned are:

1. `'year'`, the years of the counted citations, missing years are inserted with a count of 0, unless they are outside the bounds of the highest year or the lowest year and the default value is used. e.g. if the highest year is 2016, 2017 will not be inserted unless _maxYear_ has been set to 2017 or higher
2. `'count'`, the number of times the year was cited
3. `'abs-deviation'`, deviation from the 5-year median. Calculated by taking the absolute deviation of the count from the median of it and the next 2 years and the preceding 2 years
4. `'rank'`, the rank of the year, the highest ranked year being the one most cited, the second highest being the second highest citation count and so on. All years with 0 count are given the rank 0

###### Parameters

_minYear_ : `optional int`

 Default `1000`, The lowest year to be returned, note years outside this bound will be used to calculate the deviation from the 5-year median

_maxYear_ : `optional int`

 Default `2100`, The highest year to be returned, note years outside this bound will be used to calculate the deviation from the 5-year median

_dropYears_ : `optional int or list[int]`

 Default `None`, year or collection of years that will be removed from the returned value, note the dropped years will still be used to calculate the deviation from the 5-year

###### Returns

`dict[str:list]`

 The table of values from the _Referenced Publication Years Spectroscopy_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="genderStats"></a><small>RecordCollection.</small>**[<ins>genderStats</ins>]({{ site.baseurl }}{{ page.url }}#genderStats)**(_asFractions=False_):

Creates a dict (`{'Male' : maleCount, 'Female' : femaleCount, 'Unknown' : unknownCount}`) with the numbers of male, female and unknown names in the collection.

###### Parameters

_asFractions_ : `optional bool`

 Default `False`, if `True` the counts will be divided by the total number of names, giving the fraction of names in each category instead of the raw counts.

###### Returns

`dict[str:int]`

 A dict with three keys `'Male'`, `'Female'` and `'Unknown'` mapping to their respective counts


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getCitations"></a><small>RecordCollection.</small>**[<ins>getCitations</ins>]({{ site.baseurl }}{{ page.url }}#getCitations)**(_field=None, values=None, pandasFriendly=True, counts=True_):

Creates a pandas ready dict with each row a different citation the contained Records and columns containing the original string, year, journal, author's name and the number of times it occured.

There are also options to filter the output citations with _field_ and _values_

###### Parameters

_field_ : `optional str`

 Default `None`, if given all citations missing the named field will be dropped.

_values_ : `optional str or list[str]`

 Default `None`, if _field_ is also given only those citations with one of the strings given in _values_ will be included.

 e.g. to get only citations from 1990 or 1991: `field = year, values = [1991, 1990]`

_pandasFriendly_ : `optional bool`

 Default `True`, if `False` a list of the citations will be returned instead of the more complicated pandas dict

_counts_ : `optional bool`

 Default `True`, if `False` the counts columns will be removed

###### Returns

`dict`

 A pandas ready dict with all the Citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCoAuthor"></a><small>RecordCollection.</small>**[<ins>networkCoAuthor</ins>]({{ site.baseurl }}{{ page.url }}#networkCoAuthor)**(_detailedInfo=False, weighted=True, dropNonJournals=False, count=True_):

Creates a coauthorship network for the RecordCollection.

###### Parameters

_detailedInfo_ : `optional [bool or iterable[WOS tag Strings]]`

 Default `False`, if `True` all nodes will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedInfo_ is an iterable (that evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attributes.

 For each of the selected tags an attribute will be added to the node using the values of those tags on the first `Record` encountered. **Warning** iterating over `RecordCollection` objects is not deterministic the first `Record` will not always be same between runs. The node will be given attributes with the names of the WOS tags for each of the selected tags. The attributes will contain strings of containing the values (with commas removed), if multiple values are encountered they will be comma separated.

 Note: _detailedInfo_ is not identical to the _detailedCore_ argument of [`Recordcollection.networkCoCitation()`]({{ site.baseurl }}{{ page.url }}#networkCoCitation) or [`Recordcollection.networkCitation()`]({{ site.baseurl }}{{ page.url }}#networkCitation)

_weighted_ : `optional [bool]`

 Default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of co-authorships.

_dropNonJournals_ : `optional [bool]`

 Default `False`, wether to drop authors from non-journals

_count_ : `optional [bool]`

 Default `True`, causes the number of occurrences of a node to be counted

###### Returns

`Networkx Graph`

 A networkx graph with author names as nodes and collaborations as edges.



{% include docsFooter.md %}