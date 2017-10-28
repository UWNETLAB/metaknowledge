#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

import os

class TestProQuest(unittest.TestCase):

    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/ProQuest_TestFile.testtxt")
        self.R = self.RC.peek()

    def test_isCollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)

    def test_isProQuest(self):
        self.assertIsInstance(self.R, metaknowledge.ProQuestRecord)

    def test_specials(self):
        for R in self.RC:
            for s in metaknowledge.proquest.proQuestSpecialTagToFunc.keys():
                self.assertIsInstance(R.get(s), (str, type(None), list, int, metaknowledge.Citation))

    def test_allFields(self):
        for R in self.RC:
            for k,v in R.items():
                self.assertIsInstance(k, str)
                self.assertIsInstance(v, (str, list, int))

    def test_graphs(self):
        self.assertEqual(metaknowledge.graphStats(self.RC.networkMultiMode(self.RC.tags()), sentenceString = True), "The graph has 1928 nodes, 50833 edges, 0 isolates, 114 self loops, a density of 0.0273952 and a transitivity of 0.0815136")

    def test_write(self):
        #No writer currently implemented
        pass
