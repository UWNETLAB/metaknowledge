#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge."""

from .tagProcessing.tagFunctions import *
from .tagProcessing.funcDicts import tagToFullDict, fullToTagDict, tagNameConverterDict, tagsAndNameSet, knownTagsList

from .recordWOS import WOSRecord, recordParser
from .wosHandlers import isWOSFile, wosParser
