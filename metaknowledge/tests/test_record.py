#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge

class TestRecord(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.R = metaknowledge.Record(simplePaperString)
        self.Rbad = metaknowledge.Record(simplePaperString[:-3])

    def test_isRecord(self):
        self.assertTrue(isinstance(self.R, metaknowledge.WOSRecord))

    def test_bad(self):
        self.assertTrue(self.Rbad.bad)
        with self.assertRaises(TypeError):
            metaknowledge.Record(set('a','b'))

    def test_equality(self):
        self.assertEqual(self.R, self.R)
        self.assertTrue(self.R != self.Rbad)
        self.assertFalse(self.R == 1)

    def test_contains(self):
        self.assertFalse('WOS' in self.R)
        self.assertTrue('C1' in self.R)

    def test_getitem(self):
        self.assertEqual(self.R['UT'], self.R.id)
        with self.assertRaises(TypeError):
            ret = self.R[1]

    def test_get(self):
        self.assertEqual(self.R.get('VL'), '1')
        self.assertEqual(self.R.get('volume'), '1')
        self.assertEqual(self.R.get('VL', raw = True), ['1'])
        self.assertEqual(self.R.get('volume', raw = True), ['1'])
        self.assertEqual(self.R.get('!@#$%^&*&%$#'), None)

    def test_values(self):
        self.assertTrue('1' in self.R.values())
        self.assertFalse('1' in self.R.values(raw = True))

    def test_items(self):
        self.assertTrue(('volume', '1') in self.R.items())
        self.assertTrue(('VL', ['1']) in self.R.items(raw = True))

    def test_hash(self):
        self.assertNotEqual(hash(self.R), hash(self.Rbad))

    def test_repr(self):
        self.assertEqual(repr(self.R), "< metaknowledge.WOSRecord object {} >".format(self.R.id))
        self.R.bad = True
        self.assertEqual(repr(self.R), "< metaknowledge.WOSRecord object BAD >")

    def test_binary(self):
        self.assertEqual(bytes(self.R), bytes(simplePaperString, encoding = 'utf-8'))
        self.R.bad = True
        with self.assertRaises(metaknowledge.BadRecord):
            b = bytes(self.R)
    def test_state(self):
        state = self.R.__getstate__()
        Rtmp = metaknowledge.Record('PT J')
        Rtmp.__setstate__(state)
        self.assertEqual(self.R, Rtmp)

    def test_title(self):
        self.assertEqual(self.R.title, "Example Paper")
        self.assertEqual(str(self.R), "WOSRecord(Example Paper)")

    def test_author(self):
        self.assertEqual(self.R['authorsFull'], ["John, Doe"])

    def test_year(self):
        self.assertEqual(self.R['year'], 2015)

    def test_month(self):
        self.assertEqual(self.R['month'], 4)

    def test_cites(self):
        self.assertEqual(str(self.R['citations'][0]), "John D. 1999, TOPICS IN COGNITIVE SCIENCE")

        self.assertEqual(len(self.R['citations']), 1)

    def test_WOS(self):
        self.assertEqual(self.R['wosString'], 'WOS:123317623000007')

    def test_citationGen(self):
        self.assertTrue(self.R.createCitation() == metaknowledge.Citation("John D, 2015, EXAMPLE, V1, P1, DOI 10.1111"))

    def test_journal(self):
        self.assertEqual(self.R['journal'], 'TOPICS IN COGNITIVE SCIENCE')

    def test_tags(self):
        self.assertEqual(self.R.subDict(['a', 'b']), {'a': None, 'b': None})

simplePaperString = """PT J
AU John, D
AF John, Doe
TI Example Paper
SO TOPICS IN COGNITIVE SCIENCE
LA English
DT Article
DE Example; testing
ID REAL; TIME
AB This is a test.
C1 UW, Ontario, Canada.
RP John, D (reprint author), UW, Ontario, Canada.
CR John D. 1999, TOPICS IN COGNITIVE SCIENCE
J9 EXAMPLE
JI examaple
PD APR
PY 2015
VL 1
BP 1
EP 2
DI 10.1111
UT WOS:123317623000007
ER
"""
