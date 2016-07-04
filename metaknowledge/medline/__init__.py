"""
These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.
"""
from .recordMedline import MedlineRecord, medlineRecordParser
from .medlineHandlers import isMedlineFile, medlineParser
from .tagProcessing.tagNames import tagNameDict, authorBasedTags, tagNameConverterDict
from .tagProcessing.specialFunctions import medlineSpecialTagToFunc
from .tagProcessing.tagFunctions import *
