#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os
import sys

def isInteractive():
    """
    A basic check of if the program is running in interactive mode
    """
    if sys.stdout.isatty() and os.name != 'nt':
        try:
            import threading
        except ImportError:
            return False
        else:
            return True
    else:
        return False

VERBOSE_MODE = isInteractive()
