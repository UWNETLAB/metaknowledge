import collections

from .mkExceptions import UnknownFile

from .grants.cihrGrant import parserCIHRfile, isCIHRfile
from .grants.nsercGrant import parserNSERCfile, isNSERCfile
from .grants.baseGrant import parserDefaultGrantFile, isDefaultGrantFile

from .WOS.wosHandlers import isWOSFile, wosParser
from .medline.medlineHandlers import isMedlineFile, medlineParser
from .proquest.proQuestHandlers import isProQuestFile, proQuestParser

ProccessorTuple = collections.namedtuple("ProccessorTuple", ("type", "processor", "detector"))

def unrecognizedFileHandler(fileName):
    raise UnknownFile("'{}' is not recognized my metaknowledge.".format(fileName))

grantProcessors = [
    ProccessorTuple("CIHRGrant", parserCIHRfile, isCIHRfile),
    ProccessorTuple("NSERCGrant", parserNSERCfile, isNSERCfile),
    ProccessorTuple("DefaultGrant", parserDefaultGrantFile, isDefaultGrantFile),
    #Raises exception if reached, to indicate the end of the list
    #This simplifes things at the other end
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),
]

recordHandlers = [
    ProccessorTuple("WOSRecord", wosParser, isWOSFile),
    ProccessorTuple("MedlineRecord", medlineParser, isMedlineFile),
    ProccessorTuple("ProQuestRecord", proQuestParser, isProQuestFile),
    #Raises exception if reached, to indicate the end of the list
    #This simplifes things at the other end
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),
]
