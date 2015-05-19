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
        Gauths = self.RC.coCiteNetwork(authorship = True, dropAnon = False)
        nx.write_graphml(Gauths, 'dfjsfgdhdf.graphml')
        self.assertIsInstance(G, nx.classes.graph.Graph)
        self.assertEqual(len(G.nodes()), 508)
        self.assertEqual(len(G.edges()), 14351)
        self.assertEqual(len(Gauths.nodes()), 316)
        self.assertEqual(len(Gauths.edges()), 6872)

    def test_coAuth(self):
        G = self.RC.coAuthNetwork()
        self.assertIsInstance(G, nx.classes.graph.Graph)
        self.assertEqual(len(G.nodes()), 45)
        self.assertEqual(len(G.edges()), 46)


    def test_Cite(self):
        Gdefault = self.RC.citationNetwork()
        Ganon = self.RC.citationNetwork(dropAnon = False)
        Gauths = self.RC.citationNetwork(authorship = True)
        self.assertIsInstance(Gdefault, nx.classes.digraph.DiGraph)
        self.assertGreater(len(Gdefault.nodes()), len(Gauths.nodes()))
        self.assertGreater(len(Ganon.nodes()), len(Gdefault.nodes()))
        self.assertEqual(len(Gdefault.nodes()), 524)
        self.assertEqual(len(Ganon.nodes()), 543)
        self.assertEqual(len(Gauths.nodes()), 319)
        self.assertEqual(len(Gdefault.edges()), 832)
        self.assertEqual(len(Ganon.edges()), 853)
        self.assertEqual(len(Gauths.edges()), 561)
