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
        self.assertIsInstance(G, nx.classes.graph.Graph)
        self.assertEqual(len(G.nodes()), 525)
        self.assertEqual(len(G.edges()), 29297)
