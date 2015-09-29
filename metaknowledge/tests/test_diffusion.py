import unittest
import metaknowledge


class TestHelpers(unittest.TestCase):
    def setUp(self):
        metaknowledge.VERBOSE_MODE = False
        self.RC = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")

    def test_diffusionGraph(self):
        G = metaknowledge.diffusionGraph(self.RC, self.RC)
        Gcr_ut = metaknowledge.diffusionGraph(self.RC, self.RC, sourceType = "CR", targetType = "UT")
        self.assertEqual(metaknowledge.graphStats(G), 'The graph has 33 nodes, 31 edges, 11 isolates, 0 self loops, a density of 0.0293561 and a transitivity of 0.23913')
        self.assertEqual(metaknowledge.graphStats(Gcr_ut), 'The graph has 525 nodes, 597 edges, 254 isolates, 0 self loops, a density of 0.00217012 and a transitivity of 0')

    def test_diffusionCounts(self):
        d = metaknowledge.diffusionCount(self.RC, self.RC)
        dWC = metaknowledge.diffusionCount(self.RC, self.RC, sourceType = "WC")
        self.assertIsInstance(d.keys().__iter__().__next__(), metaknowledge.Record)
        self.assertTrue(-1 < d.values().__iter__().__next__() < 8)
        self.assertIsInstance(dWC.keys().__iter__().__next__(), str)
        self.assertTrue(-1 < dWC.values().__iter__().__next__() < 22)
