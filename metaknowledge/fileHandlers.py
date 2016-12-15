try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections

from .mkExceptions import UnknownFile

from .grants.cihrGrant import parserCIHRfile, isCIHRfile
from .grants.nsercGrant import parserNSERCfile, isNSERCfile
from .grants.nsfGrant import parserNSFfile, isNSFfile
from .grants.baseGrant import parserFallbackGrantFile, isFallbackGrantFile

from .WOS.wosHandlers import isWOSFile, wosParser
from .medline.medlineHandlers import isMedlineFile, medlineParser
from .proquest.proQuestHandlers import isProQuestFile, proQuestParser
from .scopus.scopusHandlers import isScopusFile, scopusParser

ProccessorTuple = collections.namedtuple("ProccessorTuple", ("type", "processor", "detector"))

def unrecognizedFileHandler(fileName):
    raise UnknownFile("'{}' is not recognized my metaknowledge.".format(fileName))

grantProcessors = [
    ProccessorTuple("NSFGrant", parserNSFfile, isNSFfile),
    ProccessorTuple("CIHRGrant", parserCIHRfile, isCIHRfile),
    ProccessorTuple("NSERCGrant", parserNSERCfile, isNSERCfile),
    ProccessorTuple("FallbackGrant", parserFallbackGrantFile, isFallbackGrantFile),
    #Raises exception if reached, to indicate the end of the list
    #This simplifes things at the other end
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),
]

recordHandlers = [
    ProccessorTuple("WOSRecord", wosParser, isWOSFile),
    ProccessorTuple("MedlineRecord", medlineParser, isMedlineFile),
    ProccessorTuple("ProQuestRecord", proQuestParser, isProQuestFile),
    ProccessorTuple("ScopusRecord", scopusParser, isScopusFile),
    #Raises exception if reached, to indicate the end of the list
    #This simplifes things at the other end
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),
]
