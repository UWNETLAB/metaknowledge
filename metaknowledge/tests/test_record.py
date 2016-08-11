#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge

class TestRecord(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.R = metaknowledge.WOSRecord(simplePaperString)
        self.Rbad = metaknowledge.WOSRecord(simplePaperString[:-3])

    def test_isRecord(self):
        self.assertTrue(isinstance(self.R, metaknowledge.WOSRecord))

    def test_base(self):
        metaknowledge.ExtendedRecord.__abstractmethods__ = frozenset()
        R = metaknowledge.ExtendedRecord(self.R._fieldDict, self.R.id, self.R.bad, self.R.error)
        self.assertEqual(R.encoding(), 'utf-8')
        with self.assertRaises(KeyError):
            R.specialFuncs('TI')
        self.assertEqual(R.writeRecord('IF_YOU_SEE_THIS_A_TEST_HAS_GONE_VERY_WRONG_PLEASE_TELL_SOMEONE.mk_test_file_that_you_should_never_see'), None)
        self.assertEqual(R.getAltName('TI'), None)
        self.assertEqual(R.tagProcessingFunc('TI')('A'), 'A')

    def test_bad(self):
        self.assertTrue(self.Rbad.bad)
        with self.assertRaises(TypeError):
            metaknowledge.WOSRecord(set('a','b'))

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

    def test_len(self):
        self.assertEqual(len(self.R), 22)

    def test_hash(self):
        self.assertNotEqual(hash(self.R), hash(self.Rbad))

    def test_repr(self):
        self.assertEqual(repr(self.R), "<metaknowledge.WOSRecord object {}>".format(self.R.id))
        self.R.bad = True
        self.assertEqual(repr(self.R), "<metaknowledge.WOSRecord object BAD>")

    def test_binary(self):
        self.assertEqual(bytes(self.R), bytes(simplePaperString, encoding = 'utf-8'))
        self.R.bad = True
        with self.assertRaises(metaknowledge.BadRecord):
            b = bytes(self.R)

    def test_state(self):
        state = self.R.__getstate__()
        Rtmp = metaknowledge.WOSRecord('PT J')
        Rtmp.__setstate__(state)
        self.assertEqual(self.R, Rtmp)

    def test_title(self):
        self.assertEqual(self.R.title, "Example Paper")
        self.assertEqual(str(self.R), "WOSRecord(Example Paper)")

    def test_author(self):
        R2 = self.R.copy()
        del R2._fieldDict['AF']
        self.assertEqual(self.R['authorsFull'], ["John, Doe"])
        self.assertEqual(self.R.authors, ["John, Doe"])
        self.assertEqual(R2.authors, ['John, D'])

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
        R2 = self.R.copy()
        R2._fieldDict['AU'] = ['John D', 'John H']
        R0 = self.R.copy()
        del R0._fieldDict['AU']
        del R0._fieldDict['AF']
        del R0._fieldDict['J9']
        self.assertTrue(self.R.createCitation() == metaknowledge.Citation("John D, 2015, EXAMPLE, V1, P1, DOI 10.1111"))
        self.assertTrue(R0.createCitation(multiCite = True)[0] == metaknowledge.Citation("2015, Example Paper, V1, P1, DOI 10.1111"))
        self.assertTrue(set(R2.createCitation(multiCite = True)) == set((self.R.createCitation(), metaknowledge.Citation("John H, 2015, EXAMPLE, V1, P1, DOI 10.1111"))))

    def test_journal(self):
        self.assertEqual(self.R['journal'], 'TOPICS IN COGNITIVE SCIENCE')

    def test_tags(self):
        self.assertEqual(self.R.subDict(['a', 'b']), {'a': None, 'b': None})

    def test_specials(self):
        for t in metaknowledge.commonRecordFields:
            if t not in ['id', 'address', 'grants', 'selfCitation']:
                self.assertIsInstance(self.R.getAltName(t), str)

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
