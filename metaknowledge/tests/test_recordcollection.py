#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge
import metaknowledge.WOS
import os
import filecmp
import networkx as nx

disableJournChecking = True

class TestRecordCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        metaknowledge.VERBOSE_MODE = False
        cls.RCmain = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")
        cls.RCbadmain = metaknowledge.RecordCollection("metaknowledge/tests/badFile.isi")

    def setUp(self):
        self.RC = self.RCmain.copy()
        self.RCbad = self.RCbadmain.copy()

    def test_isCollection(self):
        self.assertIsInstance(self.RC, metaknowledge.RecordCollection)
        self.assertEqual(str(metaknowledge.RecordCollection()), "RecordCollection(Empty)")
        self.assertTrue(self.RC == self.RC)

    def test_fullRead(self):
        RC = metaknowledge.RecordCollection("metaknowledge/tests/")
        self.assertEqual(len(RC), 1032)

    def test_caching(self):
        RC = metaknowledge.RecordCollection("metaknowledge/tests/", cached = True, name = 'testingCache', extension = 'testFile.isi')
        self.assertTrue(os.path.isfile("metaknowledge/tests/tests.[testFile.isi].mkRecordDirCache"))
        accessTime = os.stat("metaknowledge/tests/testFile.isi").st_atime
        RC2 = metaknowledge.RecordCollection("metaknowledge/tests/", cached = True, name = 'testingCache', extension = 'testFile.isi')
        self.assertEqual(accessTime, os.stat("metaknowledge/tests/testFile.isi").st_atime)
        RC.dropBadEntries()
        RC2.dropBadEntries()
        self.assertEqual(RC, RC2)
        os.remove("metaknowledge/tests/tests.[testFile.isi].mkRecordDirCache")

    def test_bad(self):
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/badFile.isi').bad)
        with self.assertRaises(metaknowledge.mkExceptions.RCTypeError):
            metaknowledge.RecordCollection('metaknowledge/tests/testFile.isi', extension = '.txt')
        self.assertEqual(self.RCbad | self.RC, self.RCbad | self.RC )
        self.assertEqual(len(self.RCbad | self.RCbad), 32)
        self.assertFalse(self.RCbad == self.RC)
        self.assertEqual('/Users/Reid/Documents/Work/NetworksLab/metaknowledge/metaknowledge/tests/badFile.isi', self.RCbad.errors.keys().__iter__().__next__())

    def test_badEntries(self):
        badRecs = self.RC.badEntries()
        self.assertTrue(badRecs <= self.RC)
        self.assertTrue(badRecs.pop().bad)
        self.RC.dropBadEntries()

    def test_dropJourn(self):
        RCcopy = self.RC.copy()
        self.RC.dropNonJournals()
        self.assertEqual(len(self.RC), len(RCcopy) - 2)
        self.RC.dropNonJournals(invert = True)
        self.assertEqual(len(self.RC), 0)
        RCcopy.dropNonJournals(ptVal = 'B')
        self.assertEqual(len(RCcopy), 1)

    def test_repr(self):
        self.assertEqual(repr(self.RC), "<metaknowledge.RecordCollection object testFile>")

    def test_hash(self):
        self.assertNotEqual(hash(self.RC), hash(self.RCbad))
        R = self.RC.pop()
        RC = metaknowledge.RecordCollection([R])
        self.assertEqual(hash(RC), hash(hash(R)))

    def test_contains(self):
        R = self.RC.peek()
        self.assertTrue(R in self.RC)
        R = self.RC.pop()
        self.assertFalse(R in self.RC)

    def test_conID(self):
        R = self.RC.peek()
        self.assertTrue(self.RC.containsID(R.id))
        self.assertFalse(self.RC.containsID('234567654'))

    def test_discard(self):
        R = self.RC.peek()
        l = len(self.RC)
        self.RC.discard(R)
        l2 = len(self.RC)
        self.assertEqual(l, l2 + 1)
        self.RC.discard(R)
        self.assertEqual(l2, len(self.RC))

    def test_pop(self):
        R = self.RC.pop()
        self.assertFalse(R in self.RC)
        self.RC.clear()
        with self.assertRaises(KeyError):
            R = self.RC.pop()

    def test_peek(self):
        R = self.RC.peek()
        self.assertTrue(R in self.RC)
        self.RC.clear()
        R = self.RC.peek()
        self.assertTrue(R is None)

    def test_clear(self):
        R = self.RCbad.peek()
        self.assertTrue(self.RCbad.bad)
        self.RCbad.clear()
        self.assertFalse(self.RCbad.bad)
        self.assertFalse(R in self.RCbad)

    def test_remove(self):
        R = self.RC.peek()
        l = len(self.RC)
        self.RC.remove(R)
        self.assertEqual(l, len(self.RC) + 1)
        with self.assertRaises(KeyError):
            self.RC.remove(R)

    def test_equOps(self):
        l = len(self.RC)
        for i in range(10):
            self.RCbad.pop()
        lb = len(self.RCbad)
        RC = metaknowledge.RecordCollection([])
        RC.bad = True
        RC |= self.RC
        self.assertEqual(self.RC, RC)
        RC -= self.RC
        self.assertNotEqual(self.RC, RC)
        RC ^= self.RC
        self.assertEqual(self.RC, RC)
        RC &= self.RCbad
        self.assertNotEqual(self.RC, RC)

    def test_newOps(self):
        l = len(self.RC)
        for i in range(10):
            self.RCbad.pop()
        lb = len(self.RCbad)
        RC = metaknowledge.RecordCollection([])
        RC.bad = True
        RC3 = self.RC | RC
        self.assertEqual(self.RC, RC3)
        RC4 = RC3 - self.RC
        self.assertNotEqual(self.RC, RC4)
        RC5 = RC4 ^ self.RC
        self.assertEqual(self.RC, RC5)
        RC6 = RC5 & self.RCbad
        self.assertNotEqual(self.RC, RC6)

    def test_opErrors(self):
        with self.assertRaises(TypeError):
            self.RC <= 1
        with self.assertRaises(TypeError):
            self.RC >= 1
        self.assertTrue(self.RC != 1)
        with self.assertRaises(TypeError):
            self.RC >= 1
        with self.assertRaises(TypeError):
            self.RC |= 1
        with self.assertRaises(TypeError):
            self.RC ^= 1
        with self.assertRaises(TypeError):
            self.RC &= 1
        with self.assertRaises(TypeError):
            self.RC -= 1
        with self.assertRaises(TypeError):
            self.RC | 1
        with self.assertRaises(TypeError):
            self.RC ^ 1
        with self.assertRaises(TypeError):
            self.RC & 1
        with self.assertRaises(TypeError):
            self.RC - 1

    def test_addRec(self):
        l = len(self.RC)
        R = self.RC.pop()
        self.assertEqual(len(self.RC), l - 1)
        self.RC.add(R)
        self.assertEqual(len(self.RC), l)
        RC2 = metaknowledge.RecordCollection("metaknowledge/tests/TwoPaper.isi")
        self.RC |= RC2
        self.assertEqual(len(self.RC), l + 2)
        with self.assertRaises(metaknowledge.CollectionTypeError):
            self.RC.add(1)

    def test_bytes(self):
        with self.assertRaises(metaknowledge.BadRecord):
            self.assertIsInstance(bytes(self.RC), bytes)
        self.RC.dropBadEntries()
        self.assertIsInstance(bytes(self.RC), bytes)

    def test_WOS(self):
        self.RC.dropBadEntries()
        R = self.RC.peek()
        l = len(self.RC)
        self.assertTrue(R, self.RC.getID(R.id))
        self.assertEqual(len(self.RC), l)
        self.RC.removeID(R.id)
        self.assertEqual(len(self.RC), l - 1)
        self.RC.getID(self.RC.peek().id)
        self.assertEqual(len(self.RC), l - 1)
        self.assertFalse(self.RC.getID(self.RC.pop().id))
        self.RC.discardID('sdfghjkjhgfdfghj')
        self.RC.discardID('WOS:A1979GV55600001')
        with self.assertRaises(KeyError):
            self.RC.removeID('ghjkljhgfdfghjmh')

    def test_directoryRead(self):
        self.assertEqual(len(metaknowledge.RecordCollection('.')), 0)
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/') >= self.RC)
        self.assertTrue(metaknowledge.RecordCollection('metaknowledge/tests/', extension= '.txt') <= self.RC)

    def test_contentType(self):
        RC = metaknowledge.RecordCollection('metaknowledge/tests/')
        self.assertEqual(RC._collectedTypes, {'MedlineRecord', 'WOSRecord', 'ProQuestRecord', 'ScopusRecord'})
        self.assertEqual(self.RC._collectedTypes, {'WOSRecord'})

    def test_write(self):
        fileName = 'OnePaper2.isi'
        RC = metaknowledge.RecordCollection('metaknowledge/tests/' + fileName)
        RC.writeFile(fileName + '.tmp')
        RC.writeFile()
        self.assertTrue(filecmp.cmp('metaknowledge/tests/' + fileName, fileName + '.tmp'))
        self.assertTrue(filecmp.cmp('metaknowledge/tests/' + fileName, RC.name + '.txt'))
        os.remove(fileName + '.tmp')
        os.remove(RC.name + '.txt')

    def test_writeCSV(self):
        filename = "test_writeCSV_temporaryFile.csv"
        if os.path.isfile(filename):
            os.remove(filename)
        self.RC.writeCSV(filename, onlyTheseTags=['UT', 'PT', 'TI', 'AF','J9' ,'CR', 'pubMedID'], firstTags = ['CR', 'UT', 'J9', 'citations'], csvDelimiter = '∂', csvQuote='≠', listDelimiter= '«', longNames=True, numAuthors = False)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 107396)
        os.remove(filename)
        self.RC.writeCSV(filename)
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(os.path.getsize(filename), 89272)
        os.remove(filename)
        self.RC.writeCSV(splitByTag = 'PY', onlyTheseTags = ['id', 'title', 'authorsFull', 'citations', 'keywords', 'DOI'])
        yearsSt = set()
        for R in self.RC:
            yearsSt.add(str(R.get('PY', 2012)))
        for year in yearsSt:
            f = open("{}-testFile.csv".format(year))
            self.assertEqual(f.readline(), '"id","TI","AF","CR","ID","DI","num-Authors","num-Male","num-Female","num-Unknown"\n')
            self.assertGreater(len(f.readline()), 1)
            f.close()
            os.remove("{}-testFile.csv".format(year))

    def test_writeBib(self):
        filename = 'testFile.bib'
        if os.path.isfile(filename):
            os.remove(filename)
        self.RC.dropBadEntries()
        self.RC.writeBib(maxStringLength = 100)
        self.assertEqual(os.path.getsize(filename), 100418)
        os.remove(filename)
        self.RC.writeBib(fname = filename, wosMode = True, reducedOutput = True, niceIDs = False)
        self.assertEqual(os.path.getsize(filename), 78163)
        os.remove(filename)

    def test_rpys(self):
        d = self.RC.rpys()
        self.assertIn(17, d['count'])
        d = self.RC.rpys(1990, 2000)
        self.assertEqual(len(d['year']), 11)
        for v in d.values():
            for i in v:
                self.assertIsInstance(i, int)

    def test_CopyrightFinder(self):
        l = self.RC.findProbableCopyright()
        self.assertEqual(len(l), 7)
        l = self.RC.findProbableCopyright()
        self.assertTrue(' (C) 2002 Optical Society of America.' in l)

    def test_NLP(self):
        filename = 'NLP_test.csv'
        full = self.RC.forNLP(filename, removeCopyright = True, extraColumns = ['ID'])
        self.assertEqual(len(full), 7)
        self.assertEqual(len(full['id']), 33)
        self.assertEqual(full['keywords'][0], full['ID'][0])
        self.assertTrue(' (C) 2002 Optical Society of America.' in full['copyright'])
        self.assertEqual(os.path.getsize(filename), 14445)
        os.remove(filename)
        dropping = self.RC.forNLP(filename,removeNumbers = False, dropList = ['a', 'and', 'the', 'is'], stemmer = lambda x: x.title())
        self.assertEqual(len(dropping), 5)
        self.assertEqual(len(dropping['id']), 33)
        self.assertEqual(os.path.getsize(filename), 12901)
        os.remove(filename)

    def test_forBurst(self):
        filename = 'Burst_test.csv'
        full = self.RC.forBurst('keywords', outputFile = filename)
        self.assertEqual(len(full), 2)
        self.assertEqual(len(full['year']), 75)
        self.assertIn('guides', full['word'])
        os.remove(filename)

    def test_genderStats(self):
        stats = self.RC.genderStats()
        self.assertEqual(stats, {'Unknown': 65, 'Male': 6, 'Female': 1})
        stats = self.RC.genderStats(asFractions = True)
        self.assertEqual(stats['Male'], 0.08333333333333333)

    def test_getCitations(self):
        cites = self.RC.getCitations()
        self.assertIn('LAUE MV, 1920, RELATIVITATSTHEORIE, V1, P227', cites['citeString'])

    def test_makeDict(self):
        d = self.RC.makeDict(onlyTheseTags = list(metaknowledge.WOS.tagsAndNameSet), longNames = True)
        self.assertEqual(len(d), 65)
        self.assertEqual(len(d['wosString']), len(self.RC))
        if d['eISSN'][0] == '2155-3165':
            self.assertEqual(d['eISSN'][1], None)
        else:
            self.assertEqual(d['eISSN'][0], None)
        self.assertIsInstance(d['citations'], list)
        d = self.RC.makeDict(longNames = False, raw = True, numAuthors = False)
        self.assertEqual(len(d), 45)
        self.assertEqual(len(d['UT']), len(self.RC))
        self.assertIsInstance(d['CR'], list)

    def test_coCite(self):
        Gdefault = self.RC.networkCoCitation(fullInfo = True)
        Gauths = self.RC.networkCoCitation(nodeType = "author", dropAnon = False, detailedCore = True)
        GauthsNoExtra = self.RC.networkCoCitation(nodeType = "author", nodeInfo = False)
        Gunwei = self.RC.networkCoCitation(nodeType = 'original', weighted = False)
        if not disableJournChecking:
            Gjour = self.RC.networkCoCitation(nodeType = "journal", dropNonJournals = True)
        Gyear = self.RC.networkCoCitation(nodeType = "year", fullInfo = True, count = False)
        Gcore = self.RC.networkCoCitation(detailedCore = ['AF','AU', 'DE', 'ID', 'PY'], coreOnly = True)
        Gexplode = self.RC.networkCoCitation(expandedCore = True, keyWords = 'a')
        Gcr = self.RC.networkCoCitation(addCR = True, coreOnly = True)
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertLessEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertLessEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()) - 1 )
        self.assertTrue('weight' in list(Gdefault.edges(data = True))[0][2])
        self.assertTrue('info' in list(Gdefault.nodes(data = True))[0][1])
        self.assertTrue('fullCite' in list(Gdefault.nodes(data = True))[0][1])
        self.assertFalse('weight' in list(Gunwei.edges(data = True))[0][2])
        self.assertEqual(metaknowledge.graphStats(Gdefault, sentenceString = True), "The graph has 493 nodes, 13000 edges, 0 isolates, 22 self loops, a density of 0.107282 and a transitivity of 0.611431")
        self.assertEqual(metaknowledge.graphStats(Gauths, sentenceString = True), "The graph has 321 nodes, 6699 edges, 1 isolates, 68 self loops, a density of 0.131094 and a transitivity of 0.598575")
        self.assertEqual(metaknowledge.graphStats(Gyear, sentenceString = True), "The graph has 91 nodes, 1898 edges, 0 isolates, 55 self loops, a density of 0.47033 and a transitivity of 0.702332")
        if not disableJournChecking:
            self.assertEqual(len(Gjour.nodes()), 85)
            self.assertEqual(len(Gjour.edges()), 1195)
            self.assertTrue('info' in Gjour.nodes(data=True)[0][1])
        self.assertTrue('info' in list(Gyear.nodes(data=True))[0][1])
        self.assertTrue('fullCite' in list(Gyear.nodes(data = True))[0][1])
        self.assertEqual(Gcore.node['Costadebeauregard O, 1975, CAN J PHYS']['info'], 'COSTADEBEAUREGARD O, COSTADEBEAUREGARD O')
        self.assertEqual(metaknowledge.graphStats(Gexplode, sentenceString = True), "The graph has 73 nodes, 366 edges, 0 isolates, 5 self loops, a density of 0.140411 and a transitivity of 0.523179")
        self.assertIn('AUDOIN C, 1976, J PHYS E SCI INSTRUM', Gcr.node['Huard S, 1979, CAN J PHYS']['citations'])

    def test_coAuth(self):
        Gdefault = self.RC.networkCoAuthor()
        if not disableJournChecking:
            Gdetailed = self.RC.networkCoAuthor(count = False, weighted = False, detailedInfo = True, dropNonJournals = True)
        self.assertIsInstance(Gdefault, nx.classes.graph.Graph)
        self.assertEqual(len(Gdefault.nodes()), 45)
        self.assertEqual(len(Gdefault.edges()), 46)
        if not disableJournChecking:
            self.assertEqual(metaknowledge.graphStats(Gdetailed, sentenceString = True), 'The graph has 45 nodes, 46 edges, 9 isolates, 0 self loops, a density of 0.0464646 and a transitivity of 0.822581')

    def test_cite(self):
        Gdefault = self.RC.networkCitation(fullInfo = True, count = False, dropAnon = True)
        Ganon = self.RC.networkCitation(dropAnon = False)
        Gauths = self.RC.networkCitation(nodeType = "author", detailedCore = True, dropAnon = True)
        GauthsNoExtra = self.RC.networkCitation(nodeType = "author", nodeInfo = False, dropAnon = True)
        Gunwei = self.RC.networkCitation(nodeType = 'original', weighted = False)
        if not disableJournChecking:
            Gjour = self.RC.networkCitation(nodeType = "author", dropNonJournals = True, nodeInfo = True, count = False)
        Gyear = self.RC.networkCitation(nodeType = "year", nodeInfo = True)
        Gcore = self.RC.networkCitation(detailedCore = True, coreOnly = False)
        Gexplode = self.RC.networkCitation(expandedCore = True, keyWords = ['b', 'c'])
        self.assertIsInstance(Gdefault, nx.classes.digraph.DiGraph)
        self.assertLessEqual(len(Gdefault.edges()), len(Gunwei.edges()))
        self.assertLessEqual(len(Gdefault.nodes()), len(Gunwei.nodes()))
        self.assertEqual(len(GauthsNoExtra.edges()), len(Gauths.edges()))
        self.assertEqual(len(GauthsNoExtra.nodes()), len(Gauths.nodes()))
        self.assertTrue('weight' in list(Gdefault.edges(data = True))[0][2])
        self.assertTrue('info' in list(Gdefault.nodes(data = True))[0][1])
        self.assertFalse('weight' in list(Gunwei.edges(data = True))[0][2])
        self.assertEqual(metaknowledge.graphStats(Gdefault, sentenceString = True), "The graph has 510 nodes, 816 edges, 1 isolates, 0 self loops, a density of 0.00314342 and a transitivity of 0.00600437")
        self.assertEqual(metaknowledge.graphStats(Ganon, sentenceString = True), "The graph has 511 nodes, 817 edges, 0 isolates, 0 self loops, a density of 0.00313495 and a transitivity of 0.00600437")
        self.assertEqual(metaknowledge.graphStats(Gauths, sentenceString = True), "The graph has 324 nodes, 568 edges, 1 isolates, 15 self loops, a density of 0.00542751 and a transitivity of 0.0210315")
        if not disableJournChecking:
            self.assertEqual(len(Gjour.edges()), 432)
            self.assertTrue('info' in list(Gjour.nodes(data=True))[0][1])
        self.assertTrue('info' in list(Gyear.nodes(data=True))[0][1])
        self.assertEqual(Gcore.node['Gilles H, 2002, OPT LETT']['info'], 'WOS:000177484300017, Gilles H, Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector, OPTICS LETTERS, 27, 1421')
        self.assertEqual(metaknowledge.graphStats(Gexplode, sentenceString = True), "The graph has 19 nodes, 29 edges, 0 isolates, 3 self loops, a density of 0.0847953 and a transitivity of 0.132075")

    def test_networkBibCoupling(self):
        G = self.RC.networkBibCoupling()
        self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 32 nodes, 304 edges, 1 isolates, 0 self loops, a density of 0.612903 and a transitivity of 0.836511')

    def test_coOccurnce(self):
        self.assertEqual(sum(self.RC.cooccurrenceCounts('TI', *tuple(self.RC.tags()))['Longitudinal and transverse effects of nonspecular reflection'].values()), 104)

    def test_nLevel(self):
        G = self.RC.networkMultiLevel(*tuple(self.RC.tags()))
        self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 1187 nodes, 58731 edges, 0 isolates, 59 self loops, a density of 0.0834803 and a transitivity of 0.493814')

    def test_oneMode(self):
        Gcr  = self.RC.networkOneMode('CR')
        Gcite = self.RC.networkOneMode('citations', nodeCount = False, edgeWeight = False)
        GcoCit = self.RC.networkCoCitation()
        Gtit = self.RC.networkOneMode('title')
        stemFunc = lambda x: x[:-1]
        Gstem = self.RC.networkOneMode('keywords', stemmer = stemFunc)
        self.assertEqual(len(Gcite.edges()), len(Gcr.edges()))
        self.assertEqual(len(Gcite.nodes()), len(Gcr.nodes()))
        self.assertAlmostEqual(len(Gcite.nodes()), len(GcoCit.nodes()), delta = 50)
        self.assertEqual(len(self.RC.networkOneMode('D2').nodes()), 0)
        self.assertEqual(len(Gtit.nodes()), 31)
        self.assertEqual(len(Gtit.edges()), 0)
        self.assertEqual(len(self.RC.networkOneMode('email').edges()), 3)
        self.assertEqual(len(self.RC.networkOneMode('UT').nodes()), len(self.RC) - 1)
        self.assertEqual(metaknowledge.graphStats(Gstem, sentenceString = True), 'The graph has 41 nodes, 142 edges, 2 isolates, 0 self loops, a density of 0.173171 and a transitivity of 0.854015')
        self.assertIsInstance(list(Gstem.nodes())[0], str)
        with self.assertRaises(TypeError):
            G = self.RC.networkOneMode(b'Not a Tag')
            del G

    def test_twoMode(self):
        self.RC.dropBadEntries()
        Gutti = self.RC.networkTwoMode('UT', 'title', directed = True, recordType = False)
        Gafwc = self.RC.networkTwoMode('AF', 'WC', nodeCount = False, edgeWeight = False)
        Gd2em = self.RC.networkTwoMode('D2', 'email')
        Gemd2 = self.RC.networkTwoMode('email', 'D2')
        Gstemm = self.RC.networkTwoMode('title', 'title', stemmerTag1 = lambda x: x[:-1], stemmerTag2 = lambda x: x + 's')
        self.assertIsInstance(Gutti, nx.classes.digraph.DiGraph)
        self.assertIsInstance(Gafwc, nx.classes.graph.Graph)
        self.assertEqual(list(Gutti.edges('WOS:A1979GV55600001'))[0][1][:31], "EXPERIMENTS IN PHENOMENOLOGICAL")
        self.assertEqual(len(Gutti.nodes()), 2 * len(self.RC) - 1)
        with self.assertRaises(metaknowledge.TagError):
            G = self.RC.networkTwoMode('TI', b'not a tag')
            del G
        with self.assertRaises(metaknowledge.TagError):
            G = self.RC.networkTwoMode(b'Not a Tag', 'TI')
            del G
        self.assertTrue(nx.is_isomorphic(Gd2em, Gemd2))
        self.assertEqual(metaknowledge.graphStats(Gstemm, sentenceString = True), 'The graph has 62 nodes, 31 edges, 0 isolates, 0 self loops, a density of 0.0163934 and a transitivity of 0')
        self.assertTrue('Optical properties of nanostructured thin filmss' in Gstemm)

    def test_nMode(self):
        G = self.RC.networkMultiMode(metaknowledge.WOS.tagToFullDict.keys())
        Gstem = self.RC.networkMultiMode(metaknowledge.WOS.tagToFullDict.keys(), stemmer = lambda x : x[0])
        self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 1186 nodes, 38564 edges, 0 isolates, 56 self loops, a density of 0.0549192 and a transitivity of 0.295384')
        self.assertEqual(metaknowledge.graphStats(Gstem, sentenceString = True), 'The graph has 50 nodes, 997 edges, 0 isolates, 35 self loops, a density of 0.828571 and a transitivity of 0.855834')

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
        self.assertEqual("WOS:A1976CW02200002", self.RC.localCitesOf(C).peek().id)
        self.assertEqual(self.RC.localCitesOf(self.RC.peek().id),
         self.RC.localCitesOf(self.RC.peek().createCitation()))

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

    def test_yearDiff(self):
        Gdefault = self.RC.networkCitation()
        Gfull = self.RC.networkCitation(nodeType="full")
        Goriginal = self.RC.networkCitation(nodeType="original")
        # Is yearDiff included as an attribute
        self.assertTrue('yearDiff' in list(Gdefault.edges(data=True))[0][2])
        self.assertTrue('yearDiff' in list(Gfull.edges(data=True))[0][2])
        self.assertTrue('yearDiff' in list(Goriginal.edges(data=True))[0][2])
        # Is yearDiff being calculated correctly?
        self.assertEqual(Gdefault["Costadebo, 1974, CR ACAD SCI A MATH"]["Gordon Jp, 1973, PHYS REV A"]["yearDiff"], 1)
        self.assertEqual(Gfull["Costadebo, 1974, CR ACAD SCI A MATH"]["Gordon Jp, 1973, PHYS REV A"]["yearDiff"], 1)
        self.assertEqual(Goriginal["COWAN JJ, 1977, J OPT SOC AM, V67, P1307, DOI 10.1364/JOSA.67.001307"]["GOOS F, 1947, ANN PHYS-BERLIN, V1, P333"]['yearDiff'], 30)

    def test_glimpse(self):
        #These tests do depend on terminal size
        gBasic = self.RC.glimpse()
        gCompact = self.RC.glimpse(compact = True)
        gEmpty = self.RC.glimpse('AF', 'qwertyhujk')
        self.assertIn('RecordCollection glimpse made at:', gBasic)
        self.assertIn('Top Authors\n', gBasic)
        self.assertIn('1 Gilles, H\n', gBasic)

        self.assertIn('|1 JOURNAL OF THE OPTICA', gCompact)
        self.assertIn('|Columns are ranked by num. of occurrences and are independent of one another++', gCompact)
        self.assertIn('qwertyhujk', gEmpty)
