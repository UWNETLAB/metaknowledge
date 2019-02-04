#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
"""_metaknowledge_ is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

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
    >>> mk.writeGraph(G, "Cocitation-Network-of-Journals")

There is also a simple command line program called `metaknowledge` that comes with the package. It allows for creating networks without any need to know Python. More information about it can be found at [networkslab.org/metaknowledge/cli]({{ site.baseurl }}/cli)

# Overview

This package can read the files downloaded from the Thomson Reuters' [Web of Science](https://webofknowledge.com) (_WOS_), Elsevier's [Scopus](https://www.scopus.com/), [ProQuest](www.proquest.com/) and Medline files from [PubMed](www.ncbi.nlm.nih.gov/pubmed). These files contain entries on the metadata of scientific records, such as authors, title, and citations. _metaknowledge_ can also read grants from various organizations including _NSF_ and _NSERC_ which are handled similarly to records.

The [metaknowledge.RecordCollection](./documentation/classes/RecordCollection.html#recordcollection-collectionwithids) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](./documentation/classes/Record.html#record-mapping-hashable) class that contains the results of the parsing of the record.

The files read by _metaknowledge_ are a databases containing a series of tags (implicitly or explicitly), e.g. `'TI'` is the title for WOS. Each tag has one or more values and metaknowledge can read them and extract useful information. As the tags differ between providers a small set of values can be accessed by special tags, the tags are listed in `commonRecordFields`. These special tags can act on the whole `Record` and as such may contain information provided by any number of other tags.

Citations are handled by a special [Citation](./documentation/classes/Citation.html#module-metaknowledge.citation) class. This class can parse the citations given by _WOS_ and journals cited by _Scopus_ and allows for better comparisons when they are used in graphs.

Note for those reading the docstrings metaknowledge's docs are written in markdown and are processed to produce the documentation found at [metaknowledge.readthedocs.io](https://metaknowledge.readthedocs.io/en/latest/), but you should have no problem reading them from the help function.
"""

from .constants import VERBOSE_MODE, __version__, commonRecordFields, FAST_CITES
from .mkExceptions import BadCitation, BadGrant, BadInputFile, BadProQuestFile, BadProQuestRecord, BadPubmedFile, BadPubmedRecord, BadRecord, BadWOSFile, BadWOSRecord, CollectionTypeError, GrantCollectionException, RCTypeError, RCValueError, RecordsNotCompatible, UnknownFile, cacheError, mkException, TagError, BadScopusRecord

from .graphHelpers import writeEdgeList, writeNodeAttributeFile, writeGraph, readGraph, dropEdges, dropNodesByDegree, dropNodesByCount, mergeGraphs, graphStats, writeTnetFile
from .diffusion import diffusionGraph, diffusionCount, diffusionAddCountsFromSource

from .citation import Citation, filterNonJournals
from .mkCollection import Collection, CollectionWithIDs
from .mkRecord import Record, ExtendedRecord

from .grantCollection import GrantCollection
from .grants import NSERCGrant, CIHRGrant, MedlineGrant, NSFGrant, Grant, FallbackGrant

from .recordCollection import RecordCollection
from .WOS import WOSRecord
from .medline import MedlineRecord
from .proquest import ProQuestRecord
from .scopus import ScopusRecord

from .journalAbbreviations.backend import updatej9DB
from .genders.nameGender import downloadData

def downloadExtras():
    """Downloads all the external files used by metaknowledge. This will overwrite exiting files
    """
    print("Downloading journal abbreviations data")
    updatej9DB()
    print("Downloading gender name data")
    downloadData()
