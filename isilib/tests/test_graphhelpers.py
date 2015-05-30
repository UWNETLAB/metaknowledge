import unittest
import isilib
import os

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.RC = isilib.RecordCollection("tests/testFile.isi")
        self.G = self.RC.coCiteNetwork()

    def test_graphwrite(self):
        fileShortName = 'testNetworks'
        fileEName = 'testNetworks_edgeList_undirected.tst'
        fileNName = 'testNetworks_nodeAttributes_undirected.tst'
        isilib.write_graph(self.G, fileShortName, suffix = 'tst')
        tmpG = isilib.read_graph(fileEName, fileNName)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
        os.remove(fileEName)
        os.remove(fileNName)
