"""
"""
from .constants import tagsAndNames
import networkx as nx

def diffusionNetwork(source, target, sourceType = "raw", targetType = "raw"):
    """Takes in two [`RecordCollections`](#recordCollection.RecordCollection) and produces a graph of the citations of the `Records` of _source_ by the `Records` of _target_. By default the graph is of `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords.

    Each node on the graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

    # Parameters

    _source_ : `RecordCollection`

    >A metaknowledge `RecordCollection` containing the `Records` being cited

    _target_ : `RecordCollection`

    >A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

    _sourceType_ : `str`

    >default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

    _targetType_ : `str`

    >default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

    # Returns

    `networkx Directed Graph`

    >A directed graph of the diffusion network
    """

    if sourceType != "raw" and sourceType not in tagsAndNames:
        raise RuntimeError("{} is not a valid node type, only 'raw' or those strings in tagsAndNames are allowed".format(nodeType))
    if targetType != "raw" and targetType not in tagsAndNames:
        raise RuntimeError("{} is not a valid node type, only 'raw' or those strings in tagsAndNames are allowed".format(nodeType))
    sourceDict = {}
    workingGraph = nx.DiGraph()
    for Rs in source:
        RsVal, RsExtras = makeNodeID(Rs, sourceType)
        if RsVal:
            sourceDict[Rs.createCitation()] = RsVal
            for val in RsVal:
                if val not in workingGraph:
                    workingGraph.add_node(val, source = True, target = False, **RsExtras)
    for Rt in target:
        RtVal, RtExtras = makeNodeID(Rt, targetType)
        if RtVal:
            for val in RtVal:
                if val not in workingGraph:
                    workingGraph.add_node(val, source = False, target = True, **RtExtras)
                else:
                    workingGraph.node[val]["target"] = True
                for Rs in (sourceDict[c] for c in Rt.CR if c in sourceDict):
                    for sVal in Rs:
                        workingGraph.add_edge(val, sVal)
    return workingGraph


def diffusionCounts(source, target):
    pass

def makeNodeID(Rec, ndType, extras = None):
    """Helper to make a node ID, extras is currently not used"""
    if ndType == 'raw':
        recID = Rec
    else:
        recID =  getattr(Rec, ndType)
    if recID is None:
        pass
    elif isinstance(recID, list):
        recID = tuple(recID)
    else:
        recID = (recID, )
    extraDict = {}
    if extras:
        for tag in extras:
            if tag == "raw":
                extraDict[Tag] = Rec
            else:
                extraDict[Tag] = getattr(Rec, tag)
    return recID, extraDict
