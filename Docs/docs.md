# <a name="isilib"></a> isilib


Doc String
sekljfsdkdfghkgdf
d'dgfkgdfhjkgdfhkjgfbgjdfkhjkgd

## Classes

<a name="isilib.BadCitation"></a>isilib.**BadCitation**():

>Exception thrown by Citation

- - -

<a name="isilib.BadISIRecord"></a>isilib.**BadISIRecord**():

>Exception thrown by the [record parser](#isilib.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:
>
>    * _Missing field on line (line Number):(line)_, which indicates a line was to short where there should have been a tag followed by information
>
>    * _End of file reached before ER_, which indicates the file end before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.
>
>    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag. This is often due to a copy and paste error.
>
>    * _Missing WOS number_, which indicates the record did not have a 'UT' tag. This tag allows comparison between Record objects so if missing most comparisons will fail.
>
>Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.

- - -

<a name="isilib.Citation"></a>isilib.**Citation**(cite):

>A object to hold citation strings and allow for comparison between them.
>It takes in a citation string from the CR tag of a WOS record then attempts to extract the DOI ,author, year, journal, Volume (V) and Page (P) of the citation string, any extra values are put in misc.
>If the citation string does not have 3 comma space separated elements or has 2 or more only numeric elements it is flagged as bad and all of the string is stored in misc

<a name="Citation.getExtra"></a>Citation.**getExtra**():

>Returns any journal, V, P or misc values as a string
> 

<a name="Citation.getID"></a>Citation.**getID**():

>Returns "author, year" if both available "author" if year is not available and "misc" otherwise
>Use for shortening labels

<a name="Citation.isAnonymous"></a>Citation.**isAnonymous**():

>checks if the author is given as "[ANONYMOUS]" and returns True if so

- - -

<a name="isilib.Record"></a>isilib.**Record**(inRecord, taglist=(), sFile='', sLine=0):

>Class for full WOS records
>
>It is meant to be immutable, many of the methods and attributes are evaluated when first called not when the object is created an the results are stored in a private dictionary.
>
>The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [getTag()](#Record.getTag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.
>
>The Record class's hashing and equality testing are based on the WOS number (the tag is 'UT', and is also called the accession number). They are strings starting with "WOS:" and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is bad it likely does not have a WOS number and thus returns false on all equality checks.
>
>When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.
>
>##### Accessing tag values by attributes
>To generally to get the information from a Record its attributes can be used. Calling `R.CR` causes [citations()](#isilib.tagFuncs.citations) from the the [tagFuncs](#isilib.tagFuncs) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case a list of Citation objects is returned. You can also call 'R.citations' to get the same effect as each known field tag, currently there are 61, has a longer name. These names are meant to make accessing tags more readable and th mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](#isilib)) but not in the raw data None is returned instead. Most tags when cleaned return a list of strings or a string, the exact results can be found in the help for tagFuncs of the particular function.
>
>##### Init
>Records are generally create by [Recordcollections](#isilib.RecordCollection) and not as individual objects. If you wish to create one on its own it is possible.
>
>###### Parameters
>
>_inRecord_: files stream, dict, str or itertools.chain
>
>> If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.
>
>> If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](#isilib.recordParser) returns.
>
>> For a str the input is the raw textual data of a single record in the WOS style, ending in 'ER'.
>
>> itertools.chain is treated indentally to a file stream an is used by [RecordCollections](#isilib.RecordCollection)
>
>_sFile_ : optional [str]
>
>> It is the name of the file the raw data was in, by default it is blank. Mostly used to make error messages more informative.
>
>_sLine_ : optional [int]
>
>> It is the line the record starts on in the raw data file. Mostly used to make error messages more informative.

<a name="Record.activeTags"></a>Record.**activeTags**():

>Returns a list of all the tags the original isi record had

<a name="Record.createCitation"></a>Record.**createCitation**():

>Creates a citation string for the Record by reading the relevant tags(year, j9, volume, beginningPage, DOI) and using it to start a Citation object

<a name="Record.getTag"></a>Record.**getTag**(tag):

>returns a list containing the raw data of the record associated with tag.
>Each line of the record is one string in the list.

<a name="Record.getTagsDict"></a>Record.**getTagsDict**(taglst):

>returns a dict of the results of getTag, with the elements of taglist as the keys and the results as the values.

<a name="Record.getTagsList"></a>Record.**getTagsList**(taglst):

>returns a list of the results of getTag for each tag in taglist, it has the same order as the original.

<a name="Record.writeRecord"></a>Record.**writeRecord**(infile):

>writes to infile the original contents of the Record

- - -

<a name="isilib.RecordCollection"></a>isilib.**RecordCollection**(inCollection=None, name='', extension=''):

>A way of containing a large number of Record objects, it provides ways of creating them from an isi file, string, list of records or directory containing isi files. The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur.
>The comparison operators <, <=, >, >= are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records
>
>When being created if there are issues the Record collection will be declared bad (self.bad = True) it will then mostly return nothing or False. The error attribute contains the exception that occurred.
>
>They also possess a name accessed with repr(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred, read __repr__'s doc string for more information
>
>inCollection is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files
>
>name sets the name of the of the record if left blank name will be generated based on the object that created the Recordcollection
>
>extension controls the extension that __init__ looks for when reading a directory, set it to the extension on the isi files you wish to load, if left blank all files will be tried and any that are not isi files will be silently skipped

<a name="RecordCollection.citationNetwork"></a>RecordCollection.**citationNetwork**(dropAnon=True, authorship=False, extraInfo=True, weighted=True):

# Needs to be written

<a name="RecordCollection.citeFilter"></a>RecordCollection.**citeFilter**(keyString='', field='all', reverse=False, caseSensitive=False):

>Filters Records by some string, keyString, in all of their citations.
>Returns all Records with at least one citation possessing keyString in the field given by field.
>
>keyString give the string to be searched for if it is is blank then all citations with the specified field will be matched
>
>field give the component of the citation to be looked at, it is one of a few strings. The default is 'all' which will cause the entire original citation to be searched. It can be used to search across fields, e.g. '1970, V2' is a valid keystring
>The other options are:
>author, searches the author field
>year, searches the year field
>journal, searches the journal field
>V, searches the volume field
>P, searches the page field
>misc, searches all the remaining uncategorized information
>anonymous, searches for anonymous citations, keyString is not used
>bad, searches for bad citations, keyString is not used
>
>reverse being True causes all Records not matching the query to be returned, default is False
>
>caseSensitive if True causes the search across the original to be case sensitive, only the 'all' option can be case sensitive

<a name="RecordCollection.coAuthNetwork"></a>RecordCollection.**coAuthNetwork**():

# Needs to be written

<a name="RecordCollection.coCiteNetwork"></a>RecordCollection.**coCiteNetwork**(dropAnon=True, authorship=False, extraInfo=True, weighted=True):

# Needs to be written

<a name="RecordCollection.dropBadRecords"></a>RecordCollection.**dropBadRecords**():

>Removes all Records with bad attributes == True from the collection

<a name="RecordCollection.extractTagged"></a>RecordCollection.**extractTagged**(taglist):

# Needs to be written

<a name="RecordCollection.getBadRecords"></a>RecordCollection.**getBadRecords**():

>returns RecordCollection containing all the Record which have their bad flag set to True, i.e. all those removed by dropBadRecords()

<a name="RecordCollection.nModeNetwork"></a>RecordCollection.**nModeNetwork**(tags, recordType=True, nodeCount=True, edgeWeight=True):

# Needs to be written

<a name="RecordCollection.oneModeNetwork"></a>RecordCollection.**oneModeNetwork**(mode, nodeCount=True, edgeWeight=True):

# Needs to be written

<a name="RecordCollection.peak"></a>RecordCollection.**peak**():

>Returns a random Record from the recordCollection, the Record is kept in the collection, use pop for faster destructive access

<a name="RecordCollection.pop"></a>RecordCollection.**pop**():

>Returns a random Record from the recordCollection, the Record is deleted from the collection, use peak for nondestructive access

<a name="RecordCollection.twoModeNetwork"></a>RecordCollection.**twoModeNetwork**(tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True):

# Needs to be written

<a name="RecordCollection.writeCSV"></a>RecordCollection.**writeCSV**(fname=None, onlyTheseTags=None, longNames=False, firstTags=['UT', 'PT', 'TI', 'AF', 'CR'], csvDelimiter=',', csvQuote='"', listDelimiter='|'):

>Writes all the Records from the collection into a csv file with each row a record and each column a tag
>
>fname is the name of the file to write to, if none is given it uses the Collections name suffixed by .csv
>
>onlyTheseTags lets you specify which tags to use, if not given then all tags in the records are given.
>If you want to use all known tags the use onlyTheseTags = isilib.knownTagsList
>
>longNames if set to True will convert the tags to their longer names, otherwise the short 2 character ones will be used
>
>firstTags is the column's tags, it is set by default to ['UT', 'PT', 'TI', 'AF', 'CR'] so those will be written first if given by onlyTheseTags.
>Note if tags are in firstTags but not in onlyTheseTags, onlyTheseTags will override onlyTheseTags
>
>csvDelimiter is the delimiter used for the cells of the csv file, default is the comma (,)
>
>csvQuote is  the quote character used for the csv, default is the double quote (")
>
>listDelimiter is the delimiter used between values of the same cell if the tag for that record has multiple outputs, default is the pipe (|)

<a name="RecordCollection.writeFile"></a>RecordCollection.**writeFile**(fname=None):

>Writes the RecordCollection to a file, the written file is identical to those download from WOS. The order of Records written is random.
>
>fname set the name of the file, if blank the RecordCollection's name's first 200 characters are use with the suffix .isi

<a name="RecordCollection.yearSplit"></a>RecordCollection.**yearSplit**(startYear, endYear):

# Needs to be written

## Functions

<a name="isilib.blondel"></a>isilib.**blondel**(G, weightParameter=None, communityParameter='community'):

# Needs to be written

- - -

<a name="isilib.btest"></a>isilib.**btest**(quite=False):

# Needs to be written

- - -

<a name="isilib.drop_edges"></a>isilib.**drop_edges**(grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False):

>Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted
>
>minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input
>
>parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct
>
>ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored

- - -

<a name="isilib.drop_nodesByCount"></a>isilib.**drop_nodesByCount**(grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False):

>Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.
>
>minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input
>
>
>parameterName is key to count field in the node's dictionary, default is count as that is often correct
>
>ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors

- - -

<a name="isilib.drop_nodesByDegree"></a>isilib.**drop_nodesByDegree**(grph, minDegree=-inf, maxDegree=inf, useWeight=False, parameterName='weight', ignoreUnweighted=False):

>Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.
>
>minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input
>
>useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges
>
>parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True
>
>ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True

- - -

<a name="isilib.isiParser"></a>isilib.**isiParser**(isifile):

>isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
>Each it finds is used to initialize a Record then all Record are returned as a list.

- - -

<a name="isilib.modularity"></a>isilib.**modularity**(G, weightParameter=None, communityParameter='community'):

>Gets modularity of network, currently not tuned

- - -

<a name="isilib.plfit"></a>isilib.**plfit**(x, *varargin):

# Needs to be written

- - -

<a name="isilib.plplot"></a>isilib.**plplot**(x, xmin, alpha):

# Needs to be written

- - -

<a name="isilib.read_graph"></a>isilib.**read_graph**(edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'):

>Reads the files given by edgeList and if given nodeList and produces a networkx graph
>This is designed only for the files produced by isilib and is meant to be the reverse of write_graph()
>
>nodeList must be given if any of the attributes of the node are needed
>directed controls if the resultant graph is directional eSource and eDest control the direction
>idKey, eSource and  eDest are the labels for the edge's id, source and destination respectively, they must match headers in the file or a keyError exception will be thrown

- - -

<a name="isilib.recordParser"></a>isilib.**recordParser**(paper):

>recordParser() reads the file paper until it reaches 'ER'.
>For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately

- - -

<a name="isilib.write_edgeList"></a>isilib.**write_edgeList**(grph, name, extraInfo=True, progBar=None):

>writes an edge list of grph with filename name, if extraInfo is true the additional information about the edges, e.g. weight, will be written.
>All edges must have the same tags

- - -

<a name="isilib.write_graph"></a>isilib.**write_graph**(grph, name, edgeInfo=True, typing=True, suffix='csv', overwrite=False):

>Writes both the edge list and the node attribute list of grph.
>The output files start with name, the file type[edgeList, nodeAttributes] then if typing is True the type of graph (directed or undirected) then the suffix, it appears as follows:
>    name_fileType_Graphtype.suffix
>If edgeInfo is true the extra information about the edges will be included in their list, i.e. their weight will be given
>If overwrite is False write_graph will throw an exception if either of the files it is attempting to write exist

- - -

<a name="isilib.write_nodeAttributeFile"></a>isilib.**write_nodeAttributeFile**(grph, name, progBar=None):

>writes a node attribute list of grph with filename name, the first column is the node's ID then all after it are its associated information.
>All nodes must have the same tags.

## <a name="isilib.tagFuncs"></a>isilib.**tagFuncs**:

>Doc String of tagFuncs

- - -

<a name="isilib.tagFuncs.DOI"></a>isilib.tagFuncs.**DOI**(val):

>return the DOI number of the record
>DI tag

- - -

<a name="isilib.tagFuncs.ISBN"></a>isilib.tagFuncs.**ISBN**(val):

>returns a list of ISBNs assocaited with the Record
>BN tag

- - -

<a name="isilib.tagFuncs.ISSN"></a>isilib.tagFuncs.**ISSN**(val):

>returns the ISSN of the Record
>SN tag

- - -

<a name="isilib.tagFuncs.ResearcherIDnumber"></a>isilib.tagFuncs.**ResearcherIDnumber**(val):

>returns a lsit of the research ids of the Record
>RI tag

- - -

<a name="isilib.tagFuncs.abstract"></a>isilib.tagFuncs.**abstract**(val):

>return abstract of the record, with newlines hopefully in the correct places
>AB tag

- - -

<a name="isilib.tagFuncs.articleNumber"></a>isilib.tagFuncs.**articleNumber**(val):

>returns a string giving the article number, not all are integers
>AR tag

- - -

<a name="isilib.tagFuncs.authAddress"></a>isilib.tagFuncs.**authAddress**(val):

>C1 tag

- - -

<a name="isilib.tagFuncs.authKeyWords"></a>isilib.tagFuncs.**authKeyWords**(val):

>returns the keywords assigned by the author of the Record
>DE tag

- - -

<a name="isilib.tagFuncs.authorsFull"></a>isilib.tagFuncs.**authorsFull**(val):

>returns a list of authors full names
>AF tag

- - -

<a name="isilib.tagFuncs.authorsShort"></a>isilib.tagFuncs.**authorsShort**(val):

>returns a list of authors shortened names
>AU tag

- - -

<a name="isilib.tagFuncs.beginningPage"></a>isilib.tagFuncs.**beginningPage**(val):

>returns the first page the record occurs on as a string not an int
>BP tag

- - -

<a name="isilib.tagFuncs.bookAuthor"></a>isilib.tagFuncs.**bookAuthor**(val):

>returns a list of the short names of the authors of a book Record
>BA tag

- - -

<a name="isilib.tagFuncs.bookAuthorFull"></a>isilib.tagFuncs.**bookAuthorFull**(val):

>returns a list of the long names of the authors of a book Record
>BF tag

- - -

<a name="isilib.tagFuncs.bookDOI"></a>isilib.tagFuncs.**bookDOI**(val):

>returns the book DOI of the Record
>D2 tag

- - -

<a name="isilib.tagFuncs.citations"></a>isilib.tagFuncs.**citations**(val):

>returns a list of all the citations in the record
>CR tag

- - -

<a name="isilib.tagFuncs.citedRefsCount"></a>isilib.tagFuncs.**citedRefsCount**(val):

>returns the numer citations, length of CR list
>NR tag

- - -

<a name="isilib.tagFuncs.confDate"></a>isilib.tagFuncs.**confDate**(val):

>returns the date string of the conference associated with the Record
>CY tag

- - -

<a name="isilib.tagFuncs.confHost"></a>isilib.tagFuncs.**confHost**(val):

>returns the host of the conference
>HO tag

- - -

<a name="isilib.tagFuncs.confLocation"></a>isilib.tagFuncs.**confLocation**(val):

>returns the sting giving the confrence's location
>CL tag

- - -

<a name="isilib.tagFuncs.confSponsors"></a>isilib.tagFuncs.**confSponsors**(val):

>returns a list of sponsors for the conference associated with the record
>SP tag

- - -

<a name="isilib.tagFuncs.confTitle"></a>isilib.tagFuncs.**confTitle**(val):

>returns the title of the conference associated with the Record
>CT tag

- - -

<a name="isilib.tagFuncs.docType"></a>isilib.tagFuncs.**docType**(val):

>returns the type of document the Record contains
>DT tag

- - -

<a name="isilib.tagFuncs.documentDeliveryNumber"></a>isilib.tagFuncs.**documentDeliveryNumber**(val):

>returns the document delivery number of the Record
>GA tag

- - -

<a name="isilib.tagFuncs.eISSN"></a>isilib.tagFuncs.**eISSN**(val):

>returns the EISSN of the Record
>EI tag

- - -

<a name="isilib.tagFuncs.editedBy"></a>isilib.tagFuncs.**editedBy**(val):

>returns a list of the editors of the Record
>BE tag

- - -

<a name="isilib.tagFuncs.editors"></a>isilib.tagFuncs.**editors**(val):

>ED

- - -

<a name="isilib.tagFuncs.email"></a>isilib.tagFuncs.**email**(val):

>returns a list of emails given by the authors of the Record
>EM tag

- - -

<a name="isilib.tagFuncs.endingPage"></a>isilib.tagFuncs.**endingPage**(val):

>return the last page the record occurs on as a string not an int
>EP tag

- - -

<a name="isilib.tagFuncs.funding"></a>isilib.tagFuncs.**funding**(val):

>Returns a list of the groups funding the Record
>FU tag

- - -

<a name="isilib.tagFuncs.fundingText"></a>isilib.tagFuncs.**fundingText**(val):

>Returns a string of the funding thank you
>FX tag

- - -

<a name="isilib.tagFuncs.getMonth"></a>isilib.tagFuncs.**getMonth**(s):

>Known formats:
>Month ("%b")
>Month Day ("%b %d")
>Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
>Season ("%s") --- this gets coerced to use the first month of the given season
>Month Day Year ("%b %d %Y")
>Month Year ("%b %Y")

- - -

<a name="isilib.tagFuncs.group"></a>isilib.tagFuncs.**group**(val):

>returns the group associated with the Record
>GP tag

- - -

<a name="isilib.tagFuncs.groupName"></a>isilib.tagFuncs.**groupName**(val):

>returns the name of the group associated with the Record
>CA tag

- - -

<a name="isilib.tagFuncs.isoAbbreviation"></a>isilib.tagFuncs.**isoAbbreviation**(val):

>returns the iso abbreviation of the journal
>JI tag

- - -

<a name="isilib.tagFuncs.issue"></a>isilib.tagFuncs.**issue**(val):

>returns a string giving the issue or range of issues the Record was in
>IS tag

- - -

<a name="isilib.tagFuncs.j9"></a>isilib.tagFuncs.**j9**(val):

>returns the J9 (29-Character Source Abbreviation) of the publication
>J9 tag

- - -

<a name="isilib.tagFuncs.journal"></a>isilib.tagFuncs.**journal**(val):

>returns the full name of the publication
>SO tag

- - -

<a name="isilib.tagFuncs.keyWords"></a>isilib.tagFuncs.**keyWords**(val):

>returns the WOS keywords of the Record
>ID tag

- - -

<a name="isilib.tagFuncs.language"></a>isilib.tagFuncs.**language**(val):

>returns the languages of the Record as a string with languages seperated by ', ', usually there is only one language
>LA tag

- - -

<a name="isilib.tagFuncs.makeReversed"></a>isilib.tagFuncs.**makeReversed**(d):

# Needs to be written

- - -

<a name="isilib.tagFuncs.meetingAbstract"></a>isilib.tagFuncs.**meetingAbstract**(val):

>returns the ID of the meeting abstract prefixed by 'EPA-'
>MA tag

- - -

<a name="isilib.tagFuncs.month"></a>isilib.tagFuncs.**month**(val):

>returns the month the record was published in as an int with January as 1, February 2, ...
>PD tag

- - -

<a name="isilib.tagFuncs.orcID"></a>isilib.tagFuncs.**orcID**(val):

>returns a list of orc IDs of the Record
>OI tag

- - -

<a name="isilib.tagFuncs.pageCount"></a>isilib.tagFuncs.**pageCount**(val):

>returns an interger giving the number of pages of the Record
>PG tag

- - -

<a name="isilib.tagFuncs.partNumber"></a>isilib.tagFuncs.**partNumber**(val):

>return an integer giving the part of the issue the Record is in
>PN tag

- - -

<a name="isilib.tagFuncs.pubMedID"></a>isilib.tagFuncs.**pubMedID**(val):

>returns the pubmed idof the record
>PM tag

- - -

<a name="isilib.tagFuncs.pubType"></a>isilib.tagFuncs.**pubType**(val):

>retunrs the type of publication as a character: conference, book, journal, book in series, or patent
>PT tag

- - -

<a name="isilib.tagFuncs.publisher"></a>isilib.tagFuncs.**publisher**(val):

>returns the publisher of the Record
>PU tag

- - -

<a name="isilib.tagFuncs.publisherAddress"></a>isilib.tagFuncs.**publisherAddress**(val):

>returns the publishers address
>PA tag

- - -

<a name="isilib.tagFuncs.publisherCity"></a>isilib.tagFuncs.**publisherCity**(val):

>Returns the city the publisher is in
>PI tag

- - -

<a name="isilib.tagFuncs.reprintAddress"></a>isilib.tagFuncs.**reprintAddress**(val):

>returns the reprint address string
>RP tag

- - -

<a name="isilib.tagFuncs.seriesSubtitle"></a>isilib.tagFuncs.**seriesSubtitle**(val):

>returns the title of the series the Record is in
>BS tag

- - -

<a name="isilib.tagFuncs.seriesTitle"></a>isilib.tagFuncs.**seriesTitle**(val):

>returns the title of the series the Record is in
>SE tag

- - -

<a name="isilib.tagFuncs.specialIssue"></a>isilib.tagFuncs.**specialIssue**(val):

>returns the special issue value
>SI tag

- - -

<a name="isilib.tagFuncs.subjectCategory"></a>isilib.tagFuncs.**subjectCategory**(val):

>returns a list of the subjects associated with the Record
>SC tag

- - -

<a name="isilib.tagFuncs.subjects"></a>isilib.tagFuncs.**subjects**(val):

>returns a lsit of subjects as assigned by WOS
>WC tag

- - -

<a name="isilib.tagFuncs.supplement"></a>isilib.tagFuncs.**supplement**(val):

>returns the supplemtn number
>SU tag

- - -

<a name="isilib.tagFuncs.title"></a>isilib.tagFuncs.**title**(val):

>returns the title of the record
>TI tag

- - -

<a name="isilib.tagFuncs.totalTimesCited"></a>isilib.tagFuncs.**totalTimesCited**(val):

>returns the total number of citations of the record
>Z9 tag

- - -

<a name="isilib.tagFuncs.volume"></a>isilib.tagFuncs.**volume**(val):

>return the volume the record is in as a string not an int
>VL tag

- - -

<a name="isilib.tagFuncs.wosString"></a>isilib.tagFuncs.**wosString**(val):

>returns the WOS number of the record as a string preceded by "WOS:""
>UT tag

- - -

<a name="isilib.tagFuncs.wosTimesCited"></a>isilib.tagFuncs.**wosTimesCited**(val):

>returns the number of times the Record has been cited byr records in WOS
>TC tag

- - -

<a name="isilib.tagFuncs.year"></a>isilib.tagFuncs.**year**(val):

>returns the year the record was published in as an int
>PY tag

