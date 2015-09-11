#!/bin/bash -e

echo "Generating docs and putting them in /_post/docs"
echo "WARNING: /_post/docs is overwritten"
cd "$(dirname "$0")"
cd ../_posts/

rm -rf docs

metaknowledge-DocsGen -d docs
