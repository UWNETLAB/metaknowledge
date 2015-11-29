---
layout: doc
title: RecordCollection
categories: docs
excerpt: Where all the stuff happens, look here if you want to make things
tags: [class]
weight: 2
---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a><small></small>**[<ins>RecordCollection</ins>]({{ site.baseurl }}{{ page.url }}#RecordCollection)**(_inCollection=None, name='', extension=''_):

A way of containing a large number of Record objects, it provides ways of creating them from an isi file, string, list of records or directory containing isi files. The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur.
The comparison operators <, <=, >, >= are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

When being created if there are issues the Record collection will be declared bad (self.bad = True) it will then mostly return nothing or False. The error attribute contains the exception that occurred.

They also possess a name accessed with repr(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred, read __repr__'s doc string for more information

inCollection is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

name sets the name of the of the record if left blank name will be generated based on the object that created the Recordcollection

extension controls the extension that __init__ looks for when reading a directory, set it to the extension on the isi files you wish to load, if left blank all files will be tried and any that are not isi files will be silently skipped

##### \_\_Init\_\_

RecordCollections are made from either a single file or directory supplied as _inCollection_.

##### Parameters

_inCollection_ : `optional [str] or None`

 the name of the source of WOS records. It can be skipped to produce an empty collection.

 If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

 If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

_name_ : `optional [str]`

 The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

_extension_ : `optional [str]`

 The extension to search for when reading a directoy for files. _extension_ is the suffix searched for when a direcorty is read for files, by default it is empty so all files are read.


The RecordCollection class has the following methods:

<ul class="post-list">
<li><article><a href="#nModeNetwork"><b>nModeNetwork</b>(<i>tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#localCiteStats"><b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
<li><article><a href="#pop"><b>pop</b>()</a></article></li>
<li><article><a href="#peak"><b>peak</b>()</a></article></li>
<li><article><a href="#dropWOS"><b>dropWOS</b>(<i>wosNum</i>)</a></article></li>
<li><article><a href="#addRec"><b>addRec</b>(<i>Rec</i>)</a></article></li>
<li><article><a href="#getWOS"><b>getWOS</b>(<i>wosNum, drop=False</i>)</a></article></li>
<li><article><a href="#getBadRecords"><b>getBadRecords</b>()</a></article></li>
<li><article><a href="#dropBadRecords"><b>dropBadRecords</b>()</a></article></li>
<li><article><a href="#dropNonJournals"><b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><b>writeCSV</b>(<i>fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#makeDict"><b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><b>coAuthNetwork</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
<li><article><a href="#coCiteNetwork"><b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, coreOnly=False</i>)</a></article></li>
<li><article><a href="#citationNetwork"><b>citationNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, coreOnly=False</i>)</a></article></li>
<li><article><a href="#yearSplit"><b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="nModeNetwork"></a><small>RecordCollection.</small>**[<ins>nModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#nModeNetwork)**(_tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None_):

Creates a network of the objects found by all WOS tags in _tags_.

A **nModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. if `"LA"` were in _tags_ node `"English"` would have the type attribute be `"LA"`.

For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `"CR"` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, note that all IDs are strings. For example:

The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCiteStats"></a><small>RecordCollection.</small>**[<ins>localCiteStats</ins>]({{ site.baseurl }}{{ page.url }}#localCiteStats)**(_pandasFriendly=False, keyType='citation'_):

Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

###### Parameters

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one "Citations" is the citations the other is their occurence counts as "Counts".

_keyType_ : `optional [str]`

 default `'citation'`, the type of key to use for the dictionary, the valid strings are `"citation"`, `"journal"`, `"year"` or `"author"`

###### Returns

`dict[str, int or Citation : int]`

 A dictionary with keys as given by _keyType_ and integers giving their rates of occurrence in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCitesOf"></a><small>RecordCollection.</small>**[<ins>localCitesOf</ins>]({{ site.baseurl }}{{ page.url }}#localCitesOf)**(_rec_):

Takes in a Record, WOS string, citation string or Citation and returns a RecordCollection of all records that cite it.
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citeFilter"></a><small>RecordCollection.</small>**[<ins>citeFilter</ins>]({{ site.baseurl }}{{ page.url }}#citeFilter)**(_keyString='', field='all', reverse=False, caseSensitive=False_):

Filters Records by some string, keyString, in all of their citations.
Returns all Records with at least one citation possessing keyString in the field given by field.

keyString give the string to be searched for if it is is blank then all citations with the specified field will be matched

field give the component of the citation to be looked at, it is one of a few strings. The default is 'all' which will cause the entire original citation to be searched. It can be used to search across fields, e.g. '1970, V2' is a valid keystring
The other options are:
`author`, searches the author field
`year`, searches the year field
`journal`, searches the journal field
`V`, searches the volume field
`P`, searches the page field
misc, searches all the remaining uncategorized information
anonymous, searches for anonymous citations, keyString is not used
bad, searches for bad citations, keyString is not used

reverse being True causes all Records not matching the query to be returned, default is False

caseSensitive if True causes the search across the original to be case sensitive, only the 'all' option can be case sensitive


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pop"></a><small>RecordCollection.</small>**[<ins>pop</ins>]({{ site.baseurl }}{{ page.url }}#pop)**():

Returns a random Record from the recordCollection, the Record is deleted from the collection, use peak for nondestructive access


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="peak"></a><small>RecordCollection.</small>**[<ins>peak</ins>]({{ site.baseurl }}{{ page.url }}#peak)**():

Returns a random Record from the recordCollection, the Record is kept in the collection, use pop for faster destructive access


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropWOS"></a><small>RecordCollection.</small>**[<ins>dropWOS</ins>]({{ site.baseurl }}{{ page.url }}#dropWOS)**(_wosNum_):

Removes the Record with WOS number (ID number) _wosNum_

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the Record to be dropped. _wosNum_ must begin with 'WOS:' or a valueError is raise.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addRec"></a><small>RecordCollection.</small>**[<ins>addRec</ins>]({{ site.baseurl }}{{ page.url }}#addRec)**(_Rec_):

Adds a Record or Records to the RecordCollection.

###### Parameters

_Rec_ : `Record or iterable[Record]`

 A Record or some iterable containg records to add


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getWOS"></a><small>RecordCollection.</small>**[<ins>getWOS</ins>]({{ site.baseurl }}{{ page.url }}#getWOS)**(_wosNum, drop=False_):

Gets the Record from the collection by its WOS number.

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the Record to be extracted. _wosNum_ must begin with 'WOS:' or a valueError is raise.

_drop_ : `optional [bool]`

 Default `False`. If `True` the Record is dropped from the collection after being extract, i.e. if `False` [getWOS()]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#getWOS) acts like [peak()]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#peak), if `True` it acts like [pop()]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#pop)

###### Returns

`metaknowledge.Record`

 The Record whose WOS number is _wosNum_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getBadRecords"></a><small>RecordCollection.</small>**[<ins>getBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#getBadRecords)**():

returns RecordCollection containing all the Record which have their bad flag set to True, i.e. all those removed by dropBadRecords()


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropBadRecords"></a><small>RecordCollection.</small>**[<ins>dropBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#dropBadRecords)**():

Removes all Records with bad attributes == True from the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNonJournals"></a><small>RecordCollection.</small>**[<ins>dropNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#dropNonJournals)**(_ptVal='J', dropBad=True, invert=False_):

Drops the non journal type Records from the collection

###### Parameters

_ptVal_ : `optional [str]`

 The value of the PT tag to be kept, default is 'J' the journal tag

_dropBad_ : `optional [bool]`

 Determines if bad Records will be dropped as well, default `True`

_invert_ : `optional [bool]`

 Set `True` to drop journals (or the PT tag given by _ptVal) instead of keeping them. Note, it still drops bad Records if _dropBad_ is `True`, default `False`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeFile"></a><small>RecordCollection.</small>**[<ins>writeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeFile)**(_fname=None_):

Writes the RecordCollection to a file, the written file is identical to those download from WOS. The order of Records written is random.

fname set the name of the file, if blank the RecordCollection's name's first 200 characters are use with the suffix .isi


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeCSV"></a><small>RecordCollection.</small>**[<ins>writeCSV</ins>]({{ site.baseurl }}{{ page.url }}#writeCSV)**(_fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

Writes all the Records from the collection into a csv file with each row a record and each column a tag

fname is the name of the file to write to, if none is given it uses the Collections name suffixed by .csv

onlyTheseTags lets you specify which tags to use, if not given then all tags in the records are given.
If you want to use all known tags the use onlyTheseTags = metaknowledge.knownTagsList

numAuthors adds the number of auhtors as the column numAuthors

longNames if set to True will convert the tags to their longer names, otherwise the short 2 character ones will be used

firstTags is the column's tags, it is set by default to ['UT', 'PT', 'TI', 'AF', 'CR'] so those will be written first if given by onlyTheseTags.
Note if tags are in firstTags but not in onlyTheseTags, onlyTheseTags will override onlyTheseTags

csvDelimiter is the delimiter used for the cells of the csv file, default is the comma (,)

csvQuote is  the quote character used for the csv, default is the double quote (")

listDelimiter is the delimiter used between values of the same cell if the tag for that record has multiple outputs, default is the pipe (|)


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="makeDict"></a><small>RecordCollection.</small>**[<ins>makeDict</ins>]({{ site.baseurl }}{{ page.url }}#makeDict)**(_onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True_):

Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

When used in pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

###### Parameters

See writeCSV()


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coAuthNetwork"></a><small>RecordCollection.</small>**[<ins>coAuthNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coAuthNetwork)**(_detailedInfo=False, weighted=True, dropNonJournals=False, count=True_):

Creates a coauthorship network for the RecordCollection.

###### Parameters

_detailedInfo_ : `optional [bool or iterable[WOS tag Strings]]`

 default `False`, if `True` all nodes will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedInfo_ is an iterable (that evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attributes.

 For each of the selected tags an attribute will be added to the node using the values of those tags on the first `Record` encountered. **Warning** iterating over `RecordCollection` objects is not deterministic the first `Record` will not always be same between runs. The node will be given attributes with the names of the WOS tags for each of the selected tags. The attributes will contain strings of containing the values (with commas removed), if multiple values are encountered they will be comma separated.

 Note: _detailedInfo_ is not identical to the _detailedCore_ argument of [`Recordcollection.coCiteNetwork()`]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#coCiteNetwork) or [`Recordcollection.citationNetwork()`]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#citationNetwork)

_weighted_ : `optional [bool]`

 default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of co-authorships.

_dropNonJournals_ : `optional [bool]`

 default `False`, wether to drop authors from non-journals

_count_ : `optional [bool]`

 default `True`, causes the number of occurrences of a node to be counted

###### Returns

`Networkx Graph`

 A networkx graph with author names as nodes and collaborations as edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coCiteNetwork"></a><small>RecordCollection.</small>**[<ins>coCiteNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coCiteNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, coreOnly=False_):

Creates a co-citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-11-29-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

 default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#coAuthNetwork)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

###### Returns

`Networkx Graph`

 A networkx graph with hashes as ID and co-citation as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citationNetwork"></a><small>RecordCollection.</small>**[<ins>citationNetwork</ins>]({{ site.baseurl }}{{ page.url }}#citationNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, coreOnly=False_):

Creates a citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-11-29-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

 default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#coAuthNetwork)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

###### Returns

`Networkx DiGraph or Networkx Graph`

 See _directed_ for explanation of returned type

 A networkx digraph with hashes as ID and citations as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="yearSplit"></a><small>RecordCollection.</small>**[<ins>yearSplit</ins>]({{ site.baseurl }}{{ page.url }}#yearSplit)**(_startYear, endYear, dropMissingYears=True_):

Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

###### Parameters

_startYear_ : `int`

 The smallest year to be included in the retuned RecordCollection

_endYear_ : `int`

 The largest year to be included in the retuned RecordCollection

_dropMissingYears_ : `optional [bool]`

 Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

###### Returns

`RecordCollection`

 A RecordCollection of Records from _startYear_ to _endYear_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="oneModeNetwork"></a><small>RecordCollection.</small>**[<ins>oneModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#oneModeNetwork)**(_mode, nodeCount=True, edgeWeight=True, stemmer=None_):

Creates a network of the objects found by one WOS tag _mode_.

A **oneModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tag given by _mode_, e.g. the `"AF"` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `"AF"` a co-authorship network is created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()]({{ site.baseurl }}{% post_url /docs/2015-11-29-RecordCollection %}#coCiteNetwork) it is more accurate and has more options.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, all IDs are strings. For example:

The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="twoModeNetwork"></a><small>RecordCollection.</small>**[<ins>twoModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#twoModeNetwork)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None_):

Creates a network of the objects found by two WOS tags _tag1_ and _tag2_.

A **twoModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `"WC"` and `"LA"` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `"WC"` and language tag `"LA"`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. the node `"English"` would have the type attribute be `"LA"`.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

The _directed_ parameter if `True` will cause the network to be directed with the first tag as the source and the second as the destination.

###### Parameters

_tag1_ : `str`

 A two character WOS tag or one of the full names for a tag, the source of edges on the graph

_tag1_ : `str`

 A two character WOS tag or one of the full names for a tag, the target of edges on the graph

_directed_ : `optional [bool]`

 Default `False`, if `True` the returned network is directed

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmerTag1_ : `optional [func]`

 default `None`, If _stemmerTag1_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node given by _tag1_ in the graph, all IDs are strings. For example:

The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

_stemmerTag2_ : `optional [func]`

 default `None`, see _stemmerTag1_ as it is the same but for _tag2_

###### Returns

`networkx Graph or networkx DiGraph`

 A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.



{% include docsFooter.md %}