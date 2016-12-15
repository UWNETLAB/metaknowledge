---
layout: doc
title: Base Functions
categories: docs
excerpt: The <i>metaknowledge</i> functions, for filtering reading and writing graphs
tags: [functions]
weight: 1
---
<a name="Base Functions"></a>
<h3>The functions provided by <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><a href="#downloadExtras"><b>downloadExtras</b>()</a></article></li>
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, weighted=True, sourceType='raw', targetType='raw', labelEdgesBy=None</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', extraValue=None, pandasFriendly=False, compareCounts=False, numAuthors=True, useAllAuthors=True, extraMapping=None</i>)</a></article></li>
<li><article><a href="#diffusionAddCountsFromSource"><b>diffusionAddCountsFromSource</b>(<i>grph, source, target, nodeType='citations', extraType=None, diffusionLabel='DiffusionCount', extraKeys=None, countsDict=None, extraMapping=None</i>)</a></article></li>
<li><article><a href="#downloadData"><b>downloadData</b>(<i>useUK=False</i>)</a></article></li>
<li><article><a href="#readGraph"><b>readGraph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#writeEdgeList"><b>writeEdgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeNodeAttributeFile"><b>writeNodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeTnetFile"><b>writeTnetFile</b>(<i>grph, name, modeNameString, weighted=False, sourceMode=None, timeString=None, nodeIndexString='tnet-ID', weightString='weight'</i>)</a></article></li>
<li><article><a href="#dropEdges"><b>dropEdges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#dropNodesByDegree"><b>dropNodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True</i>)</a></article></li>
<li><article><a href="#dropNodesByCount"><b>dropNodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#mergeGraphs"><b>mergeGraphs</b>(<i>targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True, sentenceString=False</i>)</a></article></li>
<li><article><a href="#writeGraph"><b>writeGraph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#updatej9DB"><b>updatej9DB</b>(<i>dbname='j9Abbreviations', saveRawHTML=False</i>)</a></article></li>
</ol>
<h3>The Exceptions defined by <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><b>mkException</b>(<i>Exception</i>)</article></li>
<li><article><b>TagError</b>(<i>mkException</i>)</article></li>
<li><article><b>RCValueError</b>(<i>mkException</i>)</article></li>
<li><article><b>BadInputFile</b>(<i>mkException</i>)</article></li>
<li><article><b>BadRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadPubmedRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadPubmedFile</b>(<i>mkException</i>)</article></li>
<li><article><b>BadScopusRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadProQuestRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadProQuestFile</b>(<i>mkException</i>)</article></li>
<li><article><b>CollectionTypeError</b>(<i>mkException, TypeError</i>)</article></li>
<li><article><b>RecordsNotCompatible</b>(<i>mkException</i>)</article></li>
<li><article><b>cacheError</b>(<i>mkException</i>)</article></li>
<li><article><b>BadWOSRecord</b>(<i>BadRecord</i>)</article></li>
<li><article><b>BadWOSFile</b>(<i>Warning</i>)</article></li>
<li><article><b>RCTypeError</b>(<i>mkException, TypeError</i>)</article></li>
<li><article><b>BadCitation</b>(<i>Warning</i>)</article></li>
<li><article><b>BadGrant</b>(<i>mkException</i>)</article></li>
<li><article><b>GrantCollectionException</b>(<i>mkException</i>)</article></li>
<li><article><b>UnknownFile</b>(<i>mkException</i>)</article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="downloadExtras"></a><small></small>**[<ins>downloadExtras</ins>]({{ site.baseurl }}{{ page.url }}#downloadExtras)**():

Downloads all the external files used by metaknowledge. This will overwrite exiting files
    


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="filterNonJournals"></a><small></small>**[<ins>filterNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#filterNonJournals)**(_citesLst, invert=False_):

Removes the `Citations` from _citesLst_ that are not journals

###### Parameters

_citesLst_ : `list [Citation]`

 A list of citations to be filtered

_invert_ : `optional [bool]`

 Default `False`, if `True` non-journals will be kept instead of journals

###### Returns

`list [Citation]`

 A filtered list of Citations from _citesLst_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionGraph"></a><small></small>**[<ins>diffusionGraph</ins>]({{ site.baseurl }}{{ page.url }}#diffusionGraph)**(_source, target, weighted=True, sourceType='raw', targetType='raw', labelEdgesBy=None_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a graph of the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) in _target_. By default the nodes in the are `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords. The edges of the graph go from the target to the source.

Each node on the output graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_weighted_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute `'weight'` giving the number of times the source has referenced the target.

_sourceType_ : `optional [str]`

 Default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes.

 If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

_targetType_ : `optional [str]`

 Default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes.

 If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

_labelEdgesBy_ : `optional [str]`

 Default `None`, if a WOS tag (or long name of WOS tag) then the edges of the output graph will have a attribute `'key'` that is the value of the referenced tag, of source `Record`, i.e. if `'PY'` is given then each edge will have a `'key'` value equal to the publication year of the source.

 This option will cause the output graph to be an `MultiDiGraph` and is likely to result in parallel edges. If a `Record` has multiple values for at tag (e.g. `'AF'`) the each tag will create its own edge.

###### Returns

`networkx Directed Graph or networkx multi Directed Graph`

 A directed graph of the diffusion network, _labelEdgesBy_ is used the graph will allow parallel edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionCount"></a><small></small>**[<ins>diffusionCount</ins>]({{ site.baseurl }}{{ page.url }}#diffusionCount)**(_source, target, sourceType='raw', extraValue=None, pandasFriendly=False, compareCounts=False, numAuthors=True, useAllAuthors=True, extraMapping=None_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a `dict` counting the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `optional [str]`

 default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag the keys will be of that type.

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurrence counts as `"Counts"`. The lists are the same length.

_compareCounts_ : `optional [bool]`

 default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

_extraValue_ : `optional [str]`

 default `None`, if a tag the returned dictionary will have `Records` mapped to maps, these maps will map the entries for the tag to counts. If _pandasFriendly_ is also `True` the resultant dictionary will have an additional column called `'year'`. This column will contain the year the citations occurred, in addition the Records entries will be duplicated for each year they occur in.

 For example if `'year'` was given then the count for a single `Record` could be `{1990 : 1, 2000 : 5}`

_useAllAuthors_ : `optional [bool]`

 default `True`, if `False` only the first author will be used to generate the `Citations` for the _source_ `Records`

###### Returns

`dict[:int]`

 A dictionary with the type given by _sourceType_ as keys and integers as values.

 If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

 If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labeled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionAddCountsFromSource"></a><small></small>**[<ins>diffusionAddCountsFromSource</ins>]({{ site.baseurl }}{{ page.url }}#diffusionAddCountsFromSource)**(_grph, source, target, nodeType='citations', extraType=None, diffusionLabel='DiffusionCount', extraKeys=None, countsDict=None, extraMapping=None_):

Does a diffusion using [`diffusionCount()`]({{ site.baseurl }}{{ page.url }}#diffusionCount) and updates _grph_ with it, using the nodes in the graph as keys in the diffusion, i.e. the source. The name of the attribute the counts are added to is given by _diffusionLabel_. If the graph is not composed of citations from the source and instead is another tag _nodeType_ needs to be given the tag string.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be updated

_source_ : `RecordCollection`

 The `RecordCollection` that created _grph_

_target_ : `RecordCollection`

 The `RecordCollection` that will be counted

_nodeType_ : `optional [str]`

 default `'citations'`, the tag that constants the values used to create _grph_

###### Returns

`dict[:int]`

 The counts dictioanry used to add values to _grph_. *Note* _grph_ is modified by the function and the return is done in case you need it.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="downloadData"></a><small></small>**[<ins>downloadData</ins>]({{ site.baseurl }}{{ page.url }}#downloadData)**(_useUK=False_):

# Needs to be written

<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="readGraph"></a><small></small>**[<ins>readGraph</ins>]({{ site.baseurl }}{{ page.url }}#readGraph)**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by _edgeList_ and _nodeList_ and creates a networkx graph for the files.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [writeGraph()]({{ site.baseurl }}{{ page.url }}#writeGraph), if this does not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried as it is aimed at a more general usage.

The read edge list format assumes the column named _eSource_ (default `'From'`) is the source node, then the column _eDest_ (default `'To'`) givens the destination and all other columns are attributes of the edges, e.g. weight.

The read node list format assumes the column _idKey_ (default `'ID'`) is the ID of the node for the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

**Note**: If the names of the columns do not match those given to **readGraph()** a `KeyError` exception will be raised.

**Note**: If nodes appear in the edgelist but not the nodeList they will be created silently with no attributes.

###### Parameters

_edgeList_ : `str`

 a string giving the path to the edge list file

_nodeList_ : `optional [str]`

 default `None`, a string giving the path to the node list file

_directed_ : `optional [bool]`

 default `False`, if `True` the produced network is directed from _eSource_ to _eDest_

_idKey_ : `optional [str]`

 default `'ID'`, the name of the ID column in the node list

_eSource_ : `optional [str]`

 default `'From'`, the name of the source column in the edge list

_eDest_ : `optional [str]`

 default `'To'`, the name of the destination column in the edge list

###### Returns

`networkx Graph`

 the graph described by the input files


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeEdgeList"></a><small></small>**[<ins>writeEdgeList</ins>]({{ site.baseurl }}{{ page.url }}#writeEdgeList)**(_grph, name, extraInfo=True, allSameAttribute=False_):

Writes an edge list of _grph_ at the destination _name_.

The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

**Note**: If any edges are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_edgeInfo_ : `optional [bool]`

 Default `True`, if `True` the attributes of each edge will be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the edges must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeNodeAttributeFile"></a><small></small>**[<ins>writeNodeAttributeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeNodeAttributeFile)**(_grph, name, allSameAttribute=False_):

Writes a node attribute list of _grph_ to the file given by the path _name_.

The node list has one column call `'ID'` with the node ids used by networkx and all other columns are the node attributes.

**Note**: If any nodes are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the nodes must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeTnetFile"></a><small></small>**[<ins>writeTnetFile</ins>]({{ site.baseurl }}{{ page.url }}#writeTnetFile)**(_grph, name, modeNameString, weighted=False, sourceMode=None, timeString=None, nodeIndexString='tnet-ID', weightString='weight'_):

Writes an edge list designed for reading by the _R_ package [_tnet_](https://toreopsahl.com/tnet/).

The _networkx_ graph provided must be a pure two-mode network, the modes must be 2 different values for the node attribute accessed by _modeNameString_ and all edges must be between different node types. Each node will be given an integer id, stored in the attribute given by _nodeIndexString_, these ids are then written to the file as the endpoints of the edges. Unless _sourceMode_ is given which mode is the source (first column) and which the target (second column) is random.

**Note** the _grph_ will be modified by this function, the ids of the nodes will be written to the graph at the attribute _nodeIndexString_.

###### Parameters

_grph_ : `network Graph`

 The graph that will be written to _name_

_name_ : `str`

 The path of the file to write

_modeNameString_ : `str`

 The name of the attribute _grph_'s modes are stored in

_weighted_ : `optional bool`

 Default `False`, if `True` then the attribute _weightString_ will be written to the weight column

_sourceMode_ : `optional str`

 Default `None`, if given the name of the mode used for the source (first column) in the output file

_timeString_ : `optional str`

 Default `None`, if present the attribute _timeString_ of an edge will be written to the time column surrounded by double quotes (").

**Note** The format used by tnet for dates is very strict it uses the ISO format, down to the second and without time zones.

_nodeIndexString_ : `optional str`

 Default `'tnet-ID'`, the name of the attribute to save the id for each node

_weightString_ : `optional str`

 Default `'weight'`, the name of the weight attribute


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropEdges"></a><small></small>**[<ins>dropEdges</ins>]({{ site.baseurl }}{{ page.url }}#dropEdges)**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Modifies _grph_ by dropping edges whose weight is not within the inclusive bounds of _minWeight_ and _maxWeight_, i.e after running _grph_ will only have edges whose weights meet the following inequality: _minWeight_ <= edge's weight <= _maxWeight_. A `Keyerror` will be raised if the graph is unweighted unless _ignoreUnweighted_ is `True`, the weight is determined by examining the attribute _parameterName_.

**Note**: none of the default options will result in _grph_ being modified so only specify the relevant ones, e.g. `dropEdges(G, dropSelfLoops = True)` will remove only the self loops from `G`.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minWeight_ : `optional [int or double]`

 default `-inf`, the minimum weight for an edge to be kept in the graph.

_maxWeight_ : `optional [int or double]`

 default `inf`, the maximum weight for an edge to be kept in the graph.

_parameterName_ : `optional [str]`

 default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct

_ignoreUnweighted_ : `optional [bool]`

 default `False`, if `True` unweighted edges will kept

_dropSelfLoops_ : `optional [bool]`

 default `False`, if `True` self loops will be removed regardless of their weight


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNodesByDegree"></a><small></small>**[<ins>dropNodesByDegree</ins>]({{ site.baseurl }}{{ page.url }}#dropNodesByDegree)**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True_):

Modifies _grph_ by dropping nodes that do not have a degree that is within inclusive bounds of _minDegree_ and _maxDegree_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minDegree_ <= node's degree <= _maxDegree_.

Degree is determined in two ways, the default _useWeight_ is the weight attribute of the edges to a node will be summed, the attribute's name is _parameterName_ otherwise the number of edges touching the node is used. If _includeUnweighted_ is `True` then _useWeight_ will assign a degree of 1 to unweighted edges.


###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minDegree_ : `optional [int or double]`

 default `-inf`, the minimum degree for an node to be kept in the graph.

_maxDegree_ : `optional [int or double]`

 default `inf`, the maximum degree for an node to be kept in the graph.

_useWeight_ : `optional [bool]`

 default `True`, if `True` the the edge weights will be summed to get the degree, if `False` the number of edges will be used to determine the degree.

_parameterName_ : `optional [str]`

 default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct.

_includeUnweighted_ : `optional [bool]`

 default `True`, if `True` edges with no weight will be considered to have a weight of 1, if `False` they will cause a `KeyError` to be raised.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNodesByCount"></a><small></small>**[<ins>dropNodesByCount</ins>]({{ site.baseurl }}{{ page.url }}#dropNodesByCount)**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

Modifies _grph_ by dropping nodes that do not have a count that is within inclusive bounds of _minCount_ and _maxCount_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minCount_ <= node's degree <= _maxCount_.

Count is determined by the count attribute, _parameterName_, and if missing will result in a `KeyError` being raised. _ignoreMissing_ can be set to `True` to suppress the error.

minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input

###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minCount_ : `optional [int or double]`

 default `-inf`, the minimum Count for an node to be kept in the graph.

_maxCount_ : `optional [int or double]`

 default `inf`, the maximum Count for an node to be kept in the graph.

_parameterName_ : `optional [str]`

 default `'count'`, key to count field in the nodes's attribute dictionary, the default is the same thoughout metaknowledge so is likely to be correct.

_ignoreMissing_ : `optional [bool]`

 default `False`, if `True` nodes missing a count will be kept in the graph instead of raising an exception


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="mergeGraphs"></a><small></small>**[<ins>mergeGraphs</ins>]({{ site.baseurl }}{{ page.url }}#mergeGraphs)**(_targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'_):

A quick way of merging graphs, this is meant to be quick and is only intended for graphs generated by metaknowledge. This does not check anything and as such may cause unexpected results if the source and target were not generated by the same method.

**mergeGraphs**() will **modify** _targetGraph_ in place by adding the nodes and edges found in the second, _addedGraph_. If a node or edge exists _targetGraph_ is given precedence, but the edge and node attributes given by _incrementedNodeVal_ and incrementedEdgeVal are added instead of being overwritten.

###### Parameters

_targetGraph_ : `networkx Graph`

 the graph to be modified, it has precedence.

_addedGraph_ : `networkx Graph`

 the graph that is unmodified, it is added and does **not** have precedence.

_incrementedNodeVal_ : `optional [str]`

 default `'count'`, the name of the count attribute for the graph's nodes. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.

_incrementedEdgeVal_ : `optional [str]`

 default `'weight'`, the name of the weight attribute for the graph's edges. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphStats"></a><small></small>**[<ins>graphStats</ins>]({{ site.baseurl }}{{ page.url }}#graphStats)**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True, sentenceString=False_):

Returns a string or list containing statistics about the graph _G_.

**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving each stat on a different line it can also produce a sentence containing all the requested statistics or the raw values can be accessed instead by setting _makeString_ to `False`.

###### Parameters

_G_ : `networkx Graph`

 The graph for the statistics to be determined of

_stats_ : `optional [list or tuple [str]]`

 Default `('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity')`, a list or tuple containing any number or combination of the strings:

 `"nodes"`, `"edges"`, `"isolates"`, `"loops"`, `"density"` and `"transitivity"``

 At least one occurrence of the corresponding string causes the statistics to be provided in the string output. For the non-string (tuple) output the returned tuple has the same length as the input and each output is at the same index as the string that requested it, e.g.

 `_stats_ = ("edges", "loops", "edges")`

 The return is a tuple with 2 elements the first and last of which are the number of edges and the second is the number of loops

_makeString_ : `optional [bool]`

 Default `True`, if `True` a string is returned if `False` a tuple

_sentenceString_ : `optional [bool]`

Default `False` : if `True` the returned string is a sentce, otherwise each value has a seperate line.

###### Returns

`str or tuple [float and int]`

 The type is determined by _makeString_ and the layout by _stats_
 


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeGraph"></a><small></small>**[<ins>writeGraph</ins>]({{ site.baseurl }}{{ page.url }}#writeGraph)**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True, allSameAttribute=False_):

Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [readGraph()]({{ site.baseurl }}{{ page.url }}#readGraph) and to write only one type of lsit use [writeEdgeList()]({{ site.baseurl }}{{ page.url }}#writeEdgeList) or [writeNodeAttributeFile()]({{ site.baseurl }}{{ page.url }}#writeNodeAttributeFile).

**Warning**: this function will overwrite files, if they are in the way of the output, to prevent this set _overwrite_ to `False`

**Note**: If any nodes or edges are missing an attribute a `KeyError` will be raised.

###### Parameters

_grph_ : `networkx Graph`

 A networkx graph of the network to be written.

_name_ : `str`

 The start of the file name to be written, can include a path.

_edgeInfo_ : `optional [bool]`

 Default `True`, if `True` the the attributes of each edge are written to the edge list.

_typing_ : `optional [bool]`

 Default `False`, if `True` the directed ness of the graph will be added to the file names.

_suffix_ : `optional [str]`

 Default `"csv"`, the suffix of the file.

_overwrite_ : `optional [bool]`

 Default `True`, if `True` files will be overwritten silently, otherwise an `OSError` exception will be raised.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="updatej9DB"></a><small></small>**[<ins>updatej9DB</ins>]({{ site.baseurl }}{{ page.url }}#updatej9DB)**(_dbname='j9Abbreviations', saveRawHTML=False_):

Updates the database of Journal Title Abbreviations. Requires an internet connection. The data base is saved relative to the source file not the working directory.

###### Parameters

_dbname_ : `optional [str]`

 The name of the database file, default is "j9Abbreviations.db"

_saveRawHTML_ : `optional [bool]`

 Determines if the original HTML of the pages is stored, default `False`. If `True` they are saved in a directory inside j9Raws begining with todays date.



{% include docsFooter.md %}