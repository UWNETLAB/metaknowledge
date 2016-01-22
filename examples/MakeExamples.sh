#!/bin/bash -e

cd "$(dirname "$0")"
echo "Rewriting examples/mkExamples.ipynb"
metaknowledge-mdToNb metaknowledgeExamples.md
echo "Generating the example file examples/mkExamples.html"
jupyter nbconvert --to notebook --execute --output=metaknowledgeExamples.ipynb metaknowledgeExamples.ipynb
jupyter nbconvert --to html --template basic metaknowledgeExamples.ipynb
echo "Rewriting examples/index.md"
cat exampleHeader.md metaknowledgeExamples.html exampleFooter.md > index.md
echo "Cleaning up"
rm metaknowledgeExamples.html FinalJournalCoCites_nodeAttributes.csv FinalJournalCoCites_edgeList.csv Records_Starting_with_A.csv Records_Starting_with_A.txt
