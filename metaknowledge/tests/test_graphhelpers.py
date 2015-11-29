#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge
import os
import io
from metaknowledge.graphHelpers import _ProgressBar

fileShortName = 'testNetworks'
fileEName = 'testNetworks_edgeList.tst'
fileNName = 'testNetworks_nodeAttributes.tst'
filesuffix = 'tst'

class TestHelpers(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")
        self.G = self.RC.coCiteNetwork()

    def test_graphwrite(self):
        metaknowledge.write_graph(self.G, fileShortName, suffix = filesuffix)
        tmpG = metaknowledge.read_graph(fileEName, fileNName)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
        os.remove(fileEName)
        os.remove(fileNName)

    def test_progress(self):
        metaknowledge.VERBOSE_MODE = True
        tmpIO = io.StringIO()
        P = _ProgressBar(0, "testing", output = tmpIO, dummy = True)
        metaknowledge.write_edgeList(self.G, fileEName, _progBar = P, )
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertEqual(len(s), 0)
        P = _ProgressBar(0, "testing", output = tmpIO)
        metaknowledge.write_edgeList(self.G, fileEName, _progBar = P)
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertFalse("]100.0%" in s)
        self.assertTrue("Done edge list" in s)
        os.remove(fileEName)
        metaknowledge.VERBOSE_MODE = False

    def test_dropEdges(self):
        metaknowledge.drop_edges(self.G, minWeight = 1, maxWeight = 3, dropSelfLoops = True)
        self.assertEqual(metaknowledge.graphStats(self.G), "The graph has 492 nodes, 12660 edges, 0 isolates, 0 self loops, a density of 0.104813 and a transitivity of 0.58952")
        self.assertTrue(self.G.edge['Imbert C, 1975, NOUV REV OPT']['Fainman Y, 1984, APPL OPTICS']['weight'] == 1)

    def test_dropNodeByCount(self):
        metaknowledge.drop_nodesByCount(self.G, minCount = 2, maxCount = 5)
        self.assertEqual(metaknowledge.graphStats(self.G), "The graph has 105 nodes, 1198 edges, 0 isolates, 17 self loops, a density of 0.219414 and a transitivity of 0.753426")
        self.assertTrue(self.G.node['Shih H, 1971, PHYS REV A']['count'] == 2)

    def test_dropNodesByDegree(self):
        metaknowledge.drop_nodesByDegree(self.G, minDegree = 20, maxDegree = 100)
        self.assertEqual(metaknowledge.graphStats(self.G), "The graph has 384 nodes, 5902 edges, 0 isolates, 11 self loops, a density of 0.08026 and a transitivity of 0.954765")
        self.assertTrue(self.G.edge['Mazur P, 1953, MEM ACAD ROY BELG']['Livens Gh, 1948, P CAMB PHILOS SOC']['weight'] == 1)

    def test_mergeGraphs(self):
        RC1 = self.RC.yearSplit(0,1978)
        RC2 = self.RC.yearSplit(1979,10000)
        G1 = RC1.coCiteNetwork()
        G2 = RC2.coCiteNetwork()
        metaknowledge.mergeGraphs(G1,G2)
        for node, attr in G1.nodes_iter(data = True):
            self.assertEqual(self.G.node[node]['count'], attr['count'])
        for node1, node2, attr in G1.edges(data = True):
            self.assertEqual(self.G.edge[node1][node2]['weight'], attr['weight'])
