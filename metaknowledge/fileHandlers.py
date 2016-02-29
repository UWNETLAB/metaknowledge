import collections

from .mkExceptions import UnknownFile

from .grants.cihrGrant import parserCIHRfile, isCIHRfile

from .WOS.wosHandlers import isWOSFile, wosParser
from .medline.medlineHandlers import isMedlineFile, medlineParser

ProccessorTuple = collections.namedtuple("ProccessorTuple", ("type", "processor", "detector"))

def unrecognizedFileHandler(fileName):
    raise UnknownFile("'{}' is not recognized my metaknowledge.".format(fileName))

grantProcessors = [
    ProccessorTuple("CIHRGrant", parserCIHRfile, isCIHRfile),
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),#Raise exception if reached
]



recordHandlers = [
    ProccessorTuple("WOSRecord", wosParser, isWOSFile),
    ProccessorTuple("MedlineRecord", medlineParser, isMedlineFile),
    ProccessorTuple("Invalid File", None, unrecognizedFileHandler),#Raise exception if reached
]
