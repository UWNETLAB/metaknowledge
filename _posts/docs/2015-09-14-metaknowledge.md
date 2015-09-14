---
layout: page
title: metaknowledge
categories: docs
excerpt: The metaknowledge Package
tags: [main]
weight: 1
---
<a name="metaknowledge"></a>
metaknowledge is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

#### Example

To load the data from files and make a network:

    >>> import metaknowledge as mk
    >>> RC = mk.RecordCollection("records/")
    >>> print(RC)
    Collection of 33 records
    >>> G = RC.coCiteNetwork(nodeType = 'journal')
    Done making a co-citation network of files-from-records                 1.1s
    >>> print(len(G.nodes()))
    223
    >>> mk.write_graph(G, "Cocitation-Network-of-Journals")

#### Overview

This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, language, and citations. The records are saved in groups of up-to 500 individual records in a file.

The [metaknowledge.RecordCollection]({{ site.baseurl }}{% post_url /docs/2015-09-14-RecordCollection %}#RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record]({{ site.baseurl }}{% post_url /docs/2015-09-14-Record %}#Record) class that contains the results of the parsing of the record.

The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge makes use of them to extract useful information. The approximate meanings of the tags are listed in the [tagFuncs]({{ site.baseurl }}{% post_url /docs/2015-09-14-tagFuncs %}#tagFuncs) package, there are no full official public listings of their meanings is available. metaknowledge is not attempting to provide the definitive meanings.

As citations are of great importance to sociology their handling is done with the [Citation]({{ site.baseurl }}{% post_url /docs/2015-09-14-Citation %}#Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

Note for those reading the docstring. metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation](http://networkslab.org/metaknowledge/documentation/).




- - -

<a name="drop_edges"></a>**drop_edges**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored


- - -

<a name="drop_nodesByCount"></a>**drop_nodesByCount**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


parameterName is key to count field in the node's dictionary, default is count as that is often correct

ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors


- - -

<a name="drop_nodesByDegree"></a>**drop_nodesByDegree**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True_):

Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True


- - -

<a name="filterNonJournals"></a>**filterNonJournals**(_citesLst, invert=False_):

Removes the Citations from _citesLst_ that are not journals.

##### Parameters

_citesLst_ : `list [Citation]`

 A list of citations to be filtered

_invert_ : `optional [bool]`

 Default `False`, if `True` non-journals will be kept istead of journals

##### Returns

`list [Citation]`

 A filtered list of Citations from _citesLst_


- - -

<a name="graphStats"></a>**graphStats**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

Returns a string or list containing statistics about the graph _G_.

**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

##### Parameters

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

##### Returns

`str or tuple [float and int]`

 The type is determined by _makeString_ and the layout by _stats_
 


- - -

<a name="isiParser"></a>**isiParser**(_isifile_):

isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
Each it finds is used to initialize a Record then all Record are returned as a list.


- - -

<a name="read_graph"></a>**read_graph**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by edgeList and if given nodeList. Outputs a networkx graph for the lists.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()]({{ site.baseurl }}{% post_url /docs/2015-09-14-metaknowledge %}#metaknowledge), if this dow not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried.

The read edge list format assumes the column named _eSource_ (From) is the source node, then the next column _eDest_ (To) givens the destination and all other columns are attributes of the edge, e.g. weight.

The read nodeList format assumes the column called _idKey_ is the ID of the node as used by the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

If the names of the columns do not match those given to **read_graph()** a KeyError exception will be raised.

**Note**: if nodes appear in the edgelist but not the nodeList they will be created with no attributes.

##### Parameters

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

##### Returns

`networkx Graph`

 the Graph described by the files


- - -

<a name="recordParser"></a>**recordParser**(_paper_):

Reads the file _paper_ until it reaches 'ER'.

For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

"AF BREVIK, I

    ANICIN, B"

The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

[Record]({{ site.baseurl }}{% post_url /docs/2015-09-14-metaknowledge %}#metaknowledge) objects can be created with these dictionaries as the initializer.

##### Parameters

_paper_ : `file stream`

 An open file, with the current line at the beginning of the record.

##### Returns

`dict[str : List[str]]`

 A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


- - -

<a name="write_edgeList"></a>**write_edgeList**(_grph, name, extraInfo=True_):

Writes an edge list of _grph_ at the destination _name_.

The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

##### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_edgeInfo_ : `optional [bool]`

 Default `True`, if `True` the attributes of each edge will be written


- - -

<a name="write_graph"></a>**write_graph**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [read_graph()]({{ site.baseurl }}{% post_url /docs/2015-09-14-metaknowledge %}#metaknowledge) and to write only one type of lsit use [write_edgeList()]({{ site.baseurl }}{% post_url /docs/2015-09-14-metaknowledge %}#metaknowledge) or [write_nodeAttributeFile()]({{ site.baseurl }}{% post_url /docs/2015-09-14-metaknowledge %}#metaknowledge).

**Warning**: this function will overwrite files, if they are in the way of the output, to prevent this set _overwrite_ to `False`

**Note**: If any nodes or edges are missing an attribute a `KeyError` will be raised.

##### Parameters

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


- - -

<a name="write_nodeAttributeFile"></a>**write_nodeAttributeFile**(_grph, name_):

Writes a node attribute list of _grph_ with filename _name_

The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

##### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written


<a name="BadCitation"></a>**BadCitation**():

Exception thrown by Citation


- - -

<a name="BadISIRecord"></a>**BadISIRecord**():

Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.




{% include docsFooter.md %}