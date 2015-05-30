#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import isilib
from .record import Record, BadISIRecord, BadISIFile
from .graphHelpers import ProgressBar

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
                        raise TypeError("extension of input file doess not match requested extension")
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
                PBar.updateVal(count/ len(self), "Analysing: " + str(R))
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
            PBar.updateVal(1, "Done making a co-authorship network")
        del PBar
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
                    PBar.updateVal(count / len(self), "Analysing: " + str(R))
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
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal((count/ len(self) * .5), "Analysing: " + str(R))
                Cites = R.citations
                if Cites:
                    if dropAnon:
                        Cites = [c for c in Cites if not c.isAnonymous()]
                    if len(Cites) > 1:
                        if weighted:
                            for n, c1 in enumerate(Cites):
                                tmpgrph.add_weighted_edges_from(edgeBunchGenerator(c1, Cites[n:], weighted = True))
                        else:
                            for n, c1 in enumerate(Cites):
                                tmpgrph.add_edges_from(edgeBunchGenerator(c1, Cites[n:]))
                    elif len(Cites) == 1:
                        if Cites[0] not in tmpgrph:
                            tmpgrph.add_node(Cites[0])
            if PBar:
                count = 0
                cMax = len(tmpgrph.nodes())
            for n in tmpgrph.nodes():
                if PBar:
                    count += 1
                    if count % 50 == 0:
                        PBar.updateVal((count/cMax) *.5 + .5, "Hashing: " + str(n))
                newN = hash(n)
                if extraInfo:
                    tmpgrph.add_node(newN, info=str(n))
                else:
                    tmpgrph.add_node(newN)
                if weighted:
                    tmpgrph.add_weighted_edges_from(edgeNodeReplacerGenerator(newN, tmpgrph.edges(n, data = True), 0))
                else:
                    tmpgrph.add_edges_from(edgeNodeReplacerGenerator(newN, tmpgrph.edges(n, data = True), 0))
                tmpgrph.remove_node(n)
        if PBar:
            PBar.updateVal(1, "Done making a co-citation network.")
        del PBar
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
                    PBar.updateVal(count/ len(self), "Analysing: " + str(R))
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
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count / len(self) * .5, "Analysing: " + str(R))
                reRef = R.createCitation()
                rCites = R.citations
                if dropAnon and reRef.isAnonymous():
                    continue
                if rCites:
                    rCites = [c for c in rCites if not c.isAnonymous()] if dropAnon else rCites
                    if weighted:
                        tmpgrph.add_weighted_edges_from(edgeBunchGenerator(reRef, rCites, weighted = True))
                    else:
                        tmpgrph.add_edges_from(edgeBunchGenerator(reRef, rCites))
            if PBar:
                count = 0
                cMax = len(tmpgrph.nodes())
            for n in tmpgrph.nodes():
                if PBar:
                    count += 1
                    if count % 50 == 0:
                        PBar.updateVal((count/cMax) *.5 + .5, "Hashing: " + str(n))
                newN = hash(n)
                if extraInfo:
                    tmpgrph.add_node(newN, info=str(n))
                else:
                    tmpgrph.add_node(newN)
                if weighted:
                    for edg in tmpgrph.in_edges(n, data = True):
                        tmpgrph.add_edge(edg[0], newN, weight = edg[2]['weight'])
                    for edg in tmpgrph.out_edges(n, data = True):
                        tmpgrph.add_edge(newN, edg[1], weight = edg[2]['weight'])
                else:
                    for edg in tmpgrph.in_edges(n, data = True):
                        tmpgrph.add_edge(edg[0], newN)
                    for edg in tmpgrph.out_edges(n, data = True):
                        tmpgrph.add_edge(newN, edg[1])
                tmpgrph.remove_node(n)
        if PBar:
            PBar.updateVal(1, "Done making a citation network")
            del PBar
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

def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reachs EF.
    Each it finds is used to initilize a Record then all Record are returned as a list.
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
        f.next()
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
