#! /bin/bash
cd "$(dirname "$0")"
python3 docsMaker.py -o docs.md
pandoc --standalone --write=html --read=markdown --output=docs.html docs.md
cp docs.md ../metaknowledgeDocs.md
open docs.html
