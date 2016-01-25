#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os
import sys

__version__ = '1.1a0'

specialRecordFields = [
    'authorsShort',
    'authorsFull',
    'year',
    'month',
    'title',
    'DOI',
    'volume',
    'beginningPage',
    'j9',
    'citations',
    'pubType',
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
