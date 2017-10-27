import sys
import os
import os.path
import argparse
import builtins
import code
import unittest
import unittest.mock

import metaknowledge
import metaknowledge.bin.metaknowledgeCLI

class MockInput(unittest.mock.MagicMock):

    def __init__(self, *args, **kwargs):
        unittest.mock.MagicMock.__init__(self,*args, **kwargs)
        self.calledVals = []

    def __call__(self, *args, **kwargs):
        val = self.calledVals.pop(0)
        if not isinstance(val, str):
            raise val
        else:
            return val

class TestCLI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sysArgs = sys.argv
        cls.RCmain = metaknowledge.RecordCollection("metaknowledge/tests/testFile.isi")
        cls.Gmain = cls.RCmain.networkCoAuthor()

    def setUp(self):
        self.RC = self.RCmain.copy()
        self.G = self.Gmain.copy()
        sys.argv = ['/usr/local/bin/metaknowledge']

    #Trying to make nose happy
    def tearDown(self):
        sys.argv = self.sysArgs

    def test_quit(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', return_value='q'):
                with self.assertRaises(SystemExit):
                    metaknowledge.bin.mkCLI()

    def test_startInteractive(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                m.calledVals = [KeyboardInterrupt]
                self.assertEqual(metaknowledge.bin.mkCLI(), 0)
                self.assertEqual(len(m.calledVals), 0)

    def test_keyboardInterupt(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):

            class mockExit(unittest.mock.MagicMock):
                def __call__(self, *args, **kwargs):
                    #Just want to raise an error, --debug mode means it will not be caught
                    raise RuntimeError

            with unittest.mock.patch('code.interact', new_callable = mockExit):
                with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                    m.calledVals = ['i']
                    with self.assertRaises(RuntimeError):
                        metaknowledge.bin.mkCLI()
                    self.assertEqual(len(m.calledVals), 0)

    def test_basicRun(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                fileName = 'CLITempFile.csv'
                f = open(fileName, 'w')
                f.write("tempFile for testing metaknowledge should have been deleted. A test went wrong.")
                f.close()
                m.calledVals = ['1', '6', '0', '2', fileName[:-4], 'p','y']
                self.assertEqual(metaknowledge.bin.mkCLI(), 1)
                self.assertEqual(os.path.getsize(fileName), 4110112)
                self.assertEqual(len(m.calledVals), 0)
                os.remove(fileName)

    def test_spamming(self):
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', return_value = '0') as m:
                self.assertIsInstance(metaknowledge.bin.mkCLI(), Exception)

    def test_Thresholds(self):
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                m.calledVals = ['', '0']
                G = metaknowledge.bin.metaknowledgeCLI.getThresholds(None, self.G)
                self.assertEqual(G, self.G)
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['1', '2', '3', '1', '4', '5', '5', '0', '6', 'ten', '2', '0']
                G = metaknowledge.bin.metaknowledgeCLI.getThresholds(None, self.G)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 2 nodes, 1 edges, 0 isolates, 0 self loops, a density of 1 and a transitivity of 0')
                self.assertEqual(len(m.calledVals), 0)

    def test_graphs(self):
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                m.calledVals = ['1', 'NOT A TAG', 'AF']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 45 nodes, 46 edges, 9 isolates, 0 self loops, a density of 0.0464646 and a transitivity of 0.822581')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['2', 'AF', 'UT']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 77 nodes, 66 edges, 0 isolates, 0 self loops, a density of 0.0225564 and a transitivity of 0')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['3'] + list(self.RC.tags()) + ['']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 1186 nodes, 38564 edges, 0 isolates, 56 self loops, a density of 0.0549192 and a transitivity of 0.295384')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['4']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 511 nodes, 817 edges, 0 isolates, 0 self loops, a density of 0.00313495 and a transitivity of 0.00600437')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['5']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 493 nodes, 13000 edges, 0 isolates, 22 self loops, a density of 0.107282 and a transitivity of 0.611431')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['6']
                G = metaknowledge.bin.metaknowledgeCLI.getNetwork(None, self.RC)
                self.assertEqual(metaknowledge.graphStats(G, sentenceString = True), 'The graph has 45 nodes, 46 edges, 9 isolates, 0 self loops, a density of 0.0464646 and a transitivity of 0.822581')
                self.assertEqual(len(m.calledVals), 0)

    def test_create(self):
        fileName = 'tempTestFile'
        named = argparse.Namespace()
        named.name = fileName
        unnamed = argparse.Namespace()
        unnamed.name = None
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                m.calledVals = ['1']
                self.assertTrue(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, self.RC))
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['2']
                self.RC.dropBadEntries()
                self.assertFalse(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, self.RC))
                self.assertEqual(os.path.getsize(fileName+ '.txt'), 88160)
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['3', fileName, 'n', fileName, 'g', 'y']
                self.RC.dropBadEntries()
                self.assertTrue(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(unnamed, self.RC))
                self.assertEqual(os.path.getsize(fileName+ '.txt'), 88160)
                os.remove(fileName + '.txt')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['4']
                self.RC.dropBadEntries()
                self.assertFalse(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, self.RC))
                self.assertEqual(os.path.getsize(fileName+ '.csv'), 86330)
                os.remove(fileName + '.csv')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['6', 'y']
                self.RC.dropBadEntries()
                self.assertFalse(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, self.RC))
                self.assertEqual(os.path.getsize(fileName+ '.csv'), 20123)
                os.remove(fileName + '.csv')
                self.assertEqual(len(m.calledVals), 0)

                with self.assertRaises(KeyboardInterrupt):
                    #Don't want to mess with these too much
                    m.calledVals = ['7', '', KeyboardInterrupt]
                    self.assertFalse(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, self.RC))
                self.assertEqual(len(m.calledVals), 0)
                m.calledVals = ['7', '']
                self.assertFalse(metaknowledge.bin.metaknowledgeCLI.getWhatToDo(named, metaknowledge.RecordCollection()))
                self.assertEqual(len(m.calledVals), 0)

    def test_output(self):
        fileName = 'tempTestFile'
        named = argparse.Namespace()
        named.name = fileName
        unnamed = argparse.Namespace()
        unnamed.name = None
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                f = open(fileName + '_edgeList.csv', 'w')
                f.write("tempFile for testing metaknowledge should have been deleted. A test went wrong.")
                f.close()


                m.calledVals = ['1']
                metaknowledge.bin.metaknowledgeCLI.outputNetwork(named, self.G)
                #filesize is slightly non deteministic
                self.assertAlmostEqual(os.path.getsize(fileName + '_edgeList.csv'), 1403, delta = 3)
                self.assertAlmostEqual(os.path.getsize(fileName + '_nodeAttributes.csv'), 779, delta = 4)
                os.remove(fileName + '_nodeAttributes.csv')
                os.remove(fileName + '_edgeList.csv')
                self.assertEqual(len(m.calledVals), 0)

                m.calledVals = ['4']
                metaknowledge.bin.metaknowledgeCLI.outputNetwork(named, self.G)
                #filesize is slightly non deteministic
                self.assertAlmostEqual(os.path.getsize(fileName + '.graphml'), 6817, delta = 4)
                os.remove(fileName + '.graphml')
                self.assertEqual(len(m.calledVals), 0)
