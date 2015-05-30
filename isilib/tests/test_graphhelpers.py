"""
import unittest
import isilib
import filecmp
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
        self.assertTrue(filecmp.cmp('tests/' + fileEName,  fileEName))
        self.assertTrue(filecmp.cmp('tests/' + fileNName,  fileNName))
        os.remove(fileEName)
        os.remove(fileNName)
"""
