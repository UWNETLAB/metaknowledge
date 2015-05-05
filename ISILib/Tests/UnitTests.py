import unittest
import Classes.RecordCollection

class simpleCollectionTest(unittest.TestCase):
    def setUp(self):
        self.RC = RecordCollection("OnePaper.isi")
    def test_size(self):
        assertEqual(len(self.RC._Records), 1)
