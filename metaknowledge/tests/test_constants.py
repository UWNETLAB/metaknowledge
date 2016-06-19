#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import unittest.mock
import builtins
import importlib
import sys
import metaknowledge.constants

class TestConstants(unittest.TestCase):
    def test_VerboseMode(self):
        self.assertFalse(metaknowledge.constants.isInteractive())
        sys.stdout.isatty = lambda : True
        self.assertTrue(metaknowledge.constants.isInteractive())
        class ImportMock(unittest.mock.Mock):
            def __call__(self, *args, **kwargs):
                if args[0] == 'threading':
                    raise ImportError
                else:
                    return importlib.__import__(*args, **kwargs)
        with unittest.mock.patch('builtins.__import__', new_callable = ImportMock):#, NoThreadingImport):
        #builtins.__import__ =
            self.assertFalse(metaknowledge.constants.isInteractive()) #This will fail for setup.py test
            #Failure for setup.py is what is supposed to happen as that would be an interactive enviroment
