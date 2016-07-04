#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
"""These are the functions used to process scopus csv files at the backend. They are meant for use internal use by metaknowledge.
"""
from .recordScopus import ScopusRecord, scopusRecordParser, scopusHeader
from .scopusHandlers import isScopusFile, scopusParser

from .tagProcessing.tagFunctions import scopusTagToFunction
from .tagProcessing.specialFunctions import scopusSpecialTagToFunc
