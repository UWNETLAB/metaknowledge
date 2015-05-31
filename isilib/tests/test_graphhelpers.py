import unittest
import isilib
import os
import io
from isilib.graphHelpers import ProgressBar

fileShortName = 'testNetworks'
fileEName = 'testNetworks_edgeList_undirected.tst'
fileNName = 'testNetworks_nodeAttributes_undirected.tst'
filesuffix = 'tst'

class TestHelpers(unittest.TestCase):
    def setUp(self):
        isilib.VERBOSE_MODE = False
        self.RC = isilib.RecordCollection("tests/testFile.isi")
        self.G = self.RC.coCiteNetwork()

    def test_graphwrite(self):

        isilib.write_graph(self.G, fileShortName, suffix = filesuffix)
        tmpG = isilib.read_graph(fileEName, fileNName)
        self.assertEqual(len(tmpG.edges()), len(self.G.edges()))
        self.assertEqual(len(tmpG.nodes()), len(self.G.nodes()))
        os.remove(fileEName)
        os.remove(fileNName)

    def test_progress(self):
        isilib.VERBOSE_MODE = True
        tmpIO = io.StringIO()
        P = ProgressBar(0, "testing", output = tmpIO)
        isilib.write_edgeList(self.G, fileEName, progBar = P)
        tmpIO.seek(0)
        s = ''.join(tmpIO.readlines())
        self.assertTrue(
        "[========================================================================]100.0%" in s and "Writing edge list testNetworks_edgeList_undirected.tst" in s)
        os.remove(fileEName)
        isilib.VERBOSE_MODE = False
