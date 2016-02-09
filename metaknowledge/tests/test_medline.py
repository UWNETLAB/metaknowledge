#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

class TestRecord(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/medline_test.medline")
        self.R = self.RC.peak()

    def test_isCollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)

    def test_ismedline(self):
        self.assertIsInstance(self.R, metaknowledge.MedlineRecord)

    def test_allFields(self):
        for R in self.RC:
            for k,v in R.items():
                self.assertIsInstance(k, str)
                self.assertIsInstance(v, (str, list, dict))
