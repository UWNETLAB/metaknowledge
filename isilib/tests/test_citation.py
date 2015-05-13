import unittest
import isilib

class TestCitation(unittest.TestCase):
    def setUp(self):
        self.Cite = isilib.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")

    def test_citation_author(self):
        self.assertEqual(self.Cite.author, "JOHN D")

    def test_citation_year(self):
        self.assertEqual(self.Cite.year, "2015")

    def test_citation_journal(self):
        self.assertEqual(self.Cite.journal, "TOPICS IN COGNITIVE SCIENCE")

    def test_citation_v(self):
        self.assertEqual(self.Cite.V, "V1")

    def test_citation_p(self):
        self.assertEqual(self.Cite.P, "P1")

    def test_citation_DOI(self):
        self.assertEqual(self.Cite.DOI, "0.1063/1.1695064")

    def test_citation_id(self):
        self.assertEqual(self.Cite.getID(), "JOHN D, 2015")

    def test_citation_str(self):
        self.assertEqual(str(self.Cite), "John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")

    def test_citation_extra(self):
        self.assertEqual(self.Cite.getExtra(), "TOPICS IN COGNITIVE SCIENCE, V1, P1")

    def test_citation_badDetection(self):
        self.assertTrue(isilib.Citation("").bad)

    def test_citation_equality(self):
        c = isilib.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")
        self.assertTrue(c == self.Cite)

    def test_citation_badLength(self):
        c = isilib.Citation("a, b")
        self.assertTrue(c.bad)
        self.assertEqual(str(c.error), "Too few elemets")
        self.assertEqual(c.getExtra(),'A, B')
        self.assertEqual(c.getID(),'A, B')

    def test_citation_badNumbers(self):
        c = isilib.Citation("1 2, 2, 3, 4")
        self.assertTrue(c.bad)
        self.assertEqual(c.getID(), '1 2, 2')
        self.assertEqual(str(c.error), "Too many numbers")
