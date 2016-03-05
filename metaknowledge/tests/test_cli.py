import sys
import os
import builtins
import unittest
import unittest.mock

import metaknowledge

class MockInput(unittest.mock.MagicMock):
    def __init__(self,*args, **kwargs):
        unittest.mock.MagicMock.__init__(self,*args, **kwargs)
        self.calledVals = []

    def __call__(self, *args, **kwargs):
        return self.calledVals.pop(0)

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sysArgs = sys.argv

    def setUp(self):
        sys.argv = self.sysArgs

    def test_startup(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', return_value='q'):
                with self.assertRaises(SystemExit):
                    metaknowledge.bin.mkCLI()

    def test_startup(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', '--quiet', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', new_callable = MockInput) as m:
                fileName = 'CLITempFile'
                f = open(fileName + '.csv', 'w')
                f.write("tempFile")
                f.close()
                m.calledVals = ['1', '6', '0', '2', 'temp', 'y']
                self.assertEqual(metaknowledge.bin.mkCLI(), 1)
                os.remove(fileName + '.csv')
