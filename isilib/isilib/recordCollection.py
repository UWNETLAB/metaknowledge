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
    def __init__(self, inCollection = None, name = ''):
        self.bad = False
        self._repr = name
        if not inCollection:
            if not name:
                self._repr = "empty"
            self._Records = set()
        elif isinstance(inCollection, str):
            try:
                self._repr = os.path.splitext(os.path.split(inCollection)[1])[0]
                self._Records = set(isiParser(inCollection))
            except BadISIFile as w:
                self.bad = True
                self.error = w
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
            if R.authors() and len(R.authors()) > 1:
                for i, auth1 in enumerate(R.authors()):
                    if auth1 not in grph:
                        grph.add_node(auth1, count = 1)
                    else:
                        grph.node[auth1]['count'] += 1
                    for auth2 in R.authors()[i + 1:]:
                        if auth2 not in grph:
                            grph.add_node(auth2, count = 1)
                        else:
                            grph.node[auth2]['count'] += 1
                        if grph.has_edge(auth1, auth2):
                            grph.edge[auth1][auth2]['weight'] += 1
                        else:
                            grph.add_edge(auth1, auth2, weight = 1)
        return grph

    def coCiteNetwork(self):
        grph = nx.Graph()
        for R in self._Records:
            if R.citations() and len(R.citations()) > 1:
                idDict = getCoCiteIDs(R.citations())
                idList = idDict.keys()
                if len(idList) > 1:
                    for i in range(len(pIDs)):
                        cId1 = pIDs[i]
                        if grph.has_node(cId1):
                            grph.node[cId1]['count'] += 1
                        else:
                            grph.add_node(cId1, val = pDict[cId1], count = 1)
                        for j in range(i + 1, len(pIDs)):
                            cId2 = pIDs[j]
                            if grph.has_node(cId2):
                                grph.node[cId2]['count'] += 1
                            else:
                                grph.add_node(cId2, val = pDict[cId2], count = 1)
                            if grph.has_edge(cId1, cId2):
                                grph.edge[cId1][cId2]['weight'] += 1
                            else:
                                grph.add_edge(cId1, cId2, weight = 1)

    def citationNetwork(self):
        tmpgrph = nx.DiGraph()
        for R in self:
            reRef= R.createCitation()
            rCites = R.citations()
            if rCites:
                for c in rCites:
                    tmpgrph.add_edge(reRef, c)
        grph = nx.DiGraph()
        for nodeTuple in tmpgrph.adjacency_iter():
            if nodeTuple[0] not in grph:
                grph.add_node(hash(nodeTuple[0]), label = str(nodeTuple[0]))
            for n in nodeTuple[1].keys():
                if hash(n) not in grph:
                    grph.add_node(hash(n), label = str(n))
                grph.add_edge(hash(nodeTuple[0]), hash(n))
        return grph

        return grph

    def yearSplit(startYear, endYear):
        recordsInRange = set()
        for R in self._Records:
            if R.year() >= startYear and R.year() <= endYear:
                recordsInRange.add(R)
        return RecordCollection(recordsInRange, repr(self) + "_(" + str(startYear) + " ," + str(endYear) + ")")

def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reachs EF.
    Each it finds is used to initilize a Record then all Record are returned as a list.
    """
    openfile = open(isifile, 'r')
    f = enumerate(openfile, start = 0)
    if "VR 1.0" not in f.__next__()[1] and "VR 1.0" not in f.__next__()[1]:
        raise BadISIFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
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
