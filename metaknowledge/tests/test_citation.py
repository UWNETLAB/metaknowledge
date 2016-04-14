#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge

class TestCitation(unittest.TestCase):
    def setUp(self):
        self.Cite = metaknowledge.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")

    def test_citation_author(self):
        self.assertEqual(self.Cite.author, "John D")

    def test_citation_year(self):
        self.assertEqual(self.Cite.year, 2015)

    def test_citation_journal(self):
        self.assertEqual(self.Cite.journal, "TOPICS IN COGNITIVE SCIENCE")

    def test_citation_v(self):
        self.assertEqual(self.Cite.V, "V1")

    def test_citation_p(self):
        self.assertEqual(self.Cite.P, "P1")

    def test_citation_DOI(self):
        self.assertEqual(self.Cite.DOI, "0.1063/1.1695064")

    def test_citation_id(self):
        self.assertEqual(self.Cite.ID(), "John D, 2015, TOPICS IN COGNITIVE SCIENCE")

    def test_citation_str(self):
        self.assertEqual(str(self.Cite), "John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1, DOI 0.1063/1.1695064")

    def test_citation_extra(self):
        self.assertEqual(self.Cite.Extra(), "V1, P1, 0.1063/1.1695064")

    def test_citation_badDetection(self):
        self.assertTrue(metaknowledge.Citation("").bad)

    def test_citation_equality(self):
        c1 = metaknowledge.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, P1, DOI 0.1063/1.1695064")
        c2 = metaknowledge.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1")
        c3 = metaknowledge.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P2")
        self.assertTrue(c1 == self.Cite)
        self.assertTrue(c2 == self.Cite)
        self.assertFalse(c1 != c2)
        self.assertFalse(c3 != c1)

    def test_citation_hash(self):
        self.assertTrue(bool(hash(self.Cite)))
        self.assertTrue(bool(hash(metaknowledge.Citation("John D., 2015, TOPICS IN COGNITIVE SCIENCE, V1, P1"))))
        self.assertTrue(bool(hash(metaknowledge.Citation("John D., 2015"))))

    def test_citation_badLength(self):
        c = metaknowledge.Citation("ab, c")
        self.assertTrue(c.bad)
        self.assertEqual(str(c.error), "Not a complete set of author, year and journal")
        self.assertEqual(c.Extra(),'')
        self.assertEqual(c.author,'Ab')
        self.assertEqual(c.ID(),'Ab, C')

    def test_citation_badNumbers(self):
        c = metaknowledge.Citation("1, 2, 3, 4")
        self.assertTrue(c.bad)
        self.assertEqual(c.ID(), '1, 2')
        self.assertEqual(str(c.error), "The citation did not fully match the expected pattern")
