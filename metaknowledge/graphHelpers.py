import metaknowledge

import networkx as nx
import csv
import os
import sys
import time
import math
import threading

def read_graph(edgeList, nodeList = None, directed = False, idKey = 'ID', eSource = 'From', eDest = 'To'):
    """Reads the files given by edgeList and if given nodeList. Outputs a networkx graph for the lists.

    This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()](#metaknowledge.write_graph), if this dow not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried.

    The read edge list format assumes the column named _eSource_ (From) is the source node, then the next column _eDest_ (To) givens the destination and all other columns are attributes of the edge, e.g. weight.

    The read nodeList format assumes the column called _idKey_ is the ID of the node as used by the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

    If the names of the columns do not match those given to **read_graph()** a KeyError exception will be raised.

    **Note**: if nodes appear in the edgelist but not the nodeList they will be created with no attributes.

    # Parameters

    _edgeList_ : `str`

    > a string giving the path to the edge list file

    _nodeList_ : `optional [str]`

    > a string giving the path to the node list file

    _directed_ : `optional [bool]`

    > default `False`, if `True` the produced network is directed instead of undirected

    _idKey_ : `optional [str]`

    > default `"ID"`, the name of the ID column in the node list

    _eSource_ : `optional [str]`

    > default `"From"`, the name of the source column in the edge list

    _eDest_ : `optional [str]`

    > default `"To"`, the name of the destination column in the edge list

    # Returns

    `networkx Graph`

    > the Graph described by the files
    """
    if metaknowledge.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Starting to reading graphs")
    else:
        PBar = None
    if directed:
        grph = nx.DiGraph()
    else:
        grph = nx.Graph()
    if nodeList:
        if PBar:
            PBar.updateVal(0, "Reading " + nodeList)
        f = open(nodeList)
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
    if PBar:
        PBar.updateVal(.5, "Reading " + edgeList)
    f = open(edgeList)
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
    if PBar:
        PBar.finish(str(len(grph.nodes())) + " nodes and " + str(len(grph.edges())) + " edges found")
    f.close()
    return grph

def write_graph(grph, name, edgeInfo = True, typing = False, suffix = 'csv', overwrite = True):
    """Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

    The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

    >> name_fileType.suffix

    Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

    To read back these files use [read_graph()](#metaknowledge.read_graph) and to write only one type of lsit use [write_edgeList()](#metaknowledge.write_edgeList) or [write_nodeAttributeFile()](#metaknowledge.write_nodeAttributeFile).

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
    write_edgeList(grph, edgeListName, extraInfo = edgeInfo, _progBar = PBar)
    if PBar:
        PBar.jumpUp()
    write_nodeAttributeFile(grph, nodesAtrName, _progBar = PBar)
    if PBar:
        PBar.finish(str(len(grph.nodes())) + " nodes and " + str(len(grph.edges())) + " edges written to file")

def write_edgeList(grph, name, extraInfo = True, allSameAttribute = False, _progBar = None):
    """Writes an edge list of _grph_ at the destination _name_.

    The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

    **Note**: If any edges are missing an attribute `KeyError` will be raised.

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
        outFile = open(name, 'w')
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
                for n1, n2, attribs in grph.edges_iter(data = True):
                    for key in attribs.keys():
                        if key not in csvHeader:
                            csvHeader.append(key)
                csvHeader += ['From', 'To']
        else:
            csvHeader = ['From'] +  ['To']
        f = open(name, 'w')
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

def write_nodeAttributeFile(grph, name, allSameAttribute = False,_progBar = None):
    """Writes a node attribute list of _grph_ with filename _name_

    The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

    **Note**: If any edges are missing an attribute `KeyError` will be raised.

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
        outFile = open(name, 'w')
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

class _ProgressBar(object):
    difTermAndBar = 8 #the number of characters difference between the bar's length and the terminal's width
    timeLength = 6 # width of elapse time display
    percLength = 6 # width of percent display
    def __init__(self, initPer, initString = ' ', output = sys.stdout, secondRow = False, dummy = False):
        self.dummy = dummy
        self.finished = False
        self.big = secondRow
        self.per = initPer
        self.out = output
        self.inputString = initString
        if not dummy:
            self.sTime = time.time()
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            self.ioThread = threading.Thread(target = self.threadedUpdate, kwargs = {"self" : self})
            self.ioThread.daemon = True
            self.ioThread.start()

    def __bool__(self):
        return not self.dummy

    def __del__(self):
        if not self.dummy and not self.finished:
            self.finished = True
            self.ioThread.join()
            self.out.write('\n')
            self.out.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__del__()

    def updateVal(self, inputPer, inputString = None):
        self.per = inputPer
        if inputString is not None:
            self.inputString = inputString

    def finish(self, inputString):
        if not self.dummy:
            self.finished = True
            self.inputString = str(inputString)
            self.ioThread.join()
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            if self.big:
                self.out.write('\n' + ' ' * (self.barMaxLength + self.difTermAndBar) + '\033[F')
            else:
                self.out.write('\r')
            if len(self.inputString) < self.barMaxLength + self.difTermAndBar - self.timeLength:
                tString = self.prepTime(time.time() - self.sTime, self.barMaxLength + self.difTermAndBar - len(self.inputString) - 1)
                self.out.write(self.inputString + ' ' + tString)
            else:
                self.out.write(self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength))
            self.out.write('\n')
            self.out.flush()

    def jumpUp(self):
        self.out.write('\033[F')
        self.out.flush()

    @staticmethod
    def prepString(s, maxLength):
        maxLength = maxLength - 1
        sString = str(s)
        if len(sString) <= maxLength:
            return sString.ljust(maxLength, ' ') + ' '
        else:
            if maxLength % 2 == 0:
                return sString[:int(maxLength/2 - 3)] + '...' + sString[int(-maxLength/2):] + ' '
            else:
                return sString[:int(maxLength/2 - 2)] + '...' + sString[int(-maxLength/2):] + ' '

    @staticmethod
    def prepTime(t, maxLength):
        try:
            if math.log10(t) + 3.01 > maxLength:
                return "{1:{0}.0E}s".format(maxLength - 1 ,t)
            else:
                return "{1:{0}.1f}s".format(maxLength - 1,t)
        except ValueError:
            return "{1:{0}.1f}s".format(maxLength - 1,t)

    @staticmethod
    def threadedUpdate(self = None):
        while not self.finished:
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            self.out.write('\r')
            percentString = '{:.1%}'.format(self.per).rjust(self.percLength, ' ')
            barLength = int(self.per * self.barMaxLength)
            if self.big and self.inputString:
                    self.dString = self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength)
                    if barLength >= self.barMaxLength:
                        self.out.write('[' + '=' * barLength + ']' + percentString)
                        self.out.write('\n' + self.dString + '\033[F')
                    else:
                        self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString)
                        self.out.write('\n' + self.dString + '\033[')
            elif self.inputString:
                self.dString = self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength - self.percLength - 2) + '[' + self.prepTime(time.time() - self.sTime, self.timeLength) +  ']' + percentString
                self.out.write(self.dString)
            else:
                if barLength >= self.barMaxLength:
                    self.out.write('[' + '=' * barLength + ']' + percentString + '\r')
                else:
                    self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString + '\r')
            self.out.flush()
            time.sleep(.1)

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

def drop_edges(grph, minWeight = - float('inf'), maxWeight = float('inf'), parameterName = 'weight', ignoreUnweighted = False, dropSelfLoops = False):
    """
    Modifies a graph dropping edges whose weight is not within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

    minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

    parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

    ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored
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

def drop_nodesByDegree(grph, minDegree = -float('inf'), maxDegree = float('inf'), useWeight = True, parameterName = 'weight', ignoreUnweighted = True):
    """
    Modifies the graph dropping nodes that do not nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

    minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

    useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

    parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

    ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True
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
                        if not ignoreUnweighted:
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


def drop_nodesByCount(grph, minCount = -float('inf'), maxCount = float('inf'), parameterName = 'count', ignoreMissing = False):
    """
    Modifies a graph dropping nodes that have a occurrence count that is not within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

    minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


    parameterName is key to count field in the node's dictionary, default is count as that is often correct

    ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors
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
    """
    A quick way of merging graphs, this is meant to be quick and is only intended for graphs generated by metaknowledge. This does not check anything and as such may cause unexpected results if the source and target were not generated by the same method. **mergeGraphs**() will modify the first graph, _targetGraph_ by adding the nodes and edges found in the second, _addedGraph_. If a node or edge exists _targetGraph_ is given precedence, but the edge and node attributes given by _incrementedNodeVal_ and incrementedEdgeVal are added instead of being overwritten.
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

    > Default 'nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), a list or tuple containing any number or combination of the strings:

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
