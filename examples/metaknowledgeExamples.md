# Getting started


metaknowledge is a python library for creating and analyzing scientific metadata. It uses records obtained from Web of Science (WOS) and mostly produces graphs. This will be a short overview of its capabilities, for complete coverage of the package and install institutions read full the documentation [here]({{ site.baseurl }}/documentation).


This document was made from a [jupyter](https://jupyter.org) notebook you can download the notebook [here]({{site.baseurl}}/examples/mkExamples.ipynb) if you wish to see an interactive version of these examples.


First you need to import the metaknowledge package:

[]import metaknowledge as mk


You will often need the networkx package as well:

[]import networkx as nx

I am importing these next couple things so the graphs will look nice:

[]import matplotlib.pyplot as plt
[]%matplotlib inline
