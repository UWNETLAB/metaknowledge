#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import metaknowledge

import networkx as nx
import csv
import os

from .progressBar import _ProgressBar

def readGraph(edgeList, nodeList = None, directed = False, idKey = 'ID', eSource = 'From', eDest = 'To'):
    """Reads the files given by _edgeList_ and _nodeList_ and creates a networkx graph for the files.

    This is designed only for the files produced by metaknowledge and is meant to be the reverse of [writeGraph()](#metaknowledge.writeGraph), if this does not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried as it is aimed at a more general usage.

    The read edge list format assumes the column named _eSource_ (default `'From'`) is the source node, then the column _eDest_ (default `'To'`) givens the destination and all other columns are attributes of the edges, e.g. weight.

    The read node list format assumes the column _idKey_ (default `'ID'`) is the ID of the node for the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

    **Note**: If the names of the columns do not match those given to **readGraph()** a `KeyError` exception will be raised.

    **Note**: If nodes appear in the edgelist but not the nodeList they will be created silently with no attributes.

    # Parameters

    _edgeList_ : `str`

    > a string giving the path to the edge list file

    _nodeList_ : `optional [str]`

    > default `None`, a string giving the path to the node list file

    _directed_ : `optional [bool]`

    > default `False`, if `True` the produced network is directed from _eSource_ to _eDest_

    _idKey_ : `optional [str]`

    > default `'ID'`, the name of the ID column in the node list

    _eSource_ : `optional [str]`

    > default `'From'`, the name of the source column in the edge list

    _eDest_ : `optional [str]`

    > default `'To'`, the name of the destination column in the edge list

    # Returns

    `networkx Graph`

    > the graph described by the input files
    """
    progArgs = (0, "Starting to reading graphs")
    if metaknowledge.VERBOSE_MODE:
        progKwargs = {'dummy' : False}
    else:
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        if directed:
            grph = nx.DiGraph()
        else:
            grph = nx.Graph()
        if nodeList:
            PBar.updateVal(0, "Reading " + nodeList)
            f = open(os.path.expanduser(os.path.abspath(nodeList)))
            nFile = csv.DictReader(f)
            for line in nFile:
                vals = line
                ndID = vals[idKey]
                del vals[idKey]
                if len(vals) > 0:
                    grph.add_node(ndID, attr_dict=vals)
                else:
                    grph.add_node(ndID)
            f.close()
        PBar.updateVal(.25, "Reading " + edgeList)
        f = open(os.path.expanduser(os.path.abspath(edgeList)))
        eFile = csv.DictReader(f)
        for line in eFile:
            vals = line
            eFrom = vals[eSource]
            eTo = vals[eDest]
            del vals[eSource]
            del vals[eDest]
            if len(vals) > 0:
                grph.add_edge(eFrom, eTo, attr_dict = vals)
            else:
                grph.add_edge(eFrom, eTo)
        PBar.finish("{} nodes and {} edges found".format(len(grph.nodes()), len(grph.edges())))
        f.close()
        return grph

def writeGraph(grph, name, edgeInfo = True, typing = False, suffix = 'csv', overwrite = True):
    """Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

    The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

    >> name_fileType.suffix

    Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

    To read back these files use [readGraph()](#metaknowledge.readGraph) and to write only one type of lsit use [writeEdgeList()](#metaknowledge.writeEdgeList) or [writeNodeAttributeFile()](#metaknowledge.writeNodeAttributeFile).

    **Warning**: this function will overwrite files, if they are in the way of the output, to prevent this set _overwrite_ to `False`

    **Note**: If any nodes or edges are missing an attribute a `KeyError` will be raised.

    # Parameters

    _grph_ : `networkx Graph`

    > A networkx graph of the network to be written.

    _name_ : `str`

    > The start of the file name to be written, can include a path.

    _edgeInfo_ : `optional [bool]`

    > Default `True`, if `True` the the attributes of each edge are written to the edge list.

    _typing_ : `optional [bool]`

    > Default `False`, if `True` the directed ness of the graph will be added to the file names.

    _suffix_ : `optional [str]`

    > Default `"csv"`, the suffix of the file.

    _overwrite_ : `optional [bool]`

    > Default `True`, if `True` files will be overwritten silently, otherwise an `OSError` exception will be raised.
    """
    if metaknowledge.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Writing the graph to two files starting with: " + name)
    else:
        PBar = None
    if typing:
        if isinstance(grph, nx.classes.digraph.DiGraph) or isinstance(grph, nx.classes.multidigraph.MultiDiGraph):
            grphType = "_directed"
        else:
            grphType = "_undirected"
    else:
        grphType = ''
    nameCompts = os.path.split(os.path.expanduser(os.path.normpath(name)))
    if nameCompts[0] == '' and nameCompts[1] == '':
        edgeListName = "edgeList"+ grphType + '.' + suffix
        nodesAtrName = "nodeAttributes"+ grphType + '.' + suffix
    elif nameCompts[0] == '':
        edgeListName = nameCompts[1] + "_edgeList"+ grphType + '.' + suffix
        nodesAtrName = nameCompts[1] + "_nodeAttributes"+ grphType + '.' + suffix
    elif nameCompts[1] == '':
        edgeListName = os.path.join(nameCompts[0], "edgeList"+ grphType + '.' + suffix)
        nodesAtrName = os.path.join(nameCompts[0], "nodeAttributes"+ grphType + '.' + suffix)
    else:
        edgeListName = os.path.join(nameCompts[0], nameCompts[1] + "_edgeList"+ grphType + '.' + suffix)
        nodesAtrName = os.path.join(nameCompts[0], nameCompts[1] + "_nodeAttributes"+ grphType + '.' + suffix)
    if not overwrite:
        if os.path.isfile(edgeListName):
            raise OSError(edgeListName+ " already exists")
        if os.path.isfile(nodesAtrName):
            raise OSError(nodesAtrName + " already exists")
    writeEdgeList(grph, edgeListName, extraInfo = edgeInfo, _progBar = PBar)
    if PBar:
        PBar.jumpUp()
    writeNodeAttributeFile(grph, nodesAtrName, _progBar = PBar)
    if PBar:
        PBar.finish(str(len(grph.nodes())) + " nodes and " + str(len(grph.edges())) + " edges written to file")

def writeEdgeList(grph, name, extraInfo = True, allSameAttribute = False, _progBar = None):
    """Writes an edge list of _grph_ at the destination _name_.

    The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

    **Note**: If any edges are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be written to _name_

    _name_ : `str`

    > The name of the file to be written

    _edgeInfo_ : `optional [bool]`

    > Default `True`, if `True` the attributes of each edge will be written

    _allSameAttribute_ : `optional [bool]`

    > Default `False`, if `True` all the edges must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.
    """
    if _progBar:
        count = 0
        eMax = len(grph.edges(data = True))
        if isinstance(_progBar, _ProgressBar):
            _progBar.updateVal(0, "Writing edge list " + name)
        else:
            _progBar = _ProgressBar(0, "Writing edge list " + name)
    if len(grph.edges(data = True)) < 1:
        outFile = open(os.path.expanduser(os.path.abspath(name)), 'w')
        outFile.write('"From","To"\n')
        outFile.close()
        if _progBar:
            _progBar.updateVal(1, "Done edge list " + name + ", 0 edges written.")
    else:
        if extraInfo:
            csvHeader = []
            if allSameAttribute:
                csvHeader = ['From'] +  ['To'] + list(grph.edges_iter(data = True).__next__()[2].keys())
            else:
                for eTuple in grph.edges_iter(data = True):
                    for key in eTuple[2].keys():
                        if key not in csvHeader:
                            csvHeader.append(key)
                csvHeader += ['From', 'To']
        else:
            csvHeader = ['From'] +  ['To']
        f = open(os.path.expanduser(os.path.abspath(name)), 'w')
        outFile = csv.DictWriter(f, csvHeader, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_ALL)
        outFile.writeheader()
        if extraInfo:
            for e in grph.edges_iter(data = True):
                if _progBar:
                    count += 1
                    _progBar.updateVal(count / eMax)
                eDict = e[2].copy()
                eDict['From'] = e[0]
                eDict['To'] = e[1]
                try:
                    outFile.writerow(eDict)
                except ValueError:
                    raise ValueError("Some edges in The graph do not have the same attributes")
        else:
            for e in grph.edges_iter():
                if _progBar:
                    count += 1
                    if count % 100 == 0:
                        _progBar.updateVal(count / eMax)
                eDict['From'] = e[0]
                eDict['To'] = e[1]
                outFile.writerow(eDict)
        if _progBar:
            _progBar.finish("Done edge list " + name + ", " + str(count) + " edges written.")
        f.close()

def writeNodeAttributeFile(grph, name, allSameAttribute = False,_progBar = None):
    """Writes a node attribute list of _grph_ to the file given by the path _name_.

    The node list has one column call `'ID'` with the node ids used by networkx and all other columns are the node attributes.

    **Note**: If any nodes are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be written to _name_

    _name_ : `str`

    > The name of the file to be written

    _allSameAttribute_ : `optional [bool]`

    > Default `False`, if `True` all the nodes must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.
    """
    if _progBar:
        count = 0
        nMax = len(grph.nodes())
        if isinstance(_progBar, _ProgressBar):
            _progBar.updateVal(0, "Writing edgelist " + name)
        else:
            _progBar = _ProgressBar(0, "Writing edgelist " + name)
    if len(grph.nodes(data = True)) < 1:
        outFile = open(os.path.expanduser(os.path.abspath(name)), 'w')
        outFile.write('ID\n')
        outFile.close()
        if _progBar:
            _progBar.updateVal(1, "Done node attribute list: " + name + ", 0 nodes written.")
    else:
        csvHeader = []
        if allSameAttribute:
            csvHeader = ['ID'] + list(grph.nodes_iter(data = True).__next__()[1].keys())
        else:
            for n, attribs in grph.nodes_iter(data = True):
                for key in attribs.keys():
                    if key not in csvHeader:
                        csvHeader.append(key)
            csvHeader.append('ID')
        f = open(name, 'w')
        outFile = csv.DictWriter(f, csvHeader, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
        outFile.writeheader()
        for n in grph.nodes_iter(data = True):
            if _progBar:
                count += 1
                _progBar.updateVal(count / nMax)
            nDict = n[1].copy()
            nDict['ID'] = n[0]
            try:
                outFile.writerow(nDict)
            except ValueError:
                raise ValueError("Some nodes in the graph do not have the same attributes")
        if _progBar:
            _progBar.updateVal(1, "Done node attribute list: " + name + ", " + str(count) + " nodes written.")
        f.close()

def getWeight(grph, nd1, nd2, weightString = "weight", returnType = int):
    """
    A way of getting the weight of an edge with or without weight as a parameter
    returns a the value of the weight parameter converted to returnType if it is given or 1 (also converted) if not
    """
    if not weightString:
        return returnType(1)
    else:
        return returnType(grph.edge[nd1][nd2][weightString])

def getNodeDegrees(grph, weightString = "weight", strictMode = False,  returnType = int, edgeType = 'bi'):
    """
    Retunrs a dictionary of nodes to their degrees, the degree is determined by adding the weight of edge with the weight being the string weightString that gives the name of the attribute of each edge containng thier weight. The Weights are then converted to the type returnType. If weightString is give as False instead each edge is counted as 1.

    edgeType, takes in one of three strings: 'bi', 'in', 'out'. 'bi' means both nodes on the edge count it, 'out' mans only the one the edge comes form counts it and 'in' means only the node the edge goes to counts it. 'bi' is the default. Use only on directional graphs as otherwise the selected nodes is random.
    """
    ndsDict = {}
    for nd in grph.nodes_iter():
        ndsDict[nd] = returnType(0)
    for e in grph.edges_iter(data = True):
        if weightString:
            try:
                edgVal = returnType(e[2][weightString])
            except KeyError:
                if strictMode:
                    raise KeyError("The edge from " + str(e[0]) + " to " + str(e[1]) + " does not have the attribute: '" + str(weightString) + "'")
                else:
                    edgVal = returnType(1)
        else:
            edgVal = returnType(1)
        if edgeType == 'bi':
            ndsDict[e[0]] += edgVal
            ndsDict[e[1]] += edgVal
        elif edgeType == 'in':
            ndsDict[e[1]] += edgVal
        elif edgeType == 'out':
            ndsDict[e[0]] += edgVal
        else:
            raise ValueError("edgeType must be 'bi', 'in', or 'out'")
    return ndsDict

def getDegreeDistribution(grph, weightParameter = "weight", strictWeightNames = False,  weightType = int, directionalType = 'bi'):
    if weightType != int:
        raise ValueError("Unsupported type for weights, only ints are supported")
    ndsDict = getNodeDegrees(grph, weightString = weightParameter, strictMode = strictWeightNames, returnType = weightType, edgeType = directionalType)
    distVec = [0] * (max(ndsDict.values()) + 1)
    for v in ndsDict.values():
        distVec[v] += 1
    return distVec

def dropEdges(grph, minWeight = - float('inf'), maxWeight = float('inf'), parameterName = 'weight', ignoreUnweighted = False, dropSelfLoops = False):
    """Modifies _grph_ by dropping edges whose weight is not within the inclusive bounds of _minWeight_ and _maxWeight_, i.e after running _grph_ will only have edges whose weights meet the following inequality: _minWeight_ <= edge's weight <= _maxWeight_. A `Keyerror` will be raised if the graph is unweighted unless _ignoreUnweighted_ is `True`, the weight is determined by examining the attribute _parameterName_.

    **Note**: none of the default options will result in _grph_ being modified so only specify the relevant ones, e.g. `dropEdges(G, dropSelfLoops = True)` will remove only the self loops from `G`.

    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be modified.

    _minWeight_ : `optional [int or double]`

    > default `-inf`, the minimum weight for an edge to be kept in the graph.

    _maxWeight_ : `optional [int or double]`

    > default `inf`, the maximum weight for an edge to be kept in the graph.

    _parameterName_ : `optional [str]`

    > default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct

    _ignoreUnweighted_ : `optional [bool]`

    > default `False`, if `True` unweighted edges will kept

    _dropSelfLoops_ : `optional [bool]`

    > default `False`, if `True` self loops will be removed regardless of their weight
    """
    count = 0
    total = len(grph.edges())
    if metaknowledge.VERBOSE_MODE:
        progArgs = (0, "Dropping edges")
        progKwargs = {}
    else:
        progArgs = (0, "Dropping edges")
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        if dropSelfLoops:
            slps = grph.selfloop_edges()
            if PBar:
                PBar.updateVal(0, "Dropping self {} loops".format(len(slps)))
            for e in slps:
                grph.remove_edge(e[0], e[1])
        if minWeight != - float('inf') or maxWeight != float('inf'):
            for e in grph.edges(data = True):
                try:
                    val = e[2][parameterName]
                except KeyError:
                    if not ignoreUnweighted:
                        raise KeyError("One or more Edges do not have weight or " + str(parameterName), " is not the name of the weight")
                    else:
                        pass
                else:
                    if PBar:
                        count += 1
                        if count % 100000 == 0:
                            PBar.updateVal(count/ total, str(count) + " edges analysed and " + str(total -len(grph.edges())) + " edges dropped")
                    if val > maxWeight or  val < minWeight:
                        grph.remove_edge(e[0], e[1])
        if PBar:
            PBar.finish(str(total - len(grph.edges())) + " edges out of " + str(total) + " dropped, " + str(len(grph.edges())) + " returned")

def dropNodesByDegree(grph, minDegree = -float('inf'), maxDegree = float('inf'), useWeight = True, parameterName = 'weight', includeUnweighted = True):
    """Modifies _grph_ by dropping nodes that do not have a degree that is within inclusive bounds of _minDegree_ and _maxDegree_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minDegree_ <= node's degree <= _maxDegree_.

    Degree is determined in two ways, the default _useWeight_ is the weight attribute of the edges to a node will be summed, the attribute's name is _parameterName_ otherwise the number of edges touching the node is used. If _includeUnweighted_ is `True` then _useWeight_ will assign a degree of 1 to unweighted edges.


    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be modified.

    _minDegree_ : `optional [int or double]`

    > default `-inf`, the minimum degree for an node to be kept in the graph.

    _maxDegree_ : `optional [int or double]`

    > default `inf`, the maximum degree for an node to be kept in the graph.

    _useWeight_ : `optional [bool]`

    > default `True`, if `True` the the edge weights will be summed to get the degree, if `False` the number of edges will be used to determine the degree.

    _parameterName_ : `optional [str]`

    > default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct.

    _includeUnweighted_ : `optional [bool]`

    > default `True`, if `True` edges with no weight will be considered to have a weight of 1, if `False` they will cause a `KeyError` to be raised.
    """
    count = 0
    total = len(grph.nodes())
    if metaknowledge.VERBOSE_MODE:
        progArgs = (0, "Dropping nodes by degree")
        progKwargs = {}
    else:
        progArgs = (0, "Dropping nodes by degree")
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        badNodes = []
        for n in grph.nodes_iter():
            if PBar:
                count += 1
                if count % 10000 == 0:
                    PBar.updateVal(count/ total, str(count) + " nodes analysed and " + str(len(badNodes)) + " nodes dropped")
            val = 0
            if useWeight:
                for e in grph.edges(n, data = True):
                    try:
                        val += e[2][parameterName]
                    except KeyError:
                        if not includeUnweighted:
                            raise KeyError("One or more Edges do not have weight or " + str(parameterName), " is not the name of the weight")
                        else:
                            val += 1
            else:
                val = len(grph.edges(n))
            if val < minDegree or val > maxDegree:
                badNodes.append(n)
        if PBar:
            PBar.updateVal(1, "Cleaning up graph")
        grph.remove_nodes_from(badNodes)
        if PBar:
            PBar.finish("{} nodes out of {} dropped, {} returned".format(len(badNodes), total, total - len(badNodes)))


def dropNodesByCount(grph, minCount = -float('inf'), maxCount = float('inf'), parameterName = 'count', ignoreMissing = False):
    """Modifies _grph_ by dropping nodes that do not have a count that is within inclusive bounds of _minCount_ and _maxCount_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minCount_ <= node's degree <= _maxCount_.

    Count is determined by the count attribute, _parameterName_, and if missing will result in a `KeyError` being raised. _ignoreMissing_ can be set to `True` to suppress the error.

    minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input

    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be modified.

    _minCount_ : `optional [int or double]`

    > default `-inf`, the minimum Count for an node to be kept in the graph.

    _maxCount_ : `optional [int or double]`

    > default `inf`, the maximum Count for an node to be kept in the graph.

    _parameterName_ : `optional [str]`

    > default `'count'`, key to count field in the nodes's attribute dictionary, the default is the same thoughout metaknowledge so is likely to be correct.

    _ignoreMissing_ : `optional [bool]`

    > default `False`, if `True` nodes missing a count will be kept in the graph instead of raising an exception
    """
    count = 0
    total = len(grph.nodes())
    if metaknowledge.VERBOSE_MODE:
        progArgs = (0, "Dropping nodes by count")
        progKwargs = {}
    else:
        progArgs = (0, "Dropping nodes by count")
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        badNodes = []
        for n in grph.nodes_iter(data = True):
            if PBar:
                count += 1
                if count % 10000 == 0:
                    PBar.updateVal(count/ total, str(count) + "nodes analysed and {} nodes dropped".format(len(badNodes)))
            try:
                val = n[1][parameterName]
            except KeyError:
                if not ignoreMissing:
                    raise KeyError("One or more nodes do not have counts or " + str(parameterName), " is not the name of the count parameter")
                else:
                    pass
            else:
                if val < minCount or val > maxCount:
                    badNodes.append(n[0])
        if PBar:
            PBar.updateVal(1, "Cleaning up graph")
        grph.remove_nodes_from(badNodes)
        if PBar:
            PBar.finish("{} nodes out of {} dropped, {} returned".format(len(badNodes), total, total - len(badNodes)))

def mergeGraphs(targetGraph, addedGraph, incrementedNodeVal = 'count', incrementedEdgeVal = 'weight'):
    """A quick way of merging graphs, this is meant to be quick and is only intended for graphs generated by metaknowledge. This does not check anything and as such may cause unexpected results if the source and target were not generated by the same method.

    **mergeGraphs**() will **modify** _targetGraph_ in place by adding the nodes and edges found in the second, _addedGraph_. If a node or edge exists _targetGraph_ is given precedence, but the edge and node attributes given by _incrementedNodeVal_ and incrementedEdgeVal are added instead of being overwritten.

    # Parameters

    _targetGraph_ : `networkx Graph`

    > the graph to be modified, it has precedence.

    _addedGraph_ : `networkx Graph`

    > the graph that is unmodified, it is added and does **not** have precedence.

    _incrementedNodeVal_ : `optional [str]`

    > default `'count'`, the name of the count attribute for the graph's nodes. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.

    _incrementedEdgeVal_ : `optional [str]`

    > default `'weight'`, the name of the weight attribute for the graph's edges. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.
    """

    for addedNode, attribs in addedGraph.nodes_iter(data = True):
        if incrementedNodeVal:
            try:
                targetGraph.node[addedNode][incrementedNodeVal] += attribs[incrementedNodeVal]
            except KeyError:
                targetGraph.add_node(addedNode, **attribs)
        else:
            if not targetGraph.has_node(addedNode):
                targetGraph.add_node(addedNode, **attribs)
    for edgeNode1, edgeNode2, attribs in addedGraph.edges_iter(data = True):
        if incrementedEdgeVal:
            try:
                targetGraph.edge[edgeNode1][edgeNode2][incrementedEdgeVal] += attribs[incrementedEdgeVal]
            except KeyError:
                targetGraph.add_edge(edgeNode1, edgeNode2, **attribs)
        else:
            if not targetGraph.Graph.has_edge(edgeNode1, edgeNode2):
                targetGraph.add_edge(edgeNode1, edgeNode2, **attribs)

def graphStats(G, stats = ('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString = True):
    """Returns a string or list containing statistics about the graph _G_.

    **graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

    # Parameters

    _G_ : `networkx Graph`

    > The graph for the statistics to be determined of

    _stats_ : `optional [list or tuple [str]]`

    > Default `('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity')`, a list or tuple containing any number or combination of the strings:

    > `"nodes"`, `"edges"`, `"isolates"`, `"loops"`, `"density"` and `"transitivity"``

    > At least one occurrence of the corresponding string causes the statistics to be provided in the string output. For the non-string (tuple) output the returned tuple has the same length as the input and each output is at the same index as the string that requested it, e.g.

    > `_stats_ = ("edges", "loops", "edges")`

    > The return is a tuple with 2 elements the first and last of which are the number of edges and the second is the number of loops

    _makeString_ : `optional [bool]`

    > Default `True`, if `True` a string is returned if `False` a tuple

    # Returns

    `str or tuple [float and int]`

    > The type is determined by _makeString_ and the layout by _stats_
     """

    for sts in stats:
        if sts not in ['nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity']:
            raise RuntimeError('"{}" is not a valid stat.'.format(sts))
    if makeString:
        stsData = []
    else:
        stsData = {}
    if 'nodes' in stats:
        if makeString:
            stsData.append("{:G} nodes".format(len(G.nodes())))
        else:
            stsData['nodes'] = len(G.nodes())
    if 'edges' in stats:
        if makeString:
            stsData.append("{:G} edges".format(len(G.edges())))
        else:
            stsData['edges'] = len(G.edges())
    if 'isolates' in stats:
        if makeString:
            stsData.append("{:G} isolates".format(len(nx.isolates(G))))
        else:
            stsData['isolates'] = len(nx.isolates(G))
    if 'loops' in stats:
        if makeString:
            stsData.append("{:G} self loops".format(len(G.selfloop_edges())))
        else:
            stsData['loops'] = len(G.selfloop_edges())
    if 'density' in stats:
        if makeString:
            stsData.append("a density of {:G}".format(nx.density(G)))
        else:
            stsData['density'] = nx.density(G)
    if 'transitivity' in stats:
        if makeString:
            stsData.append("a transitivity of {:G}".format(nx.transitivity(G)))
        else:
            stsData['transitivity'] = nx.transitivity(G)
    if makeString:
        retString = "The graph has "
        if len(stsData) < 1:
            return retString
        elif len(stsData) == 1:
            return retString + stsData[0]
        else:
            return retString + ', '.join(stsData[:-1]) + ' and ' + stsData[-1]
    else:
        retLst = []
        for sts in stats:
            retLst.append(stsData[sts])
        return tuple(retLst)
