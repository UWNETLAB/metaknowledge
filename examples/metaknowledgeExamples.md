# Getting Started

{% comment %}

# Notes for those who downloaded the notebook

The notebook should just work as long as you put the sample file (savedrecs.txt) in the same directory as this file.

The one issue you will have is that the urls will not work. To make them work you will need to replace ``{{ site.baseurl }}`` with `http://networkslab.org/metaknowledge`

{% endcomment %}

metaknowledge is a python library for creating and analyzing scientific metadata. It uses records obtained from Web of Science (WOS) and mostly produces graphs. This will be a short overview of its capabilities, for complete coverage of the package and install institutions read full the documentation [here]({{ site.baseurl }}/documentation).


This document was made from a [jupyter](https://jupyter.org) notebook you can download the notebook [here]({{ site.baseurl }}/examples/metaknowledgeExamples.ipynb) and the sample file is [here]({{ site.baseurl }}/examples/savedrecs.txt) if you wish to see an interactive version of these examples.


First you need to import the metaknowledge package:

[]import metaknowledge as mk


You will often need the networkx package as well:

[]import networkx as nx

I am importing these next couple things so the graphs will look nice:

[]import matplotlib.pyplot as plt
[]%matplotlib inline


# [Reading Files]({{ site.baseurl }}/docs/RecordCollection#RecordCollection)

The files from the Web of Science (WOS) can be loaded into [RecordCollections]({{ site.baseurl }}/docs/RecordCollection#RecordCollection) by creating a RecordCollection object with the path to the files given to the initializer as a string.

[]RC = mk.RecordCollection("savedrecs.txt")
[]print(repr(RC))

You can also read a whole directory

[]RC = mk.RecordCollection(".")
[]print(repr(RC))

metaknowledge can detect if a file is a valid WOS file or not and will read the entire directory and load only those that have the right header. You can also tell it to only read a certain type of file, by using the extension argument.

[]RC = mk.RecordCollection(".", extension = "txt")
[]print(repr(RC))

Now you have a RecordCollection object composed of all the WOS records in the selected file(s).

# [The RecordCollections object]({{ site.baseurl }}/docs/RecordCollection#RecordCollection)
