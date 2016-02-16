#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

class TestGrant(unittest.TestCase):
    def setUp(self):
        self.Grant1 = metaknowledge.Grant("U10 HD04267/HG/NICHD NHI HHS/Unit State")
        self.Grant2 = metaknowledge.Grant("HG/NICHD NHI HHS/Unit State")

    def test_isGrant(self):
        self.assertIsInstance(self.Grant1, metaknowledge.Grant)
        self.assertIsInstance(self.Grant2, metaknowledge.Grant)

    def test_init(self):
        Gshort = metaknowledge.Grant("U10 HD04267/NICHD NHI HHS/Unit State")
        Gmid = metaknowledge.Grant("U10 /HD04267HG/NICHD NHI HHS/Unit State")
        Glong = metaknowledge.Grant("U/10 /HD042/67HG/NICHD NHI HHS/Unit State")
        self.assertNotEqual(Gshort, Glong)
        self.assertNotEqual(Gmid, Glong)

    def test_bad(self):
        G = metaknowledge.Grant("NICHD NHI HHSUnit State")
        self.assertTrue(G.bad)

    def test_eq(self):
        self.assertNotEqual(1, self.Grant2)
        self.assertNotEqual(self.Grant1, self.Grant2)

    def test_hash(self):
        self.assertIsInstance(hash(self.Grant1), int)

    def test_orgin(self):
        self.assertEqual(str(self.Grant1), self.Grant1.original)

    def test_rerp(self):
        self.assertEqual(repr(self.Grant1), "<metaknowledge.Grant object U10 HD04267/HG/NICHD NHI HHS/Unit State>")
