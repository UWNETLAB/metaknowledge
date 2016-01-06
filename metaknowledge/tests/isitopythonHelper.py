#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import metaknowledge

if __name__ == "__main__":
    rlst = metaknowledge.wosParser("testFile.isi")
    s = '['
    for R in rlst:
        s +=(str(R.__getstate__()) + ',\n')
    s += ']'
    print(s)
