import isilib

import networkx as nx
import csv
import os
import sys
import time
import math

def read_graph(edgeList, nodeList = None, directed = False, idKey = 'ID', eSource = 'From', eDest = 'To'):
    """
    Reads the files given by edgeList and if given nodeList and produces a networkx graph
    This is designed only for the files produced by isilib and is meant to be the reverse of write_graph()

    nodeList must be given if any of the attributes of the node are needed
    directed controls if the resultant graph is directional eSource and eDest control the direction
    idKey, eSource and  eDest are the labels for the edge's id, source and destination respectively, they must match headers in the file or a keyError exception will be thrown
    """
    if isilib.VERBOSE_MODE:
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

def write_graph(grph, name, edgeInfo = True, typing = True, suffix = 'csv', overwrite = False):
    """
    Writes both the edge list and the node attribute list of grph.
    The output files start with name, the file type[edgeList, nodeAttributes] then if typing is True the type of graph (directed or undirected) then the suffix, it appears as follows:
        name_fileType_Graphtype.suffix
    If edgeInfo is true the extra information about the edges will be included in their list, i.e. their weight will be given
    If overwrite is False write_graph will throw an exception if either of the files it is attempting to write exist
    """
    if isilib.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Writing graphs: " + name)
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
    write_edgeList(grph, edgeListName, extraInfo = edgeInfo, progBar = PBar)
    if PBar:
        PBar.jumpUp()
    write_nodeAttributeFile(grph, nodesAtrName, progBar = PBar)
    if PBar:
        PBar.finish(str(len(grph.nodes())) + " nodes and " + str(len(grph.edges())) + " edges written to file")

def write_edgeList(grph, name, extraInfo = True, progBar = None):
    """
    writes an edge list of grph with filename name, if extraInfo is true the additional information about the edges, e.g. weight, will be written.
    All edges must have the same tags
    """
    if progBar:
        count = 0
        eMax = len(grph.edges(data = True))
        if isinstance(progBar, _ProgressBar):
            progBar.updateVal(0, "Writing edge list " + name)
        else:
            progBar = _ProgressBar(0, "Writing edge list " + name)
    if len(grph.edges(data = True)) < 1:
        outFile = open(name, 'w')
        outFile.write('"From","To"\n')
        outFile.close()
        if progBar:
            progBar.updateVal(1, "Done edge list " + name + ", 0 edges written.")
    else:
        if extraInfo:
            csvDict = ['From'] +  ['To'] + list(grph.edges_iter(data = True).__next__()[2].keys())
        else:
            csvDict = ['From'] +  ['To']
        f = open(name, 'w')
        outFile = csv.DictWriter(f, csvDict, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_ALL)
        outFile.writeheader()
        if extraInfo:
            for e in grph.edges_iter(data = True):
                if progBar:
                    count += 1
                    if count % 10000 == 0:
                        progBar.updateVal(count / eMax)
                eDict = e[2].copy()
                eDict['From'] = e[0]
                eDict['To'] = e[1]
                try:
                    outFile.writerow(eDict)
                except ValueError:
                    raise ValueError("Some edges in " + str(grph) + " do not have the same attributes")
        else:
            for e in grph.edges_iter():
                if progBar:
                    count += 1
                    if count % 100 == 0:
                        progBar.updateVal(count / eMax)
                eDict['From'] = e[0]
                eDict['To'] = e[1]
                outFile.writerow(eDict)
        if progBar:
            progBar.finish("Done edge list " + name + ", " + str(count) + " edges written.")
        f.close()

def write_nodeAttributeFile(grph, name, progBar = None):
    """
    writes a node attribute list of grph with filename name, the first column is the node's ID then all after it are its associated information.
    All nodes must have the same tags.
    """
    if progBar:
        count = 0
        nMax = len(grph.nodes())
        if isinstance(progBar, _ProgressBar):
            progBar.updateVal(0, "Writing edgelist " + name)
        else:
            progBar = _ProgressBar(0, "Writing edgelist " + name)
    if len(grph.nodes(data = True)) < 1:
        outFile = open(name, 'w')
        outFile.write('ID\n')
        outFile.close()
        if progBar:
            progBar.updateVal(1, "Done node attribute list: " + name + ", 0 nodes written.")
    else:
        csvDict = ['ID'] + list(grph.nodes_iter(data = True).__next__()[1].keys())
        f = open(name, 'w')
        outFile = csv.DictWriter(f, csvDict, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_ALL)
        outFile.writeheader()
        for n in grph.nodes_iter(data = True):
            if progBar:
                count += 1
                if count % 50 == 0:
                    progBar.updateVal(count / nMax)
            nDict = n[1].copy()
            nDict['ID'] = n[0]
            try:
                outFile.writerow(nDict)
            except ValueError:
                raise ValueError("Some nodes in " + str(grph) + " do not have the same attributes")
        if progBar:
            progBar.updateVal(1, "Done node attribute list: " + name + ", " + str(count) + " nodes written.")
        f.close()

class _ProgressBar(object):
    difTermAndBar = 8 #the number of characters difference between the bar's length and the terminal's width
    timeLength = 6 # width of elapse time display
    def __init__(self, initPer, initString = ' ', output = sys.stdout):
        self.finished = False
        self.per = initPer
        self.out = output
        self.sTime = time.time()
        try:
            self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
            if self.barMaxLength < 0:
                self.barMaxLength = 0
        except OSError:
            self.barMaxLength = 80 - self.difTermAndBar
        self.dString = self.prepString(initString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength)
        self.out.write('[' + ' ' * self.barMaxLength + ']' + '{:.1%}'.format(self.per).rjust(6, ' ') + '\n')
        self.out.write(self.dString + '\033[F')
        self.out.flush()

    def __del__(self):
        if not self.finished:
            self.out.write('\n\n')
            self.out.flush()

    def updateVal(self, inputPer, inputString = None):
        try:
            self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
            if self.barMaxLength < 0:
                self.barMaxLength = 0
        except OSError:
            self.barMaxLength = 80 - self.difTermAndBar
        self.out.write('\r')
        self.per = inputPer
        percentString = '{:.1%}'.format(self.per).rjust(6, ' ')
        barLength = int(self.per * self.barMaxLength)
        if inputString:
            self.dString = self.prepString(inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength)
            if barLength >= self.barMaxLength:
                self.out.write('[' + '=' * barLength + ']' + percentString)
                self.out.write('\n' + self.dString + '\033[F')
            else:
                self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString)
                self.out.write('\n' + self.dString + '\033[F')
        else:
            if barLength >= self.barMaxLength:
                self.out.write('[' + '=' * barLength + ']' + percentString + '\r')
            else:
                self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString + '\r')
        self.out.flush()

    def finish(self, inputString):
        self.finished = True
        inputString = str(inputString)
        try:
            self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
            if self.barMaxLength < 0:
                self.barMaxLength = 0
        except OSError:
            self.barMaxLength = 80 - self.difTermAndBar
        self.out.write('\n' + ' ' * (self.barMaxLength + self.difTermAndBar) + '\033[F')
        if len(inputString) < self.barMaxLength + self.difTermAndBar - self.timeLength:
            tString = self.prepTime(time.time() - self.sTime, self.barMaxLength + self.difTermAndBar - len(inputString) - 1)
            self.out.write(inputString + ' ' + tString)
        else:
            self.out.write(self.prepString(inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength))
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

def drop_edges(grph, minWeight = -float('inf'), maxWeight = float('inf'), parameterName = 'weight', ignoreUnweighted = False):
    """
    Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

    minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

    parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

    ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored
    """
    if isilib.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Dropping edges")
        count = 0
        total = len(grph.edges())
    else:
        PBar = None
    tmpGrph = grph.copy()
    for e in grph.edges_iter(data = True):
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
                    PBar.updateVal(count/ total, str(count) + " edges analysed and " + str(total -len(tmpGrph.edges())) + " edges dropped")
            if val > maxWeight or  val < minWeight:
                tmpGrph.remove_edge(e[0], e[1])
    if PBar:
        PBar.finish(str(total -len(tmpGrph.edges())) + " edges out of " + str(total) + " dropped, " + str(len(tmpGrph.edges())) + " returned")
    return tmpGrph

def drop_nodesByDegree(grph, minDegree = -float('inf'), maxDegree = float('inf'), useWeight = False, parameterName = 'weight', ignoreUnweighted = False):
    """
    Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

    minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

    useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

    parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

    ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True
    """
    if isilib.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Dropping nodes by degree")
        count = 0
        total = len(grph.nodes())
    else:
        PBar = None
    goodNodes = []
    for n in grph.nodes_iter():
        if PBar:
            count += 1
            if count % 10000 == 0:
                PBar.updateVal(count/ total, str(count) + "nodes analysed and " + str(total - len(goodNodes)) + " nodes dropped")
        val = 0
        if useWeight:
            for e in grph.edges(n, data = True):
                try:
                    val += e[2][parameterName]
                except KeyError:
                    if not ignoreUnweighted:
                        raise KeyError("One or more Edges do not have weight or " + str(parameterName), " is not the name of the weight")
                    else:
                        pass
        else:
            val = len(grph.edges(n))
        if val <= maxDegree and val >= minDegree:
            goodNodes.append(n)
    if PBar:
        PBar.finish(str(total - len(goodNodes)) + " nodes out of " + str(total) + " dropped, " + str(len(goodNodes)) + " returned")
    return grph.subgraph(goodNodes)


def drop_nodesByCount(grph, minCount = -float('inf'), maxCount = float('inf'), parameterName = 'count', ignoreMissing = False):
    """
    Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

    minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


    parameterName is key to count field in the node's dictionary, default is count as that is often correct

    ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors
    """
    if isilib.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Dropping nodes by count")
        count = 0
        total = len(grph.nodes())
    else:
        PBar = None
    goodNodes = []
    for n in grph.nodes_iter(data = True):
        if PBar:
            count += 1
            if count % 10000 == 0:
                PBar.updateVal(count/ total, str(count) + "nodes analysed and " + str(total - len(goodNodes)) + " nodes dropped")

        try:
            val = n[1][parameterName]
        except KeyError:
            if not ignoreMissing:
                raise KeyError("One or more nodes do not have counts or " + str(parameterName), " is not the name of the count parameter")
            else:
                pass
        else:
            if val <= maxCount and val >= minCount:
                goodNodes.append(n[0])
    if PBar:
        PBar.finish(str(total - len(goodNodes)) + " nodes out of " + str(total) + " dropped, " + str(len(goodNodes)) + " returned")
    return grph.subgraph(goodNodes)

def graphDensityContourPlot(G, axisSamples = 100, bluring = 10):
    """
    Requires numpy and matplotlib
    """
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.ndimage as ndi
    fig = plt.figure()
    #ax = fig.gca(projection='3d')
    pos = nx.spring_layout(G, scale = axisSamples - 1)
    grid = np.zeros( [axisSamples, axisSamples],dtype=np.float32)
    for v in pos.values():
        x, y = tuple(int(x) for x in v.round(0))
        grid[x][y] += 1
    grid = ndi.gaussian_filter(grid, (bluring, bluring))
    X = Y = np.arange(0, axisSamples, 1)
    x, y = np.meshgrid(X, Y)
    CS = plt.contour(x, y, grid)

    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Simplest default with labels')
    """
    R = np.sin(np.sqrt(X**2 + Y**2))
    ax.plot_surface(X, Y, R)
    ax.set_zlim(0, 1)
    """
    plt.show()
