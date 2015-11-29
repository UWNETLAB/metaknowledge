#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""metaknowledge is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

# Example

To load the data from files and make a network:

    >>> import metaknowledge as mk
    >>> RC = mk.RecordCollection("records/")
    >>> print(RC)
    Collection of 33 records
    >>> G = RC.coCiteNetwork(nodeType = 'journal')
    Done making a co-citation network of files-from-records                 1.1s
    >>> print(len(G.nodes()))
    223
    >>> mk.write_graph(G, "Cocitation-Network-of-Journals")

There is also a simple command line program called `metaknowledge` that comes with the package. It allows for creating networks without any need to know Python. More information about it can be found at [networkslab.org/metaknowledge/cli]({{ site.baseurl }}/cli)

# Overview

This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, language, and citations. The records are saved in groups of up-to 500 individual records in a file.

The [metaknowledge.RecordCollection](#RecordCollection.RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](#Record.Record) class that contains the results of the parsing of the record.

The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge makes use of them to extract useful information. The approximate meanings of the tags are listed in the [tagProcessing](#tagProcessing.tagProcessing) package, if you simply want the mapping [`tagToFull()`](#metaknowledge.tagToFull) is a function that maps tags to their full names it as well as a few other similar functions are provided by metaknowledge. There are no full official public listings of tag the meanings available. metaknowledge is not attempting to provide the definitive or authoritative meanings. Some

As citations are of great importance to sociology their handling is done with the [Citation](#Citation.Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

Note for those reading the docstring metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation]({{ site.baseurl }}/documentation/).
"""
from .record import Record, recordParser, BadISIRecord
from .citation import Citation, BadCitation, filterNonJournals
from .recordCollection import RecordCollection, isiParser
from .graphHelpers import write_edgeList, write_nodeAttributeFile, write_graph, read_graph, _ProgressBar, drop_edges, drop_nodesByDegree, drop_nodesByCount, mergeGraphs, graphStats
from .constants import VERBOSE_MODE
#from .blondel import blondel, modularity
from .diffusion import diffusionGraph, diffusionCount
from .tagProcessing.funcDicts import tagToFull, isTagOrName, normalizeToTag, normalizeToName
