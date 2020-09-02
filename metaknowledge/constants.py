#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os
import sys

__version__ = '3.4'

commonRecordFields = [
    'year',
    'volume',
    'beginningPage',
    'DOI',
    'address',
    'j9',
    'citations',
    'grants',
    'selfCitation',
    'authorsShort',
    'authorsFull',
    'title',
    'journal',
    'keywords',
    'abstract',
    'id',
]


def isInteractive():
    """
    A basic check of if the program is running in interactive mode
    """
    if sys.stdout.isatty() and os.name != 'nt':
        #Hopefully everything but ms supports '\r'
        try:
            import threading
        except ImportError:
            return False
        else:
            return True
    else:
        return False

VERBOSE_MODE = isInteractive()

FAST_CITES = False
