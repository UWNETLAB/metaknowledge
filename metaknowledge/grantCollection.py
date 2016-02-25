import os.path
import collections.abc

from .progressBar import _ProgressBar
from .mkExceptions import GrantCollectionException, BadInputFile, NotAGrantFile

import metaknowledge

class GrantCollection(collections.abc.MutableSet, collections.abc.Hashable):
    def __init__(self, inGrants = None, name = '', extension = '', quietStart = False):
        """Mostly based on RecordCollection with some improvents/tweaks"""

        progArgs = (0, "Starting to make a GrantCollection")
        if metaknowledge.VERBOSE_MODE and not quietStart:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            self.bad = False
            self.errors = {}
            self.name = name
            self.grantTypes = set()

            if inGrants is None:
                PBar.updateVal(.5, "Empty GrantCollection created")
                if not name:
                    self.name = "Empty"
                self._Grants = set()

            elif isinstance(inGrants, str):
                if os.path.isfile(inGrants):
                    PBar.updateVal(.2, "GrantCollection from a file started")
                    if not inGrants.endswith(extension):
                        raise GrantCollectionException("extension of input file does not match requested extension '{}'.".format(extension))
                    if not name:
                        self.name = os.path.splitext(os.path.split(inGrants)[1])[0]
                    try:
                        for grantType, processor, detector in grantProcessors:
                            if detector(inGrants):
                                self.grantTypes.add(grantType)
                                self._Grants, gError = processor(inGrants)
                                if gError is not None:
                                    self.bad = True
                                    self.errors[inGrants] = gError
                            break
                    except NotAGrantFile:
                        raise BadInputFile("'{}' does not match any known grant file type and the default parser could not handle it.\nIts header might be damaged or it could have been modified by another program.".format(inGrants))
                else:
                    raise GrantCollectionException("'{}' is not a path to a directory or file. Strings cannot be used to initialize GrantCollections".format(inGrants))
            else:
                raise GrantCollectionException("A GrantCollection cannot be created from {}".format(inGrants))
            try:
                PBar.finish("Done making a GrantCollection of {} Grants".format(len(self)))
            except AttributeError:
                PBar.finish("Done making a GrantCollection. Warning an error occured.")

    #Hashable method

    def __hash__(self):
        return hash(sum((hash(G) for G in self)))

    #Set methods

    def __len__(self):
        return len(self._Grants)

    def __iter__(self):
        for G in self._Grants:
            yield G

    def __contains__(self, item):
        return item in self._Grants

    #Mutable Set methods

    def add(self, elem):
        if isinstance(elem, Record):
            self._Grants.add(elem)
            self.grantTypes.add(elem.typeString)
        else:
            raise RCTypeError("GrantCollections can only contain Grants, '{}' is not a Grant.".format(elem))

    def discard(self, elem):
        return self._Grants.discard(elem)
