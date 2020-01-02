#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os
import os.path
import csv
import re
try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections
import networkx as nx

from .constants import __version__
from .mkRecord import Record, _pandasPrep
from .progressBar import _ProgressBar
from .WOS.tagProcessing.funcDicts import tagToFullDict, fullToTagDict, normalizeToTag
from .citation import Citation
from .fileHandlers import recordHandlers
from .mkExceptions import BadWOSRecord, RCTypeError, BadInputFile, BadRecord, RCValueError, RecordsNotCompatible, UnknownFile

from .mkCollection import CollectionWithIDs

from .scopus.scopusHandlers import scopusHeader

import metaknowledge

class RecordCollection(CollectionWithIDs):
    """A container for a large number of indivual records.

    `RecordCollection` provides ways of creating [Records](./Record.html#metaknowledge.Record) from an isi file, string, list of records or directory containing isi files.

    When being created if there are issues the Record collection will be declared bad, `bad` wil be set to `False`, it will then mostly return `None` or False. The attribute `error` contains the exception that occurred.

    They also possess an attribute `name` also accessed with `__repr__()`, this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred.

    # Customizations

    The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur. The comparison operators `<`, `<=`, `>`, `>=` are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

    # \_\_Init\_\_

    _inCollection_ is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

    # Parameters

    _inCollection_ : `optional [str] or None`

    > the name of the source of WOS records. It can be skipped to produce an empty collection.

    > If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

    > If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

    _name_ : `optional [str]`

    > The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

    _extension_ : `optional [str]`

    > The extension to search for when reading a directory for files. _extension_ is the suffix searched for when a directory is read for files, by default it is empty so all files are read.

    _cached_ : `optional [bool]`

    > Default `False`, if `True` and the _inCollection_ is a directory (a string giving the path to a directory) then the initialized `RecordCollection` will be saved in the directory as a Python pickle with the suffix `'.mkDirCache'`. Then if the `RecordCollection` is initialized a second time it will be recovered from the file, which is much faster than reprising every file in the directory.

    > _metaknowledge_ saves the names of the parsed files as well as their last modification times and will check these when recreating the `RecordCollection`, so modifying existing files or adding new ones will result in the entire directory being reanalyzed and a new cache file being created. The extension given to `__init__()` is taken into account as well and each suffix is given its own cache.

    > **Note** The pickle allows for arbitrary python code execution so only use caches that you trust.
    """

    def __init__(self, inCollection = None, name = '', extension = '', cached = False, quietStart = False):
        progArgs = (0, "Starting to make a RecordCollection")
        if metaknowledge.VERBOSE_MODE and not quietStart:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            bad = False
            errors = {}
            name = name
            recordTypes = set()
            if cached:
                cacheName = None
            if inCollection is None:
                PBar.updateVal(.5, "Empty RecordCollection created")
                if not name:
                    name = "Empty"
                recordsSet = set()
            elif isinstance(inCollection, str):
                inCollection = os.path.realpath(os.path.expanduser(inCollection))
                if os.path.isfile(inCollection):
                    PBar.updateVal(.2, "RecordCollection from a file started")
                    if not inCollection.endswith(extension):
                        raise RCTypeError("extension of input file does not match requested extension")
                    if not name:
                        name = os.path.splitext(os.path.split(inCollection)[1])[0]
                    try:
                        for recordType, processor, detector in recordHandlers:
                            if detector(inCollection):
                                recordTypes.add(recordType)
                                recordsSet, pError = processor(inCollection)
                                if pError is not None:
                                    bad = True
                                    errors[inCollection] = pError
                                break
                    except UnknownFile:
                        raise BadInputFile("'{}' does not match any known file type.\nIts header might be damaged or it could have been modified by another program.".format(inCollection))
                elif os.path.isdir(inCollection):
                    count = 0
                    PBar.updateVal(0, "RecordCollection from files in {}".format(inCollection))
                    if extension and not name:
                        name = "{}-files-from-{}".format(extension, inCollection)
                    elif not name:
                        name = "files-from-{}".format(inCollection)
                    recordsSet = set()
                    flist = []
                    for f in os.listdir(inCollection):
                        fullF = os.path.join(os.path.abspath(inCollection), f)
                        if fullF.endswith(extension) and not fullF.endswith('mkRecordDirCache') and os.path.isfile(fullF):
                            flist.append(fullF)
                    if cached:
                        PBar.updateVal(0, "Trying to load from cache")
                        cacheName = os.path.join(inCollection, '{}.[{}].mkRecordDirCache'.format(os.path.basename(os.path.abspath(inCollection)), extension))
                        if self._loadFromCache(cacheName, flist, name, extension):
                            try:
                                PBar.finish("Done reloading {} Records from cache".format(len(self)))
                            except AttributeError:
                                PBar.finish("Done reloading from the cache {}. Warning an error occured.".format(cacheName))
                            return
                        else:
                            PBar.updateVal(0, 'Cache error, rereading files')
                    for fileName in flist:
                        count += 1
                        PBar.updateVal(count / len(flist), "Reading records from: {}".format(fileName))
                        try:
                            for recordType, processor, detector in recordHandlers:
                                if detector(fileName):
                                    recordTypes.add(recordType)
                                    recs, pError = processor(fileName)
                                    if pError is not None:
                                        bad = True
                                        errors[fileName] = pError
                                    recordsSet |= recs
                                    break
                        except UnknownFile:
                            if extension != '':
                                raise BadInputFile("'{}' does not match any known file type, but has the requested extension '{}'. Its header might be damaged or it could have been modified by another program.".format(fileName, extension))
                            else:
                                pass
                else:
                    raise RCTypeError("'{}' is not a path to a directory or file. Strings cannot be used to initialize RecordCollections".format(inCollection))
            elif isinstance(inCollection, collections.abc.Iterable):
                PBar.updateVal(.5, "RecordCollection from an iterable started")
                for R in inCollection:
                    if not isinstance(R, Record):
                        raise RCTypeError("RecordCollections can only contain Records, '{}' is not a valid part of an input iterable.".format(R))
                recordsSet = set(inCollection)
            else:
                raise RCTypeError("A RecordCollection cannot be created from {}.".format(inCollection))
            CollectionWithIDs.__init__(self, recordsSet, Record, recordTypes, name, bad, errors)
            if cached:
                if cacheName is None:
                    pass
                else:
                    PBar.updateVal(1, "Writing RecordCollection cache to {}".format(cacheName))
                    self._createCache(cacheName, flist, name, extension)
            try:
                PBar.finish("Done making a RecordCollection of {} Records".format(len(self)))
            except AttributeError:
                PBar.finish("Done making a RecordCollection. Warning an error occured.")

    def __bytes__(self):
        encoding = self.peek().encoding()
        try:
            return bytes('\n', encoding = encoding).join((bytes(R) for R in self))
        except BadRecord as e:
            raise e from None

    def __add__(self, other):
        self_name = '' if not hasattr(self, 'name') else self.name
        other_name = '' if not hasattr(other, 'name') else other.name

        new_col = metaknowledge.RecordCollection(name='{} {}'.format(self_name, other_name))
        for rec in self:
            new_col.add(rec)

        for rec in other:
            new_col.add(rec)

        return new_col

    def dropNonJournals(self, ptVal = 'J', dropBad = True, invert = False):
        """Drops the non journal type `Records` from the collection, this is done by checking _ptVal_ against the PT tag

        # Parameters

        _ptVal_ : `optional [str]`

        > Default `'J'`, The value of the PT tag to be kept, default is `'J'` the journal tag, other tags can be substituted.

        _dropBad_ : `optional [bool]`

        > Default `True`, if `True` bad `Records` will be dropped as well those that are not journal entries

        _invert_ : `optional [bool]`

        > Default `False`, Set `True` to drop journals (or the PT tag given by _ptVal_) instead of keeping them. **Note**, it still drops bad Records if _dropBad_ is `True`
        """
        if dropBad:
            self.dropBadEntries()
        if invert:
            self._collection = {r for r in self._collection if r['pubType'] != ptVal.upper()}
        else:
            self._collection = {r for r in self._collection if r['pubType'] == ptVal.upper()}

    def writeFile(self, fname = None):
        """Writes the `RecordCollection` to a file, the written file's format is identical to those download from WOS. The order of `Records` written is random.

        # Parameters

        _fname_ : `optional [str]`

        > Default `None`, if given the output file will written to _fanme_, if `None` the `RecordCollection`'s name's first 200 characters are used with the suffix .isi
        """
        if len(self._collectedTypes) < 2:
            recEncoding = self.peek().encoding()
        else:
            recEncoding = 'utf-8'
        if fname:
            f = open(fname, mode = 'w', encoding = recEncoding)
        else:
            f = open(self.name[:200] + '.txt', mode = 'w', encoding = recEncoding)
        if self._collectedTypes == {'WOSRecord'}:
            f.write("\ufeffFN Thomson Reuters Web of Science\u2122\n")
            f.write("VR 1.0\n")
        elif self._collectedTypes == {'MedlineRecord'}:
            f.write('\n')
        elif self._collectedTypes == {'ScopusRecord'}:
            f.write("\ufeff{}\n".format(','.join(scopusHeader)))
        for R in self._collection:
            R.writeRecord(f)
            f.write('\n')
        if self._collectedTypes == {'WOSRecord'}:
            f.write('EF')
        f.close()

    def writeCSV(self, fname = None, splitByTag = None, onlyTheseTags = None, numAuthors = True, genderCounts = True, longNames = False, firstTags = None, csvDelimiter = ',', csvQuote = '"', listDelimiter = '|'):
        """Writes all the `Records` from the collection into a csv file with each row a record and each column a tag.

        # Parameters

        _fname_ : `optional [str]`

        > Default `None`, the name of the file to write to, if `None` it uses the collections name suffixed by .csv.

        _splitByTag_ : `optional [str]`

        > Default `None`, if a tag is given the output will be divided into different files according to the value of the tag, with only the records associated with that tag. For example if `'authorsFull'` is given then each file will only have the lines for `Records` that author is named in.

        > The file names are the values of the tag followed by a dash then the normale name for the file as given by _fname_, e.g. for the year 2016 the file could be called `'2016-fname.csv'`.

        _onlyTheseTags_ : `optional [iterable]`

        > Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

        > If you want to use all known tags pass [metaknowledge.knownTagsList](./ExtendedRecord.html#metaknowledge.ExtendedRecord.tagProcessingFunc).

        _numAuthors_ : `optional [bool]`

        > Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.

        _longNames_ : `optional [bool]`

        > Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

        _firstTags_ : `optional [iterable]`

        > Default `None`, if `None` the iterable `['UT', 'PT', 'TI', 'AF', 'CR']` is used. The tags given by the iterable are the first ones in the csv in the order given.

        > **Note** if tags are in _firstTags_ but not in _onlyTheseTags_, _onlyTheseTags_ will override _firstTags_

        _csvDelimiter_ : `optional [str]`

        > Default `','`, the delimiter used for the cells of the csv file.

        _csvQuote_ : `optional [str]`

        > Default `'"'`, the quote character used for the csv.

        _listDelimiter_ : `optional [str]`

        > Default `'|'`, the delimiter used between values of the same cell if the tag for that record has multiple outputs.
        """
        if firstTags is None:
            firstTags = ['id', 'title', 'authorsFull', 'citations', 'keywords', 'DOI']
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
                tagsLst = [t for t in R.keys() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFullDict[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        if fname:
            baseFileName = fname
        else:
            baseFileName = "{}.csv".format(self.name[:200])
        if numAuthors:
            csvWriterFields = retrievedFields + ["num-Authors"]
        else:
            csvWriterFields = retrievedFields
        if genderCounts:
            csvWriterFields += ['num-Male', 'num-Female', 'num-Unknown']
        if splitByTag is None:
            f = open(baseFileName, mode = 'w', encoding = 'utf-8', newline = '')
            csvWriter = csv.DictWriter(f, csvWriterFields, delimiter = csvDelimiter, quotechar = csvQuote, quoting=csv.QUOTE_ALL)
            csvWriter.writeheader()
        else:
            filesDict = {}
        for R in self:
            if splitByTag:
                try:
                    splitVal = R[splitByTag]
                except KeyError:
                    continue
                else:
                    if not isinstance(splitVal, list):
                        splitVal = [str(splitVal)]
            recDict = {}
            for t in retrievedFields:
                value = R.get(t)
                if isinstance(value, str):
                    recDict[t] = value
                elif hasattr(value, '__iter__'):
                    recDict[t] = listDelimiter.join([str(v) for v in value])
                elif value is None:
                    recDict[t] = ''
                else:
                    recDict[t] = str(value)
            if numAuthors:
                recDict["num-Authors"] = len(R.get('authorsShort', []))
            if genderCounts:
                recDict['num-Male'], recDict['num-Female'], recDict['num-Unknown'] = R.authGenders(_countsTuple = True)
            if splitByTag:
                for sTag in splitVal:
                    if sTag in filesDict:
                        filesDict[sTag][1].writerow(recDict)
                    else:
                        fname = "{}-{}".format(sTag[:200], baseFileName)
                        f = open(fname, mode = 'w', encoding = 'utf-8', newline = '')
                        csvWriter = csv.DictWriter(f, csvWriterFields, delimiter = csvDelimiter, quotechar = csvQuote, quoting=csv.QUOTE_ALL)
                        csvWriter.writeheader()
                        csvWriter.writerow(recDict)
                        filesDict[sTag] = (f, csvWriter)
            else:
                csvWriter.writerow(recDict)
        if splitByTag:
            for f, c in filesDict.values():
                f.close()
        else:
            f.close()

    def writeBib(self, fname = None, maxStringLength = 1000, wosMode = False, reducedOutput = False, niceIDs = True):
        """Writes a bibTex entry to _fname_ for each `Record` in the collection.

        If the Record is of a journal article (PT J) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

        **Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier only.

        **Note** Record entries that are lists have their values separated with the string `' and '`, as this is the way bibTex understands

        # Parameters

        _fname_ : `optional [str]`

        > Default `None`, The name of the file to be written. If not given one will be derived from the collection and the file will be written to .

        _maxStringLength_ : `optional [int]`

        > Default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

        _WOSMode_ : `optional [bool]`

        > Default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

        _restrictedOutput_ : `optional [bool]`

        > Default `False`, if `True` the tags output will be limited to: `'AF'`, `'BF'`, `'ED'`, `'TI'`, `'SO'`, `'LA'`, `'NR'`, `'TC'`, `'Z9'`, `'PU'`, `'J9'`, `'PY'`, `'PD'`, `'VL'`, `'IS'`, `'SU'`, `'PG'`, `'DI'`, `'D2'`, and `'UT'`

        _niceID_ : `optional [bool]`

        > Default `True`, if `True` the IDs used will be derived from the authors, publishing date and title, if `False` it will be the UT tag
        """
        if fname:
            f = open(fname, mode = 'w', encoding = 'utf-8')
        else:
            f = open(self.name[:200] + '.bib', mode = 'w', encoding = 'utf-8')
        f.write("%This file was generated by the metaknowledge Python package.\n%The contents have been automatically generated and are likely to not work with\n%LaTeX without some human intervention. This file is meant for other automatic\n%systems and not to be used directly for making citations\n")
        #I figure this is worth mentioning, as someone will get annoyed at none of the special characters being escaped and how terrible some of the fields look to humans
        for R in self:
            try:
                f.write('\n\n')
                f.write(R.bibString(maxLength =  maxStringLength, WOSMode = wosMode, restrictedOutput = reducedOutput, niceID = niceIDs))
            except BadWOSRecord:
                pass
            except AttributeError:
                raise RecordsNotCompatible("The Record '{}', with ID '{}' does not support writing to bibtext files.".format(R, R.id))
        f.close()

    def findProbableCopyright(self):
        """Finds the (likely) copyright string from all abstracts in the `RecordCollection`

        # Returns

        `list[str]`

        > A deduplicated list of all the copyright strings
        """
        retCopyrights = set()
        for R in self:
            begin, abS = findCopyright(R.get('abstract', ''))
            if abS != '':
                retCopyrights.add(abS)
        return list(retCopyrights)

    def forBurst(self, tag, outputFile = None, dropList = None, lower = True, removeNumbers = True, removeNonWords = True, removeWhitespace = True, stemmer = None):
        """Creates a pandas friendly dictionary with 2 columns one `'year'` and the other `'word'`. Each row is a word that occurred in the field given by _tag_ in a `Record` and the year of the record. Unfortunately getting the month or day with any type of accuracy has proved to be impossible so year is the only option.

        # Parameters

        _tag_ : `str`

        > The tag giving the field for the words to be extracted from.

        _outputFile_ : `optional str`

        > Default `None`, if a path is given a csv file will be created from the returned dictionary and written to that file

        _dropList_ : `optional list[str]`

        > Default `None`, if a list of strings is given each field will be checked for substrings, before any other processing, in the field, surrounded by spaces, matching those in _dropList_. The strings will only be dropped if they are surrounded on both sides with spaces (`' '`) so if `dropList = ['a']` then `'a cat'` will become `'cat'`.

        _lower_ : `optional bool`

        > default `True`, if `True` the output will made lower case

        _removeNumbers_ : `optional bool`

        > default `True`, if `True` all numbers will be removed

        _removeNonWords_ : `optional bool`

        > default `True`, if `True` all non-number non-number characters will be removed

        _removeWhitespace_ : `optional bool`

        > default `True`, if `True` all whitespace will be converted to a single space (`' '`)

        _stemmer_ : `optional func`

        > default `None`, if a function is provided it will be run on each individual word in the field and the output will replace it. For example to use the  `PorterStemmer` in the _nltk_ package you would give `nltk.PorterStemmer().stem`
        """

        whiteSpaceRegex = re.compile(r'\s+')

        if removeNumbers:
            if removeNonWords:
                otherString = r"[\W\d]"
            else:
                otherString = r"\d"
        elif removeNonWords:
            otherString = r"\W"
        else:
            otherString = ''

        def otherRepl(r):
            if r.group(0) == ' ':
                return ' '
            else:
                return ''
        otherDropsRegex = re.compile(otherString)

        def burstPreper(inString):
            if dropList is not None:
                inString = " {} ".format(inString)
                for dropS in (" {} ".format(s) for s in dropList):
                    if dropS in inString:
                        inString = inString.replace(dropS, ' ')
                inString = inString[1:-1]
            if removeWhitespace:
                inString = re.sub(whiteSpaceRegex, lambda x: ' ', inString, count = 0)
            if lower:
                inString = inString.lower()
            inString = re.sub(otherDropsRegex, otherRepl, inString, count = 0)
            sTokens = inString.split(' ')
            if stemmer is not None:
                retTokens = []
                for token in sTokens:
                    if stemmer is not None:
                        token = stemmer(token)
                    retTokens.append(token)
            else:
                retTokens = sTokens
            return retTokens

        retDict = {'year' : [], 'word' : []}

        pcount = 0
        pmax = len(self)
        progArgs = (0, "Starting to work on DataFrame for burst analysis")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            for R in self:
                pcount += 1
                PBar.updateVal(pcount/ pmax, "Analyzing: {}".format(R))
                try:
                    year = R['year']
                except KeyError:
                    continue
                try:
                    burstVal = R[tag]
                except KeyError:
                    continue
                else:
                    if isinstance(burstVal, list):
                        burstVal = ' '.join((str(i) for i in burstVal))
                    else:
                        burstVal = str(burstVal)
                for sToken in burstPreper(burstVal):
                    retDict['year'].append(year)
                    retDict['word'].append(sToken)

            if outputFile is not None:
                PBar.updateVal(.99, "Writing to file: {}".format(outputFile))
                with open(outputFile, 'w', newline = '') as f:
                    writer = csv.DictWriter(f, ['year', 'word'])
                    for row in range(len(retDict['year'])):
                        writer.writerow({k : retDict[k][row] for k in retDict.keys()})
            PBar.finish("Done burst analysis DataFrame with {} rows".format(len(retDict['year'])))
        return retDict

    def forNLP(self, outputFile = None, extraColumns = None, dropList = None, lower = True, removeNumbers = True, removeNonWords = True, removeWhitespace = True, removeCopyright = False, stemmer = None):
        """Creates a pandas friendly dictionary with each row a `Record` in the `RecordCollection` and the columns fields natural language processing uses (id, title, publication year, keywords and the abstract). The abstract is by default is processed to remove non-word, non-space characters and the case is lowered.

        # Parameters

        _outputFile_ : `optional str`

        > default `None`, if a file path is given a csv of the returned data will be written

        _extraColumns_ : `optional list[str]`

        > default `None`, if a list of tags is given each of the tag's values for a `Record` will be added to the output(s)

        _dropList_ : `optional list[str]`

        > default `None`, if a list of strings is provided they will be dropped from the output's abstracts. The matching is case sensitive and done before any other processing. The strings will only be dropped if they are surrounded on both sides with spaces (`' '`) so if `dropList = ['a']` then `'a cat'` will become `'cat'`.

        _lower_ : `optional bool`

        > default `True`, if `True` the abstract will made to lower case

        _removeNumbers_ : `optional bool`

        > default `True`, if `True` all numbers will be removed

        _removeNonWords_ : `optional bool`

        > default `True`, if `True` all non-number non-number characters will be removed

        _removeWhitespace_ : `optional bool`

        > default `True`, if `True` all whitespace will be converted to a single space (`' '`)

        _removeCopyright_ : `optional bool`

        > default `False`, if `True` the copyright statement at the end of the abstract will be removed and added to a new column. Note this is heuristic based and will not work for all papers.

        _stemmer_ : `optional func`

        > default `None`, if a function is provided it will be run on each individual word in the abstract and the output will replace it. For example to use the  `PorterStemmer` in the _nltk_ package you would give `nltk.PorterStemmer().stem`
        """
        whiteSpaceRegex = re.compile(r'\s+')

        if removeNumbers:
            if removeNonWords:
                otherString = r"[\W\d]"
            else:
                otherString = r"\d"
        elif removeNonWords:
            otherString = r"\W"
        else:
            otherString = ''

        def otherRepl(r):
            if r.group(0) == ' ':
                return ' '
            else:
                return ''
        otherDropsRegex = re.compile(otherString)

        def abPrep(abst):
            if dropList is not None:
                #incase a drop string is on the edge
                abst = " {} ".format(abst.replace('\n', ' '))
                for dropS in (" {} ".format(s) for s in dropList):
                    if dropS in abst:
                        abst = abst.replace(dropS, ' ')
                abst = abst[1:-1]
            if removeWhitespace:
                abst = re.sub(whiteSpaceRegex, lambda x: ' ', abst, count = 0)
            if removeCopyright:
                abst, copyrightString = findCopyright(abst)
            else:
                copyrightString = ''
            if lower:
                abst = abst.lower()
            abst = re.sub(otherDropsRegex, otherRepl, abst, count = 0)
            if stemmer is not None:
                sTokens = abst.split(' ')
                retTokens = []
                for token in sTokens:
                    if stemmer is not None:
                        token = stemmer(token)
                    retTokens.append(token)
                abst = ' '.join(retTokens)
            return abst, copyrightString

        pcount = 0
        pmax = len(self)
        progArgs = (0, "Starting to work on DataFrame for NLP")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}

        retDict = {'id' : [], 'year' : [], 'title' : [], 'keywords' : [], 'abstract' : []}
        if removeCopyright:
            retDict['copyright'] = []
        if extraColumns is None:
            extraColumns = []
        else:
            for builtinColumn in ['id', 'year', 'title', 'keywords', 'abstract']:
                if builtinColumn in extraColumns:
                    extraColumns.remove(builtinColumn)
        for column in extraColumns:
            retDict[column] = []
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            for R in self:
                pcount += 1
                PBar.updateVal(pcount/ pmax, "Analyzing: {}".format(R))
                abstract, copyrightString = abPrep(R.get('AB', ''))

                retDict['id'].append(R.id)
                retDict['year'].append(R.get('year', ''))
                retDict['title'].append(R.get('title', ''))
                retDict['keywords'].append('|'.join(R.get('keywords', [])))
                retDict['abstract'].append(abstract)
                if removeCopyright:
                    retDict['copyright'].append(copyrightString)
                for extraTag in extraColumns:
                    e = R.get(extraTag)
                    if isinstance(e, list):
                        e = '|'.join((str(s) for s in e))
                    elif e is None:
                        e = ''
                    retDict[extraTag].append(e)

            if outputFile is not None:
                PBar.updateVal(.99, "Writing to file: {}".format(outputFile))
                with open(outputFile, 'w', newline = '') as f:
                    fieldNames = list(retDict.keys())
                    fieldNames.remove('id')
                    fieldNames.remove('title')
                    fieldNames.remove('year')
                    fieldNames.remove('keywords')
                    fieldNames = ['id', 'year', 'title', 'keywords'] + fieldNames
                    writer = csv.DictWriter(f, fieldNames)
                    writer.writeheader()
                    for row in range(len(retDict['id'])):
                        writer.writerow({k : retDict[k][row] for k in retDict.keys()})
            PBar.finish("Done NLP DataFrame with {} rows".format(len(retDict['id'])))
        return retDict

    def makeDict(self, onlyTheseTags = None, longNames = False, raw = False, numAuthors = True, genderCounts = True):
        """Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

        When used with pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

        # Parameters

        _onlyTheseTags_ : `optional [iterable]`

        > Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

        > If you want to use all known tags pass [metaknowledge.knownTagsList](./ExtendedRecord.html#metaknowledge.ExtendedRecord.tagProcessingFunc).

        _longNames_ : `optional [bool]`

        > Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

        _cleanedVal_ : `optional [bool]`

        > Default `True`, if `True` the processed values for each `Record`'s field will be provided, otherwise the raw values are given.

        _numAuthors_ : `optional [bool]`

        > Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.
        """
        if onlyTheseTags:
            for i in range(len(onlyTheseTags)):
                if onlyTheseTags[i] in fullToTagDict:
                    onlyTheseTags[i] = fullToTagDict[onlyTheseTags[i]]
            retrievedFields = onlyTheseTags
        else:
            retrievedFields = []
            for R in self:
                tagsLst = [t for t in R.keys() if t not in retrievedFields]
                retrievedFields += tagsLst
        if longNames:
            try:
                retrievedFields = [tagToFullDict[t] for t in retrievedFields]
            except KeyError:
                raise KeyError("One of the tags could not be converted to a long name.")
        retDict = {k : [] for k in retrievedFields}
        if numAuthors:
            retDict["num-Authors"] = []
        if genderCounts:
            retDict.update({'num-Male' : [], 'num-Female' : [], 'num-Unknown' : []})
        for R in self:
            if numAuthors:
                retDict["num-Authors"].append(len(R.get('authorsShort', [])))
            if genderCounts:
                m, f, u = R.authGenders(_countsTuple = True)
                retDict['num-Male'].append(m)
                retDict['num-Female'].append(f)
                retDict['num-Unknown'].append(u)
            for k, v in R.subDict(retrievedFields, raw = raw).items():
                retDict[k].append(v)
        return retDict

    def rpys(self, minYear = None, maxYear = None, dropYears = None, rankEmptyYears = False):
        """This implements _Referenced Publication Years Spectroscopy_ a techinique for finding import years in citation data. The authors of the original papers have a website with more information, found [here](http://www.leydesdorff.net/software/rpys/).

        This function computes the spectra of the `RecordCollection` and returns a dictionary mapping strings to lists of `ints`. Each list is ordered and the values of each with the same index form a row and each list a column. The strings are the names of the columns. This is intended to be read directly by pandas `DataFrames`.

        The columns returned are:

        1. `'year'`, the years of the counted citations, missing years are inserted with a count of 0, unless they are outside the bounds of the highest year or the lowest year and the default value is used. e.g. if the highest year is 2016, 2017 will not be inserted unless _maxYear_ has been set to 2017 or higher
        2. `'count'`, the number of times the year was cited
        3. `'abs-deviation'`, deviation from the 5-year median. Calculated by taking the absolute deviation of the count from the median of it and the next 2 years and the preceding 2 years
        4. `'rank'`, the rank of the year, the highest ranked year being the one with the highest deviation, the second highest being the second highest deviation and so on. All years with 0 count are given the rank 0 by default

        # Parameters

        _minYear_ : `optional int`

        > Default `1000`, The lowest year to be returned, note years outside this bound will be used to calculate the deviation from the 5-year median

        _maxYear_ : `optional int`

        > Default `2100`, The highest year to be returned, note years outside this bound will be used to calculate the deviation from the 5-year median

        _dropYears_ : `optional int or list[int]`

        > Default `None`, year or collection of years that will be removed from the returned value, note the dropped years will still be used to calculate the deviation from the 5-year

        _rankEmptyYears_ : `optional [bool]`

        > Default `False`, if `True` years with 0 count will be ranked according to their deviance, if many 0 count years exist their ordering is not guaranteed to be stable

        # Returns

        `dict[str:list]`

        > The table of values from the _Referenced Publication Years Spectroscopy_
        """

        def deviation(targetYear, targetValue, targetDict):
            yearCounts = [targetValue]
            for deltaY in [-2, -1, 1, 2]:
                try:
                    yearCounts.append(targetDict[targetYear + deltaY])
                except KeyError:
                    yearCounts.append(0)
            medianCount = list(sorted(yearCounts))[2]
            absDiff = targetValue - medianCount
            return absDiff

        if dropYears is None:
            dropYears = set()
        yearCounts = {}
        retDict = {'year' : [], 'count' : [], 'abs-deviation' : [], 'rank' : []}

        for R in self:
            try:
                cites = R['citations']
            except KeyError:
                continue
            recYear = R.get('year', float('inf'))
            for cite in cites:
                try:
                    #year can be None
                    cYear = int(cite.year)
                except (AttributeError, TypeError):
                    continue
                else:
                    #need the extra years for the normlization
                    if (maxYear is not None and cYear > (maxYear + 2)) or (minYear is not None and cYear < (minYear - 2)):
                        continue
                    #years from before the paper are an error
                    elif recYear < (cYear + 2):
                        continue
                if cYear in yearCounts:
                    yearCounts[cYear] += 1
                else:
                    yearCounts[cYear] = 1

        if minYear is None:
            smallest = min(yearCounts.keys())
            if smallest > 1000:
                minYear = smallest
        if maxYear is None:
            biggest = max(yearCounts.keys())
            if biggest < 2100:
                maxYear = biggest

        targetYears = set(( i for i in range(minYear, maxYear + 1) if i not in dropYears))

        ranks = {}
        yearDeviances = {}

        for y in targetYears:
            try:
                c = yearCounts[y]
            except KeyError:
                c = 0
            yearDeviances[y] = deviation(y, c, yearCounts)

        for rank, year in enumerate(sorted(yearDeviances.items(), key = lambda x: x[1], reverse = False), start = 1):
            ranks[year[0]] = rank

        for y in targetYears:
            try:
                c = yearCounts[y]
            except KeyError:
                c = 0
            if c == 0 and not rankEmptyYears:
                retDict['rank'].append(0)
            else:
                retDict['rank'].append(ranks[y])
            retDict['abs-deviation'].append(yearDeviances[y])
            retDict['year'].append(y)
            retDict['count'].append(c)

        return retDict

    def genderStats(self, asFractions = False):
        """Creates a dict (`{'Male' : maleCount, 'Female' : femaleCount, 'Unknown' : unknownCount}`) with the numbers of male, female and unknown names in the collection.

        # Parameters

        _asFractions_ : `optional bool`

        > Default `False`, if `True` the counts will be divided by the total number of names, giving the fraction of names in each category instead of the raw counts.

        # Returns

        `dict[str:int]`

        > A dict with three keys `'Male'`, `'Female'` and `'Unknown'` mapping to their respective counts
        """

        maleCount = 0
        femaleCount = 0
        unknownCount = 0
        for R in self:
            m, f, u = R.authGenders(_countsTuple = True)
            maleCount += m
            femaleCount += f
            unknownCount += u
        if asFractions:
            tot = maleCount + femaleCount + unknownCount
            return {'Male' : maleCount / tot, 'Female' : femaleCount / tot, 'Unknown' : unknownCount / tot}
        return {'Male' : maleCount, 'Female' : femaleCount, 'Unknown' : unknownCount}

    def getCitations(self, field = None, values = None, pandasFriendly = True, counts = True):
        """Creates a pandas ready dict with each row a different citation the contained Records and columns containing the original string, year, journal, author's name and the number of times it occured.

        There are also options to filter the output citations with _field_ and _values_

        # Parameters

        _field_ : `optional str`

        > Default `None`, if given all citations missing the named field will be dropped.

        _values_ : `optional str or list[str]`

        > Default `None`, if _field_ is also given only those citations with one of the strings given in _values_ will be included.

        > e.g. to get only citations from 1990 or 1991: `field = year, values = [1991, 1990]`

        _pandasFriendly_ : `optional bool`

        > Default `True`, if `False` a list of the citations will be returned instead of the more complicated pandas dict

        _counts_ : `optional bool`

        > Default `True`, if `False` the counts columns will be removed

        # Returns

        `dict`

        > A pandas ready dict with all the Citations
        """
        retCites = []
        if values is not None:
            if isinstance(values, (str, int, float)) or not isinstance(values, collections.abc.Container):
                values = [values]
        for R in self:
            retCites += R.getCitations(field = field, values = values, pandasFriendly = False)
        if pandasFriendly:
            return _pandasPrep(retCites, counts)
        else:
            return list(set(retCites))

    def networkCoAuthor(self, detailedInfo = False, weighted = True, dropNonJournals = False, count = True, useShortNames = False, citeProfile = False):
        """Creates a coauthorship network for the RecordCollection.

        # Parameters

        _detailedInfo_ : `optional [bool or iterable[WOS tag Strings]]`

        > Default `False`, if `True` all nodes will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedInfo_ is an iterable (that evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attributes.

        > For each of the selected tags an attribute will be added to the node using the values of those tags on the first `Record` encountered. **Warning** iterating over `RecordCollection` objects is not deterministic the first `Record` will not always be same between runs. The node will be given attributes with the names of the WOS tags for each of the selected tags. The attributes will contain strings of containing the values (with commas removed), if multiple values are encountered they will be comma separated.

        > Note: _detailedInfo_ is not identical to the _detailedCore_ argument of [Recordcollection.networkCoCitation()](#metaknowledge.RecordCollection.networkCoCitation) or [Recordcollection.networkCitation()](#metaknowledge.RecordCollection.networkCitation)

        _weighted_ : `optional [bool]`

        > Default `True`, whether the edges are weighted. If `True` the edges are weighted by the number of co-authorships.

        _dropNonJournals_ : `optional [bool]`

        > Default `False`, whether to drop authors from non-journals

        _count_ : `optional [bool]`

        > Default `True`, causes the number of occurrences of a node to be counted

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
                infoVals = ['year', 'title', 'journal', 'volume', 'beginningPage']
            def attributeMaker(Rec):
                attribsDict = {}
                for val in infoVals:
                    recVal = Rec.get(val)
                    if isinstance(recVal, list):
                        attribsDict[val] = ', '.join((str(v).replace(',', '') for v in recVal))
                    else:
                        attribsDict[val] = str(recVal).replace(',', '')
                if count:
                    attribsDict['count'] = 1
                if citeProfile:
                    attribsDict['citeProfile'] = {}
                return attribsDict
        else:
            if count:
                if citeProfile:
                    attributeMaker = lambda x: {'count' : 1, 'citeProfile' : {}}
                else:
                    attributeMaker = lambda x: {'count' : 1}
            else:
                if citeProfile:
                    attributeMaker = lambda x: {'citeProfile' : {}}
                else:
                    attributeMaker = lambda x: {}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            for R in self:
                if PBar:
                    pcount += 1
                    PBar.updateVal(pcount/ len(self), "Analyzing: " + str(R))
                if dropNonJournals and not R.createCitation().isJournal():
                    continue
                if useShortNames:
                    authsList = R.get('authorsShort', [])
                else:
                    authsList = R.get('authorsFull', [])
                if authsList:
                    authsList = list(authsList)
                    detailedInfo = attributeMaker(R)
                    if citeProfile:
                        citesLst = R.get('citations', [])
                    for i, auth1 in enumerate(authsList):
                        if auth1 not in grph:
                            grph.add_node(auth1, **detailedInfo.copy())
                        elif count:
                            grph.nodes[auth1]['count'] += 1
                        if citeProfile:
                            for c in citesLst:
                                try:
                                    grph.nodes[auth1]['citeProfile'][c] += 1
                                except KeyError:
                                    grph.nodes[auth1]['citeProfile'][c] = 1
                        for auth2 in authsList[i + 1:]:
                            if auth2 not in grph:
                                grph.add_node(auth2, **detailedInfo.copy())
                            elif count:
                                grph.nodes[auth2]['count'] += 1
                            if citeProfile:
                                for c in citesLst:
                                    try:
                                        grph.nodes[auth2]['citeProfile'][c] += 1
                                    except KeyError:
                                        grph.nodes[auth2]['citeProfile'][c] = 1
                            if grph.has_edge(auth1, auth2) and weighted:
                                grph.edges[auth1, auth2]['weight'] += 1
                            elif weighted:
                                grph.add_edge(auth1, auth2, weight = 1)
                            else:
                                grph.add_edge(auth1, auth2)
            if citeProfile:
                if PBar:
                    PBar.updateVal(.99, "Extracting citation profiles")
                previous = {}
                for n, dat in grph.nodes(data = True):
                    previous[n] = dat
                    #zip(*l) undoes zip(l1, l2)
                    try:
                        cites, counts = zip(*dat['citeProfile'].items())
                    except ValueError:
                        cites, counts = [], []
                    dat['citeProfileCites'] = '|'.join((str(c) for c in cites))
                    dat['citeProfileCounts'] = '|'.join((str(c) for c in counts))
                    del dat['citeProfile']
            if PBar:
                PBar.finish("Done making a co-authorship network from {}".format(self))
        return grph

    def networkCoCitation(self, dropAnon = True, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, keyWords = None, detailedCore = True, detailedCoreAttributes = False, coreOnly = False, expandedCore = False, addCR = False):
        """Creates a co-citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [metaknowledge.Citation](./Citation.html#metaknowledge.citation.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

        > default `True`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

        > The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

        > Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [Recordcollection.networkCoAuthor()](#metaknowledge.RecordCollection.networkCoAuthor)

        _coreOnly_ : `optional [bool]`

        > default `False`, if `True` only Citations from the RecordCollection will be included in the network

        _expandedCore_ : `optional [bool]`

        > default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

        # Returns

        `Networkx Graph`

        > A networkx graph with hashes as ID and co-citation as edges
        """
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise RCValueError("{} is not an allowed nodeType.".format(nodeType))
        coreValues = []
        if bool(detailedCore):
            try:
                for tag in detailedCore:
                    coreValues.append(normalizeToTag(tag))
            except TypeError:
                coreValues = ['id', 'authorsFull', 'year', 'title', 'journal', 'volume', 'beginningPage']
        tmpgrph = nx.Graph()
        pcount = 0
        progArgs = (0, "Starting to make a co-citation network")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            if coreOnly or coreValues or expandedCore:
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
                    PBar.updateVal(pcount / len(self), "Analyzing: {}".format(R))
                Cites = R.get('citations')
                if Cites:
                    filteredCites = filterCites(Cites, nodeType, dropAnon, dropNonJournals, keyWords, coreCites)
                    addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo , fullInfo, coreCitesDict, coreValues, detailedCoreAttributes, addCR, headNd = None)
            if expandedCore:
                if PBar:
                    PBar.updateVal(.98, "Expanding core Records")
                expandRecs(tmpgrph, self, nodeType, weighted)
            if PBar:
                PBar.finish("Done making a co-citation network from {}".format(self))
        return tmpgrph

    def networkCitation(self, dropAnon = False, nodeType = "full", nodeInfo = True, fullInfo = False, weighted = True, dropNonJournals = False, count = True, directed = True, keyWords = None, detailedCore = True, detailedCoreAttributes = False, coreOnly = False, expandedCore = False, recordToCite = True, addCR = False, _quiet = False):
        """Creates a citation network for the RecordCollection.

        # Parameters

        _nodeType_ : `optional [str]`

        > One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [metaknowledge.Citation](./Citation.html#metaknowledge.citation.Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

        _dropAnon_ : `optional [bool]`

        > default `True`, if `True` citations labeled anonymous are removed from the network

        _nodeInfo_ : `optional [bool]`

        > default `True`, whether an extra piece of information is stored with each node.

        _fullInfo_ : `optional [bool]`

        > default `False`, whether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

        _weighted_ : `optional [bool]`

        > default `True`, whether the edges are weighted. If `True` the edges are weighted by the number of citations.

        _dropNonJournals_ : `optional [bool]`

        > default `False`, whether to drop citations of non-journals

        _count_ : `optional [bool]`

        > default `True`, causes the number of occurrences of a node to be counted

        _keyWords_ : `optional [str] or [list[str]]`

        > A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

        _directed_ : `optional [bool]`

        > Determines if the output graph is directed, default `True`

        _detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

        > default `True`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

        > If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

        > The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

        > Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [Recordcollection.networkCoAuthor()](#metaknowledge.RecordCollection.networkCoAuthor)

        _coreOnly_ : `optional [bool]`

        > default `False`, if `True` only Citations from the RecordCollection will be included in the network

        _expandedCore_ : `optional [bool]`

        > default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

        # Returns

        `Networkx DiGraph or Networkx Graph`

        > See _directed_ for explanation of returned type

        > A networkx digraph with hashes as ID and citations as edges
        """
        allowedTypes = ["full", "original", "author", "journal", "year"]
        if nodeType not in allowedTypes:
            raise RCValueError("{} is not an allowed nodeType.".format(nodeType))
        coreValues = []
        if bool(detailedCore):
            try:
                for tag in detailedCore:
                    coreValues.append(normalizeToTag(tag))
            except TypeError:
                coreValues = ['id', 'authorsFull', 'year', 'title', 'journal', 'volume', 'beginningPage']
        if directed:
            tmpgrph = nx.DiGraph()
        else:
            tmpgrph = nx.Graph()
        pcount = 0
        progArgs = (0, "Starting to make a citation network")
        if metaknowledge.VERBOSE_MODE and not _quiet:
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
                rCites = R.get('citations')
                if rCites:
                    filteredCites = filterCites(rCites, nodeType, dropAnon, dropNonJournals, keyWords, coreCites)
                    addToNetwork(tmpgrph, filteredCites, count, weighted, nodeType, nodeInfo, fullInfo, coreCitesDict, coreValues, detailedCoreAttributes, addCR, recordToCite, headNd = reRef)
            if expandedCore:
                if PBar:
                    PBar.updateVal(.98, "Expanding core Records")
                expandRecs(tmpgrph, self, nodeType, weighted)
            PBar.finish("Done making a citation network from {}".format(self))
        return tmpgrph

    def networkBibCoupling(self, weighted = True, fullInfo = False, addCR = False):
        """Creates a bibliographic coupling network based on citations for the RecordCollection.

        # Parameters

        _weighted_ : `optional bool`

        > Default `True`, if `True` the weight of the edges will be added to the network

        _fullInfo_ : `optional bool`

        > Default `False`, if `True` the full citation string will be added to each of the nodes of the network.

        # Returns

        `Networkx Graph`

        > A graph of the bibliographic coupling
        """
        progArgs = (0, "Make a citation network for coupling")
        if metaknowledge.VERBOSE_MODE:
            progKwargs = {'dummy' : False}
        else:
            progKwargs = {'dummy' : True}
        with _ProgressBar(*progArgs, **progKwargs) as PBar:
            citeGrph = self.networkCitation(weighted = False, directed = True, detailedCore = True, fullInfo = fullInfo, count = False, nodeInfo = True, addCR = addCR, _quiet = True)
            pcount = 0
            pmax = len(citeGrph)
            PBar.updateVal(.2, "Starting to classify nodes")
            workingGrph = nx.Graph()
            couplingSet = set()
            for n, d in citeGrph.nodes(data = True):
                pcount += 1
                PBar.updateVal(.2 + .4 * (pcount / pmax), "Classifying: {}".format(n))
                if d['inCore']:
                    workingGrph.add_node(n, **d)
                if citeGrph.in_degree(n) > 0:
                    couplingSet.add(n)
            pcount = 0
            pmax = len(couplingSet)
            for n in couplingSet:
                PBar.updateVal(.6 + .4 * (pcount / pmax), "Coupling: {}".format(n))
                citesLst = list(citeGrph.in_edges(n))
                for i, edgeOuter in enumerate(citesLst):
                    outerNode = edgeOuter[0]
                    for edgeInner in citesLst[i + 1:]:
                        innerNode = edgeInner[0]
                        if weighted and  workingGrph.has_edge(outerNode, innerNode):
                            workingGrph.edges[outerNode, innerNode]['weight'] += 1
                        elif weighted:
                            workingGrph.add_edge(outerNode, innerNode, weight = 1)
                        else:
                            workingGrph.add_edge(outerNode, innerNode)
            PBar.finish("Done making a bib-coupling network from {}".format(self))
        return workingGrph

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
        return RecordCollection(recordsWithTags, repr(self) + "_tags(" + ','.join(taglist) + ')', quietStart = True)

    def yearSplit(self, startYear, endYear, dropMissingYears = True):
        """Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

        # Parameters

        _startYear_ : `int`

        > The smallest year to be included in the returned RecordCollection

        _endYear_ : `int`

        > The largest year to be included in the returned RecordCollection

        _dropMissingYears_ : `optional [bool]`

        > Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

        # Returns

        `RecordCollection`

        > A RecordCollection of Records from _startYear_ to _endYear_
        """
        recordsInRange = set()
        for R in self:
            try:
                if R.get('year') >= startYear and R.get('year') <= endYear:
                    recordsInRange.add(R)
            except TypeError:
                if dropMissingYears:
                    pass
                else:
                    raise
        RCret = RecordCollection(recordsInRange, name = "{}({}-{})".format(self.name, startYear, endYear), quietStart = True)
        RCret._collectedTypes = self._collectedTypes.copy()
        return RCret

    def localCiteStats(self, pandasFriendly = False, keyType = "citation"):
        """Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

        # Parameters

        _pandasFriendly_ : `optional [bool]`

        > default `False`, makes the output be a dict with two keys one `'Citations'` is the citations the other is their occurrence counts as `'Counts'`.

        _keyType_ : `optional [str]`

        > default `'citation'`, the type of key to use for the dictionary, the valid strings are `'citation'`, `'journal'`, `'year'` or `'author'`. IF changed from `'citation'` all citations matching the requested option will be contracted and their counts added together.

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
                raise TypeError("{} is not a valid key type, only '{}' or '{}' are.".format(keyType, "', '".join(keyTypesLst[:-1]), keyTypesLst[-1]))
            for R in self:
                rCites = R.get('citations')
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

        # Parameters

        _rec_ : `Record, str or Citation`

        > The object that is being cited

        # Returns

        `RecordCollection`

        > A `RecordCollection` containing only those `Records` that cite _rec_
        """
        localCites = []
        if isinstance(rec, Record):
            recCite = rec.createCitation()
        if isinstance(rec, str):
            try:
                recCite = self.getID(rec)
            except ValueError:
                try:
                    recCite = Citation(rec)
                except AttributeError:
                    raise ValueError("{} is not a valid WOS string or a valid citation string".format(recCite))
            else:
                if recCite is None:
                    return RecordCollection(inCollection = localCites, name = "Records_citing_{}".format(rec), quietStart = True)
                else:
                    recCite = recCite.createCitation()
        elif isinstance(rec, Citation):
            recCite = rec
        else:
            raise ValueError("{} is not a valid input, rec must be a Record, string or Citation object.".format(rec))
        for R in self:
            rCites = R.get('citations')
            if rCites:
                for cite in rCites:
                    if recCite == cite:
                        localCites.append(R)
                        break
        return RecordCollection(inCollection = localCites, name = "Records_citing_'{}'".format(rec), quietStart = True)

    def citeFilter(self, keyString = '', field = 'all', reverse = False, caseSensitive = False):
        """Filters `Records` by some string, _keyString_, in their citations and returns all `Records` with at least one citation possessing _keyString_ in the field given by _field_.

        # Parameters

        _keyString_ : `optional [str]`

        > Default `''`, gives the string to be searched for, if it is is blank then all citations with the specified field will be matched

        _field_ : `optional [str]`

        > Default `'all'`, gives the component of the citation to be looked at, it can be one of a few strings. The default is `'all'` which will cause the entire original `Citation` to be searched. It can be used to search across fields, e.g. `'1970, V2'` is a valid keystring
        The other options are:

        + `'author'`, searches the author field
        + `'year'`, searches the year field
        + `'journal'`, searches the journal field
        + `'V'`, searches the volume field
        + `'P'`, searches the page field
        + `'misc'`, searches all the remaining uncategorized information
        + `'anonymous'`, searches for anonymous `Citations`, _keyString_ is not ignored
        + `'bad'`, searches for bad citations, keyString is not used

        _reverse_ : `optional [bool]`

        > Default `False`, being set to `True` causes all `Records` not matching the query to be returned

        _caseSensitive_ : `optional [bool]`

        > Default `False`, if `True` causes the search across the original to be case sensitive, **only** the `'all'` option can be case sensitive
        """
        retRecs = []
        keyString = str(keyString)
        for R in self:
            try:
                if field == 'all':
                    for cite in R.get('citations'):
                        if caseSensitive:
                            if keyString in cite.original:
                                retRecs.append(R)
                                break
                        else:
                            if keyString.upper() in cite.original.upper():
                                retRecs.append(R)
                                break
                elif field == 'author':
                    for cite in R.get('citations'):
                        try:
                            if keyString.upper() in cite.author.upper():
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'journal':
                    for cite in R.get('citations'):
                        try:
                            if keyString.upper() in cite.journal:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'year':
                    for cite in R.get('citations'):
                        try:
                            if int(keyString) == cite.year:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'V':
                    for cite in R.get('citations'):
                        try:
                            if keyString.upper() in cite.V:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'P':
                    for cite in R.get('citations'):
                        try:
                            if keyString.upper() in cite.P:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'misc':
                    for cite in R.get('citations'):
                        try:
                            if keyString.upper() in cite.misc:
                                retRecs.append(R)
                                break
                        except AttributeError:
                            pass
                elif field == 'anonymous':
                    for cite in R.get('citations'):
                        if cite.isAnonymous():
                            retRecs.append(R)
                            break
                elif field == 'bad':
                    for cite in R.get('citations'):
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
            return RecordCollection(inCollection = excluded, name = self.name, quietStart = True)
        else:
            return RecordCollection(inCollection = retRecs, name = self.name, quietStart = True)


def addToNetwork(grph, nds, count, weighted, nodeType, nodeInfo, fullInfo, coreCitesDict, coreValues, detailedValues, addCR, recordToCite = True, headNd = None):
    """Addeds the citations _nds_ to _grph_, according to the rules give by _nodeType_, _fullInfo_, etc.

    _headNd_ is the citation of the Record
    """
    if headNd is not None:
        hID = makeID(headNd, nodeType)
        if nodeType == 'full' or nodeType == 'original':
            hYear = getattr(headNd, "year")
        if hID not in grph:
            nodeName, nodeDat = makeNodeTuple(headNd, hID, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues, detailedValues, addCR)
            grph.add_node(nodeName, **nodeDat)
    else:
        hID = None
    idList = []
    yearList = []
    for n in nds:
        nID = makeID(n, nodeType)
        if nodeType == 'full' or nodeType == 'original':
            try:
                nYear = getattr(n, "year")
            except:
                nYear = None
            yearList.append(nYear)

        if nID not in grph:
            nodeName, nodeDat = makeNodeTuple(n, nID, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues, detailedValues, addCR)
            grph.add_node(nodeName, **nodeDat)
        elif count:
            grph.nodes[nID]['count'] += 1
        idList.append(nID)

    addedEdges = []
    if hID:
        for i in range(len(idList)):
            nID = idList[i]
            if nodeType == 'full' or nodeType == 'original':
                nYear = yearList[i]
                try:
                    yearDiff = abs(hYear - nYear)
                except:
                    yearDiff = None

                if weighted:
                    try:
                        if recordToCite:
                            grph[hID][nID]['weight'] += 1
                        else:
                            grph[nID][hID]['weight'] += 1
                    except KeyError:
                        if recordToCite:
                            grph.add_edge(hID, nID, weight=1, yearDiff=yearDiff)
                        else:
                            grph.add_edge(nID, hID, weight=1, yearDiff=yearDiff)
                elif nID not in grph[hID]:
                    addedEdges.append((hID, nID))

            elif weighted:
                try:
                    if recordToCite:
                        grph[hID][nID]['weight'] += 1
                    else:
                        grph[nID][hID]['weight'] += 1
                except KeyError:
                    if recordToCite:
                        grph.add_edge(hID, nID, weight=1)
                    else:
                        grph.add_edge(hID, nID, weight=1)
            elif nID not in grph[hID]:
                addedEdges.append((hID, nID, {yearDiff: yearDiff}))
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
        return citation.ID()


def makeNodeTuple(citation, idVal, nodeInfo, fullInfo, nodeType, count, coreCitesDict, coreValues, detailedValues, addCR):
    """Makes a tuple of idVal and a dict of the selected attributes"""
    d = {}
    if nodeInfo:
        if nodeType == 'full':
            if coreValues:
                if citation in coreCitesDict:
                    R = coreCitesDict[citation]
                    d['MK-ID'] = R.id
                    if not detailedValues:
                        infoVals = []
                        for tag in coreValues:
                            tagVal = R.get(tag)
                            if isinstance(tagVal, str):
                                infoVals.append(tagVal.replace(',',''))
                            elif isinstance(tagVal, list):
                                infoVals.append(tagVal[0].replace(',',''))
                            else:
                                pass
                        d['info'] = ', '.join(infoVals)
                    else:
                        for tag in coreValues:
                            v = R.get(tag, None)
                            if isinstance(v, list):
                                d[tag] = '|'.join(sorted(v))
                            else:
                                d[tag] = v
                    d['inCore'] = True
                    if addCR:
                        d['citations'] = '|'.join((str(c) for c in R.get('citations', [])))
                else:
                    d['MK-ID'] = 'None'
                    d['info'] = citation.allButDOI()
                    d['inCore'] = False
                    if addCR:
                        d['citations'] = ''
            else:
                d['info'] = citation.allButDOI()
        elif nodeType == 'journal':
            if citation.isJournal():
                d['info'] = str(citation.FullJournalName())
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
        if nodeType != "full" and hasattr(c, nodeType) and not getattr(c, nodeType):
            pass
        elif dropNonJournals and not c.isJournal():
            pass
        elif dropAnon and c.isAnonymous():
            pass
        elif coreCites is not None and c not in coreCites:
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


def expandRecs(G, RecCollect, nodeType, weighted):
    """Expand all the citations from _RecCollect_"""
    for Rec in RecCollect:
        fullCiteList = [makeID(c, nodeType) for c in Rec.createCitation(multiCite = True)]
        if len(fullCiteList) > 1:
            for i, citeID1 in enumerate(fullCiteList):
                if citeID1 in G:
                    for citeID2 in fullCiteList[i + 1:]:
                        if citeID2 not in G:
                            G.add_node(citeID2, **G.nodes[citeID1])
                            if weighted:
                                G.add_edge(citeID1, citeID2, weight = 1)
                            else:
                                G.add_edge(citeID1, citeID2)
                        elif weighted:
                            try:
                                G.edges[citeID1, citeID2]['weight'] += 1
                            except KeyError:
                                G.add_edge(citeID1, citeID2, weight = 1)
                        for e1, e2, data in G.edges(citeID1, data = True):
                            G.add_edge(citeID2, e2, **data)


def findCopyright(inS):
    possibleHits = ['. &COPY; ', '. Crown Copyright',' Elsevier Ltd. ', '. Copyright', '. Published by Els', '. (c) ', '. (C) ']
    splitString = False
    for target in possibleHits:
        if target in inS:
            splitString = target
            break
    if not splitString:
        regexHit = re.search(r'([.] [(]?(c|C)[)]? \d\d\d\d )|([.] \d\d\d\d Elsevier)', inS)
        if regexHit:
            splitString = regexHit.group(0)
    if splitString:
        copSplit = inS.split(splitString)
        if '.' == splitString[0]:
            return splitString.join(copSplit[:-1]) + '.', splitString[1:] + copSplit[-1].rstrip()
        else:
            return splitString.join(copSplit[:-1]), splitString + copSplit[-1].rstrip()
    else:
        return inS, ''
