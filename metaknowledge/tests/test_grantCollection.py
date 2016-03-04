#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

class TestGrantCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        metaknowledge.VERBOSE_MODE = False
        cls.GCmain = metaknowledge.GrantCollection("metaknowledge/tests/")

    def setUp(self):
        self.GC = self.GCmain.copy()

    def test_creation(self):
        self.assertIsInstance(self.GC, metaknowledge.GrantCollection)
        self.assertIsInstance(self.GC, metaknowledge.Collection)
        self.assertEqual(len(self.GC), 1989)
        self.assertIsInstance(self.GC.peak(), metaknowledge.Record)
