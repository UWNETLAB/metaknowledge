---
layout: doc
title: CollectionWithIDs
categories: docs
excerpt: A Collection that only holds <i>metaknowledge</i> objects
tags: [class]
weight: 2
---
<a name="CollectionWithIDs"></a>
<a name="CollectionWithIDs"></a><small></small>**[<ins>CollectionWithIDs</ins>]({{ site.baseurl }}{{ page.url }}#CollectionWithIDs)**(_<a href="#Collection"><u style="border-bottom: .5px dashed gray;">Collection</u></a>_):

<a name="CollectionWithIDs.__init__"></a><small></small>**[<ins>CollectionWithIDs.__init__</ins>]({{ site.baseurl }}{{ page.url }}#CollectionWithIDs.__init__)**(_inSet, allowedTypes, collectedTypes, name, bad, errors, quietStart=False_):

A [`Collection`]({{ site.baseurl }}{{ page.url }}#Collection) with a few extra methods that assume all the contained items have an id attribute and a bad attribute, e.g. [`Records`]({{ site.baseurl }}{{ page.url }}#Record) or [`Grants`]({{ site.baseurl }}{{ page.url }}#Grant).

\_\_Init\_\_

As `CollectionWithIDs` is mostly meant to be base for other classes all but one of the arguments in the `__init__` are not optional and the optional one is not used. The `__init__()` function is the same as a [`Collection`]({{ site.baseurl }}{{ page.url }}#Collection).


<h3>
The CollectionWithIDs class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#networkMultiMode"><b>networkMultiMode</b>(<i>*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None</i>)</a></article></li>
<li><article><a href="#containsID"><b>containsID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#discardID"><b>discardID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#removeID"><b>removeID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#getID"><b>getID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#badEntries"><b>badEntries</b>()</a></article></li>
<li><article><a href="#dropBadEntries"><b>dropBadEntries</b>()</a></article></li>
<li><article><a href="#tags"><b>tags</b>()</a></article></li>
<li><article><a href="#glimpse"><b>glimpse</b>(<i>*tags, compact=False</i>)</a></article></li>
<li><article><a href="#rankedSeries"><b>rankedSeries</b>(<i>tag, outputFile=None, giveCounts=True, giveRanks=False, greatestFirst=True, pandasMode=True, limitTo=None</i>)</a></article></li>
<li><article><a href="#timeSeries"><b>timeSeries</b>(<i>tag=None, outputFile=None, giveYears=True, greatestFirst=True, limitTo=False, pandasMode=True</i>)</a></article></li>
<li><article><a href="#cooccurrenceCounts"><b>cooccurrenceCounts</b>(<i>keyTag, *countedTags</i>)</a></article></li>
<li><article><a href="#networkMultiLevel"><b>networkMultiLevel</b>(<i>*modes, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None</i>)</a></article></li>
<li><article><a href="#networkOneMode"><b>networkOneMode</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None</i>)</a></article></li>
<li><article><a href="#networkTwoMode"><b>networkTwoMode</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkMultiMode"></a><small>CollectionWithIDs.</small>**[<ins>networkMultiMode</ins>]({{ site.baseurl }}{{ page.url }}#networkMultiMode)**(_*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None_):

Creates a network of the objects found by all tags in _tags_, each node is marked by which tag spawned it making the resultant graph n-partite.

A **networkMultiMode()** looks are each item in the collection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. if `'LA'` were in _tags_ node `'English'` would have the type attribute be `'LA'`.

For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `'CR'` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

###### Parameters

_tags_ : `str`, `str`, `str`, ... or `list [str]`

 Any number of tags, or a list of tags

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called `'count'` that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called `'weight'` that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 Default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, note that all IDs are strings.

 For example: the function `f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="containsID"></a><small>CollectionWithIDs.</small>**[<ins>containsID</ins>]({{ site.baseurl }}{{ page.url }}#containsID)**(_idVal_):

Checks if the collected items contains the give _idVal_

###### Parameters

_idVal_ : `str`

 The queried id string

###### Returns

`bool`

 `True` if the item is in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="discardID"></a><small>CollectionWithIDs.</small>**[<ins>discardID</ins>]({{ site.baseurl }}{{ page.url }}#discardID)**(_idVal_):

Checks if the collected items contains the give _idVal_ and discards it if it is found, will not raise an exception if item is not found

###### Parameters

_idVal_ : `str`

 The discarded id string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="removeID"></a><small>CollectionWithIDs.</small>**[<ins>removeID</ins>]({{ site.baseurl }}{{ page.url }}#removeID)**(_idVal_):

Checks if the collected items contains the give _idVal_ and removes it if it is found, will raise a `KeyError` if item is not found

###### Parameters

_idVal_ : `str`

 The removed id string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getID"></a><small>CollectionWithIDs.</small>**[<ins>getID</ins>]({{ site.baseurl }}{{ page.url }}#getID)**(_idVal_):

Looks up an item with _idVal_ and returns it if it is found, returns `None` if it does not find the item

###### Parameters

_idVal_ : `str`

 The requested item's id string

###### Returns

`object`

 The requested object or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="badEntries"></a><small>CollectionWithIDs.</small>**[<ins>badEntries</ins>]({{ site.baseurl }}{{ page.url }}#badEntries)**():

Creates a new collection of the same type with only the bad entries

###### Returns

`CollectionWithIDs`

 A collection of only the bad entries


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropBadEntries"></a><small>CollectionWithIDs.</small>**[<ins>dropBadEntries</ins>]({{ site.baseurl }}{{ page.url }}#dropBadEntries)**():

Removes all the bad entries from the collection
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tags"></a><small>CollectionWithIDs.</small>**[<ins>tags</ins>]({{ site.baseurl }}{{ page.url }}#tags)**():

Creates a list of all the tags of the contained items

###### Returns

`list [str]`

 A list of all the tags


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="glimpse"></a><small>CollectionWithIDs.</small>**[<ins>glimpse</ins>]({{ site.baseurl }}{{ page.url }}#glimpse)**(_*tags, compact=False_):

Creates a printable table with the most frequently occurring values of each of the requested _tags_, or if none are provided the top authors, journals and citations. The table will be as wide and as tall as the terminal (or 80x24 if there is no terminal) so `print(RC.glimpse())`should always create a nice looking table. Below is a table created from some of the testing files:

```
> > print(RC.glimpse())
+RecordCollection glimpse made at: 2016-01-01 12:00:00++++++++++++++++++++++++++
|33 Records from testFile++++++++++++++++++++++++++++++++++++++++++++++++++++++|
|Columns are ranked by num. of occurrences and are independent of one another++|
|-------Top Authors--------+------Top Journals-------+--------Top Cited--------|
|1                Girard, S|1 CANADIAN JOURNAL OF PH.|1 LEVY Y, 1975, OPT COMM.|
|1                Gilles, H|1 JOURNAL OF THE OPTICAL.|2 GOOS F, 1947, ANN PHYS.|
|2                IMBERT, C|2          APPLIED OPTICS|3 LOTSCH HKV, 1970, OPTI.|
|2                Pillon, F|2   OPTICS COMMUNICATIONS|4 RENARD RH, 1964, J OPT.|
|3          BEAUREGARD, OCD|2 NUOVO CIMENTO DELLA SO.|5 IMBERT C, 1972, PHYS R.|
|3               Laroche, M|2 JOURNAL OF THE OPTICAL.|6 ARTMANN K, 1948, ANN P.|
|3                 HUARD, S|2 JOURNAL OF THE OPTICAL.|6 COSTADEB.O, 1973, PHYS.|
|4                  PURI, A|2 NOUVELLE REVUE D OPTIQ.|6 ROOSEN G, 1973, CR ACA.|
|4               COSTADEB.O|3 PHYSICS REPORTS-REVIEW.|7 Imbert C., 1972, Nouve.|
|4           PATTANAYAK, DN|3 PHYSICAL REVIEW LETTERS|8 HOROWITZ BR, 1971, J O.|
|4           Gazibegovic, A|3 USPEKHI FIZICHESKIKH N.|8 BRETENAKER F, 1992, PH.|
|4                ROOSEN, G|3 APPLIED PHYSICS B-LASE.|8 SCHILLIN.H, 1965, ANN .|
|4               BIRMAN, JL|3 AEU-INTERNATIONAL JOUR.|8 FEDOROV FI, 1955, DOKL.|
|4                Kaiser, R|3 COMPTES RENDUS HEBDOMA.|8 MAZET A, 1971, CR ACAD.|
|5                  LEVY, Y|3 CHINESE PHYSICS LETTERS|9 IMBERT C, 1972, CR ACA.|
|5              BEAUREGA.OC|3       PHYSICAL REVIEW B|9 LOTSCH HKV, 1971, OPTI.|
|5               PAVLOV, VI|3 LETTERE AL NUOVO CIMEN.|9 ASHBY N, 1973, PHYS RE.|
|5                BREVIK, I|3 PROGRESS IN QUANTUM EL.|9 BOULWARE DG, 1973, PHY.|
> >
```

###### Parameters

_*tags_ : `str, str, ...`

 Any number of tag strings to be made into columns in the output table

###### Returns

`str`

 A string containing the table


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="rankedSeries"></a><small>CollectionWithIDs.</small>**[<ins>rankedSeries</ins>]({{ site.baseurl }}{{ page.url }}#rankedSeries)**(_tag, outputFile=None, giveCounts=True, giveRanks=False, greatestFirst=True, pandasMode=True, limitTo=None_):

Creates an pandas dict of the ordered list of all the values of _tag_, with and ranked by their number of occurrences. A list can also be returned with the the counts or ranks added or it can be written to a file.

###### Parameters

_tag_ : `str`

 The tag to be ranked

_outputFile_ : `optional str`

 A file path to write a csv with 2 columns, one the tag values the other their counts

_giveCounts_ : `optional bool`

 Default `True`, if `True` the retuned list will be composed of tuples the first values being the tag value and the second their counts. This supersedes _giveRanks_.

_giveRanks_ : `optional bool`

 Default `False`, if `True` and _giveCounts_ is `False`, the retuned list will be composed of tuples the first values being the tag value and the second their ranks. This is superseded by _giveCounts_.

_greatestFirst_ : `optional bool`

 Default `True`, if `True` the returned list will be ordered with the highest ranked value first, otherwise the lowest ranked will be first.

_pandasMode_ : `optional bool`

 Default `True`, if `True` a `dict` ready for pandas will be returned, otherwise a list

_limitTo_ : `optional list[values]`

 Default `None`, if a list is provided only those values in the list will be counted or returned

###### Returns

`dict[str:list[value]] or list[str]`

 A `dict` or `list` will be returned depending on if _pandasMode_ is `True`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="timeSeries"></a><small>CollectionWithIDs.</small>**[<ins>timeSeries</ins>]({{ site.baseurl }}{{ page.url }}#timeSeries)**(_tag=None, outputFile=None, giveYears=True, greatestFirst=True, limitTo=False, pandasMode=True_):

Creates an pandas dict of the ordered list of all the values of _tag_, with and ranked by the year the occurred in, multiple year occurrences will create multiple entries. A list can also be returned with the the counts or years added or it can be written to a file.

If no _tag_ is given the `Records` in the collection will be used

###### Parameters

_tag_ : `optional str`

 Default `None`, if provided the tag will be ordered

_outputFile_ : `optional str`

 A file path to write a csv with 2 columns, one the tag values the other their years

_giveYears_ : `optional bool`

 Default `True`, if `True` the retuned list will be composed of tuples the first values being the tag value and the second their years.

_greatestFirst_ : `optional bool`

 Default `True`, if `True` the returned list will be ordered with the highest years first, otherwise the lowest years will be first.

_pandasMode_ : `optional bool`

 Default `True`, if `True` a `dict` ready for pandas will be returned, otherwise a list

_limitTo_ : `optional list[values]`

 Default `None`, if a list is provided only those values in the list will be counted or returned

###### Returns

`dict[str:list[value]] or list[str]`

 A `dict` or `list` will be returned depending on if _pandasMode_ is `True`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="cooccurrenceCounts"></a><small>CollectionWithIDs.</small>**[<ins>cooccurrenceCounts</ins>]({{ site.baseurl }}{{ page.url }}#cooccurrenceCounts)**(_keyTag, *countedTags_):

Counts the number of times values from any of the _countedTags_ occurs with _keyTag_. The counts are retuned as a dictionary with the values of _keyTag_ mapping to dictionaries with each of the _countedTags_ values mapping to thier counts.

###### Parameters

_keyTag_ : `str`

 The tag used as the key for the returned dictionary

_*countedTags_ : `str, str, str, ...`

 The tags used as the key for the returned dictionary's values

###### Returns

`dict[str:dict[str:int]]`

 The dictionary of counts


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkMultiLevel"></a><small>CollectionWithIDs.</small>**[<ins>networkMultiLevel</ins>]({{ site.baseurl }}{{ page.url }}#networkMultiLevel)**(_*modes, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None_):

Creates a network of the objects found by any number of tags _modes_, with edges between all co-occurring values. IF you only want edges between co-occurring values from different tags use [`networkMultiMode()`]({{ site.baseurl }}{{ page.url }}#networkMultiMode).

A **networkMultiLevel**() looks are each entry in the collection and extracts its values for the tag given by each of the _modes_, e.g. the `'authorsFull'` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `'authorsFull'` a co-authorship network is created. Then for each other tag the entries are also added and edges between the first tag's node and theirs are created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.networkCoCitation()]({{ site.baseurl }}{{ page.url }}#networkCoCitation) it is more accurate and has more options.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 Default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, all IDs are strings. For example:

 The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkOneMode"></a><small>CollectionWithIDs.</small>**[<ins>networkOneMode</ins>]({{ site.baseurl }}{{ page.url }}#networkOneMode)**(_mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None_):

Creates a network of the objects found by one tag _mode_. This is the same as [`networkMultiLevel()`]({{ site.baseurl }}{{ page.url }}#networkMultiLevel) with only one tag.

A **networkOneMode**() looks are each entry in the collection and extracts its values for the tag given by _mode_, e.g. the `'authorsFull'` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `'authorsFull'` a co-authorship network is created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.networkCoCitation()]({{ site.baseurl }}{{ page.url }}#networkCoCitation) it is more accurate and has more options.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 Default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, all IDs are strings. For example:

 The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkTwoMode"></a><small>CollectionWithIDs.</small>**[<ins>networkTwoMode</ins>]({{ site.baseurl }}{{ page.url }}#networkTwoMode)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None_):

Creates a network of the objects found by two WOS tags _tag1_ and _tag2_, each node marked by which tag spawned it making the resultant graph bipartite.

A **networkTwoMode()** looks at each Record in the `RecordCollection` and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `'WC'` and `'LA'` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `'WC'` and language tag `'LA'`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. the node `'English'` would have the type attribute be `'LA'`.

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

 Default `None`, If _stemmerTag1_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node given by _tag1_ in the graph, all IDs are strings.

 For example: the function `f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

_stemmerTag2_ : `optional [func]`

 Default `None`, see _stemmerTag1_ as it is the same but for _tag2_

###### Returns

`networkx Graph or networkx DiGraph`

 A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.



{% include docsFooter.md %}