#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from RecordCollection import *

if __name__ == '__main__':
    R = RecordCollection("Imbert_C_CITED.txt")
    print(R)
    print(R._Records)
    for r in R._Records:
        if r.bad:
            print(r.error)
        else:
            print(r.authors())
            print(r.year())
            print(r.month())
    print("Network")
    print(R.coAuthNetwork().edges())
