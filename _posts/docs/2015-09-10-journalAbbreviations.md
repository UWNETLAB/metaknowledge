---
layout: page
title: journalAbbreviations
categories: docs
excerpt: The journalAbbreviations Module
tags: [module]
weight: 3
---
<a name="journalAbbreviations"></a>
<a name="journalAbbreviations.drop_edges"></a>journalAbbreviations.**drop_edges**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored


- - -

<a name="journalAbbreviations.drop_nodesByCount"></a>journalAbbreviations.**drop_nodesByCount**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to count field in the node's dictionary, default is count as that is often correct

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors


- - -

<a name="journalAbbreviations.drop_nodesByDegree"></a>journalAbbreviations.**drop_nodesByDegree**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True


- - -

<a name="journalAbbreviations.filterNonJournals"></a>journalAbbreviations.**filterNonJournals**(_citesLst, invert=False_):

# Needs to be written

- - -

<a name="journalAbbreviations.graphStats"></a>journalAbbreviations.**graphStats**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

# Needs to be written

- - -

<a name="journalAbbreviations.isiParser"></a>journalAbbreviations.**isiParser**(_isifile_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each it finds is used to initialize a Record then all Record are returned as a list.


- - -

<a name="journalAbbreviations.read_graph"></a>journalAbbreviations.**read_graph**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads the files given by edgeList and if given nodeList and produces a networkx graph
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is designed only for the files produced by metaknowledge and is meant to be the reverse of write_graph()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodeList must be given if any of the attributes of the node are needed
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;directed controls if the resultant graph is directional eSource and eDest control the direction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idKey, eSource and  eDest are the labels for the edge's id, source and destination respectively, they must match headers in the file or a keyError exception will be thrown

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igraph Style


- - -

<a name="journalAbbreviations.recordParser"></a>journalAbbreviations.**recordParser**(_paper_):

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

<a name="journalAbbreviations.write_edgeList"></a>journalAbbreviations.**write_edgeList**(_grph, name, extraInfo=True, progBar=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;writes an edge list of grph with filename name, if extraInfo is true the additional information about the edges, e.g. weight, will be written.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All edges must have the same tags


- - -

<a name="journalAbbreviations.write_graph"></a>journalAbbreviations.**write_graph**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes both the edge list and the node attribute list of grph.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The output files start with name, the file type[edgeList, nodeAttributes] then if typing is True the type of graph (directed or undirected) then the suffix, it appears as follows:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    name_fileType_Graphtype.suffix
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If edgeInfo is true the extra information about the edges will be included in their list, i.e. their weight will be given
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If overwrite is False write_graph will throw an exception if either of the files it is attempting to write exist


- - -

<a name="journalAbbreviations.write_nodeAttributeFile"></a>journalAbbreviations.**write_nodeAttributeFile**(_grph, name, progBar=None_):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;writes a node attribute list of grph with filename name, the first column is the node's ID then all after it are its associated information.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All nodes must have the same tags.


