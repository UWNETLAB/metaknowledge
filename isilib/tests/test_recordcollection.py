import unittest
import isilib
import os
import filecmp
import networkx as nx

class TestRecordCollection(unittest.TestCase):

    def setUp(self):
        self.RC = isilib.RecordCollection("tests/testFile.isi")

    def test_iscollection(self):
        self.assertIsInstance(self.RC, isilib.RecordCollection)
    """
    def test_write(self):
        fileName = 'OnePaper2.isi'
        RC = isilib.RecordCollection('tests/' + fileName)
        RC.writeFile(fileName + '.tmp')
        RC.writeFile()
        self.assertTrue(filecmp.cmp('tests/' + fileName, fileName + '.tmp'))
        self.assertTrue(filecmp.cmp('tests/' + fileName, repr(RC)[:200] + '.isi'))
        os.remove(fileName + '.tmp')
        os.remove(repr(RC)[:200] + '.isi')

    def test_coCite(self):
        G = self.RC.coCiteNetwork()
        self.assertIsInstance(G, nx.classes.graph.Graph)
        self.assertEqual(len(G.nodes()), 526)
        self.assertEqual(len(G.edges()), 29297)


    def test_coAuth(self):
        G = self.RC.coAuthNetwork()
        self.assertIsInstance(G, nx.classes.graph.Graph)
        self.assertEqual(len(G.nodes()), 45)
        self.assertEqual(len(G.edges()), 46)
    """

    def test_Cite(self):
        Gdefault = self.RC.citationNetwork()
        Ganon = self.RC.citationNetwork(dropAnon = False)
        Gauths = self.RC.citationNetwork(authorship = True)
        nx.write_graphml(Gauths, "Gauths.graphml")
        #self.assertIsInstance(Gdefault, nx.classes.digraph.DiGraph)
        #self.assertGreater(len(Gdefault.nodes()), len(Gauths.nodes()))
        #self.assertGreater(len(Ganon.nodes()), len(Gdefault.nodes()))
        #self.assertEqual(len(Gdefault.nodes()), 529)
        #self.assertEqual(len(Ganon.nodes()), 548)
        self.assertEqual(len(Gauths.nodes()), 334)
        self.assertEqual(len(Gdefault.edges()), 832)
        self.assertEqual(len(Ganon.edges()), 832)
        self.assertEqual(len(Gauths.edges()), 10)
