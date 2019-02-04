import os.path
try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections

import networkx as nx

from .progressBar import _ProgressBar

from .mkCollection import CollectionWithIDs
from .mkExceptions import GrantCollectionException, BadInputFile, UnknownFile

from .grants.baseGrant import Grant

from .fileHandlers import grantProcessors

import metaknowledge

class GrantCollection(CollectionWithIDs):
    def __init__(self, inGrants = None, name = '', extension = '', cached = False, quietStart = False):

        progArgs = (0, "Starting to make a GrantCollection")
        if metaknowledge.VERBOSE_MODE and not quietStart:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            bad = False
            errors = {}
            name = name
            grantTypes = set()

            if inGrants is None:
                PBar.updateVal(.5, "Empty GrantCollection created")
                if not name:
                    name = "Empty"
                grantsSet = set()

            elif isinstance(inGrants, str):
                if os.path.isfile(inGrants):
                    PBar.updateVal(.2, "GrantCollection from a file started")
                    if not inGrants.endswith(extension):
                        raise GrantCollectionException("extension of input file does not match requested extension '{}'.".format(extension))
                    if not name:
                        name = os.path.splitext(os.path.split(inGrants)[1])[0]
                    try:
                        for grantType, processor, detector in grantProcessors:
                            if detector(inGrants):
                                grantTypes.add(grantType)
                                grantsSet, gError = processor(inGrants)
                                if gError is not None:
                                    bad = True
                                    errors[inGrants] = gError
                                break
                    except UnknownFile:
                        raise BadInputFile("'{}' does not match any known grant file type and the default parser could not handle it.\nIts header might be damaged or it could have been modified by another program.".format(inGrants))
                elif os.path.isdir(inGrants):
                    count = 0
                    PBar.updateVal(0, "GrantCollection from files in {}".format(inGrants))
                    if extension and not name:
                        name = "{}-files-from-{}".format(extension, inGrants)
                    elif not name:
                        name = "files-from-{}".format(inGrants)
                    grantsSet = set()
                    flist = []
                    for f in os.listdir(inGrants):
                        fullF = os.path.join(os.path.abspath(inGrants), f)
                        if fullF.endswith(extension) and os.path.isfile(fullF):
                            flist.append(fullF)
                    if cached:
                        cacheName = os.path.join(inGrants, '{}.[{}].mkGrantDirCache'.format(os.path.basename(os.path.abspath(inGrants)), extension))
                        if self._loadFromCache(cacheName, flist, name, extension):
                            try:
                                PBar.finish("Done reloading {} Grants from cache".format(len(self)))
                            except AttributeError:
                                PBar.finish("Done reloading from the cache {}. Warning an error occured.".format(cacheName))
                            return
                        else:
                            PBar.updateVal(0, 'Cache error, rereading files')
                    for fileName in flist:
                        count += 1
                        PBar.updateVal(count / len(flist), "Reading grants from: {}".format(fileName))
                        try:
                            for grantType, processor, detector in grantProcessors:
                                if detector(fileName):
                                    grantTypes.add(grantType)
                                    grants, gError = processor(fileName)
                                    if gError is not None:
                                        bad = True
                                        errors[fileName] = gError
                                    #This is need for any grants thats can span mutiple files
                                    if grantType == "NSERCGrant":
                                        if len(grants & grantsSet) > 0:
                                            #In theory this could be done with
                                            #the builtin operators (& and ^),
                                            #but the exact results are not
                                            #defined for objects with identical
                                            #hashes without identical attributes
                                            #so it could not be counted on
                                            #Thus we get this mess
                                            overlap = {}
                                            for Gin in grants:
                                                if Gin in grantsSet:
                                                    overlap[Gin.id] = Gin
                                            for Gover in overlap.values():
                                                grants.remove(Gover)
                                            for Gset in grantsSet:
                                                if Gset.id in overlap:
                                                    Gset.update(overlap[Gset.id])
                                    grantsSet |= grants
                                    break
                        except UnknownFile:
                            if extension != '':
                                raise BadInputFile("'{}' does not match any known file type, but has the requested extension '{}'. Its header might be damaged or it could have been modified by another program.".format(fileName, extension))
                            else:
                                pass
                else:
                    raise GrantCollectionException("'{}' is not a path to a directory or file. Strings cannot be used to initialize GrantCollections".format(inGrants))

            elif isinstance(inGrants, collections.abc.Iterable):
                PBar.updateVal(.5, "GrantCollection started from {}".format(type(inGrants).__name__))
                if not name:
                    name = "Grants-from-a-{}".format(type(inGrants).__name__)
                for G in inGrants:
                    if not isinstance(G, Grant):
                        raise GrantCollectionException("A GrantCollection cannot be created from a Iterable containing {}".format(G))
                grantsSet = set(inGrants)
            else:
                raise GrantCollectionException("A GrantCollection cannot be created from {}".format(inGrants))
            CollectionWithIDs.__init__(self, grantsSet, Grant, grantTypes, name, bad, errors, quietStart = quietStart)
            if cached:
                PBar.updateVal(1, "Writing GrantCollection cache to {}".format(cacheName))
                self._createCache(cacheName, flist, name, extension)
            try:
                PBar.finish("Done making a GrantCollection of {} Grants".format(len(self)))
            except AttributeError:
                PBar.finish("Done making a GrantCollection. Warning an error occured.")

    def networkCoInvestigatorInstitution(self, targetTags = None, tagSeperator = ';', count = True, weighted = True):
        """This works the same as [networkCoInvestigator()](#metaknowledge.GrantCollection.networkCoInvestigator) see it for details."""
        return self.networkCoInvestigator(targetTags = targetTags, tagSeperator = tagSeperator, count = count, weighted = weighted, _institutionLevel = True)

    def networkCoInvestigator(self, targetTags = None, tagSeperator = ';', count = True, weighted = True, _institutionLevel = False):
        """Creates a co-investigator from the collection

        Most grants do not have a known investigator tag so it must be provided by the user in _targetTags_ and the separator character if it is not a semicolon should also be given.

        # Parameters

        > _targetTags_ : `optional list[str]`

        > A list of all the Grant tags to check for investigators

        _tagSeperator_ : `optional str`

        > The character that separates the individual investigator's names

        _count_ : `optional bool`

        > Default `True`, if `True` the number of time a name occurs will be given

        _weighted_ : `optional bool`

        > Default `True`, if `True` the edge weights will be calculated and added to the edges

        # Returns

        `networkx Graph`

        > The graph of co-investigator
        """
        grph = nx.Graph()
        pcount = 0
        if _institutionLevel:
            progArgs = (0, "Starting to make a co-institution network")
        else:
            progArgs = (0, "Starting to make a co-investigator network")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            for G in self:
                if PBar:
                    pcount += 1
                    PBar.updateVal(pcount/ len(self), "Analyzing: " + str(G))
                if _institutionLevel:
                    investList = G.getInstitutions(tags = targetTags, seperator = tagSeperator, _getTag = True)
                else:
                    investList = G.getInvestigators(tags = targetTags, seperator = tagSeperator, _getTag = True)
                if len(investList) > 1:
                    for i, invest1 in enumerate(investList):
                        if invest1[0] not in grph:
                            if count:
                                grph.add_node(invest1[0], count = 1, field = invest1[1])
                            else:
                                grph.add_node(invest1[0], field = invest1[1])
                        elif count:
                            grph.node[invest1[0]]['count'] += 1
                        for invest2 in investList[i + 1:]:
                            if invest2[0] not in grph:
                                if count:
                                    grph.add_node(invest2[0], count = 1, field = invest2[1])
                                else:
                                    grph.add_node(invest2[0], field = invest2[1])
                            elif count:
                                grph.node[invest2[0]]['count'] += 1
                            if grph.has_edge(invest1[0], invest2[0]) and weighted:
                                grph.edges[invest1[0], invest2[0]]['weight'] += 1
                            elif weighted:
                                grph.add_edge(invest1[0], invest2[0], weight = 1)
                            else:
                                grph.add_edge(invest1[0], invest2[0])
                elif len(investList) > 0:
                    invest1 = investList[0]
                    if invest1[0] not in grph:
                        if count:
                            grph.add_node(invest1[0], count = 1, field = invest1[1])
                        else:
                            grph.add_node(invest1[0], field = invest1[1])
                    elif count:
                        grph.node[invest1[0]]['count'] += 1
            if _institutionLevel:
                PBar.finish("Done making a co-institution network from {}".format(self))
            else:
                PBar.finish("Done making a co-investigator network from {}".format(self))
        return grph
