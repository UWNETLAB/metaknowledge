import unittest
import isilib
import os.path

class TestRecord(unittest.TestCase):
    def setUp(self):
        self.R = isilib.Record(simplePaperString)
    def test_isRecord(self):
        self.assertTrue(isinstance(self.R, isilib.Record))
    def test_title(self):
        self.assertEqual(self.R.title(), "Example Paper")
    def test_author(self):
        self.assertEqual(self.R.authors(), ["John, Doe"])
    def test_year(self):
        self.assertEqual(self.R.year(), 2015)
    def test_month(self):
        self.assertEqual(self.R.month(), 4)
    def test_cites(self):
        self.assertEqual(str(self.R.citations()[0]), "John D. 1999, TOPICS IN COGNITIVE SCIENCE")
        self.assertEqual(len(self.R.citations()), 1)
    def test_WOS(self):
        self.assertEqual(self.R.wosString(), 'WOS:123317623000007')

simplePaperString = """PT J
AU John, D
AF John, Doe
TI Example Paper
SO TOPICS IN COGNITIVE SCIENCE
LA English
DT Article
DE Example; testing
ID REAL; TIME
AB This is a test.
C1 UW, Ontario, Canada.
RP John, D (reprint author), UW, Ontario, Canada.
CR John D. 1999, TOPICS IN COGNITIVE SCIENCE
J9 EXAMPLE
JI examaple
PD APR
PY 2015
UT WOS:123317623000007
ER
"""
