# About Jupyter Notebooks


This document was made from a [jupyter](https://jupyter.org) notebook and can show and run python code. The document is broken up into what are called cells, each cell is either code, output, or markdown (text). For example this cell is markdown, which means it is plain text with a couple small formatting things, like the link in the first sentence. You can change the cell type using the dropdown menu at the top of the page.

[]#This cell is python
[]#The cell below it is output
[]print("This is an output cell")

The code cells contain python code that you can edit and run your self. Try changing the one above.


# Importing


First you need to import the _metaknowledge_ package

[]import metaknowledge as mk


And you will often need the [_networkx_](https://networkx.github.io/documentation/networkx-1.9.1/) package

[]import networkx as nx

And [_matplotlib_](http://matplotlib.org/) to display the graphs and to make them look nice when displayed

[]import matplotlib.pyplot as plt
[]%matplotlib inline

_metaknowledge_ also has a _matplotlib_ based graph [visualizer](http://networkslab.org/metaknowledge/docs/visual#visual) that will be used sometimes

[]import metaknowledge.visual as mkv

These lines of code will be at the top of all the other lessons as they are what let us use _metaknowledge_.
