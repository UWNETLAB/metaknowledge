#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2016
"""These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.
"""
from .recordProQuest import ProQuestRecord, proQuestRecordParser
from .proQuestHandlers import isProQuestFile, proQuestParser
from .tagProcessing.specialFunctions import proQuestSpecialTagToFunc
from .tagProcessing.tagFunctions import proQuestTagToFunc
