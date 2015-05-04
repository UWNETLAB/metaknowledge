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
                self._Records = isiParser(inCollection)
            except:
                raise
        elif isinstance(inCollection, list):
            self._Records = inCollection
        else:
            raise TypeError
    def __add__(self, other):
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records + other._Records)

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
