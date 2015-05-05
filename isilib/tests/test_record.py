import unittest
import isilib
import os.path

class TestRecord(unittest.TestCase):
    def setUp(self):
        currentPath = os.path.dirname(os.path.realpath(__file__))
        f = open(currentPath + "/SimplePaper.isi")
        self.R = isilib.Record(f)
        f.close()

    def test_isRecord(self):
        self.assertTrue(isinstance(self.R, isilib.Record))
    def test_title(self):
        self.assertEqual(self.R.title(), "Example Paper")
    def test_author(self):
        self.assertEqual(self.R.authors(), ["John, Doe"])
