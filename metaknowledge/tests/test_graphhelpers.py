import unittest
import metaknowledge
import os
import io
from metaknowledge.graphHelpers import _ProgressBar

fileShortName = 'testNetworks'
fileEName = 'testNetworks_edgeList_undirected.tst'
fileNName = 'testNetworks_nodeAttributes_undirected.tst'
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
        P = _ProgressBar(0, "testing", output = tmpIO)
        metaknowledge.write_edgeList(self.G, fileEName, progBar = P)
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertFalse(
        "==================================================]100.0%" in s)
        self.assertTrue("Writing edge list testNetworks_edgeList_undirected.tst" in s)
        os.remove(fileEName)
        metaknowledge.VERBOSE_MODE = False
    """
    def test_dropEdges(self):
        tmpG = metaknowledge.drop_edges(self.G, 4)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))

    def test_dropNodes(self):
        tmpG = metaknowledge.drop_nodes(self.G, 4)
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
    """
