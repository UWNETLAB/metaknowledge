#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
import unittest
import builtins
import importlib
import sys
import metaknowledge.constants

class TestHelpers(unittest.TestCase):
    def test_VerboseMode(self):
        self.assertFalse(metaknowledge.constants.isInteractive())
        sys.stdout.isatty = lambda : True
        self.assertTrue(metaknowledge.constants.isInteractive())
        def NoThreadingImport(*args, **kwargs):
            if args[0] == 'threading':
                raise ImportError
            else:
                return importlib.__import__(*args, **kwargs)
        builtins.__import__ = NoThreadingImport
        self.assertFalse(metaknowledge.constants.isInteractive())
