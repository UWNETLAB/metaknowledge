#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import metaknowledge
from .record import Record, BadISIFile
from .graphHelpers import _ProgressBar
from .tagProcessing.funcDicts import tagsAndNameSet, tagToFullDict, fullToTagDict, normalizeToTag
from .citation import Citation

import itertools
import os
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
                count = 0
                if metaknowledge.VERBOSE_MODE:
                    progArgs = (0, "Reading files from " + str(inCollection))
                    progKwargs = {}
                else:
                    progArgs = (0, "Reading files from " + str(inCollection))
                    progKwargs = {'dummy' : True}
                with _ProgressBar(*progArgs, **progKwargs) as PBar:
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

    def addRec(self, Rec):
        """Adds a Record or Records to the RecordCollection.

        # Parameters

        _Rec_ : `Record or iterable[Record]`

        > A Record or some iterable containg records to add
        """
        if hasattr(Rec, '__iter__'):
            self._Records |= set(Rec)
        elif Rec not in self:
            self._Records.add(Rec)

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

    def writeCSV(self, fname = None, onlyTheseTags = None, numAuthors = True, longNames = False, firstTags = None, csvDelimiter = ',', csvQuote = '"', listDelimiter = '|'):
        """Writes all the Records from the collection into a csv file with each row a record and each column a tag

        fname is the name of the file to write to, if none is given it uses the Collections name suffixed by .csv

        onlyTheseTags lets you specify which tags to use, if not given then all tags in the records are given.
        If you want to use all known tags the use onlyTheseTags = metaknowledge.knownTagsList

        numAuthors adds the number of auhtors as the column numAuthors

        longNames if set to True will convert the tags to their longer names, otherwise the short 2 character ones will be used

        firstTags is the column's tags, it is set by default to ['UT', 'PT', 'TI', 'AF', 'CR'] so those will be written first if given by onlyTheseTags.
        Note if tags are in firstTags but not in onlyTheseTags, onlyTheseTags will override onlyTheseTags

        csvDelimiter is the delimiter used for the cells of the csv file, default is the comma (,)

        csvQuote is  the quote character used for the csv, default is the double quote (")

        listDelimiter is the delimiter used between values of the same cell if the tag for that record has multiple outputs, default is the pipe (|)
        """
        if firstTags is None:
            firstTags = ['UT', 'PT', 'TI', 'AF', 'CR']
        for i in range(len(firstTags)):
            if firstTags[i] in fullToTagDict:
                firstTags[i] = fullToTagDict[firstTags[i]]
        if onlyTheseTags:
            for i in range(len(onlyTheseTags)):
                if onlyTheseTags[i] in fullToTagDict:
                    onlyTheseTags[i] = fullToTagDict[onlyTheseTags[i]]
            retrievedFields = [t for t in firstTags if t in onlyTheseTags] + [t for t in onlyTheseTags if t not in firstTags]
        else:
            retrievedFields = firstTags
            for R in self:
                tagsLst = [t for t in R.activeTags() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFullDict[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        if fname:
            f = open(fname, mode = 'w', encoding = 'utf-8')
        else:
            f = open(repr(self)[:200] + '.csv', mode = 'w', encoding = 'utf-8')
        if numAuthors:
            csvWriter = csv.DictWriter(f, retrievedFields + ["numAuthors"], delimiter = csvDelimiter, quotechar = csvQuote, quoting=csv.QUOTE_ALL)
        else:
            csvWriter = csv.DictWriter(f, retrievedFields, delimiter = csvDelimiter, quotechar = csvQuote, quoting=csv.QUOTE_ALL)
        csvWriter.writeheader()
        for R in self:
            recDict = R.getTagsDict(retrievedFields)
            if numAuthors:
                recDict["numAuthors"] = str(R.numAuthors())
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

    def makeDict(self, onlyTheseTags = None, longNames = False, cleanedVal = True, numAuthors = True):
        """Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

        When used in pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

        # Parameters

        See writeCSV()
        """
        if onlyTheseTags:
            for i in range(len(onlyTheseTags)):
                if onlyTheseTags[i] in fullToTagDict:
                    onlyTheseTags[i] = fullToTagDict[onlyTheseTags[i]]
            retrievedFields = onlyTheseTags
        else:
            retrievedFields = []
            for R in self:
                tagsLst = [t for t in R.activeTags() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFullDict[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        retDict = {k : [] for k in retrievedFields}
        if numAuthors:
            retDict["numAuthors"] = []
        for R in self:
            if numAuthors:
                retDict["numAuthors"].append(R.numAuthors())
            for k, v in R.getTagsDict(retrievedFields, cleaned = cleanedVal).items():
                retDict[k].append(v)
        return retDict

    def coAuthNetwork(self, detailedInfo = False, weighted = True, dropNonJournals = False, count = True):
        """Creates a coauthorship network for the RecordCollection.

        # Parameters

        _detailedInfo_ : `optional [bool or iterable[WOS tag Strings]]`

        > default `False`, if `True` all nodes will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedInfo_ is an iterable (that evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attributes.

        > For each of the selected tags an attribute will be added to the node using the values of those tags on the first `Record` encountered. **Warning** iterating over `RecordCollection` objects is not deterministic the first `Record` will not always be same between runs. The node will be given attributes with the names of the WOS tags for each of the selected tags. The attributes will contain strings of containing the values (with commas removed), if multiple values are encountered they will be comma separated.

        > Note: _detailedInfo_ is not identical to the _detailedCore_ argument of [`Recordcollection.coCiteNetwork()`](#RecordCollection.coCiteNetwork) or [`Recordcollection.citationNetwork()`](#RecordCollection.citationNetwork)

        _weighted_ : `optional [bool]`

        > default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of co-authorships.

        _dropNonJournals_ : `optional [bool]`

        > default `False`, wether to drop authors from non-journals

        _count_ : `optional [bool]`

        > default `True`, causes the number of occurrences of a node to be counted

        # Returns

        `Networkx Graph`

        > A networkx graph with author names as nodes and collaborations as edges.
        """
        grph = nx.Graph()
        pcount = 0
        progArgs = (0, "Starting to make a co-authorship network")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        if bool(detailedInfo):
            try:
                infoVals = []
                for tag in detailedInfo:
                    infoVals.append(normalizeToTag(tag))
            except TypeError:
                infoVals = ['PY', 'TI', 'SO', 'VL', 'BP']
            def attributeMaker(Rec):
                attribsDict = {}
                for val in infoVals:
                    recVal = getattr(Rec, val)
                    if isinstance(recVal, list):
                        attribsDict[val] = ', '.join((str(v).replace(',', '') , recVal))
                    else:
                        attribsDict[val] = str(recVal).replace(',', '')
                if count:
                    attribsDict['count'] = 1
                return attribsDict
        else:
            if count:
                attributeMaker = lambda x: {'count' : 1}
            else:
                attributeMaker = lambda x: {}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            for R in self:
                if PBar:
                    pcount += 1
                    PBar.updateVal(pcount/ len(self), "Analyzing: " + str(R))
                if dropNonJournals and not R.createCitation().isJournal():
                    continue
                authsList = R.authorsFull
                if authsList:
                    authsList = list(authsList)
                    detailedInfo = attributeMaker(R)
                    if len(authsList) > 1:
                        for i, auth1 in enumerate(authsList):
                            if auth1 not in grph:
                                grph.add_node(auth1, attr_dict = detailedInfo)
                            elif count:
                                grph.node[auth1]['count'] += 1
                            for auth2 in authsList[i + 1:]:
                                if auth2 not in grph:
                                    grph.add_node(auth2, attr_dict = detailedInfo)
                                elif count:
                                    grph.node[auth2]['count'] += 1
                                if grph.has_edge(auth1, auth2) and weighted:
                                    grph.edge[auth1][auth2]['weight'] += 1
                                elif weighted:
                                    grph.add_edge(auth1, auth2, weight = 1)
                                else:
                                    grph.add_edge(auth1, auth2)
                    else:
                        auth1 = authsList[0]
                        if auth1 not in grph:
                            grph.add_node(auth1, attr_dict = detailedInfo)
                        elif count:
                            grph.node[auth1]['count'] += 1
            if PBar:
                PBar.finish("Done making a co-authorship network")
        return grph

    def coCiteNetwork(self, dropAnon = True, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, keyWords = None, detailedCore = None, coreOnly = False):
        """Creates a co-citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`](#Citation.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

        _dropAnon_ : `optional [bool]`

        > default `True`, if `True` citations labeled anonymous are removed from the network

        _nodeInfo_ : `optional [bool]`

        > default `True`, if `True` an extra piece of information is stored with each node. The extra inforamtion is detemined by _nodeType_.

        _fullInfo_ : `optional [bool]`

        > default `False`, if `True` the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

        _weighted_ : `optional [bool]`

        > default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

        _dropNonJournals_ : `optional [bool]`

        > default `False`, wether to drop citations of non-journals

        _count_ : `optional [bool]`

        > default `True`, causes the number of occurrences of a node to be counted

        _keyWords_ : `optional [str] or [list[str]]`

        > A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

        _detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

        > default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

        > The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

        > Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`](#RecordCollection.coAuthNetwork)

        _coreOnly_ : `optional [bool]`

        > default `False`, if `True` only Citations from the RecordCollection will be included in the network

        # Returns

        `Networkx Graph`

        > A networkx graph with hashes as ID and co-citation as edges
        """
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise ValueError("{} is not an allowed nodeType.".format(nodeType))
        coreValues = []
        if bool(detailedCore):
            try:
                for tag in detailedCore:
                    coreValues.append(normalizeToTag(tag))
            except TypeError:
                coreValues = ['AF', 'PY', 'TI', 'SO', 'VL', 'BP']
        tmpgrph = nx.Graph()
        pcount = 0
        progArgs = (0, "Starting to make a co-citation network")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            if coreOnly or coreValues:
                coreCitesDict = {R.createCitation() : R for R in self}
                if coreOnly:
                    coreCites = coreCitesDict.keys()
                else:
                    coreCites = None
            else:
                coreCitesDict = None
                coreCites = None
            for R in self:
                if PBar:
                    pcount += 1
                    PBar.updateVal(pcount / len(self), "Analyzing: " + str(R))
                Cites = R.citations
                if Cites:
                    filteredCites = filterCites(Cites, nodeType, dropAnon, dropNonJournals, keyWords, coreCites)
                    addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo , fullInfo, coreCitesDict, coreValues, headNd = None)
            if PBar:
                PBar.finish("Done making a co-citation network of " + repr(self))
        return tmpgrph


    def citationNetwork(self, dropAnon = True, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, directed = True, keyWords = None, detailedCore = None, coreOnly = False):

        """Creates a citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`](#Citation.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

        _detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

        > default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

        > The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

        > Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`](#RecordCollection.coAuthNetwork)

        _coreOnly_ : `optional [bool]`

        > default `False`, if `True` only Citations from the RecordCollection will be included in the network

        # Returns

        `Networkx DiGraph or Networkx Graph`

        > See _directed_ for explanation of returned type

        > A networkx digraph with hashes as ID and citations as edges
        """
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise ValueError("{} is not an allowed nodeType.".format(nodeType))
        coreValues = []
        if bool(detailedCore):
            try:
                for tag in detailedCore:
                    coreValues.append(normalizeToTag(tag))
            except TypeError:
                coreValues = ['AF', 'PY', 'TI', 'SO', 'VL', 'BP']
        if directed:
            tmpgrph = nx.DiGraph()
        else:
            tmpgrph = nx.Graph()
        pcount = 0
        progArgs = (0, "Starting to make a citation network")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            if coreOnly or coreValues:
                coreCitesDict = {R.createCitation() : R for R in self}
                if coreOnly:
                    coreCites = coreCitesDict.keys()
                else:
                    coreCites = None
            else:
                coreCitesDict = None
                coreCites = None
            for R in self:
                if PBar:
                    pcount += 1
                    PBar.updateVal(pcount/ len(self), "Analyzing: " + str(R))
                reRef = R.createCitation()
                if len(filterCites([reRef], nodeType, dropAnon, dropNonJournals, keyWords, coreCites)) == 0:
                    continue
                rCites = R.citations
                if rCites:
                    filteredCites = filterCites(rCites, nodeType, dropAnon, dropNonJournals, keyWords, coreCites)
                    addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo, fullInfo, coreCitesDict, coreValues, headNd = reRef)
            if PBar:
                PBar.finish("Done making a citation network of " + repr(self))
        return tmpgrph

    def _extractTagged(self, taglist):
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

    def yearSplit(self, startYear, endYear, dropMissingYears = True):
        """Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

        # Parameters

        _startYear_ : `int`

        > The smallest year to be included in the retuned RecordCollection

        _endYear_ : `int`

        > The largest year to be included in the retuned RecordCollection

        _dropMissingYears_ : `optional [bool]`

        > Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

        # Returns

        `RecordCollection`

        > A RecordCollection of Records from _startYear_ to _endYear_
        """

        recordsInRange = set()
        for R in self._Records:
            try:
                if R.year >= startYear and R.year <= endYear:
                    recordsInRange.add(R)
            except TypeError:
                if dropMissingYears:
                    pass
                else:
                    raise
        return RecordCollection(recordsInRange, repr(self) + "_(" + str(startYear) + " ," + str(endYear) + ")")

    def oneModeNetwork(self, mode, nodeCount = True, edgeWeight = True, stemmer = None):
        """Creates a network of the objects found by one WOS tag _mode_.

        A **oneModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tag given by _mode_, e.g. the `"AF"` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `"AF"` a co-authorship network is created.

        The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

        **Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()](#RecordCollection.coCiteNetwork) it is more accurate and has more options.

        # Parameters

        _mode_ : `str`

        > A two character WOS tag or one of the full names for a tag

        _nodeCount_ : `optional [bool]`

        > Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

        _edgeWeight_ : `optional [bool]`

        > Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

        _stemmer_ : `optional [func]`

        > default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, all IDs are strings. For example:

        >The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

        # Returns

        `networkx Graph`

        > A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges
        """
        try:
            mode = normalizeToTag(mode)
        except KeyError:
            raise TypeError(str(mode) + " is not a known tag, or the name of a known tag.")
        stemCheck = False
        if stemmer is not None:
            if hasattr(stemmer, '__call__'):
                stemCheck = True
            else:
                raise TypeError("stemmer must be callable, e.g. a function or class with a __call__ method.")
        count = 0
        progArgs = (0, "Starting to make a one mode network with " + mode)
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            grph = nx.Graph()
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count / len(self), "Analyzing: " + str(R))
                contents = getattr(R, mode, None)
                if contents:
                    if isinstance(contents, list):
                        if stemCheck:
                            tmplst = [stemmer(str(n)) for n in contents]
                        else:
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
                        if stemCheck:
                            nodeVal = stemmer(str(contents))
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

    def twoModeNetwork(self, tag1, tag2, directed = False, recordType = True, nodeCount = True, edgeWeight = True, stemmerTag1 = None, stemmerTag2 = None):
        """Creates a network of the objects found by two WOS tags _tag1_ and _tag2_.

        A **twoModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `"WC"` and `"LA"` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `"WC"` and language tag `"LA"`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. the node `"English"` would have the type attribute be `"LA"`.

        The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

        The _directed_ parameter if `True` will cause the network to be directed with the first tag as the source and the second as the destination.

        # Parameters

        _tag1_ : `str`

        > A two character WOS tag or one of the full names for a tag, the source of edges on the graph

        _tag1_ : `str`

        > A two character WOS tag or one of the full names for a tag, the target of edges on the graph

        _directed_ : `optional [bool]`

        > Default `False`, if `True` the returned network is directed

        _nodeCount_ : `optional [bool]`

        > Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

        _edgeWeight_ : `optional [bool]`

        > Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

        _stemmerTag1_ : `optional [func]`

        > default `None`, If _stemmerTag1_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node given by _tag1_ in the graph, all IDs are strings. For example:

        >The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

        _stemmerTag2_ : `optional [func]`

        > default `None`, see _stemmerTag1_ as it is the same but for _tag2_

        # Returns

        `networkx Graph or networkx DiGraph`

        > A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.
        """
        try:
            tag1 = normalizeToTag(tag1)
            tag2 = normalizeToTag(tag2)
        except KeyError:
            raise TypeError(str(tag1) + " or " + str(tag2) + " is not a known tag, or the name of a known tag.")
        if stemmerTag1 is not None:
            if hasattr(stemmerTag1, '__call__'):
                stemCheck = True
            else:
                raise TypeError("stemmerTag1 must be callable, e.g. a function or class with a __call__ method.")
        else:
            stemmerTag1 = lambda x: x
        if stemmerTag2 is not None:
            if hasattr(stemmerTag2, '__call__'):
                stemCheck = True
            else:
                raise TypeError("stemmerTag2 must be callable, e.g. a function or class with a __call__ method.")
        else:
            stemmerTag2 = lambda x: x
        count = 0
        progArgs = (0, "Starting to make a two mode network of " + tag1 + " and " + tag2)
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
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
                    contents1 = [stemmerTag1(str(v)) for v in contents1]
                elif contents1 == None:
                    contents1 = []
                else:
                    contents1 = [stemmerTag1(str(contents1))]
                if isinstance(contents2, list):
                    contents2 = [stemmerTag2(str(v)) for v in contents2]
                elif contents2 == None:
                    contents2 = []
                else:
                    contents2 = [stemmerTag2(str(contents2))]
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

    def nModeNetwork(self, tags, recordType = True, nodeCount = True, edgeWeight = True, stemmer = None):
        """Creates a network of the objects found by all WOS tags in _tags_.

        A **nModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. if `"LA"` were in _tags_ node `"English"` would have the type attribute be `"LA"`.

        For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `"CR"` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

        The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

        # Parameters

        _mode_ : `str`

        > A two character WOS tag or one of the full names for a tag

        _nodeCount_ : `optional [bool]`

        > Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

        _edgeWeight_ : `optional [bool]`

        > Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

        _stemmer_ : `optional [func]`

        > default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, note that all IDs are strings. For example:

        >The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

        # Returns

        `networkx Graph`

        > A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges
        """
        nomalizedTags = []
        for t in tags:
            try:
                nomalizedTags.append(normalizeToTag(t))
            except KeyError:
                raise TypeError(str(t) + " is not a known tag, or the name of a known tag.")
        stemCheck = False
        if stemmer is not None:
            if hasattr(stemmer, '__call__'):
                stemCheck = True
            else:
                raise TypeError("stemmer must be callable, e.g. a function or class with a __call__ method.")
        tags = nomalizedTags
        count = 0
        progArgs = (0, "Starting to make a " + str(len(tags)) + "-mode network of: " + ', '.join(tags))
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            grph = nx.Graph()
            for R in self:
                if PBar:
                    count += 1
                    PBar.updateVal(count / len(self), "Analyzing: " + str(R))
                contents = []
                for t in tags:
                    tmpVal = getattr(R, t, None)
                    if stemCheck:
                        if tmpVal:
                            if isinstance(tmpVal, list):
                                contents.append((t, [stemmer(str(v)) for v in tmpVal]))
                            else:
                                contents.append((t, [stemmer(str(tmpVal))]))
                    else:
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

    def localCiteStats(self, pandasFriendly = False, keyType = "citation"):
        """Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

        # Parameters

        _pandasFriendly_ : `optional [bool]`

        > default `False`, makes the output be a dict with two keys one "Citations" is the citations the other is their occurence counts as "Counts".

        _keyType_ : `optional [str]`

        > default `'citation'`, the type of key to use for the dictionary, the valid strings are `"citation"`, `"journal"`, `"year"` or `"author"`

        # Returns

        `dict[str, int or Citation : int]`

        > A dictionary with keys as given by _keyType_ and integers giving their rates of occurrence in the collection
        """
        count = 0
        recCount = len(self)
        progArgs = (0, "Starting to get the local stats on {}s.".format(keyType))
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            keyTypesLst = ["citation", "journal", "year", "author"]
            citesDict = {}
            if keyType not in keyTypesLst:
                raise TypeError("{} is not a valid key type, only '{}' or '{}' are.".format(keyType, "', '".join(keyTypesLst[:-1], keyTypesLst[-1]) ))
            for R in self:
                rCites = R.CR
                if PBar:
                    count += 1
                    PBar.updateVal(count / recCount, "Analysing: {}".format(R.UT))
                if rCites:
                    for c in rCites:
                        if keyType == keyTypesLst[0]:
                            cVal = c
                        else:
                            cVal = getattr(c, keyType)
                            if cVal is None:
                                continue
                        if cVal in citesDict:
                            citesDict[cVal] += 1
                        else:
                            citesDict[cVal] = 1
            if PBar:
                PBar.finish("Done, {} {} fields analysed".format(len(citesDict), keyType))
        if pandasFriendly:
            citeLst = []
            countLst = []
            for cite, occ in citesDict.items():
                citeLst.append(cite)
                countLst.append(occ)
            return {"Citations" : citeLst, "Counts" : countLst}
        else:
            return citesDict

    def localCitesOf(self, rec):
        """Takes in a Record, WOS string, citation string or Citation and returns a RecordCollection of all records that cite it.
        """
        localCites = []
        if isinstance(rec, Record):
            recCite = rec.createCitation()
        if isinstance(rec, str):
            try:
                recCite = self.getWOS(rec)
            except ValueError:
                try:
                    recCite = Citation(rec)
                except AttributeError:
                    raise ValueError("{} is not a valid WOS string or a valid citation string".format(recCite))
            else:
                if recCite is None:
                    return RecordCollection(inCollection = localCites, name = "Records_citing_{}".format(rec))
                else:
                    recCite = recCite.createCitation()
        elif isinstance(rec, Citation):
            recCite = rec
        else:
            raise ValueError("{} is not a valid input, rec must be a Record, string or Citation object.".format(rec))
        for R in self:
            rCites = R.CR
            if rCites:
                for cite in rCites:
                    if recCite == cite:
                        localCites.append(R)
                        break
        return RecordCollection(inCollection = localCites, name = "Records_citing_'{}'".format(rec))

    def citeFilter(self, keyString = '', field = 'all', reverse = False, caseSensitive = False):
        """
        Filters Records by some string, keyString, in all of their citations.
        Returns all Records with at least one citation possessing keyString in the field given by field.

        keyString give the string to be searched for if it is is blank then all citations with the specified field will be matched

        field give the component of the citation to be looked at, it is one of a few strings. The default is 'all' which will cause the entire original citation to be searched. It can be used to search across fields, e.g. '1970, V2' is a valid keystring
        The other options are:
        `author`, searches the author field
        `year`, searches the year field
        `journal`, searches the journal field
        `V`, searches the volume field
        `P`, searches the page field
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
                            if keyString.upper() in cite.author.upper():
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
                            if int(keyString) == cite.year:
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


def addToNetwork(grph, nds, count, weighted, nodeType, nodeInfo, fullInfo, coreCitesDict, coreValues, headNd = None):
    """Addeds the citations _nds_ to _grph_, according to the rules give by _nodeType_, _fullInfo_, etc.

    _headNd_ is the citation of the Record
    """
    if headNd is not None:
        hID = makeID(headNd, nodeType)
        if hID not in grph:
            grph.add_node(*makeNodeTuple(headNd, hID, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues))
    else:
        hID = None
    idList = []
    for n in nds:
        nID = makeID(n, nodeType)
        if nID not in grph:
            grph.add_node(*makeNodeTuple(n, nID, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues))
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

def makeID(citation, nodeType):
    """Makes the id, of the correct type for the network"""
    if nodeType != "full":
        return getattr(citation, nodeType)
    else:
        return citation.getID()

def makeNodeTuple(citation, idVal, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues):
    """Makes a tuple of idVal and a dict of the selected attributes"""
    d = {}
    if nodeInfo:
        if nodeType == 'full':
            if coreValues:
                if citation in coreCitesDict:
                    R = coreCitesDict[citation]
                    infoVals = []
                    for tag in coreValues:
                        tagVal = getattr(R, tag)
                        if isinstance(tagVal, str):
                            infoVals.append(tagVal.replace(',',''))
                        elif isinstance(tagVal, list):
                            infoVals.append(tagVal[0].replace(',',''))
                        else:
                            pass
                    d['info'] = ', '.join(infoVals)
                    d['inCore'] = True
                else:
                    d['info'] = citation.allButDOI()
                    d['inCore'] = False
            else:
                d['info'] = citation.allButDOI()
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

def filterCites(cites, nodeType, dropAnon, dropNonJournals, keyWords, coreCites):
    filteredCites = []
    for c in cites:
        if nodeType != "full" and not getattr(c, nodeType):
            pass
        elif dropNonJournals and not c.isJournal():
            pass
        elif dropAnon and c.isAnonymous():
            pass
        elif coreCites and c not in coreCites:
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
