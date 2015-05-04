#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from RecordCollection import *
from IPython import embed

if __name__ == '__main__':
    R1 = RecordCollection("Tests/testFile.isi")
    R2 = RecordCollection("Tests/ManyAuthors.isi")
    print(R1)
    print(R1._Records)
    for r in R1._Records:
        if r.bad:
            print(r.error)
        else:
            print(r)
            print(r.authors())
            print(r.year())
            print(r.month())
            print(r.citations())
            print(r.title())
    print("Network")
    print(R1.coAuthNetwork().edges())
    R3 = R1 + R2
    print(R3._Records)
    print(R3.coAuthNetwork().edges())
    print(R3._Records.pop().year())
    print(R3._Records.pop())
    print(dir(R3))
    r1 = R3._Records.pop()
    for r in R3._Records:
        if r.wosString():
            print(r.wosString(), end = '')
        else:
            print(r)
