import isilib

import networkx as nx
import csv
import os
import sys

def read_graph(edgeList, nodeList = None, directed = False, idKey = 'ID', eSource = 'From', eDest = 'To'):
    if isilib.VERBOSE_MODE:
        PBar = ProgressBar(0, "Starting to reading graphs")
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
        PBar.updateVal(1, str(len(grph.nodes())) + " nodes and " + str(len(grph.edges()) + " edges found"))
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
        PBar = ProgressBar(0, "Writing graphs: " + name)
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
    write_nodeAttributeFile(grph, nodesAtrName, progBar = PBar)

def write_edgeList(grph, name, extraInfo = True, progBar = None):
    """
    writes an edge list of grph with filename name, if extraInfo is true the additional information about the edges, e.g. weight, will be written.
    All edges must have the same tags
    """
    if progBar:
        count = 0
        eMax = len(grph.edges(data = True))
        if isinstance(progBar, ProgressBar):
            progBar.updateVal(0, "Writing edge list " + name)
        else:
            progBar = ProgressBar(0, "Writing edge list " + name)
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
            progBar.updateVal(1, "Done edge list " + name + ", " + str(count) + " edges written.")
        f.close()

def write_nodeAttributeFile(grph, name, progBar = None):
    """
    writes a node attribute list of grph with filename name, the first column is the node's ID then all after it are its associated information.
    All nodes must have the same tags.
    """
    if progBar:
        count = 0
        nMax = len(grph.nodes())
        if isinstance(progBar, ProgressBar):
            progBar.updateVal(0, "Writing edgelist " + name)
        else:
            progBar = ProgressBar(0, "Writing edgelist " + name)
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

"""
def drop_edges

def drop_nodes

def louvain
"""

class ProgressBar(object):
    difTermAndBar = 8 #the number of characters difference between the bar's lenght anf the terminal's width
    def __init__(self, initPer, initString = ' ', output = sys.stdout):
        self.per = initPer
        self.out = output
        try:
            self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
            if self.barMaxLength < 0:
                self.barMaxLength = 0
        except OSError:
            self.barMaxLength = 80 - self.difTermAndBar
        self.dString = self.prepString(initString, self.barMaxLength + self.difTermAndBar)
        self.out.write('[' + ' ' * self.barMaxLength + ']' + '{:.1%}'.format(self.per) + '\n')
        self.out.write(self.dString + '\033[F')
        self.out.flush()
    def __del__(self):
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
            self.dString = self.prepString(inputString, self.barMaxLength + self.difTermAndBar)
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

    @staticmethod
    def prepString(s, maxLength):
        sString = str(s)
        if len(sString) <= maxLength:
            return sString.ljust(maxLength, ' ')
        else:
            if maxLength % 2 == 0:
                return sString[:int(maxLength/2 - 3)] + '...' + sString[int(-maxLength/2):]
            else:
                return sString[:int(maxLength/2 - 2)] + '...' + sString[int(-maxLength/2):]
