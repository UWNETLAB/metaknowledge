#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import metaknowledge

import os

class TestRecord(unittest.TestCase):

    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/scopus_testing.csv.scopus")
        self.R = self.RC.peek()

    def test_creation(self):
        Rstart = self.RC.peek()
        R = metaknowledge.ScopusRecord(Rstart._fieldDict)
        self.assertEqual(R, Rstart)
        with open("metaknowledge/tests/scopus_testing.csv.scopus") as f:
            f.readline()
            R = metaknowledge.ScopusRecord(f.readline())
            self.assertEqual(R.id, 'EID:2-s2.0-84963944162')
            R = metaknowledge.ScopusRecord(f.readline())
            self.assertEqual(R.id, 'EID:2-s2.0-84943362392')
        with self.assertRaises(TypeError):
            R = metaknowledge.ScopusRecord(12345678)
        R = metaknowledge.ScopusRecord(",2132,4,3fdgf,fgdgdfdg,dgfdg,,,,,,,,,,,,,,,,,,,2e5r6t789765432\n")
        self.assertTrue(R.bad)
        with self.assertRaises(metaknowledge.BadScopusRecord):
            R.writeRecord('not a file')

    def test_isCollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)

    def test_isscopus(self):
        self.assertIsInstance(self.R, metaknowledge.ScopusRecord)

    def test_specials(self):
        for R in self.RC:
            for s in metaknowledge.medline.medlineSpecialTagToFunc.keys():
                self.assertIsInstance(R.get(s), (str, type(None), list, int, metaknowledge.Citation))

    def test_allFields(self):
        for R in self.RC:
            for k,v in R.items():
                self.assertIsInstance(k, str)
                self.assertIsInstance(v, (str, list, int))

    def test_write(self):
        fileName = 'tempFile.scopus.tmp'
        self.RC.writeFile(fileName)
        self.assertEqual(os.path.getsize(fileName), os.path.getsize("metaknowledge/tests/scopus_testing.csv.scopus") + 10838) #Not quite identical due to double quotes
        os.remove(fileName)
