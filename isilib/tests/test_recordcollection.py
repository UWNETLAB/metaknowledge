import unittest
import isilib
import os
import filecmp
import networkx as nx

class TestRecordCollection(unittest.TestCase):

    def setUp(self):
        isilib.VERBOSE_MODE = False
        self.RC = isilib.RecordCollection("isilib/tests/testFile.isi")
        self.RCbad = isilib.RecordCollection("isilib/tests/badFile.isi")

    def test_iscollection(self):
        self.assertIsInstance(self.RC, isilib.RecordCollection)
        self.assertEqual(repr(isilib.RecordCollection()), "empty")
        self.assertTrue(self.RC == self.RC)

    def test_bad(self):
        self.assertTrue(isilib.RecordCollection('isilib/tests/badFile.isi').bad)
        with self.assertRaises(TypeError):
            isilib.RecordCollection('isilib/tests/testFile.isi', extension= '.txt')
        self.assertTrue(self.RCbad + self.RC <= self.RC + self.RCbad)
        self.assertTrue(len(self.RCbad + self.RCbad) == 0)
        self.assertFalse(self.RCbad == self.RC)

    def test_badRecords(self):
        badRecs = self.RC.getBadRecords()
        self.assertTrue(badRecs <= self.RC)
        self.assertTrue(badRecs.pop().bad)
        self.RC.dropBadRecords()

    def test_directoryRead(self):
        self.assertEqual(len(isilib.RecordCollection('.')), 0)
        self.assertTrue(isilib.RecordCollection('isilib/tests/') >= self.RC)
        self.assertTrue(isilib.RecordCollection('isilib/tests/', extension= '.txt') <= self.RC)

    def test_write(self):
        fileName = 'OnePaper2.isi'
        RC = isilib.RecordCollection('isilib/tests/' + fileName)
        RC.writeFile(fileName + '.tmp')
        RC.writeFile()
        self.assertTrue(filecmp.cmp('isilib/tests/' + fileName, fileName + '.tmp'))
        self.assertTrue(filecmp.cmp('isilib/tests/' + fileName, repr(RC)[:200] + '.isi'))
        os.remove(fileName + '.tmp')
        os.remove(repr(RC)[:200] + '.isi')

    def test_writeCSV(self):
        filename = "test_writeCSV_temporaryFile.csv"
        if os.path.isfile(filename):
            os.remove(filename)
        self.RC.writeCSV(filename, onlyTheseTags=['UT', 'PT', 'TI', 'AF','J9' ,'CR', 'pubMedID'], firstTags = ['CR', 'UT', 'J9', 'citations'], csvDelimiter = '∂', csvQuote='≠', listDelimiter= '«', longNames=True)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 106373)
        os.remove(filename)
        self.RC.writeCSV(filename)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 88201)
        os.remove(filename)


    def test_coCite(self):
        Gdefault = self.RC.coCiteNetwork()
        Gauths = self.RC.coCiteNetwork(authorship = True, dropAnon = False)
        GauthsNoExtra = self.RC.coCiteNetwork(authorship = True, extraInfo = False)
        Gunwei = self.RC.coCiteNetwork(weighted = False)
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()) - 1 )
        self.assertTrue('weight' in Gdefault.edges(data = True)[0][2])
        self.assertTrue('info' in Gdefault.nodes(data = True)[0][1])
        self.assertFalse('weight' in Gunwei.edges(data = True)[0][2])
        self.assertEqual(len(Gdefault.nodes()), 518)
        self.assertEqual(len(Gdefault.edges()), 14775)
        self.assertEqual(len(Gauths.nodes()), 322)
        self.assertEqual(len(Gauths.edges()), 6996)

    def test_coAuth(self):
        Gdefault = self.RC.coAuthNetwork()
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertEqual(len(Gdefault.nodes()), 45)
        self.assertEqual(len(Gdefault.edges()), 46)

    def test_Cite(self):
        Gdefault = self.RC.citationNetwork()
        Ganon = self.RC.citationNetwork(dropAnon = False)
        Gauths = self.RC.citationNetwork(authorship = True)
        GauthsNoExtra = self.RC.citationNetwork(authorship = True, extraInfo = False)
        Gunwei = self.RC.citationNetwork(weighted = False)
        self.assertIsInstance(Gdefault, nx.classes.digraph.DiGraph)
        self.assertEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()))
        self.assertTrue('weight' in Gdefault.edges(data = True)[0][2])
        self.assertTrue('info' in Gdefault.nodes(data = True)[0][1])
        self.assertFalse('weight' in Gunwei.edges(data = True)[0][2])
        self.assertGreater(len(Gdefault.nodes()), len(Gauths.nodes()))
        self.assertGreater(len(Ganon.nodes()), len(Gdefault.nodes()))
        self.assertEqual(len(Gdefault.nodes()), 535)
        self.assertEqual(len(Ganon.nodes()), 536)
        self.assertEqual(len(Gauths.nodes()), 325)
        self.assertEqual(len(Gdefault.edges()), 847)
        self.assertEqual(len(Ganon.edges()), 848)
        self.assertEqual(len(Gauths.edges()), 569)


    def test_oneMode(self):
        Gcr  = self.RC.oneModeNetwork('CR')
        Gcite = self.RC.oneModeNetwork('citations', nodeCount = False, edgeWeight = False)
        GcoCit = self.RC.coCiteNetwork()
        Gtit = self.RC.oneModeNetwork('title')
        self.assertEqual(len(Gcite.edges()), len(Gcr.edges()))
        self.assertEqual(len(Gcite.nodes()), len(Gcr.nodes()))
        self.assertAlmostEqual(len(Gcite.nodes()), len(GcoCit.nodes()), delta = 50)
        self.assertEqual(len(self.RC.oneModeNetwork('D2').nodes()), 0)
        self.assertEqual(len(Gtit.nodes()), 31)
        self.assertEqual(len(Gtit.edges()), 0)
        self.assertEqual(len(self.RC.oneModeNetwork('email').edges()), 3)
        self.assertEqual(len(self.RC.oneModeNetwork('UT').nodes()), len(self.RC) - 1)
        with self.assertRaises(TypeError):
            G = self.RC.oneModeNetwork('Not a Tag')
            del G

    def test_twoMode(self):
        self.RC.dropBadRecords()
        Gutti = self.RC.twoModeNetwork('UT', 'title', directed = True, recordType = False)
        Gafwc = self.RC.twoModeNetwork('AF', 'WC', nodeCount = False, edgeWeight = False)
        Gd2em = self.RC.twoModeNetwork('D2', 'email')
        Gemd2 = self.RC.twoModeNetwork('email', 'D2')
        self.assertIsInstance(Gutti, nx.classes.digraph.DiGraph)
        self.assertIsInstance(Gafwc, nx.classes.graph.Graph)
        self.assertEqual(Gutti.edges('WOS:A1979GV55600001')[0][1][:31], "EXPERIMENTS IN PHENOMENOLOGICAL")
        self.assertEqual(len(Gutti.nodes()), 2 * len(self.RC) - 1)
        with self.assertRaises(TypeError):
            G = self.RC.oneModeNetwork('Not a Tag', 'TI')
            del G
        self.assertTrue(nx.is_isomorphic(Gd2em, Gemd2))

    def test_nMode(self):
        G = self.RC.nModeNetwork(isilib.tagToFull.keys())
        self.assertEqual(len(G.nodes()), 1185)
        self.assertEqual(len(G.edges()), 38557)

    def test_citeFilter(self):
        RCmin = self.RC.citeFilter('', reverse = True)
        RCmax = self.RC.citeFilter('')
        RCanon = self.RC.citeFilter('', 'anonymous')
        RC1970 = self.RC.citeFilter('1970', 'year')
        RCno1970 = self.RC.citeFilter(1970, 'year', reverse = True)
        RCMELLER = self.RC.citeFilter('meller', 'author')
        self.assertEqual(len(RCmin), 0)
        self.assertEqual(len(RCmax), len(self.RC))
        self.assertEqual(len(RCanon), 1)
        self.assertEqual(len(RC1970), 15)
        self.assertEqual(len(RC1970) + len(RCno1970), len(self.RC))
        self.assertEqual(len(RCMELLER), 1)
