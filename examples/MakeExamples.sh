#!/bin/bash -e

cd "$(dirname "$0")"
echo "Rewriting examples/mkExamples.ipynb"
metaknowledge-mdToNb mkExamples.md
echo "Generating the example file examples/mkExamples.html"
jupyter nbconvert --to html --template basic --execute mkExamples.ipynb
echo "Rewriting examples/index.md"
cat exampleHeader.md mkExamples.html exampleFooter.md > index.md
echo "Cleaning up"
rm mkExamples.html
