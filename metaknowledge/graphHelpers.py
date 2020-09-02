#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import networkx as nx
import csv
import os
sel
from .progressBar import _ProgressBar
from .mkExceptions import RCValueError

import metaknowledge

def readGraph(edgeList, nodeList = None, directed = False, idKey = 'ID', eSource = 'Source', eDest = 'Target'):
    """Reads the files given by _edgeList_ and _nodeList_ and creates a networkx graph for the files.

    This is designed only for the files produced by metaknowledge and is meant to be the reverse of [writeGraph()](#metaknowledge.graphHelpers.writeGraph), if this does not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried as it is aimed at a more general usage.

    The read edge list format assumes the column named _eSource_ (default `'Source'`) is the source node, then the column _eDest_ (default `'Target'`) givens the destination and all other columns are attributes of the edges, e.g. weight.

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

    > default `'Source'`, the name of the source column in the edge list

    _eDest_ : `optional [str]`

    > default `'Target'`, the name of the destination column in the edge list

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
                    grph.add_node(ndID, **vals)
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
                grph.add_edge(eFrom, eTo, **vals)
            else:
                grph.add_edge(eFrom, eTo)
        PBar.finish("{} nodes and {} edges found".format(len(grph.nodes()), len(grph.edges())))
        f.close()
        return grph

def writeGraph(grph, name, edgeInfo = True, typing = False, suffix = 'csv', overwrite = True, allSameAttribute = False):
    """Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

    The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

    >> name_fileType.suffix

    Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, `'Source'` and `'Target'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

    To read back these files use [readGraph()](#metaknowledge.graphHelpers.readGraph) and to write only one type of lsit use [writeEdgeList()](#metaknowledge.graphHelpers.writeEdgeList) or [writeNodeAttributeFile()](#metaknowledge.graphHelpers.writeNodeAttributeFile).

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
    progArgs = (0, "Writing the graph to files starting with: {}".format(name))
    if metaknowledge.VERBOSE_MODE:
        progKwargs = {'dummy' : False}
    else:
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
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
        writeEdgeList(grph, edgeListName, extraInfo = edgeInfo, allSameAttribute = allSameAttribute, _progBar = PBar)
        writeNodeAttributeFile(grph, nodesAtrName, allSameAttribute = allSameAttribute, _progBar = PBar)
        PBar.finish("{} nodes and {} edges written to file".format(len(grph.nodes()), len(grph.edges())))

def writeEdgeList(grph, name, extraInfo = True, allSameAttribute = False, _progBar = None):
    """Writes an edge list of _grph_ at the destination _name_.

    The edge list has two columns for the source and destination of the edge, `'Source'` and `'Target'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

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
    count = 0
    eMax = len(grph.edges())
    if metaknowledge.VERBOSE_MODE or isinstance(_progBar, _ProgressBar):
        if isinstance(_progBar, _ProgressBar):
            PBar = _progBar
            PBar.updateVal(0, "Writing edge list {}".format(name))
        else:
            PBar = _ProgressBar(0, "Writing edge list {}".format(name))
    else:
        PBar = _ProgressBar(0, "Writing edge list {}".format(name), dummy = True)
    if len(grph.edges(data = True)) < 1:
        outFile = open(os.path.expanduser(os.path.abspath(name)), 'w')
        outFile.write('"Source","Target"\n')
        outFile.close()
        PBar.updateVal(1, "Done edge list '{}', 0 edges written.".format(name))
    else:
        if extraInfo:
            csvHeader = []
            if allSameAttribute:
                csvHeader = ['Source'] +  ['Target'] + list(grph.edges(data = True).__next__()[2].keys())
            else:
                extraAttribs = set()
                for eTuple in grph.edges(data = True):
                    count += 1
                    if count % 1000 == 0:
                        PBar.updateVal(count / eMax * .10, "Checking over edge: '{}' to '{}'".format(eTuple[0], eTuple[1]))
                    s = set(eTuple[2].keys()) - extraAttribs
                    if len(s) > 0:
                        for i in s:
                            extraAttribs.add(i)
                csvHeader = ['Source', 'Target'] + list(extraAttribs)
        else:
            csvHeader = ['Source'] +  ['Target']
        count = 0
        PBar.updateVal(.01, "Opening file {}".format(name))
        f = open(os.path.expanduser(os.path.abspath(name)), 'w', newline = '')
        outFile = csv.DictWriter(f, csvHeader, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_NONNUMERIC)
        outFile.writeheader()
        if extraInfo:
            for e in grph.edges(data = True):
                count += 1
                if count % 1000 == 0:
                    PBar.updateVal(count / eMax * .90 + .10, "Writing edge: '{}' to '{}'".format(e[0], e[1]))
                eDict = e[2].copy()
                eDict['Source'] = e[0]
                eDict['Target'] = e[1]
                try:
                    outFile.writerow(eDict)
                except UnicodeEncodeError:
                    #Because Windows
                    newDict = {k.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(k, str) else k: v.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(v, str) else v for k, v in eDict.items()}
                    outFile.writerow(newDict)
                except ValueError:
                    raise ValueError("Some edges in The graph do not have the same attributes")
        else:
            for e in grph.edges():
                count += 1
                if count % 1000 == 0:
                    PBar.updateVal(count / eMax * .90 + .10, "Writing edge: '{}' to '{}'".format(e[0], e[1]))
                eDict['Source'] = e[0]
                eDict['Target'] = e[1]
                try:
                    outFile.writerow(eDict)
                except UnicodeEncodeError:
                    #Because Windows
                    newDict = {k.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(k, str) else k: v.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(v, str) else v for k, v in eDict.items()}
                    outFile.writerow(newDict)
        PBar.updateVal(1, "Closing {}".format(name))
        f.close()
        if not isinstance(_progBar, _ProgressBar):
            PBar.finish("Done edge list {}, {} edges written.".format(name, count))

def writeNodeAttributeFile(grph, name, allSameAttribute = False, _progBar = None):
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
    count = 0
    nMax = len(grph.nodes())
    if metaknowledge.VERBOSE_MODE or isinstance(_progBar, _ProgressBar):
        if isinstance(_progBar, _ProgressBar):
            PBar = _progBar
            PBar.updateVal(0, "Writing node list {}".format(name))
        else:
            PBar = _ProgressBar(0, "Writing node list {}".format(name))
    else:
        PBar = _ProgressBar(0, "Writing node list {}".format(name), dummy = True)
    if len(grph.nodes(data = True)) < 1:
        outFile = open(os.path.expanduser(os.path.abspath(name)), 'w')
        outFile.write('ID\n')
        outFile.close()
        PBar.updateVal(1, "Done node attribute list: {}, 0 nodes written.".format(name))
    else:
        csvHeader = []
        if allSameAttribute:
            csvHeader = ['ID'] + list(grph.nodes(data = True).__next__()[1].keys())
        else:
            extraAttribs = set()
            for n, attribs in grph.nodes(data = True):
                count += 1
                if count % 100 == 0:
                    PBar.updateVal(count / nMax * .10, "Checking over node: '{}'".format(n))
                s = set(attribs.keys()) - extraAttribs
                if len(s) > 0:
                    for i in s:
                        extraAttribs.add(i)
            csvHeader = ['ID'] + list(extraAttribs)
        count = 0
        PBar.updateVal(.10, "Opening '{}'".format(name))
        f = open(name, 'w', newline = '')
        outFile = csv.DictWriter(f, csvHeader, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
        outFile.writeheader()
        for n in grph.nodes(data = True):
            count += 1
            if count % 100 == 0:
                PBar.updateVal(count / nMax * .90 + .10, "Writing node: '{}'".format(n[0]))
            nDict = n[1].copy()
            nDict['ID'] = n[0]
            try:
                outFile.writerow(nDict)
            except UnicodeEncodeError:
                #Because Windows
                newDict = {k.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(k, str) else k: v.encode('ASCII', errors='ignore').decode('ASCII', errors='ignore') if isinstance(v, str) else v for k, v in nDict.items()}
                outFile.writerow(newDict)
            except ValueError:
                raise ValueError("Some nodes in the graph do not have the same attributes")
        PBar.updateVal(1, "Closing {}".format(name))
        f.close()
        if not isinstance(_progBar, _ProgressBar):
            PBar.finish("Done node attribute list: {}, {} nodes written.".format(name, count))

def writeTnetFile(grph, name, modeNameString, weighted = False, sourceMode = None, timeString = None, nodeIndexString = 'tnet-ID', weightString = 'weight'):
    """Writes an edge list designed for reading by the _R_ package [tnet](https://toreopsahl.com/tnet/).

    The _networkx_ graph provided must be a pure two-mode network, the modes must be 2 different values for the node attribute accessed by _modeNameString_ and all edges must be between different node types. Each node will be given an integer id, stored in the attribute given by _nodeIndexString_, these ids are then written to the file as the endpoints of the edges. Unless _sourceMode_ is given which mode is the source (first column) and which the target (second column) is random.

    **Note** the _grph_ will be modified by this function, the ids of the nodes will be written to the graph at the attribute _nodeIndexString_.

    # Parameters

    _grph_ : `network Graph`

    > The graph that will be written to _name_

    _name_ : `str`

    > The path of the file to write

    _modeNameString_ : `str`

    > The name of the attribute _grph_'s modes are stored in

    _weighted_ : `optional bool`

    > Default `False`, if `True` then the attribute _weightString_ will be written to the weight column

    _sourceMode_ : `optional str`

    > Default `None`, if given the name of the mode used for the source (first column) in the output file

    _timeString_ : `optional str`

    > Default `None`, if present the attribute _timeString_ of an edge will be written to the time column surrounded by double quotes (").

    **Note** The format used by tnet for dates is very strict it uses the ISO format, down to the second and without time zones.

    _nodeIndexString_ : `optional str`

    > Default `'tnet-ID'`, the name of the attribute to save the id for each node

    _weightString_ : `optional str`

    > Default `'weight'`, the name of the weight attribute
    """
    count = 0
    eMax = len(grph.edges())
    progArgs = (0, "Writing tnet edge list {}".format(name))
    if metaknowledge.VERBOSE_MODE:
        progKwargs = {'dummy' : False}
    else:
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        if sourceMode is not None:
            modes = [sourceMode]
        else:
            modes = []
        mode1Set = set()
        PBar.updateVal(.1, "Indexing nodes for tnet")
        for nodeIndex, node in enumerate(grph.nodes(data = True), start = 1):
            try:
                nMode = node[1][modeNameString]
            except KeyError:
                #too many modes so will fail
                modes = [1,2,3]
                nMode = 4
            if nMode not in modes:
                if len(modes) < 2:
                    modes.append(nMode)
                else:
                    raise RCValueError("Too many modes of '{}' found in the network or one of the nodes was missing its mode. There must be exactly 2 modes.".format(modeNameString))
            if nMode == modes[0]:
                mode1Set.add(node[0])
            node[1][nodeIndexString] = nodeIndex
        if len(modes) != 2:
            raise RCValueError("Too few modes of '{}' found in the network. There must be exactly 2 modes.".format(modeNameString))
        with open(name, 'w', encoding = 'utf-8') as f:
            edgesCaller = {'data' : True}
            if timeString is not None:
                edgesCaller['keys'] = True
            for *nodes, eDict in grph.edges(**edgesCaller):
                if timeString is not None:
                    n1, n2, keyVal = nodes
                else:
                    n1, n2 = nodes
                count += 1
                if count % 1000 == 1:
                    PBar.updateVal(count/ eMax * .9 + .1, "writing edge: '{}'-'{}'".format(n1, n2))
                if n1 in mode1Set:
                    if n2 in mode1Set:
                        raise RCValueError("The nodes '{}' and '{}' have an edge and the same type. The network must be purely 2-mode.".format(n1, n2))
                elif n2 in mode1Set:
                    n1, n2 = n2, n1
                else:
                    raise RCValueError("The nodes '{}' and '{}' have an edge and the same type. The network must be purely 2-mode.".format(n1, n2))
                if timeString is not None:
                    eTimeString = '"{}" '.format(keyVal)
                else:
                    eTimeString = ''
                if weighted:
                    f.write("{}{} {} {}\n".format(eTimeString, grph.node[n1][nodeIndexString], grph.node[n2][nodeIndexString], eDict[weightString]))
                else:
                    f.write("{}{} {}\n".format(eTimeString, grph.node[n1][nodeIndexString], grph.node[n2][nodeIndexString]))
        PBar.finish("Done writing tnet file '{}'".format(name))

def getWeight(grph, nd1, nd2, weightString = "weight", returnType = int):
    """
    A way of getting the weight of an edge with or without weight as a parameter
    returns a the value of the weight parameter converted to returnType if it is given or 1 (also converted) if not
    """
    if not weightString:
        return returnType(1)
    else:
        return returnType(grph.edges[nd1, nd2][weightString])

def getNodeDegrees(grph, weightString = "weight", strictMode = False,  returnType = int, edgeType = 'bi'):
    """
    Retunrs a dictionary of nodes to their degrees, the degree is determined by adding the weight of edge with the weight being the string weightString that gives the name of the attribute of each edge containng thier weight. The Weights are then converted to the type returnType. If weightString is give as False instead each edge is counted as 1.

    edgeType, takes in one of three strings: 'bi', 'in', 'out'. 'bi' means both nodes on the edge count it, 'out' mans only the one the edge comes form counts it and 'in' means only the node the edge goes to counts it. 'bi' is the default. Use only on directional graphs as otherwise the selected nodes is random.
    """
    ndsDict = {}
    for nd in grph.nodes():
        ndsDict[nd] = returnType(0)
    for e in grph.edges(data = True):
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
            slps = list(nx.selfloop_edges(grph))

            PBar.updateVal(0, "Dropping self {} loops".format(len(slps)))
            for e in slps:
                grph.remove_edge(e[0], e[1])
        edgesToDrop = []
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

                    count += 1
                    if count % 100000 == 0:
                        PBar.updateVal(count/ total, str(count) + " edges analysed and " + str(total -len(grph.edges())) + " edges dropped")
                    if val > maxWeight or  val < minWeight:
                        edgesToDrop.append((e[0], e[1]))
        grph.remove_edges_from(edgesToDrop)
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
        for n in grph.nodes():
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
        for n in grph.nodes(data = True):
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

    for addedNode, attribs in addedGraph.nodes(data = True):
        if incrementedNodeVal:
            try:
                targetGraph.node[addedNode][incrementedNodeVal] += attribs[incrementedNodeVal]
            except KeyError:
                targetGraph.add_node(addedNode, **attribs)
        else:
            if not targetGraph.has_node(addedNode):
                targetGraph.add_node(addedNode, **attribs)
    for edgeNode1, edgeNode2, attribs in addedGraph.edges(data = True):
        if incrementedEdgeVal:
            try:
                targetGraph.edges[edgeNode1, edgeNode2][incrementedEdgeVal] += attribs[incrementedEdgeVal]
            except KeyError:
                targetGraph.add_edge(edgeNode1, edgeNode2, **attribs)
        else:
            if not targetGraph.Graph.has_edge(edgeNode1, edgeNode2):
                targetGraph.add_edge(edgeNode1, edgeNode2, **attribs)

def graphStats(G, stats = ('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString = True, sentenceString = False):
    """Returns a string or list containing statistics about the graph _G_.

    **graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving each stat on a different line it can also produce a sentence containing all the requested statistics or the raw values can be accessed instead by setting _makeString_ to `False`.

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

    _sentenceString_ : `optional [bool]`

    >Default `False` : if `True` the returned string is a sentce, otherwise each value has a seperate line.

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
            if sentenceString:
                stsData.append("{:G} nodes".format(len(G.nodes())))
            else:
                stsData.append("Nodes: {:G}".format(len(G.nodes())))
        else:
            stsData['nodes'] = len(G.nodes())
    if 'edges' in stats:
        if makeString:
            if sentenceString:
                stsData.append("{:G} edges".format(len(G.edges())))
            else:
                stsData.append("Edges: {:G}".format(len(G.edges())))
        else:
            stsData['edges'] = len(G.edges())
    if 'isolates' in stats:
        if makeString:
            if sentenceString:
                stsData.append("{:G} isolates".format(len(list(nx.isolates(G)))))
            else:
                stsData.append("Isolates: {:G}".format(len(list(nx.isolates(G)))))
        else:
            stsData['isolates'] = len(list(nx.isolates(G)))
    if 'loops' in stats:
        if makeString:
            if sentenceString:
                stsData.append("{:G} self loops".format(len(list(nx.selfloop_edges(G)))))
            else:
                stsData.append("Self loops: {:G}".format(len(list(nx.selfloop_edges(G)))))
        else:
            stsData['loops'] = len(list(nx.selfloop_edges(G)))
    if 'density' in stats:
        if makeString:
            if sentenceString:
                stsData.append("a density of {:G}".format(nx.density(G)))
            else:
                stsData.append("Density: {:G}".format(nx.density(G)))
        else:
            stsData['density'] = nx.density(G)
    if 'transitivity' in stats:
        if makeString:
            if sentenceString:
                stsData.append("a transitivity of {:G}".format(nx.transitivity(G)))
            else:
                stsData.append("Transitivity: {:G}".format(nx.transitivity(G)))
        else:
            stsData['transitivity'] = nx.transitivity(G)
    if makeString:
        if sentenceString:
            retString = "The graph has "
            if len(stsData) < 1:
                return retString
            elif len(stsData) == 1:
                return retString + stsData[0]
            else:
                return retString + ', '.join(stsData[:-1]) + ' and ' + stsData[-1]
        else:
            return '\n'.join(stsData)
    else:
        retLst = []
        for sts in stats:
            retLst.append(stsData[sts])
        return tuple(retLst)
