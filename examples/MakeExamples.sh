#!/bin/bash -e

echo "Generating the example file examples/index.md"
cd "$(dirname "$0")"


jupyter nbconvert --to html --template basic mkExamples.ipynb

cat exampleHeader.md mkExamples.html exampleFooter.md> index.md

rm mkExamples.html
