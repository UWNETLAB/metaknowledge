#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import unittest
import metaknowledge


class TestHelpers(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")

    def test_diffusionGraph(self):
        G = metaknowledge.diffusionGraph(self.RC, self.RC)
        Gcr_ut = metaknowledge.diffusionGraph(self.RC, self.RC, sourceType = "CR", targetType = "UT")
        self.assertEqual(metaknowledge.graphStats(G), 'The graph has 42 nodes, 1569 edges, 0 isolates, 35 self loops, a density of 0.91115 and a transitivity of 0.894934')
        self.assertEqual(metaknowledge.graphStats(Gcr_ut), 'The graph has 528 nodes, 3591 edges, 246 isolates, 0 self loops, a density of 0.0129054 and a transitivity of 0')

    def test_multiGraph(self):
        G = metaknowledge.diffusionGraph(self.RC, self.RC, labelEdgesBy = 'PY')
        self.assertEqual(metaknowledge.graphStats(G, stats = ('nodes', 'edges', 'isolates', 'loops', 'density')), 'The graph has 42 nodes, 30956 edges, 0 isolates, 914 self loops and a density of 17.9768')

    def test_diffusionCounts(self):
        d = metaknowledge.diffusionCount(self.RC, self.RC)
        dc = metaknowledge.diffusionCount(self.RC, self.RC, compareCounts = True)
        dWC = metaknowledge.diffusionCount(self.RC, self.RC, sourceType = "WC")
        self.assertIsInstance(d.keys().__iter__().__next__(), metaknowledge.Record)
        self.assertTrue(-1 < d.values().__iter__().__next__() < 8)
        self.assertIsInstance(dWC.keys().__iter__().__next__(), str)
        self.assertTrue(-1 < dWC.values().__iter__().__next__() < 22)
        for t in dc.values():
            self.assertEqual(t[0], t[1])

    def test_diffusionPandas(self):
        d = metaknowledge.diffusionCount(self.RC, self.RC, pandasFriendly = True)
        dwc = metaknowledge.diffusionCount(self.RC, self.RC, pandasFriendly = True, sourceType = "WC", compareCounts = True)
        dyear = metaknowledge.diffusionCount(self.RC, self.RC, pandasFriendly = True, extraValue = 'year')
        self.assertTrue("TI" in d.keys())
        self.assertEqual(len(d), 44)
        self.assertTrue(len(d["UT"]), len(self.RC))
        self.assertTrue("WC" in dwc)
        self.assertEqual(3, len(dwc))
        self.assertEqual(len(dwc["TargetCount"]), 9)
        self.assertEqual(dwc["TargetCount"], dwc["SourceCount"])
        self.assertEqual(len(dyear), len(d) + 1)
        self.assertNotEqual(dyear["TargetCount"], dwc["SourceCount"])
        self.assertEqual(len([c for c in dyear["TargetCount"] if c > 1]), 7)
        self.assertTrue(1979 in dyear['year'])
