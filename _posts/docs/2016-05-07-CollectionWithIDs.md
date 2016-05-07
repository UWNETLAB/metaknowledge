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
<li><article><a href="#containsID"><b>containsID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#discardID"><b>discardID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#removeID"><b>removeID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#getID"><b>getID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#badEntries"><b>badEntries</b>()</a></article></li>
<li><article><a href="#dropBadEntries"><b>dropBadEntries</b>()</a></article></li>
<li><article><a href="#tags"><b>tags</b>()</a></article></li>
<li><article><a href="#oneModeNetwork"><b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><b>nModeNetwork</b>(<i>*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None</i>)</a></article></li>
</ol>
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

<a name="oneModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>oneModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#oneModeNetwork)**(_mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None_):

Creates a network of the objects found by one tag _mode_.

A **oneModeNetwork**() looks are each entry in the collection and extracts its values for the tag given by _mode_, e.g. the `'authorsFull'` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `'authorsFull'` a co-authorship network is created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()]({{ site.baseurl }}{{ page.url }}#coCiteNetwork) it is more accurate and has more options.

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

<a name="twoModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>twoModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#twoModeNetwork)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None_):

Creates a network of the objects found by two WOS tags _tag1_ and _tag2_, each node marked by which tag spawned it making the resultant graph bipartite.

A **twoModeNetwork()** looks at each Record in the `RecordCollection` and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `'WC'` and `'LA'` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `'WC'` and language tag `'LA'`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. the node `'English'` would have the type attribute be `'LA'`.

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="nModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>nModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#nModeNetwork)**(_*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None_):

Creates a network of the objects found by all tags in _tags_, each node is marked by which tag spawned it making the resultant graph n-partite.

A **nModeNetwork()** looks are each item in the collection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. if `'LA'` were in _tags_ node `'English'` would have the type attribute be `'LA'`.

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



{% include docsFooter.md %}