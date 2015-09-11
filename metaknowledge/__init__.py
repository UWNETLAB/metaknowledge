"""Doc String for metaknowledge main
"""
from .record import Record, recordParser, BadISIRecord
from .citation import Citation, BadCitation, filterNonJournals
from .recordCollection import RecordCollection, isiParser
from .graphHelpers import write_edgeList, write_nodeAttributeFile, write_graph, read_graph, _ProgressBar, drop_edges, drop_nodesByDegree, drop_nodesByCount, graphStats
from .constants import VERBOSE_MODE, tagToFull, fullToTag, tagNameConverter, tagsAndNames, knownTagsList
#from .blondel import blondel, modularity
