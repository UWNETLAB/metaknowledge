#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge
import os
import io
import sys
from metaknowledge.progressBar import _ProgressBar

fileShortName = 'testNetworks'
fileEName = 'testNetworks_edgeList.tst'
fileNName = 'testNetworks_nodeAttributes.tst'
filesuffix = 'tst'

class TestHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.RCmain = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")
        cls.Gmain = cls.RCmain.networkCoCitation()

    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = self.RCmain.copy()
        self.G = self.Gmain.copy()

    def test_graphwrite(self):
        metaknowledge.writeGraph(self.G, fileShortName, suffix = filesuffix)
        tmpG = metaknowledge.readGraph(fileEName, fileNName)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
        os.remove(fileEName)
        os.remove(fileNName)

    def test_tnetWriter(self):
        fName = fileShortName + "_tnet.csv"
        G = self.RC.networkTwoMode('AF', 'WC', edgeAttribute = 'PY')
        metaknowledge.writeTnetFile(G, fName, 'type', weighted = True, timeString = 'key')
        self.assertAlmostEqual(os.path.getsize(fName), 1015, delta=100)
        os.remove(fName)
        metaknowledge.writeTnetFile(G, fName, 'type')
        self.assertAlmostEqual(os.path.getsize(fName), 378, delta=50)
        os.remove(fName)

    def test_progress(self):
        metaknowledge.VERBOSE_MODE = True
        tmpIO = io.StringIO()
        P = _ProgressBar(0, "testing", output = tmpIO, dummy = True)
        metaknowledge.writeEdgeList(self.G, fileEName, _progBar = P, )
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertEqual(len(s), 0)
        P = _ProgressBar(0, "testing", output = tmpIO)
        metaknowledge.writeEdgeList(self.G, fileEName, _progBar = P)
        tmpIO.seek(0)
        os.remove(fileEName)
        s = ''.join(tmpIO.readlines())
        self.assertEqual(s[-14], '[')
        self.assertEqual(s[-1], '%')
        P.finish("done test")
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertEqual(s[-81:-3], 'done test                                                                   0.')
        metaknowledge.VERBOSE_MODE = False

    def test_dropEdges(self):
        metaknowledge.dropEdges(self.G, minWeight = 1, maxWeight = 3, dropSelfLoops = True)
        self.assertEqual(metaknowledge.graphStats(self.G, sentenceString = True), "The graph has 493 nodes, 12711 edges, 0 isolates, 0 self loops, a density of 0.104809 and a transitivity of 0.588968")
        self.assertTrue(self.G.edges['Imbert C, 1975, NOUV REV OPT', 'Fainman Y, 1984, APPL OPTICS']['weight'] == 1)

    def test_dropNodeByCount(self):
        metaknowledge.dropNodesByCount(self.G, minCount = 2, maxCount = 5)
        self.assertEqual(metaknowledge.graphStats(self.G, sentenceString = True), "The graph has 106 nodes, 1205 edges, 0 isolates, 17 self loops, a density of 0.218149 and a transitivity of 0.751036")
        self.assertTrue(self.G.node['Shih H, 1971, PHYS REV A']['count'] == 2)

    def test_dropNodesByDegree(self):
        metaknowledge.dropNodesByDegree(self.G, minDegree = 20, maxDegree = 100)
        self.assertEqual(metaknowledge.graphStats(self.G, sentenceString = True), "The graph has 385 nodes, 5923 edges, 0 isolates, 11 self loops, a density of 0.0802083 and a transitivity of 0.954487")
        self.assertTrue(self.G.edges['Mazur P, 1953, MEM ACAD ROY BELG', 'Livens Gh, 1948, P CAMB PHILOS SOC']['weight'] == 1)

    def test_mergeGraphs(self):
        RC1 = self.RC.yearSplit(0,1978)
        RC2 = self.RC.yearSplit(1979,10000)
        G1 = RC1.networkCoCitation()
        G2 = RC2.networkCoCitation()
        metaknowledge.mergeGraphs(G1,G2)
        for node, attr in G1.nodes(data = True):
            self.assertEqual(self.G.node[node]['count'], attr['count'])
        for node1, node2, attr in G1.edges(data = True):
            self.assertEqual(self.G.edges[node1, node2]['weight'], attr['weight'])
