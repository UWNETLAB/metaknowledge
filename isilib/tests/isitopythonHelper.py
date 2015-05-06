import isilib

if __name__ == "__main__":
    rlst = isilib.isiParser("testFile.isi")
    s = '['
    for R in rlst:
        s +=(str(R.__getstate__()) + ',\n')
    s += ']'
    print(s)
