#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import shutil
import os

import metaknowledge

class TestGrantCollection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metaknowledge.VERBOSE_MODE = False
        cls.GCmain = metaknowledge.GrantCollection("metaknowledge/tests/", cached = True)

    def setUp(self):
        self.GC = self.GCmain.copy()

    def test_empty(self):
        GCempty = metaknowledge.GrantCollection()
        self.assertEqual(len(GCempty), 0)
        self.assertEqual(GCempty.name, "Empty")

    def test_creationErrors(self):
        with self.assertRaises(metaknowledge.mkExceptions.GrantCollectionException):
            GCbad = metaknowledge.GrantCollection("README.md", extension = '.csv')
        with self.assertRaises(metaknowledge.mkExceptions.BadInputFile):
            GCbad = metaknowledge.GrantCollection("README.md")
        with self.assertRaises(metaknowledge.mkExceptions.BadInputFile):
            GCbad = metaknowledge.GrantCollection("README.md", extension = '.md')
        with self.assertRaises(metaknowledge.mkExceptions.BadInputFile):
            GCbad = metaknowledge.GrantCollection(".", extension = '.md')
        with self.assertRaises(metaknowledge.mkExceptions.GrantCollectionException):
            GCbad = metaknowledge.GrantCollection("README")
        with self.assertRaises(metaknowledge.mkExceptions.GrantCollectionException):
            GCbad = metaknowledge.GrantCollection(1)
        with self.assertRaises(metaknowledge.mkExceptions.GrantCollectionException):
            GCbad = metaknowledge.GrantCollection({1})

    def test_creation(self):
        self.assertIsInstance(self.GC, metaknowledge.GrantCollection)
        self.assertIsInstance(self.GC, metaknowledge.Collection)
        self.assertAlmostEqual(len(self.GC), 2022, delta = 4)
        self.assertIsInstance(self.GC.peek(), metaknowledge.Record)
        self.assertEqual(metaknowledge.GrantCollection(self.GC), self.GC)

    def test_Caching(self):
        self.assertTrue(os.path.isfile("metaknowledge/tests/tests.[].mkGrantDirCache"))
        os.remove("metaknowledge/tests/tests.[].mkGrantDirCache")

    def test_fallback(self):
        fname = "DefaultGrantTestFile.csv"
        shutil.copyfile("metaknowledge/tests/NSERC_TEST_PARTNER.testcsv", fname)
        GC = metaknowledge.GrantCollection(fname, extension = '.csv')
        self.assertEqual(GC._collectedTypes, {"FallbackGrant"})
        os.remove(fname)

    def test_CoInstitution(self):
        G = self.GC.networkCoInvestigatorInstitution()
        self.assertEqual(metaknowledge.graphStats(G), 'Nodes: 641\nEdges: 2034\nIsolates: 79\nSelf loops: 0\nDensity: 0.00991615\nTransitivity: 0.273548')
