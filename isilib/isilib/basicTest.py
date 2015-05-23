#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from isilib import RecordCollection
import os
import sys
import io

def btest(quite = False):
    if quite:
        stdOut = sys.stdout
        sys.stdout = io.StringIO()
    currentPath = '.' #os.path.dirname(os.path.realpath(__file__))
    R1 = RecordCollection(currentPath + "/tests/testFile.isi")
    R2 = RecordCollection(currentPath + "/tests/ManyAuthors.isi")
    print(R1)
    print(R1._Records)

    print("Network")
    print(R1.coAuthNetwork().edges)
    R3 = R1 + R2
    print(R3._Records)
    print(R3.coAuthNetwork().edges())
    print(R3._Records.pop().year)
    print(R3._Records.pop())
    print(dir(R3))
    r1 = R3._Records.pop()
    for r in R3:
        if r.wosString:
            print(r.wosString, end = ': \t')
            print(r.month, end = ',\t')
            print(r.year)
        else:
            print(r)
    print(R3)
    print(R2)
    print(R1)
    print(R2 & R1)
    print(R2 + R2)
    print(R2 ^ R1)
    print(R3 & R1)
    print(repr(R1))
    print(repr(R3 + R2 - R3 & R1))
    for r in R1:
        if r.bad:
            print(r.error)
        else:
            print(r)
            print(r.authorsFull)
            print(r.year)
            print(r.month)

            print(r.title)
            print(r.month)
            print(r.wosString)
            print(r.DOI)
            print(r.citations)
    print(R3.pop())
    if quite:
        sys.stdout = stdOut
