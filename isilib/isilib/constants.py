def isInteractive():
    import sys
    try:
        sys.ps1
        return True
    except AttributeError:
        return False

VERBOSE_MODE = isInteractive()
