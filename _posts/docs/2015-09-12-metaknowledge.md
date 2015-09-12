---
layout: page
title: metaknowledge
categories: docs
excerpt: The metaknowledge Package
tags: [main]
weight: 1
---
<a name="metaknowledge"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metaknowledge is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

####&nbsp;&nbsp;&nbsp; Example

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To load the data from files and make a network:

    >>> import metaknowledge as mk
    >>> RC = mk.RecordCollection("records/")
    >>> print(RC)
    Collection of 33 records
    >>> G = RC.coCiteNetwork(nodeType = 'journal')
    Done making a co-citation network of files-from-records                 1.1s
    >>> print(len(G.nodes()))
    223
    >>> mk.write_graph(G, "Cocitation-Network-of-Journals")

####&nbsp;&nbsp;&nbsp; Overview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, language, and citations. The records are saved in groups of up-to 500 individual records in a file.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The [metaknowledge.RecordCollection]({{ site.baseurl }}{% post_url /docs/2015-09-12-RecordCollection %}#RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record]({{ site.baseurl }}{% post_url /docs/2015-09-12-Record %}#Record) class that contains the results of the parsing of the record.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge makes use of them to extract useful information. The approximate meanings of the tags are listed in the [tagFuncs]({{ site.baseurl }}{% post_url /docs/2015-09-12-tagFuncs %}#tagFuncs) package, there are no full official public listings of their meanings is available. metaknowledge is not attempting to provide the definitive meanings.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As citations are of great importance to sociology their handling is done with the [Citation]({{ site.baseurl }}{% post_url /docs/2015-09-12-Citation %}#Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note for those reading the docstring. metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation](http://networkslab.org/metaknowledge/documentation/).




- - -

<a name="drop_edges"></a>**drop_edges**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored


- - -

<a name="drop_nodesByCount"></a>**drop_nodesByCount**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to count field in the node's dictionary, default is count as that is often correct

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors


- - -

<a name="drop_nodesByDegree"></a>**drop_nodesByDegree**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True


- - -

<a name="filterNonJournals"></a>**filterNonJournals**(_citesLst, invert=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes the Citations from _citesLst_ that are not journals.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_citesLst_ : `list [Citation]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A list of citations to be filtered

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_invert_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `False`, if `True` non-journals will be kept istead of journals

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`list [Citation]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A filtered list of Citations from _citesLst_


- - -

<a name="graphStats"></a>**graphStats**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a string or list containing statistics about the graph _G_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_G_ : `networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The graph for the statistics to be determined of

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_stats_ : `optional [list or tuple [str]]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default 'nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), a list or tuple containing any number or combination of the strings:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `"nodes"`, `"edges"`, `"isolates"`, `"loops"`, `"density"` and `"transitivity"``

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; At least one occurrence of the corresponding string causes the statistics to be provided in the string output. For the non-string (tuple) output the returned tuple has the same length as the input and each output is at the same index as the string that requested it, e.g.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `_stats_ = ("edges", "loops", "edges")`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The return is a tuple with 2 elements the first and last of which are the number of edges and the second is the number of loops

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_makeString_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` a string is returned if `False` a tuple

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`str or tuple [float and int]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The type is determined by _makeString_ and the layout by _stats_
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 


- - -

<a name="isiParser"></a>**isiParser**(_isifile_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each it finds is used to initialize a Record then all Record are returned as a list.


- - -

<a name="read_graph"></a>**read_graph**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads the files given by edgeList and if given nodeList. Outputs a networkx graph for the lists.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()]({{ site.baseurl }}{% post_url /docs/2015-09-12-metaknowledge %}#metaknowledge), if this dow not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The read edge list format assumes the column named _eSource_ (From) is the source node, then the next column _eDest_ (To) givens the destination and all other columns are attributes of the edge, e.g. weight.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The read nodeList format assumes the column called _idKey_ is the ID of the node as used by the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the names of the columns do not match those given to **read_graph()** a KeyError exception will be raised.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note**: if nodes appear in the edgelist but not the nodeList they will be created with no attributes.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeList_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a string giving the path to the edge list file

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_nodeList_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a string giving the path to the node list file

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_directed_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `False`, if `True` the produced network is directed instead of undirected

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_idKey_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `"ID"`, the name of the ID column in the node list

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_eSource_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `"From"`, the name of the source column in the edge list

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_eDest_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default `"To"`, the name of the destination column in the edge list

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the Graph described by the files


- - -

<a name="recordParser"></a>**recordParser**(_paper_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads the file _paper_ until it reaches 'ER'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"AF BREVIK, I

    ANICIN, B"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Record]({{ site.baseurl }}{% post_url /docs/2015-09-12-metaknowledge %}#metaknowledge) objects can be created with these dictionaries as the initializer.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_paper_ : `file stream`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; An open file, with the current line at the beginning of the record.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dict[str : List[str]]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


- - -

<a name="write_edgeList"></a>**write_edgeList**(_grph, name, extraInfo=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes an edge list of _grph_ at the destination _name_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note**: If any edges are missing an attribute `KeyError` will be raised.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_grph_ : `networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The graph to be written to _name_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_name_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The name of the file to be written

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` the attributes of each edge will be written


- - -

<a name="write_graph"></a>**write_graph**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To read back these files use [read_graph()]({{ site.baseurl }}{% post_url /docs/2015-09-12-metaknowledge %}#metaknowledge) and to write only one type of lsit use [write_edgeList()]({{ site.baseurl }}{% post_url /docs/2015-09-12-metaknowledge %}#metaknowledge) or [write_nodeAttributeFile()]({{ site.baseurl }}{% post_url /docs/2015-09-12-metaknowledge %}#metaknowledge).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning**: this function will overwrite files, if they are in the way of the output, to prevent this set _overwrite_ to `False`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note**: If any nodes or edges are missing an attribute a `KeyError` will be raised.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_grph_ : `networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A networkx graph of the network to be written.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_name_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The start of the file name to be written, can include a path.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_edgeInfo_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` the the attributes of each edge are written to the edge list.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_typing_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `False`, if `True` the directed ness of the graph will be added to the file names.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_suffix_ : `optional [str]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `"csv"`, the suffix of the file.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_overwrite_ : `optional [bool]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default `True`, if `True` files will be overwritten silently, otherwise an `OSError` exception will be raised.


- - -

<a name="write_nodeAttributeFile"></a>**write_nodeAttributeFile**(_grph, name_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes a node attribute list of _grph_ with filename _name_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note**: If any edges are missing an attribute `KeyError` will be raised.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_grph_ : `networkx Graph`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The graph to be written to _name_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_name_ : `str`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The name of the file to be written


<a name="BadCitation"></a>**BadCitation**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exception thrown by Citation


- - -

<a name="BadISIRecord"></a>**BadISIRecord**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.




{% include docsFooter.md %}