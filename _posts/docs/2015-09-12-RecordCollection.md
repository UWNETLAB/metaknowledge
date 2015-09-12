---
layout: page
title: RecordCollection
categories: docs
excerpt: The RecordCollection Class
tags: [class]
weight: 2
---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a>**RecordCollection**(_inCollection=None, name='', extension=''_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A way of containing a large number of Record objects, it provides ways of creating them from an isi file, string, list of records or directory containing isi files. The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The comparison operators <, <=, >, >= are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When being created if there are issues the Record collection will be declared bad (self.bad = True) it will then mostly return nothing or False. The error attribute contains the exception that occurred.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;They also possess a name accessed with repr(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred, read __repr__'s doc string for more information

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inCollection is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name sets the name of the of the record if left blank name will be generated based on the object that created the Recordcollection

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extension controls the extension that __init__ looks for when reading a directory, set it to the extension on the isi files you wish to load, if left blank all files will be tried and any that are not isi files will be silently skipped

#####&nbsp;&nbsp;&nbsp; \_\_Init\_\_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RecordCollections are made from either a single file or directory supplied as _inCollection_.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_inCollection_ : `optional [str] or None`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the name of the source of WOS records. It can be skipped to produce an empty collection.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_name_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_extension_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The extension to search for when reading a directoy for files. _extension_ is the suffix searched for when a direcorty is read for files, by default it is empty so all files are read.


<a name="RecordCollection.citationNetwork"></a>RecordCollection.**citationNetwork**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a citation network for the RecordCollection.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeType_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-09-12-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_dropAnon_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, if `True` citations labeled anonymous are removed from the network

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, wether an extra piece of information is stored with each node.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_fullInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_weighted_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_dropNonJournals_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `False`, wether to drop citations of non-journals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_count_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, causes the number of occurrences of a node to be counted

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_keyWords_ : `optional [str] or [list[str]]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_directed_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Determines if the output graph is directed, default `True`

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Networkx DiGraph or Networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; See _directed_ for explanation of returned type

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx digraph with hashes as ID and citations as edges


<a name="RecordCollection.citeFilter"></a>RecordCollection.**citeFilter**(_keyString='', field='all', reverse=False, caseSensitive=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Filters Records by some string, keyString, in all of their citations.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns all Records with at least one citation possessing keyString in the field given by field.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyString give the string to be searched for if it is is blank then all citations with the specified field will be matched

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field give the component of the citation to be looked at, it is one of a few strings. The default is 'all' which will cause the entire original citation to be searched. It can be used to search across fields, e.g. '1970, V2' is a valid keystring
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The other options are:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;author, searches the author field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;year, searches the year field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;journal, searches the journal field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;V, searches the volume field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P, searches the page field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;misc, searches all the remaining uncategorized information
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;anonymous, searches for anonymous citations, keyString is not used
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bad, searches for bad citations, keyString is not used

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reverse being True causes all Records not matching the query to be returned, default is False

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;caseSensitive if True causes the search across the original to be case sensitive, only the 'all' option can be case sensitive


<a name="RecordCollection.coAuthNetwork"></a>RecordCollection.**coAuthNetwork**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a coauthorship network for the RecordCollection.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx graph with author names as nodes and collaborations as edges.


<a name="RecordCollection.coCiteNetwork"></a>RecordCollection.**coCiteNetwork**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a co-citation network for the RecordCollection.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeType_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-09-12-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_dropAnon_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, if `True` citations labeled anonymous are removed from the network

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, wether an extra piece of information is stored with each node.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_fullInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_weighted_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_dropNonJournals_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `False`, wether to drop citations of non-journals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_count_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `True`, causes the number of occurrences of a node to be counted

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_keyWords_ : `optional [str] or [list[str]]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx graph with hashes as ID and co-citation as edges


<a name="RecordCollection.dropBadRecords"></a>RecordCollection.**dropBadRecords**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes all Records with bad attributes == True from the collection


<a name="RecordCollection.dropNonJournals"></a>RecordCollection.**dropNonJournals**(_ptVal='J', dropBad=True, invert=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drops the non journal type Records from the collection

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_ptVal_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The value of the PT tag to be kept, default is 'J' the journal tag

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_dropBad_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Determines if bad Records will be dropped as well, default `True`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_invert_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set `True` to drop journals (or the PT tag given by _ptVal) instead of keeping them. Note, it still drops bad Records if _dropBad_ is `True`, default `False`


<a name="RecordCollection.dropWOS"></a>RecordCollection.**dropWOS**(_wosNum_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes the Record with WOS number (ID number) _wosNum_

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_wosNum_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _wosNum_ is the WOS number of the Record to be dropped. _wosNum_ must begin with 'WOS:' or a valueError is raise.


<a name="RecordCollection.getBadRecords"></a>RecordCollection.**getBadRecords**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;returns RecordCollection containing all the Record which have their bad flag set to True, i.e. all those removed by dropBadRecords()


<a name="RecordCollection.getWOS"></a>RecordCollection.**getWOS**(_wosNum, drop=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gets the Record from the collection by its WOS number.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_wosNum_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _wosNum_ is the WOS number of the Record to be extracted. _wosNum_ must begin with 'WOS:' or a valueError is raise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_drop_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `False`. If `True` the Record is dropped from the collection after being extract, i.e. if `False` [getWOS()]({{ site.baseurl }}{% post_url /docs/2015-09-12-RecordCollection %}#RecordCollection) acts like [peak()]({{ site.baseurl }}{% post_url /docs/2015-09-12-RecordCollection %}#RecordCollection), if `True` it acts like [pop()]({{ site.baseurl }}{% post_url /docs/2015-09-12-RecordCollection %}#RecordCollection)

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`metaknowledge.Record`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Record whose WOS number is _wosNum_


<a name="RecordCollection.localCiteStats"></a>RecordCollection.**localCiteStats**(_pandasFriendly=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a dict with all the citations in the CR field as keys and the number of time s they occur as the values

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pandasFriendly makes the output be a dict with two keys one "Citations" is the citations the other is their occurence counts as "Counts".


<a name="RecordCollection.localCitesOf"></a>RecordCollection.**localCitesOf**(_rec_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Takes in a Record, WOS string, citation string or Citation and returns a list of all records that cite it.
        


<a name="RecordCollection.makeDict"></a>RecordCollection.**makeDict**(_onlyTheseTags=None, longNames=False, cleanedVal=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When used in pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See writeCSV()


<a name="RecordCollection.nModeNetwork"></a>RecordCollection.**nModeNetwork**(_tags, recordType=True, nodeCount=True, edgeWeight=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a network of the objects found by all WOS tags in _tags_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A **nModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. if `"LA"` were in _tags_ node `"English"` would have the type attribute be `"LA"`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `"CR"` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_mode_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A two character WOS tag or one of the full names for a tag

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeCount_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeWeight_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges


<a name="RecordCollection.oneModeNetwork"></a>RecordCollection.**oneModeNetwork**(_mode, nodeCount=True, edgeWeight=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a network of the objects found by one WOS tag _mode_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A **oneModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tag given by _mode_, e.g. the `"AF"` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `"AF"` a co-authorship network is created.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()]({{ site.baseurl }}{% post_url /docs/2015-09-12-RecordCollection %}#RecordCollection) it is more accurate and has more options.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_mode_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A two character WOS tag or one of the full names for a tag

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeCount_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeWeight_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges


<a name="RecordCollection.peak"></a>RecordCollection.**peak**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a random Record from the recordCollection, the Record is kept in the collection, use pop for faster destructive access


<a name="RecordCollection.pop"></a>RecordCollection.**pop**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a random Record from the recordCollection, the Record is deleted from the collection, use peak for nondestructive access


<a name="RecordCollection.twoModeNetwork"></a>RecordCollection.**twoModeNetwork**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a network of the objects found by two WOS tags _tag1_ and _tag2_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A **twoModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `"WC"` and `"LA"` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `"WC"` and language tag `"LA"`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. the node `"English"` would have the type attribute be `"LA"`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The _directed_ parameter if `True` will cause the network to be directed with the first tag as the source and the second as the destination.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_mode_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A two character WOS tag or one of the full names for a tag

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_directed_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `False`, if `True` the returned network is directed

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeCount_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeWeight_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`networkx Graph or networkx DiGraph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.


<a name="RecordCollection.writeCSV"></a>RecordCollection.**writeCSV**(_fname=None, onlyTheseTags=None, longNames=False, firstTags=['UT', 'PT', 'TI', 'AF', 'CR'], csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes all the Records from the collection into a csv file with each row a record and each column a tag

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fname is the name of the file to write to, if none is given it uses the Collections name suffixed by .csv

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;onlyTheseTags lets you specify which tags to use, if not given then all tags in the records are given.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you want to use all known tags the use onlyTheseTags = metaknowledge.knownTagsList

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longNames if set to True will convert the tags to their longer names, otherwise the short 2 character ones will be used

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firstTags is the column's tags, it is set by default to ['UT', 'PT', 'TI', 'AF', 'CR'] so those will be written first if given by onlyTheseTags.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note if tags are in firstTags but not in onlyTheseTags, onlyTheseTags will override onlyTheseTags

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;csvDelimiter is the delimiter used for the cells of the csv file, default is the comma (,)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;csvQuote is  the quote character used for the csv, default is the double quote (")

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listDelimiter is the delimiter used between values of the same cell if the tag for that record has multiple outputs, default is the pipe (|)


<a name="RecordCollection.writeFile"></a>RecordCollection.**writeFile**(_fname=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes the RecordCollection to a file, the written file is identical to those download from WOS. The order of Records written is random.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fname set the name of the file, if blank the RecordCollection's name's first 200 characters are use with the suffix .isi


<a name="RecordCollection.yearSplit"></a>RecordCollection.**yearSplit**(_startYear, endYear_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_startYear_ : `int`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The smallest year to be included in the retuned RecordCollection

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_endYear_ : `int`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The largest year to be included in the retuned RecordCollection

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`RecordCollection`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A RecordCollection of Records from _startYear_ to _endYear_




{% include docsFooter.md %}