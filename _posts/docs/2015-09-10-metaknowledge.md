---
layout: page
title: metaknowledge
categories: docs
excerpt: The metaknowledge Package
tags: [main]
weight: 1
---
<a name="metaknowledge"></a>
<a name="blondel"></a>**blondel**(_G, weightParameter=None, communityParameter='community'_):

# Needs to be written

- - -

<a name="btest"></a>**btest**(_quite=False_):

# Needs to be written

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

# Needs to be written

- - -

<a name="graphStats"></a>**graphStats**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

# Needs to be written

- - -

<a name="isiParser"></a>**isiParser**(_isifile_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each it finds is used to initialize a Record then all Record are returned as a list.


- - -

<a name="modularity"></a>**modularity**(_G, weightParameter=None, communityParameter='community'_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gets modularity of network, currently not tuned


- - -

<a name="read_graph"></a>**read_graph**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads the files given by edgeList and if given nodeList and produces a networkx graph
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is designed only for the files produced by metaknowledge and is meant to be the reverse of write_graph()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodeList must be given if any of the attributes of the node are needed
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;directed controls if the resultant graph is directional eSource and eDest control the direction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idKey, eSource and  eDest are the labels for the edge's id, source and destination respectively, they must match headers in the file or a keyError exception will be thrown

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igraph Style


- - -

<a name="recordParser"></a>**recordParser**(_paper_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads the file _paper_ until it reaches 'ER'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"AF BREVIK, I

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ANICIN, B"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Record](#metaknowledge.Record) objects can be created with these dictionaries as the initializer.

#####&nbsp;&nbsp;&nbsp; Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_paper_ : `file stream`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; An open file, with the current line at the beginning of the record.

#####&nbsp;&nbsp;&nbsp; Returns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dict[str : List[str]]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


- - -

<a name="write_edgeList"></a>**write_edgeList**(_grph, name, extraInfo=True, progBar=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;writes an edge list of grph with filename name, if extraInfo is true the additional information about the edges, e.g. weight, will be written.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All edges must have the same tags


- - -

<a name="write_graph"></a>**write_graph**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes both the edge list and the node attribute list of grph.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The output files start with name, the file type[edgeList, nodeAttributes] then if typing is True the type of graph (directed or undirected) then the suffix, it appears as follows:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    name_fileType_Graphtype.suffix
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If edgeInfo is true the extra information about the edges will be included in their list, i.e. their weight will be given
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If overwrite is False write_graph will throw an exception if either of the files it is attempting to write exist


- - -

<a name="write_nodeAttributeFile"></a>**write_nodeAttributeFile**(_grph, name, progBar=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;writes a node attribute list of grph with filename name, the first column is the node's ID then all after it are its associated information.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All nodes must have the same tags.


<a name="BadCitation"></a>**BadCitation**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exception thrown by Citation


- - -

<a name="BadISIRecord"></a>**BadISIRecord**():

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.


