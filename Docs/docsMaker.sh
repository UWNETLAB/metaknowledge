#! /bin/bash

python3 docsMaker.py -o docs.md .
pandoc --standalone --write=html --read=markdown --output=docs.html docs.md
