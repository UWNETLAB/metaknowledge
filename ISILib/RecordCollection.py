#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from Record import Record, lazy

import itertools
import networkx as nx

class BadISIFile(Warning):
    """
    Exception thrown by isiParser for mis-formated files
    """
    pass

class RecordCollection(object):
    def __init__(self, inCollection):
        self.bad = False
        if isinstance(inCollection, str):
            try:
                self._Records = set(isiParser(inCollection))
            except:
                raise
        elif isinstance(inCollection, list):
            self._Records = set(inCollection)
        elif isinstance(inCollection, set):
            self._Records = inCollection
        else:
            raise TypeError

    def __add__(self, other):
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records | other._Records)

    def __eq__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return self._Records == other._Records

    @lazy
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

    @lazy
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

    def yearSplit(startYear, endYear):
        recordsInRange = set()
        for R in self._Records:
            if R.year() >= startYear and R.year() <= endYear:
                recordsInRange.add(R)
        return RecordCollection(recordsInRange)




def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reachs EF.
    Each it finds is used to initilize a Record then all Record are returned as a list.
    """
    f = enumerate(open(isifile, 'r'), start = 0)
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
        return plst

def getCoCiteIDs(clst):
    """
    Creates a dict of the ID-extra information pairs for a CR tag.
    """
    idDict = {}
    for c in clst:
        splitCit = c.split(', ')
        if len(splitCit) > 1:
            cId = splitCit[0].replace(' ',' ').replace('.','').upper() + ' ' + splitCit[1]
        else:
            cId = c.upper()
        if cId not in idDict and not excludedSource(splitCit):
            if len(splitCit) < 3:
                cExtra = ''
            elif len(splitCit[-1]) > 3 and 'DOI' in splitCit[-1][:3].upper():
                cExtra = ', '.join(splitCit[2:-1])
            else:
                cExtra = ', '.join(splitCit[2:])
            idDict[cId] = cExtra
    return idDict
