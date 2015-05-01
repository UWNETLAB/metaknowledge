#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from ..RecordCollection import RecordCollection

if __name__ == '__main__':
    R = RecordCollection("testFile.isi")
    print(R)
    print(R._Records)
    for r in R._Records:
        if r.bad:
            print(r.error)
        else:
            print(r.authors())
            print(r.year())
            print(r.month())
            print(r.citations())
            print(r.title())
    print("Network")
    print(R.coAuthNetwork().edges())
