#!/bin/bash -e

cd "$(dirname "$0")"
echo "Rewriting examples/mkExamples.ipynb"
metaknowledge-mdToNb metaknowledgeExamples.md
echo "Generating the example file examples/mkExamples.html"
jupyter nbconvert --to html --template basic --execute metaknowledgeExamples.ipynb
echo "Rewriting examples/index.md"
cat exampleHeader.md metaknowledgeExamples.html exampleFooter.md > index.md
echo "Cleaning up"
rm metaknowledgeExamples.html
