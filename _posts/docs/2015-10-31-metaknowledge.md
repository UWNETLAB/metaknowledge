---
layout: doc
title: Base Functions
categories: docs
excerpt: The metaknowledge functions, for filtering reading and writing graphs
tags: [functions]
weight: 1
---
<a name="Base Functions"></a>
The functions provided by metaknowledge are:

<ul class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, sourceType='raw', targetType='raw'</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True</i>)</a></article></li>
<li><article><a href="#read_graph"><b>read_graph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#write_edgeList"><b>write_edgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#write_nodeAttributeFile"><b>write_nodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#drop_edges"><b>drop_edges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#drop_nodesByDegree"><b>drop_nodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True</i>)</a></article></li>
<li><article><a href="#drop_nodesByCount"><b>drop_nodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True</i>)</a></article></li>
<li><article><a href="#write_graph"><b>write_graph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True</i>)</a></article></li>
<li><article><a href="#recordParser"><b>recordParser</b>(<i>paper</i>)</a></article></li>
<li><article><a href="#isiParser"><b>isiParser</b>(<i>isifile</i>)</a></article></li>
<li><article><a href="#tagToFull"><b>tagToFull</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#normalizeToTag"><b>normalizeToTag</b>(<i>val</i>)</a></article></li>
<li><article><a href="#normalizeToName"><b>normalizeToName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isTagOrName"><b>isTagOrName</b>(<i>val</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="filterNonJournals"></a><small></small>**[<ins>filterNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#filterNonJournals)**(_citesLst, invert=False_):

Removes the Citations from _citesLst_ that are not journals.

###### Parameters

_citesLst_ : `list [Citation]`

 A list of citations to be filtered

_invert_ : `optional [bool]`

 Default `False`, if `True` non-journals will be kept istead of journals

###### Returns

`list [Citation]`

 A filtered list of Citations from _citesLst_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionGraph"></a><small></small>**[<ins>diffusionGraph</ins>]({{ site.baseurl }}{{ page.url }}#diffusionGraph)**(_source, target, sourceType='raw', targetType='raw'_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{% post_url /docs/2015-10-31-RecordCollection %}#RecordCollection) and produces a graph of the citations of the `Records` of _source_ by the `Records` of _target_. By default the graph is of `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords.

Each node on the graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

###### Parameters

_source_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `str`

default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

_targetType_ : `str`

default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

###### Returns

`networkx Directed Graph`

A directed graph of the diffusion network


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionCount"></a><small></small>**[<ins>diffusionCount</ins>]({{ site.baseurl }}{{ page.url }}#diffusionCount)**(_source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{% post_url /docs/2015-10-31-RecordCollection %}#RecordCollection) and produces a `dict` counting the citations of the `Records` of _source_ by the `Records` of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

###### Parameters

_source_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `optional [str]`

default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag of the long name of one then the keys will be of that type.

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurence counts as `"Counts"`.

_compareCounts_ : `optional [boo]`

 default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

###### Returns

`dict[:int]`

 A dictionary with the type given by _sourceType_ as keys and integers as values, by default. If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

 If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="read_graph"></a><small></small>**[<ins>read_graph</ins>]({{ site.baseurl }}{{ page.url }}#read_graph)**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by edgeList and if given nodeList. Outputs a networkx graph for the lists.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()]({{ site.baseurl }}{% post_url /docs/2015-10-31-metaknowledge %}#write_graph), if this dow not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried.

The read edge list format assumes the column named _eSource_ (From) is the source node, then the next column _eDest_ (To) givens the destination and all other columns are attributes of the edge, e.g. weight.

The read nodeList format assumes the column called _idKey_ is the ID of the node as used by the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

If the names of the columns do not match those given to **read_graph()** a KeyError exception will be raised.

**Note**: if nodes appear in the edgelist but not the nodeList they will be created with no attributes.

###### Parameters

_edgeList_ : `str`

 a string giving the path to the edge list file

_nodeList_ : `optional [str]`

 a string giving the path to the node list file

_directed_ : `optional [bool]`

 default `False`, if `True` the produced network is directed instead of undirected

_idKey_ : `optional [str]`

 default `"ID"`, the name of the ID column in the node list

_eSource_ : `optional [str]`

 default `"From"`, the name of the source column in the edge list

_eDest_ : `optional [str]`

 default `"To"`, the name of the destination column in the edge list

###### Returns

`networkx Graph`

 the Graph described by the files


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_edgeList"></a><small></small>**[<ins>write_edgeList</ins>]({{ site.baseurl }}{{ page.url }}#write_edgeList)**(_grph, name, extraInfo=True, allSameAttribute=False_):

Writes an edge list of _grph_ at the destination _name_.

The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

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

<a name="write_nodeAttributeFile"></a><small></small>**[<ins>write_nodeAttributeFile</ins>]({{ site.baseurl }}{{ page.url }}#write_nodeAttributeFile)**(_grph, name, allSameAttribute=False_):

Writes a node attribute list of _grph_ with filename _name_

The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the nodes must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_edges"></a><small></small>**[<ins>drop_edges</ins>]({{ site.baseurl }}{{ page.url }}#drop_edges)**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByDegree"></a><small></small>**[<ins>drop_nodesByDegree</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByDegree)**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True_):

Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByCount"></a><small></small>**[<ins>drop_nodesByCount</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByCount)**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


parameterName is key to count field in the node's dictionary, default is count as that is often correct

ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphStats"></a><small></small>**[<ins>graphStats</ins>]({{ site.baseurl }}{{ page.url }}#graphStats)**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

Returns a string or list containing statistics about the graph _G_.

**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

###### Parameters

_G_ : `networkx Graph`

 The graph for the statistics to be determined of

_stats_ : `optional [list or tuple [str]]`

 Default 'nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), a list or tuple containing any number or combination of the strings:

 `"nodes"`, `"edges"`, `"isolates"`, `"loops"`, `"density"` and `"transitivity"``

 At least one occurrence of the corresponding string causes the statistics to be provided in the string output. For the non-string (tuple) output the returned tuple has the same length as the input and each output is at the same index as the string that requested it, e.g.

 `_stats_ = ("edges", "loops", "edges")`

 The return is a tuple with 2 elements the first and last of which are the number of edges and the second is the number of loops

_makeString_ : `optional [bool]`

 Default `True`, if `True` a string is returned if `False` a tuple

###### Returns

`str or tuple [float and int]`

 The type is determined by _makeString_ and the layout by _stats_
 


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_graph"></a><small></small>**[<ins>write_graph</ins>]({{ site.baseurl }}{{ page.url }}#write_graph)**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [read_graph()]({{ site.baseurl }}{% post_url /docs/2015-10-31-metaknowledge %}#read_graph) and to write only one type of lsit use [write_edgeList()]({{ site.baseurl }}{% post_url /docs/2015-10-31-metaknowledge %}#write_edgeList) or [write_nodeAttributeFile()]({{ site.baseurl }}{% post_url /docs/2015-10-31-metaknowledge %}#write_nodeAttributeFile).

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

<a name="recordParser"></a><small></small>**[<ins>recordParser</ins>]({{ site.baseurl }}{{ page.url }}#recordParser)**(_paper_):

Reads the file _paper_ until it reaches 'ER'.

For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

"AF BREVIK, I

    ANICIN, B"

The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

[Record]({{ site.baseurl }}{% post_url /docs/2015-10-31-metaknowledge %}#Record) objects can be created with these dictionaries as the initializer.

###### Parameters

_paper_ : `file stream`

 An open file, with the current line at the beginning of the record.

###### Returns

`dict[str : List[str]]`

 A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isiParser"></a><small></small>**[<ins>isiParser</ins>]({{ site.baseurl }}{{ page.url }}#isiParser)**(_isifile_):

isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
Each it finds is used to initialize a Record then all Record are returned as a list.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagToFull"></a><small></small>**[<ins>tagToFull</ins>]({{ site.baseurl }}{{ page.url }}#tagToFull)**(_tag_):

A wrapper for [`tagToFullDict`]({{ site.baseurl }}{% post_url /docs/2015-10-31-tagProcessing %}#tagProcessing) it maps 2 character tags to thir full names.

###### Parameters

_tag_: `str`

 A two character string giving the tag

###### Returns

`str`

 The full name of _tag_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToTag"></a><small></small>**[<ins>normalizeToTag</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToTag)**(_val_):

Converts tags or full names to tags

###### Parameters

_val_: `str`

 A two character string giving the tag or its full name

###### Returns

`str`

 The short name of _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToName"></a><small></small>**[<ins>normalizeToName</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToName)**(_val_):

Converts tags or full names to full names

###### Parameters

_val_: `str`

 A two character string giving the tag or its full name

###### Returns

`str`

 The full name of _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isTagOrName"></a><small></small>**[<ins>isTagOrName</ins>]({{ site.baseurl }}{{ page.url }}#isTagOrName)**(_val_):

Checks if _val_ is a tag or full name of tag if so returns `True`


###### Parameters

_val_: `str`

 A string possible forming a tag or name

###### Returns

`bool`

 `True` if _val_ is a tag or name, otherwise `False`


<a name="BadCitation"></a><small></small>**[<ins>BadCitation</ins>]({{ site.baseurl }}{{ page.url }}#BadCitation)**():

Exception thrown by Citation


The BadCitation class has the following methods:

<ul class="post-list">

</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="BadISIRecord"></a><small></small>**[<ins>BadISIRecord</ins>]({{ site.baseurl }}{{ page.url }}#BadISIRecord)**():

Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.


The BadISIRecord class has the following methods:

<ul class="post-list">

</ul>

{% include docsFooter.md %}