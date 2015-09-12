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

# Overview

This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, language, and citations. The records are saved in groups of up-to 500 individual records in a file.

The [metaknowledge.RecordCollection](#RecordCollection.RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](#Record.Record) class that contains the results of the parsing of the record.

The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge makes use of them to extract useful information. The approximate meanings of the tags are listed in the [tagFuncs](#tagFuncs.tagFuncs) package, there are no full official public listings of their meanings is available. metaknowledge is not attempting to provide the definitive meanings.

As citations are of great importance to sociology their handling is done with the [Citation](#Citation.Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

Note for those reading the docstring. metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation](http://networkslab.org/metaknowledge/documentation/).
"""
from .record import Record, recordParser, BadISIRecord
from .citation import Citation, BadCitation, filterNonJournals
from .recordCollection import RecordCollection, isiParser
from .graphHelpers import write_edgeList, write_nodeAttributeFile, write_graph, read_graph, _ProgressBar, drop_edges, drop_nodesByDegree, drop_nodesByCount, graphStats
from .constants import VERBOSE_MODE, tagToFull, fullToTag, tagNameConverter, tagsAndNames, knownTagsList
#from .blondel import blondel, modularity
