#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
from .recordScopus import ScopusRecord, scopusRecordParser
from .scopusHandlers import isScopusFile, scopusParser

from .tagProcessing.tagFunctions import scopusTagToFunction
from .tagProcessing.specialFunctions import scopusSpecialTagToFunc
