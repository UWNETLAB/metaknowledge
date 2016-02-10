#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import os.path
import os

import metaknowledge

class TestRecord(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/medline_test.medline")
        self.R = self.RC.peak()

    def test_creation(self):
        Rstart = self.RC.peak()
        R = metaknowledge.MedlineRecord(Rstart._fieldDict)
        self.assertEqual(R, Rstart)
        with open("metaknowledge/tests/medline_test.medline") as f:
            f.readline()
            R = metaknowledge.MedlineRecord(f)
            self.assertEqual(R.id, 'PMID:26524502')
            s = f.read()
            R = metaknowledge.MedlineRecord(s)
            self.assertEqual(R.id, 'PMID:25802386')
        with self.assertRaises(TypeError):
            R = metaknowledge.MedlineRecord(12345678)
        R = metaknowledge.MedlineRecord("PMID- 25802386\njhgjhghjbgjhgjghhjgjh\nhdghjdfgjdfsgjh\n")
        self.assertTrue(R.bad)
        with self.assertRaises(metaknowledge.BadPubmedRecord):
            R.writeRecord('not a file')
    def test_isCollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)

    def test_ismedline(self):
        self.assertIsInstance(self.R, metaknowledge.MedlineRecord)

    def test_specials(self):
        for R in self.RC:
            for s in metaknowledge.medlineSpecialTagToFunc.keys():
                self.assertIsInstance(R.get(s), (str, type(None), list, int))

    def test_allFields(self):
        for R in self.RC:
            for k,v in R.items():
                self.assertIsInstance(k, str)
                self.assertIsInstance(v, (str, list, dict))

    def test_write(self):
        fileName = 'tempFile.medline.tmp'
        self.RC.writeFile(fileName)
        self.assertEqual(os.path.getsize(fileName), os.path.getsize("metaknowledge/tests/medline_test.medline") + 526) #Not quite identical
        os.remove(fileName)
