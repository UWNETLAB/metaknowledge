"""
hdvfghjhg
"""
from .recordMedline import MedlineRecord, medlineRecordParser
from .medlineHandlers import isMedlineFile, medlineParser
from .tagProcessing.tagNames import tagNameDict, authorBasedTags, tagNameConverterDict
from .tagProcessing.specialFunctions import medlineSpecialTagToFunc
from .tagProcessing.tagFunctions import *
