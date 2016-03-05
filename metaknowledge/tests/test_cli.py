import sys
import builtins
import unittest
import unittest.mock

import metaknowledge

class MyTestCase(unittest.TestCase):

    def test_test(self):
        sys.argv = ['/usr/local/bin/metaknowledge', '--debug', 'metaknowledge/tests']
        with unittest.mock.patch('builtins.print'):
            with unittest.mock.patch('builtins.input', return_value='1'):
                #with self.assertRaises(TypeError):
                    metaknowledge.bin.mkCLI()
