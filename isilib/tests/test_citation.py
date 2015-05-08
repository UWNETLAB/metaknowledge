import unittest
import isilib

class TestCitation(unittest.TestCase):
    def setUp(self):
        self.Cite = isilib.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")
    def test_author(self):
        self.assertEqual(self.Cite.author, "JOHN D")

    def test_year(self):
        self.assertEqual(self.Cite.year, "2015")

    def test_journal(self):
        self.assertEqual(self.Cite.journal, "TOPICS IN COGNITIVE SCIENCE")

    def test_v(self):
        self.assertEqual(self.Cite.V, "V1")

    def test_p(self):
        self.assertEqual(self.Cite.P, "P1")

    def test_DOI(self):
        self.assertEqual(self.Cite.DOI, "0.1063/1.1695064")

    def test_id(self):
        self.assertEqual(self.Cite.getID(), "JOHN D, 2015")

    def test_extra(self):
        self.assertEqual(self.Cite.getExtra(), "TOPICS IN COGNITIVE SCIENCE, V1, P1")

    def test_badDetection(self):
        self.assertTrue(isilib.Citation("").bad)

    def test_badLength(self):
        c = isilib.Citation("a, b")
        self.assertTrue(c.bad)
        self.assertEqual(str(c.error), "Too few elemets")

    def test_badNumbers(self):
        c = isilib.Citation("1, 2, 3, 4")
        self.assertTrue(c.bad)
        self.assertEqual(str(c.error), "Too many numbers")
