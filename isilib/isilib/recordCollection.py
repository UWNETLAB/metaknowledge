#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import isilib
from .record import Record, BadISIFile
from .graphHelpers import ProgressBar
from .constants import tagNameConverter, tagsAndNames

import itertools
import os.path

import networkx as nx

class RecordCollection(object):
    def __init__(self, inCollection = None, name = '', extension = ''):
        self.bad = False
        self._repr = name
        if not inCollection:
            if not name:
                self._repr = "empty"
            self._Records = set()
        elif isinstance(inCollection, str):
            if os.path.isfile(inCollection):
                try:
                    if not inCollection.endswith(extension):
                        raise TypeError("extension of input file does not match requested extension")
                    self._repr = os.path.splitext(os.path.split(inCollection)[1])[0]
                    self._Records = set(isiParser(inCollection))
                except BadISIFile as w:
                    self.bad = True
                    self.error = w
            elif os.path.isdir(inCollection):
                if isilib.VERBOSE_MODE:
                    PBar = ProgressBar(0, "Reading files from " + str(inCollection))
                    count = 0
                else:
                    PBar = None
                if extension and not name:
                    if extension[0] == '.':
                        self._repr = extension[1:] + "-files-from-" + os.path.dirname(inCollection)
                    else:
                        self._repr = extension + "-files-from-" + inCollection
                elif not name:
                    self._repr = "files-from-" + inCollection
                self._Records = set()
                flist = []
                for f in os.listdir(inCollection):
                    fullF = os.path.join(os.path.abspath(inCollection), f)
                    if fullF.endswith(extension) and os.path.isfile(fullF):
                        flist.append(fullF)
                for file in flist:
                    if PBar:
                        count += 1
                        PBar.updateVal(count / len(flist), "Reading records from: " + file)
                    else:
                        PBar = None
                    try:
                        self._Records |= set(isiParser(file))
                    except BadISIFile:
                        pass
                    except UnicodeDecodeError:
                        pass
                if PBar:
                    PBar.finish("Done reading records from: " + str(inCollection))
            else:
                raise TypeError("inCollection is not a directory or a file")
        elif isinstance(inCollection, list):
            self._Records = set(inCollection)
        elif isinstance(inCollection, set):
            self._Records = inCollection
        else:
            raise TypeError

    def __add__(self, other):
        if self.bad and other.bad:
            return RecordCollection(set(), '[BAD ' + repr(self) + ']'+ '_plus_' + '[BAD ' +  repr(other) + ']')
        if self.bad:
            return RecordCollection(other._Records, '[BAD ' + repr(self) + ']' + '_plus_' + repr(other))
        elif other.bad:
            return RecordCollection(self._Records,  repr(self) + '[BAD ' + repr(other) + ']')
        else:
            return RecordCollection(self._Records | other._Records, repr(self) + '_plus_' + repr(other))

    def __and__(self, other):
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records & other._Records, repr(self) + '_and_' + repr(other))

    def __sub__(self, other):
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records - other._Records, repr(self) + '_diff_' + repr(other))

    def __xor__(self, other):
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records ^ other._Records, repr(self) + '_symdiff_' + repr(other))

    def __str__(self):
        return "Collection of " + str(len(self._Records)) + " records"

    def __repr__(self):
        return self._repr

    def __lt__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) < len(other)
    def __le__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) <= len(other)
    def __gt__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) > len(other)
    def __ge__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) >= len(other)

    def __eq__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return self._Records == other._Records

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self._Records)

    def __iter__(self):
        for R in self._Records:
            yield R

    def pop(self):
        if len(self._Records) > 0:
            self._repr = "Pop " + self._repr
            return self._Records.pop()
        else:
            return None

    def peak(self):
        if len(self._Records) > 0:
            return self._Records.__iter__().__next__()
        else:
            return None

    def getBadRecords(self):
        badRecords = set()
        for R in self._Records:
            if R.bad:
                badRecords.add(R)
        return RecordCollection(badRecords, repr(self) + '_badRecords')

    def dropBadRecords(self):
        self._Records = {r for r in self._Records if not r.bad}

    def writeFile(self, fname = None):
        if fname:
            f = open(fname, mode = 'w', encoding = 'utf-8')
        else:
            f = open(repr(self)[:200] + '.isi', mode = 'w', encoding = 'utf-8')
        f.write("\ufeffFN Thomson Reuters Web of Science\u2122\n")
        f.write("VR 1.0\n")
        for R in self._Records:
            R.writeRecord(f)
            f.write('\n')
        f.write('EF')
        f.close()

    def coAuthNetwork(self):
        grph = nx.Graph()
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a co-authorship network")
            count = 0
        else:
            PBar = None
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count/ len(self), "Analyzing: " + str(R))
            if R.authorsFull and len(R.authorsFull) > 1:
                for i, auth1 in enumerate(R.authorsFull):
                    if auth1 not in grph:
                        grph.add_node(auth1, count = 1)
                    else:
                        grph.node[auth1]['count'] += 1
                    for auth2 in R.authorsFull[i + 1:]:
                        if auth2 not in grph:
                            grph.add_node(auth2, count = 1)
                        else:
                            grph.node[auth2]['count'] += 1
                        if grph.has_edge(auth1, auth2):
                            grph.edge[auth1][auth2]['weight'] += 1
                        else:
                            grph.add_edge(auth1, auth2, weight = 1)
            if R.authorsFull and len(R.authorsFull) == 1:
                auth1 = R.authorsFull[0]
                if auth1 not in grph:
                    grph.add_node(auth1, count = 1)
                else:
                    grph.node[auth1]['count'] += 1
        if PBar:
            PBar.finish("Done making a co-authorship network")
        return grph

    def coCiteNetwork(self, dropAnon = True, authorship = False, extraInfo = True, weighted = True):
        tmpgrph = nx.Graph()
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a co-citation network")
            count = 0
        else:
            PBar = None
        if authorship:
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count / len(self), "Analyzing: " + str(R))
                Cites = R.citations
                if Cites:
                    if dropAnon:
                        Cites = [c for c in Cites if not c.isAnonymous() and hasattr(c, 'author')]
                    else:
                        Cites = [c for c in Cites if hasattr(c, 'author')]
                    if len(Cites) > 1:
                        for n, c1 in enumerate(Cites):
                            c1Auth = c1.author
                            c2Auths = [c.author for c in Cites[n:]]
                            if weighted:
                                tmpgrph.add_weighted_edges_from(edgeBunchGenerator(c1Auth, c2Auths, weighted = True))
                            else:
                                tmpgrph.add_edges_from(edgeBunchGenerator(c1Auth, c2Auths))
                            if extraInfo and not hasattr(tmpgrph.node[c1Auth], 'info'):
                                tmpgrph.node[c1Auth]['info'] = str(c1)
                    elif len(Cites) == 1:
                        if Cites[0] not in tmpgrph and extraInfo:
                            tmpgrph.add_node(Cites[0].author, info = str(Cites[0]))
                        elif Cites[0] not in tmpgrph:
                            tmpgrph.add_node(Cites[0].author)
        else:
            citesSet = set()
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal((count/ len(self)), "Analyzing: " + str(R))
                Cites = R.citations
                if Cites:
                    if dropAnon:
                        Cites = [c for c in Cites if not c.isAnonymous()]
                    citeHashList = []
                    for cite in Cites:
                        citeHash = hash(cite)
                        if citeHash not in tmpgrph:
                            if cite in citesSet:
                                for c in citesSet:
                                    if cite == c:
                                        citeHash = hash(c)
                            else:
                                citesSet.add(cite)
                                if extraInfo:
                                    tmpgrph.add_node(citeHash, info = str(cite))
                                else:
                                    tmpgrph.add_node(citeHash)
                        citeHashList.append(citeHash)
                    if len(citeHashList) > 1:
                        if weighted:
                            for n, c1 in enumerate(citeHashList):
                                tmpgrph.add_weighted_edges_from(edgeBunchGenerator(c1, citeHashList[n:], weighted = True))
                        else:
                            for n, c1 in enumerate(citeHashList):
                                tmpgrph.add_edges_from(edgeBunchGenerator(c1, citeHashList[n:]))
        if PBar:
            PBar.finish("Done making a co-citation network of " + repr(self))
        return tmpgrph

    def citationNetwork(self, dropAnon = True, authorship = False, extraInfo = True, weighted = True):
        tmpgrph = nx.DiGraph()
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a citation network")
            count = 0
        else:
            PBar = None
        if authorship:
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count/ len(self), "Analyzing: " + str(R))
                reRef = R.createCitation()
                if hasattr(reRef, 'author'):
                    authRef = reRef.author
                    if extraInfo:
                        tmpgrph.add_node(authRef, info = str(reRef))
                    else:
                        tmpgrph.add_node(authRef)
                else:
                    continue
                rCites = R.citations
                if rCites:
                    rCites = [c for c in R.citations if hasattr(c, 'author')]
                    rCitesAuths = [c.author for c in rCites]
                    if extraInfo:
                        for i in range(len(rCites)):
                            if rCitesAuths[i] not in tmpgrph:
                                tmpgrph.add_node(rCitesAuths[i], info = str(rCites[i]))
                    if weighted:
                        tmpgrph.add_weighted_edges_from(edgeBunchGenerator(authRef, rCitesAuths, weighted = True))
                    else:
                        tmpgrph.add_edges_from(edgeBunchGenerator(authRef, rCitesAuths))
            if dropAnon:
                tmpgrph.remove_node("[ANONYMOUS]")
        else:
            citesSet = set()
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count / len(self), "Analyzing: " + str(R))
                reRef = R.createCitation()
                recHash = hash(reRef)
                rCites = R.citations
                if dropAnon and reRef.isAnonymous():
                    continue
                if recHash not in tmpgrph:
                    if reRef in citesSet:
                        for c in citesSet:
                            if reRef == c:
                                recHash = hash(c)
                    else:
                        citesSet.add(reRef)
                        if extraInfo:
                            tmpgrph.add_node(recHash, info = str(reRef))
                        else:
                            tmpgrph.add_node(recHash)
                if rCites:
                    rCites = [c for c in rCites if not c.isAnonymous()] if dropAnon else rCites
                    citeHashs = []
                    for refCite in rCites:
                        citeHash = hash(refCite)
                        if citeHash not in tmpgrph:
                            if refCite in citesSet:
                                for c in citesSet:
                                    if refCite == c:
                                        citeHash = hash(c)
                            else:
                                citesSet.add(refCite)
                                if extraInfo:
                                    tmpgrph.add_node(citeHash, info = str(refCite))
                                else:
                                    tmpgrph.add_node(citeHash)
                        citeHashs.append(citeHash)
                    if weighted:
                        tmpgrph.add_weighted_edges_from(edgeBunchGenerator(recHash, citeHashs, weighted = True))
                    else:
                        tmpgrph.add_edges_from(edgeBunchGenerator(recHash, citeHashs))
        if PBar:
            PBar.finish("Done making a citation network of " + repr(self))
        return tmpgrph

    def extractTagged(self, taglist):
        recordsWithTags = set()
        for R in self:
            for t in taglist:
                hasTags = True
                if t not in R.tags:
                    hasTags = False
                    break
            if hasTags:
                recordsWithTags.add(R)
        return RecordCollection(recordsWithTags, repr(self) + "_tags(" + ','.join(taglist) + ')')

    def yearSplit(self, startYear, endYear):
        recordsInRange = set()
        for R in self._Records:
            if R.year >= startYear and R.year <= endYear:
                recordsInRange.add(R)
        return RecordCollection(recordsInRange, repr(self) + "_(" + str(startYear) + " ," + str(endYear) + ")")

    def oneModeNetwork(self, mode, nodeCount = True, edgeWeight = True):
        if mode not in tagsAndNames:
            raise TypeError(mode + "is not a known tag, or the name of a known tag.")
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a one mode network with " + mode)
            count = 0
        else:
            PBar = None
        grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents = getattr(R, mode, None)
            if contents:
                if isinstance(contents, list):
                    tmplst = [str(n) for n in contents]
                    if len(tmplst) > 1:
                        for i, node1 in enumerate(tmplst):
                            for node2 in tmplst[i + 1:]:
                                if edgeWeight:
                                    try:
                                        grph.edge[node1][node2]['weight'] += 1
                                    except KeyError:
                                        grph.add_edge(node1, node2, weight = 1)
                                else:
                                    if not grph.has_edge(node1, node2):
                                        grph.add_edge(node1, node2)
                            if nodeCount:
                                try:
                                    grph.node[node1]['count'] += 1
                                except KeyError:
                                    grph.node[node1]['count'] = 1
                            else:
                                if not grph.has_node(node1):
                                    grph.add_node(node1)
                    elif len(tmplst) == 1:
                        if nodeCount:
                            try:
                                grph.node[tmplst[0]]['count'] += 1
                            except KeyError:
                                grph.add_node(tmplst[0], count = 1)
                        else:
                            if not grph.has_node(tmplst[0]):
                                grph.add_node(tmplst[0])
                    else:
                        pass
                else:
                    nodeVal = str(contents)
                    if nodeCount:
                        try:
                            grph.node[nodeVal]['count'] += 1
                        except KeyError:
                            grph.add_node(nodeVal, count = 1)
                    else:
                        if not grph.has_node(nodeVal):
                            grph.add_node(nodeVal)
        if PBar:
            PBar.finish("Done making a one mode network with " + mode)
        return grph

    def twoModeNetwork(self, tag1, tag2, directed = False, recordType = True, nodeCount = True, edgeWeight = True):
        if (not tag1 in tagsAndNames) or (not tag2 in tagsAndNames):
            raise TypeError(str(tag1) + " or " + str(tag2) + "is not a known tag, or the name of a known tag.")
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a two mode network of " + tag1 + " and " + tag2)
            count = 0
        else:
            PBar = None
        if directed:
            grph = nx.DiGraph()
        else:
            grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents1 = getattr(R, tag1, None)
            contents2 = getattr(R, tag2, None)
            if isinstance(contents1, list):
                contents1 = [str(v) for v in contents1]
            elif contents1 == None:
                contents1 = []
            else:
                contents1 = [str(contents1)]
            if isinstance(contents2, list):
                contents2 = [str(v) for v in contents2]
            elif contents2 == None:
                contents2 = []
            else:
                contents2 = [str(contents2)]
            for node1 in contents1:
                for node2 in contents2:
                    if edgeWeight:
                        try:
                            grph.edge[node1][node2]['weight'] += 1
                        except KeyError:
                            grph.add_edge(node1, node2, weight = 1)
                    else:
                        if not grph.has_edge(node1, node2):
                            grph.add_edge(node1, node2)
                if nodeCount:
                    try:
                        grph.node[node1]['count'] += 1
                    except KeyError:
                        try:
                            grph.node[node1]['count'] = 1
                            if recordType:
                                grph.node[node1]['type'] = tag1
                        except KeyError:
                            if recordType:
                                grph.add_node(node1, type = tag1)
                            else:
                                grph.add_node(node1)
                else:
                    if not grph.has_node(node1):
                        if recordType:
                            grph.add_node(node1, type = tag1)
                        else:
                            grph.add_node(node1)
                    elif recordType:
                        try:
                            grph.node[node1]['type'] += tag1
                        except KeyError:
                            grph.node[node1]['type'] = tag1

            for node2 in contents2:
                if nodeCount:
                    try:
                        grph.node[node2]['count'] = 1
                    except KeyError:
                        try:
                            grph.node[node2]['count'] = 1
                        except KeyError:
                            grph.add_node(node2, count = 1)
                            if recordType:
                                grph.node[node2]['type'] = tag2
                else:
                    if not grph.has_node(node2):
                        if recordType:
                            grph.add_node(node2, type = tag2)
                        else:
                            grph.add_node(node2)
                    elif recordType:
                        try:
                            grph.node[node2]['type'] = tag2
                        except KeyError:
                            grph.node[node2]['type'] = tag2
        if PBar:
            PBar.finish("Done making a two mode network of " + tag1 + " and " + tag2)
        return grph

    def nModeNetwork(self, tags, recordType = True, nodeCount = True, edgeWeight = True):
        for t in tags:
            if t not in tagsAndNames:
                raise TypeError(str(t) + " is not a known tag, or the name of a known tag.")
        if isilib.VERBOSE_MODE:
            PBar = ProgressBar(0, "Starting to make a " + str(len(tags)) + "-mode network of: " + ', '.join(tags))
            count = 0
        else:
            PBar = None
        grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents = []
            for t in tags:
                tmpVal = getattr(R, t, None)
                if tmpVal:
                    if isinstance(tmpVal, list):
                        contents.append((t, [str(v) for v in tmpVal]))
                    else:
                        contents.append((t, [str(tmpVal)]))
            for i, vlst1 in enumerate(contents):
                for node1 in vlst1[1]:
                    for vlst2 in contents[i + 1:]:
                        for node2 in vlst2[1]:
                            if edgeWeight:
                                try:
                                    grph.edge[node1][node2]['weight'] += 1
                                except KeyError:
                                    grph.add_edge(node1, node2, weight = 1)
                            else:
                                if not grph.has_edge(node1, node2):
                                    grph.add_edge(node1, node2)
                    if nodeCount:
                        try:
                            grph.node[node1]['count'] += 1
                        except KeyError:
                            try:
                                grph.node[node1]['count'] = 1
                                if recordType:
                                    grph.node[node1]['type'] = vlst1[0]
                            except KeyError:
                                if recordType:
                                    grph.add_node(node1, type = vlst1[0])
                                else:
                                    grph.add_node(node1)
                    else:
                        if not grph.has_node(node1):
                            if recordType:
                                grph.add_node(node1, type = vlst1[0])
                            else:
                                grph.add_node(node1)
                        elif recordType:
                            try:
                                grph.node[node1]['type'] += vlst1[0]
                            except KeyError:
                                grph.node[node1]['type'] = vlst1[0]
        if PBar:
            PBar.finish("Done making a " + str(len(tags)) + "-mode network of: " +  ', '.join(tags))
        return grph

def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
    Each it finds is used to initialize a Record then all Record are returned as a list.
    """
    try:
        openfile = open(isifile, 'r')
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    f = enumerate(openfile, start = 0)
    try:
        if "VR 1.0" not in f.__next__()[1] and "VR 1.0" not in f.__next__()[1]:
            openfile.close()
            raise BadISIFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
    except StopIteration as e:
        openfile.close()
        raise BadISIFile("File ends before EF found")
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    notEnd = True
    plst = []
    while notEnd:
        try:
            line = f.__next__()
        except StopIteration as e:
            raise BadISIFile("File ends before EF found")
        if not line[1]:
            raise BadISIFile("No ER found in " + isifile)
        elif line[1].isspace():
            continue
        elif 'EF' in line[1][:2]:
            notEnd = False
            continue
        else:
            try:
                plst.append(Record(itertools.chain([line], f), isifile, line[0]))
            except BadISIFile as w:
                try:
                    s = f.__next__()[1]
                    while s[:2] != 'ER':
                        s = f.__next__()[1]
                except:
                    raise BadISIFile(str(w) + " could not be resolved")
            except Exception as e:
                openfile.close()
                raise e
    try:
        f.__next__()
        raise BadISIFile("EF not at end of " + isifile)
    except StopIteration as e:
        pass
    finally:
        openfile.close()
    return plst

def getCoCiteIDs(clst):
    """
    Creates a dict of the ID-extra information pairs for a CR tag.
    """
    idDict = {}
    for c in clst:
        cId = c.getID()
        if cId not in idDict:
            idDict[cId] = c.getExtra()
    return idDict

def edgeBunchGenerator(base, nodes, weighted = False, reverse = False):
    """
    A helper function for generating a bunch of edges from 1 node base to a list of nodes nodes.
    """
    if weighted and reverse:
        for n in nodes:
            yield (n, base, 1)
    elif weighted:
        for n in nodes:
            yield (base, n, 1)
    elif reverse:
        for n in nodes:
            yield (n, base)
    else:
        for n in nodes:
            yield (base, n)

def edgeNodeReplacerGenerator(base, nodes, loc):
    """
    A helper function for replacing an element of nodes at loc with base
    """
    for n in nodes:
        tmpN = list(n)
        tmpN[loc] = base
        yield tmpN
