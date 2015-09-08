#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import metaknowledge
from .record import Record, BadISIFile
from .graphHelpers import _ProgressBar
from .constants import tagsAndNames, tagToFull, fullToTag
from .citation import filterNonJournals, Citation

import itertools
import os.path
import csv

import networkx as nx

class RecordCollection(object):
    """
    A way of containing a large number of Record objects, it provides ways of creating them from an isi file, string, list of records or directory containing isi files. The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur.
    The comparison operators <, <=, >, >= are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

    When being created if there are issues the Record collection will be declared bad (self.bad = True) it will then mostly return nothing or False. The error attribute contains the exception that occurred.

    They also possess a name accessed with repr(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred, read __repr__'s doc string for more information

    inCollection is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

    name sets the name of the of the record if left blank name will be generated based on the object that created the Recordcollection

    extension controls the extension that __init__ looks for when reading a directory, set it to the extension on the isi files you wish to load, if left blank all files will be tried and any that are not isi files will be silently skipped

    # \_\_Init\_\_

    RecordCollections are made from either a single file or directory supplied as _inCollection_.

    # Parameters

    _inCollection_ : `optional [str] or None`

    > the name of the source of WOS records. It can be skipped to produce an empty collection.

    > If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

    > If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

    _name_ : `optional [str]`

    > The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

    _extension_ : `optional [str]`

    > The extension to search for when reading a directoy for files. _extension_ is the suffix searched for when a direcorty is read for files, by default it is empty so all files are read.
    """

    def __init__(self, inCollection = None, name = '', extension = ''):
        self.bad = False
        self._repr = name
        if not inCollection:
            if not name:
                self._repr = "empty"
            self._Records = set()
        elif isinstance(inCollection, str):
            if os.path.isfile(inCollection):
                try:
                    if not inCollection.endswith(extension):
                        raise TypeError("extension of input file does not match requested extension")
                    self._repr = os.path.splitext(os.path.split(inCollection)[1])[0]
                    self._Records = set(isiParser(inCollection))
                except BadISIFile as w:
                    self.bad = True
                    self.error = w
            elif os.path.isdir(inCollection):
                if metaknowledge.VERBOSE_MODE:
                    PBar = _ProgressBar(0, "Reading files from " + str(inCollection))
                    count = 0
                else:
                    PBar = None
                if extension and not name:
                    if extension[0] == '.':
                        self._repr = extension[1:] + "-files-from-" + os.path.dirname(inCollection)
                    else:
                        self._repr = extension + "-files-from-" + inCollection
                elif not name:
                    self._repr = "files-from-" + inCollection
                self._Records = set()
                flist = []
                for f in os.listdir(inCollection):
                    fullF = os.path.join(os.path.abspath(inCollection), f)
                    if fullF.endswith(extension) and os.path.isfile(fullF):
                        flist.append(fullF)
                for file in flist:
                    if PBar:
                        count += 1
                        PBar.updateVal(count / len(flist), "Reading records from: " + file)
                    else:
                        PBar = None
                    try:
                        self._Records |= set(isiParser(file))
                    except BadISIFile:
                        if extension != '':
                            raise
                        else:
                            pass
                    except UnicodeDecodeError:
                        pass
                if PBar:
                    PBar.finish("Done reading records from: " + str(inCollection))
            else:
                raise TypeError("inCollection is not a directory or a file")
        elif isinstance(inCollection, list):
            self._Records = set(inCollection)
        elif isinstance(inCollection, set):
            self._Records = inCollection
        else:
            raise TypeError

    def __add__(self, other):
        """
        returns the union of the two RecordCollections
        """
        if self.bad and other.bad:
            return RecordCollection(set(), '[BAD ' + repr(self) + ']'+ '_plus_' + '[BAD ' +  repr(other) + ']')
        if self.bad:
            return RecordCollection(other._Records, '[BAD ' + repr(self) + ']' + '_plus_' + repr(other))
        elif other.bad:
            return RecordCollection(self._Records,  repr(self) + '[BAD ' + repr(other) + ']')
        else:
            return RecordCollection(self._Records | other._Records, repr(self) + '_plus_' + repr(other))

    def __and__(self, other):
        """
        returns the intersection of the two RecordCollections
        """
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records & other._Records, repr(self) + '_and_' + repr(other))

    def __sub__(self, other):
        """
        returns the difference of the two RecordCollections
        """
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records - other._Records, repr(self) + '_diff_' + repr(other))

    def __xor__(self, other):
        """
        returns the symmetric difference of the two RecordCollections
        """
        if self.bad or other.bad:
            raise Exception
        else:
            return RecordCollection(self._Records ^ other._Records, repr(self) + '_symdiff_' + repr(other))

    def __str__(self):
        """
        Returns a string giving the the number Records in a sentence:
        "Collection of # records"
        """
        return "Collection of " + str(len(self._Records)) + " records"

    def __repr__(self):
        """
        The name of the RecordCollection, this used to identify the Collection when it is written as a file by writeFile() or in some of CL scripts
        It is updated when some modification of the RecordCollection occurs i.e.
        >>> RC = metaknowledge.RecordCollection('.', extension = 'isi')
        >>> repr(RC)
        isi-files-from-.
        >>> R = RC.pop()
        >>> repr(RC)
        pop-isi-files-from-.
        """
        return self._repr

    def __lt__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) < len(other)
    def __le__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) <= len(other)
    def __gt__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) > len(other)
    def __ge__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return len(self) >= len(other)

    def __eq__(self, other):
        if self.bad or other.bad:
            return False
        else:
            return self._Records == other._Records

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        """
        returns the number or Records
        """
        return len(self._Records)

    def __iter__(self):
        """
        iterates over the Records
        """
        for R in self._Records:
            yield R

    def __contains__(self, item):
        """
        Returns True if the item is a WOS string of one of the Records containing or if item is a Record checks if the record is in the RecordCollection, otherwise returns False
        """
        if isinstance(item, str):
            for R in self:
                if R.UT == item:
                    return True
            return False
        elif isinstance(item, Record):
            return item in self._Records
        else:
            return False


    def pop(self):
        """
        Returns a random Record from the recordCollection, the Record is deleted from the collection, use peak for nondestructive access
        """
        if len(self._Records) > 0:
            self._repr = "Pop-" + self._repr
            return self._Records.pop()
        else:
            return None

    def peak(self):
        """
        Returns a random Record from the recordCollection, the Record is kept in the collection, use pop for faster destructive access
        """
        if len(self._Records) > 0:
            return self._Records.__iter__().__next__()
        else:
            return None

    def dropWOS(self, wosNum):
        """Removes the Record with WOS number (ID number) _wosNum_

        # Parameters

        _wosNum_ : `str`

        > _wosNum_ is the WOS number of the Record to be dropped. _wosNum_ must begin with 'WOS:' or a valueError is raise.
        """
        if wosNum[:4] != 'WOS:':
            raise ValueError("{} is not a valid WOS number string, it does not start with 'WOS:'.".format(wosNum))
        for R in self._Records:
            if R.wosString == wosNum:
                self._Records.remove(R)
                break

    def getWOS(self, wosNum, drop = False):
        """Gets the Record from the collection by its WOS number.

        # Parameters

        _wosNum_ : `str`

        > _wosNum_ is the WOS number of the Record to be extracted. _wosNum_ must begin with 'WOS:' or a valueError is raise.

        _drop_ : `optional [bool]`

        > Default `False`. If `True` the Record is dropped from the collection after being extract, i.e. if `False` [getWOS()](#RecordCollection.getWOS) acts like [peak()](#RecordCollection.peak), if `True` it acts like [pop()](#RecordCollection.pop)

        # Returns

        `metaknowledge.Record`

        > The Record whose WOS number is _wosNum_
        """
        try:
            if wosNum[:4] != 'WOS:':
                raise ValueError("{} is not a valid WOS number string, it does not start with 'WOS:'.".format(wosNum))
        except (TypeError, IndexError):
            raise ValueError("{} is not a valid WOS number string, it does not start with 'WOS:'.".format(wosNum))
        for R in self:
            if R.wosString == wosNum:
                if drop:
                    self._Records.remove(R)
                return R
        return None

    def getBadRecords(self):
        """
        returns RecordCollection containing all the Record which have their bad flag set to True, i.e. all those removed by dropBadRecords()
        """
        badRecords = set()
        for R in self._Records:
            if R.bad:
                badRecords.add(R)
        return RecordCollection(badRecords, repr(self) + '_badRecords')

    def dropBadRecords(self):
        """
        Removes all Records with bad attributes == True from the collection
        """
        self._Records = {r for r in self._Records if not r.bad}
        self._repr = repr(self) + '_badRecordsDropped'

    def dropNonJournals(self, ptVal = 'J', dropBad = True, invert = False):
        """Drops the non journal type Records from the collection

        # Parameters

        _ptVal_ : `optional [str]`

        > The value of the PT tag to be kept, default is 'J' the journal tag

        _dropBad_ : `optional [bool]`

        > Determines if bad Records will be dropped as well, default `True`

        _invert_ : `optional [bool]`

        > Set `True` to drop journals (or the PT tag given by _ptVal) instead of keeping them. Note, it still drops bad Records if _dropBad_ is `True`, default `False`
        """
        if dropBad:
            self.dropBadRecords()
        if invert:
            self._Records = {r for r in self._Records if r.PT != ptVal.upper()}
            self._repr = repr(self) + '_PT-{}-Dropped'.format(ptVal)
        else:
            self._Records = {r for r in self._Records if r.PT == ptVal.upper()}
            self._repr = repr(self) + '_PT-{}-Only'.format(ptVal)

    def writeFile(self, fname = None):
        """
        Writes the RecordCollection to a file, the written file is identical to those download from WOS. The order of Records written is random.

        fname set the name of the file, if blank the RecordCollection's name's first 200 characters are use with the suffix .isi
        """
        if fname:
            f = open(fname, mode = 'w', encoding = 'utf-8')
        else:
            f = open(repr(self)[:200] + '.isi', mode = 'w', encoding = 'utf-8')
        f.write("\ufeffFN Thomson Reuters Web of Science\u2122\n")
        f.write("VR 1.0\n")
        for R in self._Records:
            R.writeRecord(f)
            f.write('\n')
        f.write('EF')
        f.close()

    def writeCSV(self, fname = None, onlyTheseTags = None, longNames = False, firstTags = ['UT', 'PT', 'TI', 'AF', 'CR'], csvDelimiter = ',', csvQuote = '"', listDelimiter = '|'):
        """Writes all the Records from the collection into a csv file with each row a record and each column a tag

        fname is the name of the file to write to, if none is given it uses the Collections name suffixed by .csv

        onlyTheseTags lets you specify which tags to use, if not given then all tags in the records are given.
        If you want to use all known tags the use onlyTheseTags = metaknowledge.knownTagsList

        longNames if set to True will convert the tags to their longer names, otherwise the short 2 character ones will be used

        firstTags is the column's tags, it is set by default to ['UT', 'PT', 'TI', 'AF', 'CR'] so those will be written first if given by onlyTheseTags.
        Note if tags are in firstTags but not in onlyTheseTags, onlyTheseTags will override onlyTheseTags

        csvDelimiter is the delimiter used for the cells of the csv file, default is the comma (,)

        csvQuote is  the quote character used for the csv, default is the double quote (")

        listDelimiter is the delimiter used between values of the same cell if the tag for that record has multiple outputs, default is the pipe (|)
        """
        for i in range(len(firstTags)):
            if firstTags[i] in fullToTag:
                firstTags[i] = fullToTag[firstTags[i]]
        if onlyTheseTags:
            for i in range(len(onlyTheseTags)):
                if onlyTheseTags[i] in fullToTag:
                    onlyTheseTags[i] = fullToTag[onlyTheseTags[i]]
            retrievedFields = [t for t in firstTags if t in onlyTheseTags] + [t for t in onlyTheseTags if t not in firstTags]
        else:
            retrievedFields = firstTags
            for R in self:
                tagsLst = [t for t in R.activeTags() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFull[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        if fname:
            f = open(fname, mode = 'w', encoding = 'utf-8')
        else:
            f = open(repr(self)[:200] + '.csv', mode = 'w', encoding = 'utf-8')
        csvWriter = csv.DictWriter(f, retrievedFields, delimiter = csvDelimiter, quotechar = csvQuote, quoting=csv.QUOTE_ALL)
        csvWriter.writeheader()
        for R in self:
            recDict = R.getTagsDict(retrievedFields)
            for k in recDict.keys():
                value = recDict[k]
                if hasattr(value, '__iter__'):
                    recDict[k] = listDelimiter.join([str(v) for v in value])
                elif recDict[k] == None:
                    recDict[k] = ''
                else:
                    recDict[k] = str(value)
            csvWriter.writerow(recDict)
        f.close()


    def makeDict(self, onlyTheseTags = None, longNames = False, cleanedVal = True):
        """Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

        When used in pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

        # Parameters

        See writeCSV()
        """
        if onlyTheseTags:
            for i in range(len(onlyTheseTags)):
                if onlyTheseTags[i] in fullToTag:
                    onlyTheseTags[i] = fullToTag[onlyTheseTags[i]]
            retrievedFields = onlyTheseTags
        else:
            retrievedFields = []
            for R in self:
                tagsLst = [t for t in R.activeTags() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFull[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        retDict = {k : [] for k in retrievedFields}
        for R in self:
            for k, v in R.getTagsDict(retrievedFields, cleaned = cleanedVal).items():
                retDict[k].append(v)
        return retDict

    def coAuthNetwork(self):
        """Creates a coauthorship network for the RecordCollection.

        # Returns

        `Networkx Graph`

        > A networkx graph with author names as nodes and collaborations as edges.
        """
        grph = nx.Graph()
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a co-authorship network")
            pcount = 0
        else:
            PBar = None
        for R in self:
            if PBar:
                pcount += 1
                PBar.updateVal(pcount/ len(self), "Analyzing: " + str(R))
            authsList = R.authorsFull
            if authsList:
                authsList = list(authsList)
                if len(authsList) > 1:
                    for i, auth1 in enumerate(authsList):
                        if auth1 not in grph:
                            grph.add_node(auth1, count = 1)
                        else:
                            grph.node[auth1]['count'] += 1
                        for auth2 in authsList[i + 1:]:
                            if auth2 not in grph:
                                grph.add_node(auth2, count = 1)
                            else:
                                grph.node[auth2]['count'] += 1
                            if grph.has_edge(auth1, auth2):
                                grph.edge[auth1][auth2]['weight'] += 1
                            else:
                                grph.add_edge(auth1, auth2, weight = 1)
                else:
                    auth1 = authsList[0]
                    if auth1 not in grph:
                        grph.add_node(auth1, count = 1)
                    else:
                        grph.node[auth1]['count'] += 1
        if PBar:
            PBar.finish("Done making a co-authorship network")
        return grph

    def coCiteNetwork(self, dropAnon = True, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, keyWords = None):
        """Creates a co-citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`](metaknowledge.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

        _dropAnon_ : `optional [bool]`

        > default `True`, if `True` citations labeled anonymous are removed from the network

        _nodeInfo_ : `optional [bool]`

        > default `True`, wether an extra piece of information is stored with each node.

        _fullInfo_ : `optional [bool]`

        > default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

        _weighted_ : `optional [bool]`

        > default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

        _dropNonJournals_ : `optional [bool]`

        > default `False`, wether to drop citations of non-journals

        _count_ : `optional [bool]`

        > default `True`, causes the number of occurrences of a node to be counted

        _keyWords_ : `optional [str] or [list[str]]`

        > A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

        # Returns

        `Networkx Graph`

        > A networkx graph with hashes as ID and co-citation as edges
        """

        builinFilters = ["dropAnon", "dropNonJournals", "dropJournals"]
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise ValueError("{} is not an allowed nodeType.".format(nodeType))
        tmpgrph = nx.Graph()
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a co-citation network")
            count = 0
        else:
            PBar = None
        if nodeType == "full":
            citesSet = set()
        else:
            citesSet = None
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            Cites = R.citations
            if Cites:
                filteredCites = filterCites(Cites, nodeType, dropAnon, dropNonJournals, keyWords)
                addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo , fullInfo, headNd = None, cSet = citesSet)
        if PBar:
            PBar.finish("Done making a co-citation network of " + repr(self))
        return tmpgrph


    def citationNetwork(self, dropAnon = True, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, directed = True, keyWords = None):

        """Creates a citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`](metaknowledge.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

        _dropAnon_ : `optional [bool]`

        > default `True`, if `True` citations labeled anonymous are removed from the network

        _nodeInfo_ : `optional [bool]`

        > default `True`, wether an extra piece of information is stored with each node.

        _fullInfo_ : `optional [bool]`

        > default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

        _weighted_ : `optional [bool]`

        > default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

        _dropNonJournals_ : `optional [bool]`

        > default `False`, wether to drop citations of non-journals

        _count_ : `optional [bool]`

        > default `True`, causes the number of occurrences of a node to be counted

        _keyWords_ : `optional [str] or [list[str]]`

        > A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

        _directed_ : `optional [bool]`

        > Determines if the output graph is directed, default `True`

        # Returns

        `Networkx DiGraph or Networkx Graph`

        > See _directed_ for explanation of returned type

        > A networkx digraph with hashes as ID and citations as edges
        """
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise ValueError("{} is not an allowed nodeType.".format(nodeType))
        if directed:
            tmpgrph = nx.DiGraph()
        else:
            tmpgrph = nx.Graph()
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a citation network")
            count = 0
        else:
            PBar = None
        if nodeType == allowedTypes[0]:
            citesSet = set()
        else:
            citesSet = None
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count/ len(self), "Analyzing: " + str(R))
            reRef = R.createCitation()
            if len(filterCites([reRef], nodeType, dropAnon, dropNonJournals, keyWords)) == 0:
                continue
            rCites = R.citations
            if rCites:
                filteredCites = filterCites(rCites, nodeType, dropAnon, dropNonJournals, keyWords)
                addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo , fullInfo, headNd = reRef, cSet = citesSet)
        if PBar:
            PBar.finish("Done making a citation network of " + repr(self))
        return tmpgrph

    def extractTagged(self, taglist):
        recordsWithTags = set()
        for R in self:
            for t in taglist:
                hasTags = True
                if t not in R.tags:
                    hasTags = False
                    break
            if hasTags:
                recordsWithTags.add(R)
        return RecordCollection(recordsWithTags, repr(self) + "_tags(" + ','.join(taglist) + ')')

    def yearSplit(self, startYear, endYear):
        recordsInRange = set()
        for R in self._Records:
            if R.year >= startYear and R.year <= endYear:
                recordsInRange.add(R)
        return RecordCollection(recordsInRange, repr(self) + "_(" + str(startYear) + " ," + str(endYear) + ")")

    def oneModeNetwork(self, mode, nodeCount = True, edgeWeight = True):
        if mode not in tagsAndNames:
            raise TypeError(str(mode) + " is not a known tag, or the name of a known tag.")
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a one mode network with " + mode)
            count = 0
        else:
            PBar = None
        grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents = getattr(R, mode, None)
            if contents:
                if isinstance(contents, list):
                    tmplst = [str(n) for n in contents]
                    if len(tmplst) > 1:
                        for i, node1 in enumerate(tmplst):
                            for node2 in tmplst[i + 1:]:
                                if edgeWeight:
                                    try:
                                        grph.edge[node1][node2]['weight'] += 1
                                    except KeyError:
                                        grph.add_edge(node1, node2, weight = 1)
                                else:
                                    if not grph.has_edge(node1, node2):
                                        grph.add_edge(node1, node2)
                            if nodeCount:
                                try:
                                    grph.node[node1]['count'] += 1
                                except KeyError:
                                    grph.node[node1]['count'] = 1
                            else:
                                if not grph.has_node(node1):
                                    grph.add_node(node1)
                    elif len(tmplst) == 1:
                        if nodeCount:
                            try:
                                grph.node[tmplst[0]]['count'] += 1
                            except KeyError:
                                grph.add_node(tmplst[0], count = 1)
                        else:
                            if not grph.has_node(tmplst[0]):
                                grph.add_node(tmplst[0])
                    else:
                        pass
                else:
                    nodeVal = str(contents)
                    if nodeCount:
                        try:
                            grph.node[nodeVal]['count'] += 1
                        except KeyError:
                            grph.add_node(nodeVal, count = 1)
                    else:
                        if not grph.has_node(nodeVal):
                            grph.add_node(nodeVal)
        if PBar:
            PBar.finish("Done making a one mode network with " + mode)
        return grph

    def twoModeNetwork(self, tag1, tag2, directed = False, recordType = True, nodeCount = True, edgeWeight = True):
        if (not tag1 in tagsAndNames) or (not tag2 in tagsAndNames):
            raise TypeError(str(tag1) + " or " + str(tag2) + " is not a known tag, or the name of a known tag.")
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a two mode network of " + tag1 + " and " + tag2)
            count = 0
        else:
            PBar = None
        if directed:
            grph = nx.DiGraph()
        else:
            grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents1 = getattr(R, tag1, None)
            contents2 = getattr(R, tag2, None)
            if isinstance(contents1, list):
                contents1 = [str(v) for v in contents1]
            elif contents1 == None:
                contents1 = []
            else:
                contents1 = [str(contents1)]
            if isinstance(contents2, list):
                contents2 = [str(v) for v in contents2]
            elif contents2 == None:
                contents2 = []
            else:
                contents2 = [str(contents2)]
            for node1 in contents1:
                for node2 in contents2:
                    if edgeWeight:
                        try:
                            grph.edge[node1][node2]['weight'] += 1
                        except KeyError:
                            grph.add_edge(node1, node2, weight = 1)
                    else:
                        if not grph.has_edge(node1, node2):
                            grph.add_edge(node1, node2)
                if nodeCount:
                    try:
                        grph.node[node1]['count'] += 1
                    except KeyError:
                        try:
                            grph.node[node1]['count'] = 1
                            if recordType:
                                grph.node[node1]['type'] = tag1
                        except KeyError:
                            if recordType:
                                grph.add_node(node1, type = tag1)
                            else:
                                grph.add_node(node1)
                else:
                    if not grph.has_node(node1):
                        if recordType:
                            grph.add_node(node1, type = tag1)
                        else:
                            grph.add_node(node1)
                    elif recordType:
                        if 'type' not in grph.node[node1]:
                            grph.node[node1]['type'] = tag1

            for node2 in contents2:
                if nodeCount:
                    try:
                        grph.node[node2]['count'] += 1
                    except KeyError:
                        try:
                            grph.node[node2]['count'] = 1
                            if recordType:
                                grph.node[node2]['type'] = tag2
                        except KeyError:
                            grph.add_node(node2, count = 1)
                            if recordType:
                                grph.node[node2]['type'] = tag2
                else:
                    if not grph.has_node(node2):
                        if recordType:
                            grph.add_node(node2, type = tag2)
                        else:
                            grph.add_node(node2)
                    elif recordType:
                        if 'type' not in grph.node[node2]:
                            grph.node[node2]['type'] = tag2
        if PBar:
            PBar.finish("Done making a two mode network of " + tag1 + " and " + tag2)
        return grph

    def nModeNetwork(self, tags, recordType = True, nodeCount = True, edgeWeight = True):
        for t in tags:
            if t not in tagsAndNames:
                raise TypeError(str(t) + " is not a known tag, or the name of a known tag.")
        if metaknowledge.VERBOSE_MODE:
            PBar = _ProgressBar(0, "Starting to make a " + str(len(tags)) + "-mode network of: " + ', '.join(tags))
            count = 0
        else:
            PBar = None
        grph = nx.Graph()
        for R in self:
            if PBar:
                count += 1
                PBar.updateVal(count / len(self), "Analyzing: " + str(R))
            contents = []
            for t in tags:
                tmpVal = getattr(R, t, None)
                if tmpVal:
                    if isinstance(tmpVal, list):
                        contents.append((t, [str(v) for v in tmpVal]))
                    else:
                        contents.append((t, [str(tmpVal)]))
            for i, vlst1 in enumerate(contents):
                for node1 in vlst1[1]:
                    for vlst2 in contents[i + 1:]:
                        for node2 in vlst2[1]:
                            if edgeWeight:
                                try:
                                    grph.edge[node1][node2]['weight'] += 1
                                except KeyError:
                                    grph.add_edge(node1, node2, weight = 1)
                            else:
                                if not grph.has_edge(node1, node2):
                                    grph.add_edge(node1, node2)
                    if nodeCount:
                        try:
                            grph.node[node1]['count'] += 1
                        except KeyError:
                            try:
                                grph.node[node1]['count'] = 1
                                if recordType:
                                    grph.node[node1]['type'] = vlst1[0]
                            except KeyError:
                                if recordType:
                                    grph.add_node(node1, type = vlst1[0])
                                else:
                                    grph.add_node(node1)
                    else:
                        if not grph.has_node(node1):
                            if recordType:
                                grph.add_node(node1, type = vlst1[0])
                            else:
                                grph.add_node(node1)
                        elif recordType:
                            try:
                                grph.node[node1]['type'] += vlst1[0]
                            except KeyError:
                                grph.node[node1]['type'] = vlst1[0]
        if PBar:
            PBar.finish("Done making a " + str(len(tags)) + "-mode network of: " +  ', '.join(tags))
        return grph

    def localCiteStats(self):
        """Returns a dict with all the citations in the CR field as keys and the number of time s they occur as the values
        """
        citesDict = {}
        for R in self:
            rCites = R.CR
            if rCites:
                for c in rCites:
                    found = False
                    for dC, occus in citesDict.items():
                        if dC == c:
                            citesDict[dC] = occus + 1
                            found = True
                            break
                    if not found:
                         citesDict[c] = 1
        return citesDict

    def localCitesOf(self, rec):
        """Takes in a Record, WOS string, citation string or Citation and returns a list of all records that cite it
        """
        localCites = []
        if isinstance(rec, Record):
            rec = rec.createCitation()
        if isinstance(rec, str):
            try:
                rec = self.getWOS(rec)
            except ValueError:
                try:
                    rec = Citation(rec)
                except AttributeError:
                    raise ValueError("{} is not a valid WOS string or a valid citation string".format(rec))
            else:
                if rec is None:
                    return localCites
                else:
                    rec = rec.createCitation()
        elif isinstance(rec, Citation):
            pass
        else:
            raise ValueError("{} is not a vaild input, rec must be a Record, string or Citation object.".format(Rec))
        for R in self:
            rCites = R.CR
            if rCites:
                for cite in rCites:
                    if rec == cite:
                        localCites.append(R)
                        break
        return localCites

    def citeFilter(self, keyString = '', field = 'all', reverse = False, caseSensitive = False):
        """
        Filters Records by some string, keyString, in all of their citations.
        Returns all Records with at least one citation possessing keyString in the field given by field.

        keyString give the string to be searched for if it is is blank then all citations with the specified field will be matched

        field give the component of the citation to be looked at, it is one of a few strings. The default is 'all' which will cause the entire original citation to be searched. It can be used to search across fields, e.g. '1970, V2' is a valid keystring
        The other options are:
        author, searches the author field
        year, searches the year field
        journal, searches the journal field
        V, searches the volume field
        P, searches the page field
        misc, searches all the remaining uncategorized information
        anonymous, searches for anonymous citations, keyString is not used
        bad, searches for bad citations, keyString is not used

        reverse being True causes all Records not matching the query to be returned, default is False

        caseSensitive if True causes the search across the original to be case sensitive, only the 'all' option can be case sensitive

        """
        retRecs = []
        keyString = str(keyString)
        for R in self:
            try:
                if field == 'all':
                    for cite in R.citations:
                        if caseSensitive:
                            if keyString in cite.original:
                                retRecs.append(R)
                                break
                        else:
                            if keyString.upper() in cite.original.upper():
                                retRecs.append(R)
                                break
                elif field == 'author':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.author:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'journal':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.journal:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'year':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.year:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'V':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.V:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'P':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.P:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'misc':
                    for cite in R.citations:
                        try:
                            if keyString.upper() in cite.misc:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'anonymous':
                    for cite in R.citations:
                        if cite.isAnonymous():
                            retRecs.append(R)
                            break
                elif field == 'bad':
                    for cite in R.citations:
                        if cite.bad:
                            retRecs.append(R)
                            break
            except TypeError:
                pass
        if reverse:
            excluded = []
            for R in self:
                if R not in retRecs:
                    excluded.append(R)
            return RecordCollection(inCollection = excluded, name = self._repr + '_subsetByNotCite')
        else:
            return RecordCollection(inCollection = retRecs, name = self._repr + '_subsetByCite')


def isiParser(isifile):
    """
    isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
    Each it finds is used to initialize a Record then all Record are returned as a list.
    """
    try:
        openfile = open(isifile, 'r', encoding='utf-8-sig')
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    f = enumerate(openfile, start = 0)
    try:
        linesChecked = 3
        for i in range(linesChecked):
            if "VR 1.0" in f.__next__()[1]:
                break
            if i == linesChecked - 1:
                openfile.close()
                raise BadISIFile(isifile + " Does not have a valid header, 'VR 1.0' not in first two lines")
    except StopIteration as e:
        openfile.close()
        raise BadISIFile("File ends before EF found")
    except UnicodeDecodeError as e:
        openfile.close()
        raise e
    notEnd = True
    plst = []
    while notEnd:
        try:
            line = f.__next__()
        except StopIteration as e:
            raise BadISIFile("File ends before EF found")
        if not line[1]:
            raise BadISIFile("No ER found in " + isifile)
        elif line[1].isspace():
            continue
        elif 'EF' in line[1][:2]:
            notEnd = False
            continue
        else:
            try:
                plst.append(Record(itertools.chain([line], f), isifile, line[0]))
            except BadISIFile as w:
                try:
                    s = f.__next__()[1]
                    while s[:2] != 'ER':
                        s = f.__next__()[1]
                except:
                    raise BadISIFile(str(w) + " could not be resolved")
            except Exception as e:
                openfile.close()
                raise e
    try:
        f.__next__()
        raise BadISIFile("EF not at end of " + isifile)
    except StopIteration as e:
        pass
    finally:
        openfile.close()
    return plst

def getCoCiteIDs(clst):
    """
    Creates a dict of the ID-extra information pairs for a CR tag.
    """
    idDict = {}
    for c in clst:
        cId = c.getID()
        if cId not in idDict:
            idDict[cId] = c.getExtra()
    return idDict

def updateWeightedEdges(grph, ebunch):
    for e in ebunch:
        try:
            grph.edge[e[0]][e[1]]['weight'] += e[2]
        except KeyError:
            grph.add_edge(e[0], e[1], weight = e[2])

def edgeBunchGenerator(base, nodes, weighted = False, reverse = False):
    """
    A helper function for generating a bunch of edges from 1 node base to a list of nodes nodes.
    """
    if weighted and reverse:
        for n in nodes:
            yield (n, base, 1)
    elif weighted:
        for n in nodes:
            yield (base, n, 1)
    elif reverse:
        for n in nodes:
            yield (n, base)
    else:
        for n in nodes:
            yield (base, n)

def edgeNodeReplacerGenerator(base, nodes, loc):
    """
    A helper function for replacing an element of nodes at loc with base
    """
    for n in nodes:
        tmpN = list(n)
        tmpN[loc] = base
        yield tmpN


def addToNetwork(grph, nds, count, weighted, nodeType, nodeInfo , fullInfo, headNd = None, cSet = None):
    """Addeds the citations _nds_ to _grph_, arroring to the rules give by _nodeType_, _fullInfo_, etc.

    cSet is the set of known citations, used for _nodeType_ = "full"

    _headNd_ is the citation of the Record
    """
    if headNd is not None:
        hID = makeID(headNd, nodeType, cSet, grph)
        if hID not in grph:
            grph.add_node(*makeNodeTuple(headNd, hID, nodeInfo, fullInfo, nodeType, count))
    else:
        hID = None
    idList = []
    for n in nds:
        nID = makeID(n, nodeType, cSet, grph)
        if nID not in grph:
            grph.add_node(*makeNodeTuple(n, nID, nodeInfo, fullInfo, nodeType, count))
        elif count:
            grph.node[nID]['count'] += 1
        idList.append(nID)
    addedEdges = []
    if hID:
        for nID in idList:
            if weighted:
                try:
                    grph[hID][nID]['weight'] += 1
                except KeyError:
                    grph.add_edge(hID, nID, weight = 1)
            elif nID not in grph[hID]:
                addedEdges.append((hID, nID))
    elif len(idList) > 1:
        for i, outerID in enumerate(idList):
            for innerID in idList[i + 1:]:
                if weighted:
                    try:
                        grph[outerID][innerID]['weight'] += 1
                    except KeyError:
                        grph.add_edge(outerID, innerID, weight = 1)
                elif innerID not in grph[outerID]:
                    addedEdges.append((outerID, innerID))
    grph.add_edges_from(addedEdges)

def makeID(citation, nodeType, cSet, G):
    """Makes the id, of the correct type for the network"""
    if nodeType != "full":
        return getattr(citation, nodeType)
    elif cSet is not None:
        cHash = hash(citation)
        if cHash in G:
            return cHash
        elif citation in cSet:
                for c in cSet:
                    if citation == c:
                        return hash(c)
        else:
            cSet.add(citation)
            return cHash
    else:
        raise ValueError("cSet must be a set of Citations if nodeType is 'full'.")

def makeNodeTuple(citation, idVal, nodeInfo, fullInfo, nodeType, count):
    """Makes a tuple of idVal and a dict of the selected attributes"""
    d = {}
    if nodeInfo:
        if nodeType == 'full':
            d['info'] = str(citation)
        elif nodeType == 'journal':
            if citation.isJournal():
                d['info'] = str(citation.getFullJournalName())
            else:
                d['info'] = "None"
        elif nodeType == 'original':
            d['info'] = str(citation)
        else:
            d['info'] = idVal
    if fullInfo:
        d['fullCite'] = str(citation)
    if count:
        d['count'] = 1
    return (idVal, d)

def filterCites(cites, nodeType, dropAnon, dropNonJournals, keyWords):
    filteredCites = []
    for c in cites:
        if nodeType != "full" and not hasattr(c, nodeType):
            pass
        elif dropNonJournals and not c.isJournal():
            pass
        elif dropAnon and c.isAnonymous():
            pass
        elif keyWords:
            found = False
            citeString = str(c).upper()
            if isinstance(keyWords, str):
                if keyWords.upper() in citeString:
                    found = True
            else:
                for k in keyWords:
                    if k.upper() in citeString:
                        found = True
                        break
            if not found:
                filteredCites.append(c)
        else:
            filteredCites.append(c)
    return filteredCites
