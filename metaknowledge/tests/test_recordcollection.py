import unittest
import metaknowledge
import metaknowledge.tagProcessing
import os
import filecmp
import copy
import networkx as nx

class TestRecordCollection(unittest.TestCase):

    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")
        self.RCbad = metaknowledge.RecordCollection("metaknowledge/tests/badFile.isi")

    def test_iscollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)
        self.assertEqual(repr(metaknowledge.RecordCollection()), "empty")
        self.assertTrue(self.RC == self.RC)

    def test_bad(self):
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/badFile.isi').bad)
        with self.assertRaises(TypeError):
            metaknowledge.RecordCollection('metaknowledge/tests/testFile.isi', extension= '.txt')
        self.assertTrue(self.RCbad + self.RC <= self.RC + self.RCbad)
        self.assertTrue(len(self.RCbad + self.RCbad) == 0)
        self.assertFalse(self.RCbad == self.RC)

    def test_badRecords(self):
        badRecs = self.RC.getBadRecords()
        self.assertTrue(badRecs <= self.RC)
        self.assertTrue(badRecs.pop().bad)
        self.RC.dropBadRecords()

    def test_dropJourn(self):
        RCcopy = copy.copy(self.RC)
        self.RC.dropNonJournals()
        self.assertEqual(len(self.RC), len(RCcopy) - 2)
        self.RC.dropNonJournals(invert = True)
        self.assertEqual(len(self.RC), 0)
        RCcopy.dropNonJournals(ptVal = 'B')
        self.assertEqual(len(RCcopy), 1)

    def test_addRec(self):
        l = len(self.RC)
        R = self.RC.pop()
        self.assertEqual(len(self.RC), l - 1)
        self.RC.addRec(R)
        self.assertEqual(len(self.RC), l)
        RC2 = metaknowledge.RecordCollection("metaknowledge/tests/TwoPaper.isi")
        self.RC.addRec(RC2)
        self.assertEqual(len(self.RC), l + 2)

    def test_getWOS(self):
        self.RC.dropBadRecords()
        R = self.RC.peak()
        l = len(self.RC)
        self.assertTrue(R, self.RC.getWOS(R.UT))
        self.assertEqual(len(self.RC), l)
        self.RC.dropWOS(R.UT)
        self.assertEqual(len(self.RC), l - 1)
        self.RC.getWOS(self.RC.peak().UT, drop = True)
        self.assertEqual(len(self.RC), l - 2)
        self.assertFalse(self.RC.getWOS(self.RC.pop().UT))
        with self.assertRaises(ValueError):
            self.RC.getWOS("asdfghjkjhgfdsdfghj")
            self.RC.dropWOS("asdfghjkjhgfdsdfghj")

    def test_directoryRead(self):
        self.assertEqual(len(metaknowledge.RecordCollection('.')), 0)
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/') >= self.RC)
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/', extension= '.txt') <= self.RC)

    def test_write(self):
        fileName = 'OnePaper2.isi'
        RC = metaknowledge.RecordCollection('metaknowledge/tests/' + fileName)
        RC.writeFile(fileName + '.tmp')
        RC.writeFile()
        self.assertTrue(filecmp.cmp('metaknowledge/tests/' + fileName, fileName + '.tmp'))
        self.assertTrue(filecmp.cmp('metaknowledge/tests/' + fileName, repr(RC)[:200] + '.isi'))
        os.remove(fileName + '.tmp')
        os.remove(repr(RC)[:200] + '.isi')

    def test_writeCSV(self):
        filename = "test_writeCSV_temporaryFile.csv"
        if os.path.isfile(filename):
            os.remove(filename)
        self.RC.writeCSV(filename, onlyTheseTags=['UT', 'PT', 'TI', 'AF','J9' ,'CR', 'pubMedID'], firstTags = ['CR', 'UT', 'J9', 'citations'], csvDelimiter = '∂', csvQuote='≠', listDelimiter= '«', longNames=True, numAuthors = False)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 106373)
        os.remove(filename)
        self.RC.writeCSV(filename)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 88346)
        os.remove(filename)

    def test_makeDict(self):
        d = self.RC.makeDict(onlyTheseTags = list(metaknowledge.tagProcessing.tagsAndNameSet), longNames = True)
        self.assertEqual(len(d), 62)
        self.assertEqual(len(d['wosString']), len(self.RC))
        self.assertEqual(d['eISSN'][0], None)
        self.assertIsInstance(d['citations'], list)
        d = self.RC.makeDict(longNames = False, cleanedVal = False, numAuthors = False)
        self.assertEqual(len(d), 42)
        self.assertEqual(len(d['UT']), len(self.RC))
        self.assertIsInstance(d['CR'], list)

    def test_coCite(self):
        Gdefault = self.RC.coCiteNetwork(fullInfo = True)
        Gauths = self.RC.coCiteNetwork(nodeType = "author", dropAnon = False)
        GauthsNoExtra = self.RC.coCiteNetwork(nodeType = "author", nodeInfo = False)
        Gunwei = self.RC.coCiteNetwork(nodeType = 'original', weighted = False)
        Gjour = self.RC.coCiteNetwork(nodeType = "journal", dropNonJournals = True)
        Gyear = self.RC.coCiteNetwork(nodeType = "year", fullInfo = True, count = False)
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertLessEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertLessEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()) - 1 )
        self.assertTrue('weight' in Gdefault.edges(data = True)[0][2])
        self.assertTrue('info' in Gdefault.nodes(data = True)[0][1])
        self.assertTrue('fullCite' in Gdefault.nodes(data = True)[0][1])
        self.assertFalse('weight' in Gunwei.edges(data = True)[0][2])
        self.assertEqual(len(Gdefault.nodes()), 492)
        self.assertEqual(len(Gdefault.edges()), 12968)
        self.assertEqual(len(Gauths.nodes()), 323)
        self.assertEqual(len(Gauths.edges()), 6777)
        self.assertEqual(len(Gyear.nodes()), 91)
        self.assertEqual(len(Gyear.edges()), 1926)
        self.assertEqual(len(Gjour.nodes()), 85)
        self.assertEqual(len(Gjour.edges()), 1195)
        self.assertTrue('info' in Gjour.nodes(data=True)[0][1])
        self.assertTrue('info' in Gyear.nodes(data=True)[0][1])
        self.assertTrue('fullCite' in Gyear.nodes(data = True)[0][1])

    def test_coAuth(self):
        Gdefault = self.RC.coAuthNetwork()
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertEqual(len(Gdefault.nodes()), 45)
        self.assertEqual(len(Gdefault.edges()), 46)

    def test_Cite(self):
        Gdefault = self.RC.citationNetwork(fullInfo = True, count = False)
        Ganon = self.RC.citationNetwork(dropAnon = False)
        Gauths = self.RC.citationNetwork(nodeType = "author")
        GauthsNoExtra = self.RC.citationNetwork(nodeType = "author", nodeInfo = False)
        Gunwei = self.RC.citationNetwork(nodeType = 'original', weighted = False)
        Gjour = self.RC.citationNetwork(nodeType = "author", dropNonJournals = True, nodeInfo = True, count = False)
        Gyear = self.RC.citationNetwork(nodeType = "year", nodeInfo = True)
        self.assertIsInstance(Gdefault, nx.classes.digraph.DiGraph)
        self.assertLessEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertLessEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()))
        self.assertTrue('weight' in Gdefault.edges(data = True)[0][2])
        self.assertTrue('info' in Gdefault.nodes(data = True)[0][1])
        self.assertFalse('weight' in Gunwei.edges(data = True)[0][2])
        self.assertEqual(len(Gdefault.nodes()), 509)
        self.assertEqual(len(Ganon.nodes()), 510)
        self.assertEqual(len(Gauths.nodes()), 326)
        self.assertEqual(len(Gdefault.edges()), 815)
        self.assertEqual(len(Ganon.edges()), 816)
        self.assertEqual(len(Gauths.edges()), 570)
        self.assertEqual(len(Gjour.edges()), 432)
        self.assertTrue('info' in Gjour.nodes(data=True)[0][1])
        self.assertTrue('info' in Gyear.nodes(data=True)[0][1])


    def test_oneMode(self):
        Gcr  = self.RC.oneModeNetwork('CR')
        Gcite = self.RC.oneModeNetwork('citations', nodeCount = False, edgeWeight = False)
        GcoCit = self.RC.coCiteNetwork()
        Gtit = self.RC.oneModeNetwork('title')
        stemFunc = lambda x: x[:-1]
        Gstem = self.RC.oneModeNetwork('keywords', stemmer = stemFunc)
        self.assertEqual(len(Gcite.edges()), len(Gcr.edges()))
        self.assertEqual(len(Gcite.nodes()), len(Gcr.nodes()))
        self.assertAlmostEqual(len(Gcite.nodes()), len(GcoCit.nodes()), delta = 50)
        self.assertEqual(len(self.RC.oneModeNetwork('D2').nodes()), 0)
        self.assertEqual(len(Gtit.nodes()), 31)
        self.assertEqual(len(Gtit.edges()), 0)
        self.assertEqual(len(self.RC.oneModeNetwork('email').edges()), 3)
        self.assertEqual(len(self.RC.oneModeNetwork('UT').nodes()), len(self.RC) - 1)
        self.assertEqual(metaknowledge.graphStats(Gstem), 'The graph has 41 nodes, 142 edges, 2 isolates, 0 self loops, a density of 0.173171 and a transitivity of 0.854015')
        self.assertIsInstance(Gstem.nodes()[0], str)
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
        G = self.RC.nModeNetwork(metaknowledge.tagProcessing.tagToFullDict.keys())
        self.assertEqual(len(G.nodes()), 1186)
        self.assertEqual(len(G.edges()), 38592)

    def test_localCiteStats(self):
        d = self.RC.localCiteStats()
        dPan = self.RC.localCiteStats(pandasFriendly = True)
        dYear = self.RC.localCiteStats(keyType = 'year')
        self.assertEqual(d[metaknowledge.Citation("Azzam R. M. A., 1977, ELLIPSOMETRY POLARIZ")], 1)
        self.assertEqual(len(dPan['Citations']),len(d))
        self.assertTrue(dPan['Citations'][0] in d)
        self.assertEqual(dYear[2009], 2)

    def test_localCitesOf(self):
        C = metaknowledge.Citation("COSTADEB.O, 1974, LETT NUOVO CIMENTO, V10, P852")
        self.assertEqual("WOS:A1976CW02200002", self.RC.localCitesOf(C).peak().UT)
        self.assertEqual(self.RC.localCitesOf(self.RC.peak().UT), self.RC.localCitesOf(self.RC.peak().createCitation()))

    def test_citeFilter(self):
        RCmin = self.RC.citeFilter('', reverse = True)
        RCmax = self.RC.citeFilter('')
        RCanon = self.RC.citeFilter('', 'anonymous')
        RC1970 = self.RC.citeFilter(1970, 'year')
        RCno1970 = self.RC.citeFilter(1970, 'year', reverse = True)
        RCMELLER = self.RC.citeFilter('meller', 'author')
        self.assertEqual(len(RCmin), 0)
        self.assertEqual(len(RCmax), len(self.RC))
        self.assertEqual(len(RCanon), 1)
        self.assertEqual(len(RC1970), 15)
        self.assertEqual(len(RC1970) + len(RCno1970), len(self.RC))
        self.assertEqual(len(RCMELLER), 1)
        RCnocite = metaknowledge.RecordCollection('metaknowledge/tests/OnePaperNoCites.isi')
        self.assertEqual(len(RCnocite.citeFilter('')), 0)
