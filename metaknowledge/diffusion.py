#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import itertools
import networkx as nx

from .WOS.tagProcessing.funcDicts import tagsAndNameSet, normalizeToTag
from .progressBar import _ProgressBar
from .recordCollection import RecordCollection

import metaknowledge

def diffusionGraph(source, target, weighted = True, sourceType = "raw", targetType = "raw", labelEdgesBy = None):
    """Takes in two [RecordCollections](../classes/RecordCollection.html#metaknowledge.RecordCollection) and produces a graph of the citations of _source_ by the [Records](../classes/Record.html#metaknowledge.Record) in _target_. By default the nodes in the are `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords. The edges of the graph go from the target to the source.

    Each node on the output graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

    # Parameters

    _source_ : `RecordCollection`

    > A metaknowledge `RecordCollection` containing the `Records` being cited

    _target_ : `RecordCollection`

    > A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

    _weighted_ : `optional [bool]`

    > Default `True`, if `True` each edge will have an attribute `'weight'` giving the number of times the source has referenced the target.

    _sourceType_ : `optional [str]`

    > Default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes.

    > If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

    _targetType_ : `optional [str]`

    > Default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes.

    > If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

    _labelEdgesBy_ : `optional [str]`

    > Default `None`, if a WOS tag (or long name of WOS tag) then the edges of the output graph will have a attribute `'key'` that is the value of the referenced tag, of source `Record`, i.e. if `'PY'` is given then each edge will have a `'key'` value equal to the publication year of the source.

    > This option will cause the output graph to be an `MultiDiGraph` and is likely to result in parallel edges. If a `Record` has multiple values for at tag (e.g. `'AF'`) the each tag will create its own edge.

    # Returns

    `networkx Directed Graph or networkx multi Directed Graph`

    > A directed graph of the diffusion network, _labelEdgesBy_ is used the graph will allow parallel edges.
    """
    if sourceType != "raw" and sourceType not in tagsAndNameSet:
        raise RuntimeError("{} is not a valid node type, only 'raw' or those strings in tagsAndNameSet are allowed".format(sourceType))
    if targetType != "raw" and targetType not in tagsAndNameSet:
        raise RuntimeError("{} is not a valid node type, only 'raw' or those strings in tagsAndNameSet are allowed".format(targetType))
    if labelEdgesBy is not None:
        try:
            normVal = normalizeToTag(labelEdgesBy)
        except KeyError:
            raise RuntimeError ("{} is not a known tag, only tags in tagsAndNameSet are allowed.".format(labelEdgesBy))
        else:
            labelEdgesBy = normVal
    count = 0
    maxCount = len(source)
    progArgs = (0, "Starting to make a diffusion network")
    if metaknowledge.VERBOSE_MODE:
        progKwargs = {'dummy' : False}
    else:
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        sourceDict = {}
        if labelEdgesBy is None:
            workingGraph = nx.DiGraph()
        else:
            workingGraph = nx.MultiDiGraph()
        for Rs in source:
            if PBar:
                count += 1
                PBar.updateVal(count / maxCount * .25, "Analyzing source: " + str(Rs))
            RsVal, RsExtras = makeNodeID(Rs, sourceType)
            if RsVal:
                sourceDict[Rs.createCitation()] = RsVal
                for val in RsVal:
                    if val not in workingGraph:
                        workingGraph.add_node(val, source = True, target = False, **RsExtras)
        if PBar:
            count = 0
            maxCount = len(target)
            PBar.updateVal(.25, "Done analyzing sources, starting on targets")
        for Rt in target:
            RtVal, RtExtras = makeNodeID(Rt, targetType)
            if labelEdgesBy is not None:
                edgeVals = Rt.get(labelEdgesBy)
                if edgeVals is None:
                    continue
                if not isinstance(edgeVals, list):
                    edgeVals = [edgeVals]
            if PBar:
                count += 1
                PBar.updateVal(count / maxCount * .75 + .25, "Analyzing target: " + str(Rt))
            if RtVal:
                for val in RtVal:
                    if val not in workingGraph:
                        workingGraph.add_node(val, source = False, target = True, **RtExtras)
                    else:
                        workingGraph.node[val]["target"] = True
                    targetCites = Rt.get('CR')
                    if targetCites:
                        for Rs in (sourceDict[c] for c in targetCites if c in sourceDict):
                            for sVal in Rs:
                                if labelEdgesBy is not None:
                                    for edgeVal in (str(ev) for ev in edgeVals):
                                        if weighted:
                                            if workingGraph.has_edge(sVal, val, key = edgeVal):
                                                for i, a in workingGraph[sVal][val].items():
                                                    if a['key'] == edgeVal:
                                                        workingGraph[sVal][val][i]['weight'] += 1
                                                        break
                                            else:
                                                attrDict = {'key' : edgeVal, 'weight' : 1}
                                                workingGraph.add_edge(sVal, val, attr_dict = attrDict)
                                        else:
                                            if not workingGraph.has_edge(sVal, val, key = edgeVal):
                                                workingGraph.add_edge(sVal, val, key = edgeVal)
                                else:
                                    if weighted:
                                        try:
                                            workingGraph[sVal][val]['weight'] += 1
                                        except KeyError:
                                            workingGraph.add_edge(sVal, val, weight = 1)
                                    else:
                                        workingGraph.add_edge(sVal, val)
        if PBar:
            PBar.finish("Done making a diffusion network of {} sources and {} targets".format(len(source), len(target)))
    return workingGraph

def diffusionCount(source, target, sourceType = "raw", extraValue = None, pandasFriendly = False,  compareCounts = False, numAuthors = True, useAllAuthors = True, _ProgBar = None, extraMapping = None):
    """Takes in two [RecordCollections](../classes/RecordCollection.html#metaknowledge.RecordCollection) and produces a `dict` counting the citations of _source_ by the [Records](../classes/Record.html#metaknowledge.Record) of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

    # Parameters

    _source_ : `RecordCollection`

    > A metaknowledge `RecordCollection` containing the `Records` being cited

    _target_ : `RecordCollection`

    > A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

    _sourceType_ : `optional [str]`

    > default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag the keys will be of that type.

    _pandasFriendly_ : `optional [bool]`

    > default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurrence counts as `"Counts"`. The lists are the same length.

    _compareCounts_ : `optional [bool]`

    > default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

    _extraValue_ : `optional [str]`

    > default `None`, if a tag the returned dictionary will have `Records` mapped to maps, these maps will map the entries for the tag to counts. If _pandasFriendly_ is also `True` the resultant dictionary will have an additional column called `'year'`. This column will contain the year the citations occurred, in addition the Records entries will be duplicated for each year they occur in.

    > For example if `'year'` was given then the count for a single `Record` could be `{1990 : 1, 2000 : 5}`

    _useAllAuthors_ : `optional [bool]`

    > default `True`, if `False` only the first author will be used to generate the `Citations` for the _source_ `Records`

    # Returns

    `dict[:int]`

    > A dictionary with the type given by _sourceType_ as keys and integers as values.

    > If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

    > If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labeled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.
    """
    sourceCountString = "SourceCount"
    targetCountString = "TargetCount"
    if not isinstance(sourceType, str):
        raise RuntimeError("{} is not a valid node type, only tags or the string 'raw' are allowed".format(sourceType))
    if not isinstance(source, RecordCollection) or not isinstance(target, RecordCollection):
        raise RuntimeError("Source and target must be RecordCollections.")
    if extraValue is not None and not isinstance(extraValue, str):
        raise RuntimeError("{} is not a valid extraValue, only tags are allowed".format(extraValue))
    if extraMapping is None:
        extraMapping = lambda x : x
    if metaknowledge.VERBOSE_MODE or _ProgBar:
        if _ProgBar:
            PBar = _ProgBar
            PBar.updateVal(0, "Starting to analyse a diffusion network")
        else:
            PBar = _ProgressBar(0, "Starting to analyse a diffusion network")
        count = 0
        maxCount = len(source)
    else:
        PBar = _ProgressBar("Starting to analyse a diffusion network", dummy = True)
    count = 0
    maxCount = len(source)
    sourceDict = {}
    #Tells the function if the IDs are made of lists or of str
    listIds = None

    for Rs in source:
        if listIds is None and Rs.get(sourceType) is not None:
            listIds = isinstance(Rs.get(sourceType), list)
        count += 1
        PBar.updateVal(count / maxCount * .10, "Analyzing source: " + str(Rs))
        RsVal, RsExtras = makeNodeID(Rs, sourceType)
        if RsVal:
            if useAllAuthors:
                for c in Rs.createCitation(multiCite = True):
                    sourceDict[c] = RsVal
            else:
                sourceDict[Rs.createCitation()] = RsVal
    if extraValue is not None:
        if listIds:
            sourceCounts = {s : {targetCountString : 0} for s in itertools.chain.from_iterable(sourceDict.values())}
        else:
            sourceCounts = {s : {targetCountString : 0} for s in sourceDict.values()}
    else:
        if listIds:
            sourceCounts = {s : 0 for s in itertools.chain.from_iterable(sourceDict.values())}
        else:
            sourceCounts = {s : 0 for s in sourceDict.values()}
    count = 0
    maxCount = len(target)
    PBar.updateVal(.10, "Done analyzing sources, starting on targets")
    for Rt in target:
        count += 1
        PBar.updateVal(count / maxCount * .90 + .10, "Analyzing target: {}".format(Rt))
        targetCites = Rt.get('citations', [])
        if extraValue is not None:
            values = Rt.get(extraValue, [])
            if values is None:
                values = []
            elif not isinstance(values, list):
                values = [values]
            values = [extraMapping(val) for val in values]
        for c in  targetCites:
            try:
                RsourceVals = sourceDict[c]
            except KeyError:
                continue
            if listIds:
                for sVal in RsourceVals:
                    if extraValue:
                        sourceCounts[sVal][targetCountString] += 1
                        for val in values:
                            try:
                                sourceCounts[sVal][val] += 1
                            except KeyError:
                                sourceCounts[sVal][val] = 1
                    else:
                        sourceCounts[sVal] += 1
            else:
                if extraValue:
                    sourceCounts[RsourceVals][targetCountString] += 1
                    for val in values:
                        try:
                            sourceCounts[RsourceVals][val] += 1
                        except KeyError:
                            sourceCounts[RsourceVals][val] = 1
                else:
                    sourceCounts[RsourceVals] += 1
    if compareCounts:
        localCounts = diffusionCount(source, source, sourceType = sourceType, pandasFriendly = False,  compareCounts = False, extraValue = extraValue, _ProgBar = PBar)
    if PBar and not _ProgBar:
        PBar.finish("Done counting the diffusion of {} sources into {} targets".format(len(source), len(target)))
    if pandasFriendly:
        retDict = {targetCountString : []}
        if numAuthors:
            retDict["numAuthors"] = []
        if compareCounts:
            retDict[sourceCountString] = []
        if extraValue is not None:
            retDict[extraValue] = []
        if sourceType == 'raw':
            retrievedFields = []
            targetCount = []
            for R in sourceCounts.keys():
                tagsLst = [t for t in R.keys() if t not in retrievedFields]
                retrievedFields += tagsLst
            for tag in retrievedFields:
                retDict[tag] = []
            for R, occ in sourceCounts.items():
                if extraValue:
                    Rvals = R.subDict(retrievedFields)
                    for extraVal, occCount in occ.items():
                        retDict[extraValue].append(extraVal)
                        if numAuthors:
                            retDict["numAuthors"].append(len(R.get('authorsShort')))
                        for tag in retrievedFields:
                            retDict[tag].append(Rvals[tag])
                        retDict[targetCountString].append(occCount)
                        if compareCounts:
                            try:
                                retDict[sourceCountString].append(localCounts[R][extraVal])
                            except KeyError:
                                retDict[sourceCountString].append(0)
                else:
                    Rvals = R.subDict(retrievedFields)
                    if numAuthors:
                        retDict["numAuthors"].append(len(R.get('authorsShort')))
                    for tag in retrievedFields:
                        retDict[tag].append(Rvals[tag])
                    retDict[targetCountString].append(occ)
                    if compareCounts:
                        retDict[sourceCountString].append(localCounts[R])
        else:
            countLst = []
            recLst = []
            locLst = []
            if extraValue:
                extraValueLst = []
            for R, occ in sourceCounts.items():
                if extraValue:
                    for extraVal, occCount in occ.items():
                        countLst.append(occCount)
                        recLst.append(R)
                        extraValueLst.append(extraVal)
                        if compareCounts:
                            try:
                                locLst.append(localCounts[R][extraValue])
                            except KeyError:
                                locLst.append(0)
                else:
                    countLst.append(occ)
                    recLst.append(R)
                    if compareCounts:
                        locLst.append(localCounts[R])
            if compareCounts:
                retDict = {sourceType : recLst, targetCountString : countLst, sourceCountString : locLst}
            else:
                retDict = {sourceType : recLst, targetCountString : countLst}
            if extraValue:
                retDict[extraValue] = extraValueLst
        return retDict
    else:
        if compareCounts:
            for R, occ in localCounts.items():
                sourceCounts[R] = (sourceCounts[R], occ)
        return sourceCounts

def makeNodeID(Rec, ndType, extras = None):
    """Helper to make a node ID, extras is currently not used"""
    if ndType == 'raw':
        recID = Rec
    else:
        recID = Rec.get(ndType)
    if recID is None:
        pass
    elif isinstance(recID, list):
        recID = tuple(recID)
    else:
        recID = recID
    extraDict = {}
    if extras:
        for tag in extras:
            if tag == "raw":
                extraDict['Tag'] = Rec
            else:
                extraDict['Tag'] = Rec.get(tag)
    return recID, extraDict

def diffusionAddCountsFromSource(grph, source, target, nodeType = 'citations', extraType = None, diffusionLabel = 'DiffusionCount', extraKeys = None, countsDict = None, extraMapping = None):
    """Does a diffusion using [diffusionCount()](#metaknowledge.diffusion.diffusionCount) and updates _grph_ with it, using the nodes in the graph as keys in the diffusion, i.e. the source. The name of the attribute the counts are added to is given by _diffusionLabel_. If the graph is not composed of citations from the source and instead is another tag _nodeType_ needs to be given the tag string.

    # Parameters

    _grph_ : `networkx Graph`

    > The graph to be updated

    _source_ : `RecordCollection`

    > The `RecordCollection` that created _grph_

    _target_ : `RecordCollection`

    > The `RecordCollection` that will be counted

    _nodeType_ : `optional [str]`

    > default `'citations'`, the tag that constants the values used to create _grph_

    # Returns

    `dict[:int]`

    > The counts dictioanry used to add values to _grph_. *Note* _grph_ is modified by the function and the return is done in case you need it.
    """
    progArgs = (0, "Starting to add counts to graph")
    if metaknowledge.VERBOSE_MODE:
        progKwargs = {'dummy' : False}
    else:
        progKwargs = {'dummy' : True}
    with _ProgressBar(*progArgs, **progKwargs) as PBar:
        PBar.updateVal(0, 'Getting counts')
        if countsDict is None:
            countsDict = diffusionCount(source, target, sourceType = nodeType, extraValue = extraType, _ProgBar = PBar, extraMapping = extraMapping)
        try:
            if not isinstance(countsDict.keys().__iter__().__next__(), str):
                PBar.updateVal(.5, "Prepping the counts")
                newCountsDict = {}
                while True:
                    try:
                        k, v = countsDict.popitem()
                    except KeyError:
                        break
                    newCountsDict[str(k)] = v
                countsDict = newCountsDict
        except StopIteration:
            pass
        count = 0
        for n in grph.nodes_iter():
            PBar.updateVal(.5 + .5 * (count / len(grph)), "Adding count for '{}'".format(n))
            if extraType is not None:
                if extraKeys:
                    for key in extraKeys:
                        grph.node[n][key] = 0
                grph.node[n][diffusionLabel] = 0
                try:
                    for k, v in countsDict[n].items():
                        if k == 'TargetCount':
                            grph.node[n][diffusionLabel] = v
                        else:
                            if k:
                                grph.node[n][k] = v
                except KeyError:
                    grph.node[n][diffusionLabel] = 0
            else:
                grph.node[n][diffusionLabel] = countsDict.get(n, 0)
            count += 1
        PBar.finish("Done adding diffusion counts to a graph")
    return countsDict
