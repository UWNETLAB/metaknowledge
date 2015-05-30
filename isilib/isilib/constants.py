def isInteractive():
    import sys
    try:
        s = sys.ps1
        if isinstance(str, s):
            return True
        else:
            return False
    except AttributeError:
        return False

VERBOSE_MODE = isInteractive()
