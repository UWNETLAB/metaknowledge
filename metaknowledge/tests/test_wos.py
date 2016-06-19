#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

class TestWOS(unittest.TestCase):
    def setUp(self):
        self.R = metaknowledge.WOSRecord(simplePaperString)
        self.Rbad = metaknowledge.WOSRecord(simplePaperString[:-3])

    def test_creation(self):
        R = metaknowledge.WOSRecord(self.R._fieldDict)
        self.assertEqual(R, self.R)
        with open("metaknowledge/tests/testFile.isi") as f:
            f.readline()
            f.readline()
            R = metaknowledge.WOSRecord(f)
            self.assertEqual(R.id, 'WOS:A1979GV55600001')
        with self.assertRaises(TypeError):
            R = metaknowledge.WOSRecord(123456789)

    def test_badwrite(self):
        with self.assertRaises(metaknowledge.BadWOSRecord):
            self.Rbad.writeRecord('not a file object.txt')

    def test_dupDetection(self):
        s = simplePaperString[:-3] + "DE Example; testing\nPD APR\nER\n"
        R = metaknowledge.WOSRecord(s)
        self.assertTrue(R.bad)

    def test_WOSNum(self):
        self.assertEqual(self.R.UT, 'WOS:123317623000007')
        self.assertEqual(self.R.wosString, 'WOS:123317623000007')


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
VL 1
BP 1
EP 2
DI 10.1111
UT WOS:123317623000007
ER
"""
