# Making a network

For this class most of the types of network you will want to make can be produced by _metaknowledge_. The first three co-citation network, citation network and co-author network are specialized versions of the last three one-mode network, two-mode network and multi-mode network.

First we need to import metaknowledge and because we will be dealing with graphs the graphs package _networkx_ as should be imported

[]import metaknowledge as mk
[]import networkx as nx

And so we can visualize the graphs

[]import matplotlib.pyplot as plt
[]%matplotlib inline
[]import metaknowledge.visual as mkv

Before we start we should also get a `RecordCollection` to work with.

[]RC = mk.RecordCollection('../savedrecs.txt')

Now lets look at the different types of graph.


# Making a co-citation network


To make a basic co-citation network of Records use [`coCiteNetwork()`](http://networkslab.org/metaknowledge/docs/RecordCollection#coCiteNetwork).

[]coCites = RC.coCiteNetwork()
[]print(mk.graphStats(coCites, makeString = True)) #makestring by default is True so it is not strictly necessary to include

[`graphStats()`](http://networkslab.org/metaknowledge/docs/metaknowledge#graphStats) is a function to extract some of the statists of a graph and make them into a nice string.

`coCites` is now a [_networkx_](https://networkx.github.io/documentation/networkx-1.9.1/) graph of the co-citation network, with the hashes of the `Citations` as nodes and the full citations stored  as an attributes. Lets look at one node

[]coCites.nodes(data = True)[0]

and an edge

[]coCites.edges(data = True)[0]

All the graphs _metaknowledge_ use are _networkx_ graphs, a few functions to trim them are implemented in _metaknowledge_, [here](#filtering-graphs) is the example section, but many useful functions are implemented by it. Read the documentation [here](https://networkx.github.io/documentation/networkx-1.9.1/) for more information.

The `coCiteNetwork()` function has many options for filtering and determining the nodes. The default is to use the `Citations` themselves. If you wanted to make a network of co-citations of journals you would have to make the node type `'journal'` and remove the non-journals.

[]coCiteJournals = RC.coCiteNetwork(nodeType = 'journal', dropNonJournals = True)
[]print(mk.graphStats(coCiteJournals))

Lets take a look at the graph after a quick spring layout

[]nx.draw_spring(coCiteJournals)

A bit basic but gives a general idea. If you want to make a much better looking and more informative visualization you could try [gephi](https://gephi.github.io/) or [visone](http://visone.info/). Exporting to them is covered below in [**Exporting graphs**](#exporting-graphs).

# Making a citation network


The [`citationNetwork()`](http://networkslab.org/metaknowledge/docs/RecordCollection#citationNetwork) method is nearly identical to `coCiteNetwork()` in its parameters. It has one additional keyword argument `directed` that controls if it produces a directed network. Read [**Making a co-citation network**](http://networkslab.org/metaknowledge/examples/#Making-a-co-citation-network) to learn more about `citationNetwork()`.


One small example is still worth providing. If you want to make a network of the citations of years by other years and have the letter `'A'` in them then you would write:

[]citationsA = RC.citationNetwork(nodeType = 'year', keyWords = ['A'])
[]print(mk.graphStats(citationsA))


[]nx.draw_spring(citationsA, with_labels = True)


# Making a co-author network


The [`coAuthNetwork()`](http://networkslab.org/metaknowledge/docs/RecordCollection#coAuthNetwork) function produces the co-authorship network of the RecordCollection as is used as shown

[]coAuths = RC.coAuthNetwork()
[]print(mk.graphStats(coAuths))

# Making a one-mode network


In addition to the specialized network generators _metaknowledge_ lets you make a one-mode co-occurence network of any of the WOS tags, with the [oneModeNetwork()](http://networkslab.org/metaknowledge/docs/RecordCollection#oneModeNetwork) function. For examples the WOS subject tag `'WC'` can be examined.

[]wcCoOccurs = RC.oneModeNetwork('WC')
[]print(mk.graphStats(wcCoOccurs))


[]nx.draw_spring(wcCoOccurs, with_labels = True)

# Making a two-mode network


If you wish to study the relationships between 2 tags you can use the [`twoModeNetwork()`](http://networkslab.org/metaknowledge/docs/RecordCollection#twoModeNetwork) function which creates a two mode network showing the connections between the tags. For example to look at the connections between titles(`'TI'`) and subjects (`'WC'`)

[]ti_wc = RC.twoModeNetwork('WC', 'title')
[]print(mk.graphStats(ti_wc))


The network is directed by default with the first tag going to the second.

[]mkv.quickVisual(ti_wc, showLabel = False) #default is False as there are usually lots of labels


[`quickVisual()`](http://networkslab.org/metaknowledge/docs/visual#quickVisual) makes a graph with the different types of nodes coloured differently and a couple other small visual tweaks from _networkx_'s `draw_spring`.


# Making a multi-mode network


For any number of tags the [`nModeNetwork()`](http://networkslab.org/metaknowledge/docs/RecordCollection#nModeNetwork) function will do the same thing as the `oneModeNetwork()` but with any number of tags and it will keep track of their types. So to look at the co-occurence of titles `'TI'`, WOS number `'UT'` and authors `'AU'`.

[]tags = ['TI', 'UT', 'AU']
[]multiModeNet = RC.nModeNetwork(tags)
[]mk.graphStats(multiModeNet)

[]mkv.quickVisual(multiModeNet)

Beware this can very easily produce hairballs

[]tags = mk.tagsAndNames #All the tags, twice
[]sillyMultiModeNet = RC.nModeNetwork(tags)
[]mk.graphStats(sillyMultiModeNet)

[]mkv.quickVisual(sillyMultiModeNet)


# Post processing graphs


If you wish to apply a well known algorithm or process to a graph [_networkx_](https://networkx.github.io/documentation/networkx-1.9.1/) is a good place to look as they do a good job at implementing  them.

One of the features it lacks though is pruning of graphs, _metaknowledge_ has these capabilities. To remove edges outside of some weight range, use [`drop_edges()`](http://networkslab.org/metaknowledge/docs/metaknowledge#drop_edges). For example if you wish to remove the self loops, edges with weight less than 2 and weight higher than 10 from `coCiteJournals`.

[]minWeight = 3
[]maxWeight = 10
[]proccessedCoCiteJournals = mk.drop_edges(coCiteJournals, minWeight, maxWeight, dropSelfLoops = True)
[]mk.graphStats(proccessedCoCiteJournals)

Then to remove all the isolates, i.e. nodes with degree less than 1, use [`drop_nodesByDegree()`](http://networkslab.org/metaknowledge/docs/metaknowledge#drop_nodesByDegree)

[]proccessedCoCiteJournals = mk.drop_nodesByDegree(proccessedCoCiteJournals, 1)
[]mk.graphStats(proccessedCoCiteJournals)

Now before the processing the graph can be seen [here](#Making-a-co-citation-network). After the processing it looks like

[]nx.draw_spring(proccessedCoCiteJournals)

Hm, it looks a bit thinner. Using a visualizer will make the difference a bit more noticeable.


#Exporting graphs


Now you have a graph the last step is to write it to disk. _networkx_ has a few ways of doing this, but they tend to be slow. _metaknowledge_ can write an edge list and node attribute file that contain all the information of the graph. The function to do this is called [`write_graph()`](http://networkslab.org/metaknowledge/docs/metaknowledge#write_graph). You give it the start of the file name and it makes two labeled files containing the graph.


[]mk.write_graph(proccessedCoCiteJournals, "FinalJournalCoCites")

These files are simple CSVs an can be read easily by most systems. If you want to read them back into Python the [`read_graph()`](http://networkslab.org/metaknowledge/docs/metaknowledge#read_graph) function will do that.

[] FinalJournalCoCites = mk.read_graph("FinalJournalCoCites_edgeList.csv", "FinalJournalCoCites_nodeAttributes.csv")
[]mk.graphStats(FinalJournalCoCites)

This is full example workflow for _metaknowledge_, the package is flexible and you hopefully will be able to customize it to do what you want (I assume you do not want the Records staring with 'A').
