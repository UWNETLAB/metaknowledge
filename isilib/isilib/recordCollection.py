#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from .record import Record

import itertools
import os.path
import networkx as nx

class BadISIFile(Warning):
    """
    Exception thrown by isiParser for mis-formated files
    """
    pass

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
                if extension and not name:
                    if extension[0] == '.':
                        self._repr = extension[1:] + "-files-from-" + inCollection
                    else:
                        self._repr = extension + "-files-from-" + inCollection
                elif not name:
                    self._repr = "files-from-" + inCollection
                self._Records = set()
                flist = []
                for f in os.listdir(inCollection):
                    fullF = inCollection + f
                    if fullF.endswith(extension) and os.path.isfile(fullF):
                        flist.append(fullF)
                for file in flist:
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
        for R in self._Records:
            if R.bad:
                self._Records.remove(R)

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
        for R in self._Records:
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

        return grph

    def coCiteNetwork(self, dropAnon = True, authorship = False):
        tmpgrph = nx.Graph()
        for R in self:
            Cites = R.citations
            if Cites:
                Cites = [c for c in Cites if not c.isAnonymous()]
                if len(Cites) > 1:
                    for n, c1 in enumerate(Cites):
                        for c2 in Cites[n:]:
                            tmpgrph.add_edge(c1, c2)
                elif len(Cites) == 1:
                    if Cites[0] not in tmpgrph:
                        tmpgrph.add_node(Cites[0])

        grph = nx.Graph()
        nodesIter = tmpgrph.adjacency_iter()
        if authorship:
            authsIter = filter(lambda x: hasattr(x[0], 'author'), nodesIter)
            for nodeTuple in authsIter:
                a1 = getattr(nodeTuple[0], 'author')
                if a1 not in grph:
                    grph.add_node(a1, label = str(nodeTuple[0]))
                for n in filter(lambda x: hasattr(x, 'author'), nodeTuple[1].keys()):
                    a2 = getattr(n, 'author')
                    if a2 not in grph:
                        grph.add_node(a2, label = str(n))
                    grph.add_edge(a1, a2)
        else:
            for nodeTuple in nodesIter:
                    if hash(nodeTuple[0]) not in grph:
                        grph.add_node(hash(nodeTuple[0]), label = str(nodeTuple[0]))
                    for n in nodeTuple[1].keys():
                        if hash(n) not in grph:
                            grph.add_node(hash(n), label = str(n))
                        grph.add_edge(hash(nodeTuple[0]), hash(n))
        return grph

    def citationNetwork(self, dropAnon = True, authorship = False):
        tmpgrph = nx.DiGraph()
        for R in self:
            reRef = R.createCitation()
            rCites = R.citations
            if dropAnon and reRef.isAnonymous():
                continue
            if rCites:
                rCites = filter(lambda x: not x.isAnonymous(), rCites) if dropAnon else rCites
                for c in rCites:
                    tmpgrph.add_edge(reRef, c)
        grph = nx.DiGraph()
        nodesIter = tmpgrph.adjacency_iter()
        if authorship:
            authsIter = filter(lambda x: hasattr(x[0], 'author'), nodesIter)
            for nodeTuple in authsIter:
                a1 = getattr(nodeTuple[0], 'author')
                if a1 not in grph:
                    grph.add_node(a1, label = str(nodeTuple[0]))
                for n in filter(lambda x: hasattr(x, 'author'), nodeTuple[1].keys()):
                    a2 = getattr(n, 'author')
                    if a2 not in grph:
                        grph.add_node(a2, label = str(n))
                    grph.add_edge(a1, a2)
        else:
            for nodeTuple in nodesIter:
                    if hash(nodeTuple[0]) not in grph:
                        grph.add_node(hash(nodeTuple[0]), label = str(nodeTuple[0]))
                    for n in nodeTuple[1].keys():
                        if hash(n) not in grph:
                            grph.add_node(hash(n), label = str(n))
                        grph.add_edge(hash(nodeTuple[0]), hash(n))
        return grph

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
    openfile = open(isifile, 'r')
    f = enumerate(openfile, start = 0)
    try:
        if "VR 1.0" not in f.__next__()[1] and "VR 1.0" not in f.__next__()[1]:
            raise BadISIFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
    except StopIteration as e:
        raise BadISIFile("File ends before EF found")
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
            except Exception as e:
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
