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
    """
    def test_dropEdges(self):
        tmpG = metaknowledge.drop_edges(self.G, 4)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))

    def test_dropNodes(self):
        tmpG = metaknowledge.drop_nodes(self.G, 4)
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
    """
