#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

class TestGrants(unittest.TestCase):
    def setUp(self):
        self.Grant1 = metaknowledge.MedlineGrant("U10 HD04267/HG/NICHD NHI HHS/Unit State")
        self.Grant2 = metaknowledge.MedlineGrant("HG/NICHD NHI HHS/Unit State")

    def test_isGrant(self):
        self.assertIsInstance(self.Grant1, metaknowledge.Grant)
        self.assertIsInstance(self.Grant2, metaknowledge.Grant)

    def test_init(self):
        Gshort = metaknowledge.MedlineGrant("U10 HD04267/NICHD NHI HHS/Unit State")
        Gmid = metaknowledge.MedlineGrant("U10 /HD04267HG/NICHD NHI HHS/Unit State")
        Glong = metaknowledge.MedlineGrant("U/10 /HD042/67HG/NICHD NHI HHS/Unit State")
        self.assertNotEqual(Gshort, Glong)
        self.assertNotEqual(Gmid, Glong)

    def test_bad(self):
        G = metaknowledge.MedlineGrant("NICHD NHI HHSUnit State")
        self.assertTrue(G.bad)

    def test_eq(self):
        self.assertNotEqual(1, self.Grant2)
        self.assertNotEqual(self.Grant1, self.Grant2)

    def test_hash(self):
        self.assertIsInstance(hash(self.Grant1), int)

    def test_orgin(self):
        self.assertEqual("U10 HD04267/HG/NICHD NHI HHS/Unit State", self.Grant1.original)

    def test_rerp(self):
        self.assertEqual(repr(self.Grant1), "<metaknowledge.MedlineGrant object U10 HD04267/HG-Unit State>")

    def test_NSF(self):
        GC = metaknowledge.GrantCollection("metaknowledge/tests/nsfTestFiles")
        G = GC.networkMultiMode(GC.tags())
        self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), "The graph has 244 nodes, 2077 edges, 0 isolates, 19 self loops, a density of 0.0703974 and a transitivity of 0.497237")
