import unittest
import isilib
import os.path

class TestRecordCollection(unittest.TestCase):
    def setUp(self):
        currentPath = os.path.dirname(os.path.realpath(__file__))
        self.RC = isilib.RecordCollection(currentPath + "/TwoPaper.isi")

    def test_iscollection(self):
        self.assertTrue(isinstance(self.RC, isilib.RecordCollection))
