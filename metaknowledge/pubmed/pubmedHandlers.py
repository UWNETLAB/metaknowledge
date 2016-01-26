

def isPubmed(infile, checkedLines = 2):
    """Checks if _infile_ has the right header in the first _checkedLines_ lines
    """
    try:
        with open(infile, 'r', encoding='latin-1') as openfile:
            f = enumerate(openfile, start = 0)
            for i in range(checkedLines):
                if f.__next__()[1].startswith("PMID- "):
                    return True
    except (StopIteration, UnicodeDecodeError):
        return False
    else:
        return False
