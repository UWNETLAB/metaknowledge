---
layout: page
title: Full Documentation
author:
- name: Reid McIlroy-Young
  department:
  affiliation: University of Waterloo, Waterloo ON, Canada
  email: rmcilroy@uwaterloo.ca
- name: John McLevey
  affiliation: University of Waterloo, Waterloo ON, Canada
  email: john.mclevey@uwaterloo.ca
shorttitle: metaknowledge
search_omit: true
---
<a name="objlist"></a>The classes and modules of metaknowledge are:

<ul class="post-list">
<li><article><a href="#Citation"><b>Citation</b><span class="excerpt">Citation are special, here is how they are handled</span></a></article></li>
<li><article><a href="#Record"><b>Record</b><span class="excerpt">What RecordCollections are made of</span></a></article></li>
<li><article><a href="#RecordCollection"><b>RecordCollection</b><span class="excerpt">Where all the stuff happens, look here if you want to make things</span></a></article></li>
<li><article><a href="#visual"><b>visual</b><span class="excerpt">A nicer matplotlib graph visualizer and contour plot</span></a></article></li>
<li><article><a href="#journalAbbreviations"><b>journalAbbreviations</b><span class="excerpt">Look here to get your J9 database</span></a></article></li>
<li><article><a href="#tagProcessing"><b>tagProcessing</b><span class="excerpt">All the tags and how they are handled</span></a></article></li>
</ul>
<a name="fulllist"></a>All the functions and methods of metaknowledge are as follows:

<ul class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, sourceType='raw', targetType='raw'</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True, byYear=False</i>)</a></article></li>
<li><article><a href="#read_graph"><b>read_graph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#write_edgeList"><b>write_edgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#write_nodeAttributeFile"><b>write_nodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#drop_edges"><b>drop_edges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#drop_nodesByDegree"><b>drop_nodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True</i>)</a></article></li>
<li><article><a href="#drop_nodesByCount"><b>drop_nodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#mergeGraphs"><b>mergeGraphs</b>(<i>targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True</i>)</a></article></li>
<li><article><a href="#write_graph"><b>write_graph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True</i>)</a></article></li>
<li><article><a href="#recordParser"><b>recordParser</b>(<i>paper</i>)</a></article></li>
<li><article><a href="#isiParser"><b>isiParser</b>(<i>isifile</i>)</a></article></li>
<li><article><a href="#tagToFull"><b>tagToFull</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#normalizeToTag"><b>normalizeToTag</b>(<i>val</i>)</a></article></li>
<li><article><a href="#normalizeToName"><b>normalizeToName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isTagOrName"><b>isTagOrName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isAnonymous"><small>Citation</small>.<b>isAnonymous</b>()</a></article></li>
<li><article><a href="#getID"><small>Citation</small>.<b>getID</b>()</a></article></li>
<li><article><a href="#allButDOI"><small>Citation</small>.<b>allButDOI</b>()</a></article></li>
<li><article><a href="#getExtra"><small>Citation</small>.<b>getExtra</b>()</a></article></li>
<li><article><a href="#isJournal"><small>Citation</small>.<b>isJournal</b>(<i>dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#getFullJournalName"><small>Citation</small>.<b>getFullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><small>Citation</small>.<b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
<li><article><a href="#numAuthors"><small>Record</small>.<b>numAuthors</b>()</a></article></li>
<li><article><a href="#getTag"><small>Record</small>.<b>getTag</b>(<i>tag, clean=False</i>)</a></article></li>
<li><article><a href="#createCitation"><small>Record</small>.<b>createCitation</b>(<i>multiCite=False</i>)</a></article></li>
<li><article><a href="#getTagsList"><small>Record</small>.<b>getTagsList</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#getTagsDict"><small>Record</small>.<b>getTagsDict</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#activeTags"><small>Record</small>.<b>activeTags</b>()</a></article></li>
<li><article><a href="#writeRecord"><small>Record</small>.<b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#bibString"><small>Record</small>.<b>bibString</b>(<i>maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True</i>)</a></article></li>
<li><article><a href="#bibTexType"><small>Record</small>.<b>bibTexType</b>()</a></article></li>
<li><article><a href="#twoModeNetwork"><small>RecordCollection</small>.<b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><small>RecordCollection</small>.<b>nModeNetwork</b>(<i>tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#localCiteStats"><small>RecordCollection</small>.<b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><small>RecordCollection</small>.<b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><small>RecordCollection</small>.<b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
<li><article><a href="#pop"><small>RecordCollection</small>.<b>pop</b>()</a></article></li>
<li><article><a href="#peak"><small>RecordCollection</small>.<b>peak</b>()</a></article></li>
<li><article><a href="#dropWOS"><small>RecordCollection</small>.<b>dropWOS</b>(<i>wosNum</i>)</a></article></li>
<li><article><a href="#addRec"><small>RecordCollection</small>.<b>addRec</b>(<i>Rec</i>)</a></article></li>
<li><article><a href="#getWOS"><small>RecordCollection</small>.<b>getWOS</b>(<i>wosNum, drop=False</i>)</a></article></li>
<li><article><a href="#getBadRecords"><small>RecordCollection</small>.<b>getBadRecords</b>()</a></article></li>
<li><article><a href="#dropBadRecords"><small>RecordCollection</small>.<b>dropBadRecords</b>()</a></article></li>
<li><article><a href="#dropNonJournals"><small>RecordCollection</small>.<b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><small>RecordCollection</small>.<b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><small>RecordCollection</small>.<b>writeCSV</b>(<i>fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#writeBib"><small>RecordCollection</small>.<b>writeBib</b>(<i>fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True</i>)</a></article></li>
<li><article><a href="#makeDict"><small>RecordCollection</small>.<b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><small>RecordCollection</small>.<b>coAuthNetwork</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
<li><article><a href="#coCiteNetwork"><small>RecordCollection</small>.<b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#citationNetwork"><small>RecordCollection</small>.<b>citationNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#yearSplit"><small>RecordCollection</small>.<b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><small>RecordCollection</small>.<b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#graphDensityContourPlot"><small>visual</small>.<b>graphDensityContourPlot</b>(<i>G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'</i>)</a></article></li>
<li><article><a href="#quickVisual"><small>visual</small>.<b>quickVisual</b>(<i>G, showLabel=False</i>)</a></article></li>
<li><article><a href="#getj9dict"><small>journalAbbreviations</small>.<b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><small>journalAbbreviations</small>.<b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#excludeFromDB"><small>journalAbbreviations</small>.<b>excludeFromDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#updatej9DB"><small>journalAbbreviations</small>.<b>updatej9DB</b>(<i>dbname='j9Abbreviations', saveRawHTML=False</i>)</a></article></li>
<li><article><a href="#getMonth"><small>tagProcessing</small>.<b>getMonth</b>(<i>s</i>)</a></article></li>
<li><article><a href="#confHost"><small>tagProcessing</small>.<b>confHost</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherAddress"><small>tagProcessing</small>.<b>publisherAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#endingPage"><small>tagProcessing</small>.<b>endingPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#year"><small>tagProcessing</small>.<b>year</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authKeyWords"><small>tagProcessing</small>.<b>authKeyWords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#reprintAddress"><small>tagProcessing</small>.<b>reprintAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthor"><small>tagProcessing</small>.<b>bookAuthor</b>(<i>val</i>)</a></article></li>
<li><article><a href="#totalTimesCited"><small>tagProcessing</small>.<b>totalTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#partNumber"><small>tagProcessing</small>.<b>partNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#specialIssue"><small>tagProcessing</small>.<b>specialIssue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjects"><small>tagProcessing</small>.<b>subjects</b>(<i>val</i>)</a></article></li>
<li><article><a href="#keyWords"><small>tagProcessing</small>.<b>keyWords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubMedID"><small>tagProcessing</small>.<b>pubMedID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#documentDeliveryNumber"><small>tagProcessing</small>.<b>documentDeliveryNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthorFull"><small>tagProcessing</small>.<b>bookAuthorFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#groupName"><small>tagProcessing</small>.<b>groupName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#title"><small>tagProcessing</small>.<b>title</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editors"><small>tagProcessing</small>.<b>editors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#journal"><small>tagProcessing</small>.<b>journal</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesTitle"><small>tagProcessing</small>.<b>seriesTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesSubtitle"><small>tagProcessing</small>.<b>seriesSubtitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#language"><small>tagProcessing</small>.<b>language</b>(<i>val</i>)</a></article></li>
<li><article><a href="#docType"><small>tagProcessing</small>.<b>docType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsFull"><small>tagProcessing</small>.<b>authorsFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confTitle"><small>tagProcessing</small>.<b>confTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confDate"><small>tagProcessing</small>.<b>confDate</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confSponsors"><small>tagProcessing</small>.<b>confSponsors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosTimesCited"><small>tagProcessing</small>.<b>wosTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authAddress"><small>tagProcessing</small>.<b>authAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confLocation"><small>tagProcessing</small>.<b>confLocation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#j9"><small>tagProcessing</small>.<b>j9</b>(<i>val</i>)</a></article></li>
<li><article><a href="#funding"><small>tagProcessing</small>.<b>funding</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjectCategory"><small>tagProcessing</small>.<b>subjectCategory</b>(<i>val</i>)</a></article></li>
<li><article><a href="#group"><small>tagProcessing</small>.<b>group</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citations"><small>tagProcessing</small>.<b>citations</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherCity"><small>tagProcessing</small>.<b>publisherCity</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISSN"><small>tagProcessing</small>.<b>ISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#articleNumber"><small>tagProcessing</small>.<b>articleNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#issue"><small>tagProcessing</small>.<b>issue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#email"><small>tagProcessing</small>.<b>email</b>(<i>val</i>)</a></article></li>
<li><article><a href="#eISSN"><small>tagProcessing</small>.<b>eISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DOI"><small>tagProcessing</small>.<b>DOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosString"><small>tagProcessing</small>.<b>wosString</b>(<i>val</i>)</a></article></li>
<li><article><a href="#orcID"><small>tagProcessing</small>.<b>orcID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubType"><small>tagProcessing</small>.<b>pubType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editedBy"><small>tagProcessing</small>.<b>editedBy</b>(<i>val</i>)</a></article></li>
<li><article><a href="#meetingAbstract"><small>tagProcessing</small>.<b>meetingAbstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isoAbbreviation"><small>tagProcessing</small>.<b>isoAbbreviation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pageCount"><small>tagProcessing</small>.<b>pageCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisher"><small>tagProcessing</small>.<b>publisher</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><small>tagProcessing</small>.<b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#month"><small>tagProcessing</small>.<b>month</b>(<i>val</i>)</a></article></li>
<li><article><a href="#fundingText"><small>tagProcessing</small>.<b>fundingText</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookDOI"><small>tagProcessing</small>.<b>bookDOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#volume"><small>tagProcessing</small>.<b>volume</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ResearcherIDnumber"><small>tagProcessing</small>.<b>ResearcherIDnumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsShort"><small>tagProcessing</small>.<b>authorsShort</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citedRefsCount"><small>tagProcessing</small>.<b>citedRefsCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#beginningPage"><small>tagProcessing</small>.<b>beginningPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#abstract"><small>tagProcessing</small>.<b>abstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#supplement"><small>tagProcessing</small>.<b>supplement</b>(<i>val</i>)</a></article></li>
</ul>

---
<a name="Overview"></a>
metaknowledge is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

#### Example

To load the data from files and make a network:

    >>> import metaknowledge as mk
    >>> RC = mk.RecordCollection("records/")
    >>> print(RC)
    Collection of 33 records
    >>> G = RC.coCiteNetwork(nodeType = 'journal')
    Done making a co-citation network of files-from-records                 1.1s
    >>> print(len(G.nodes()))
    223
    >>> mk.write_graph(G, "Cocitation-Network-of-Journals")

There is also a simple command line program called `metaknowledge` that comes with the package. It allows for creating networks without any need to know Python. More information about it can be found at [networkslab.org/metaknowledge/cli]({{ site.baseurl }}/cli)

#### Overview

This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, title, and citations. The records are exported in groups of up-to 500 individual records to a file.

The [metaknowledge.RecordCollection](#RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](#Record) class that contains the results of the parsing of the record.

The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge can read them to extract useful information. The approximate meanings of the tags are listed in the [tagProcessing](#tagProcessing) package, along with the parsing functions for each tag. If you simply want the mapping [`tagToFull()`](#tagToFull) is a function that maps tags to their full names it, as well as a few other similar functions are provided by the base metaknowledge import. Note, the long names can be used in place of the short 2 character codes within metaknowledge. There are no full official public listings of tag the meanings available. metaknowledge is not attempting to provide the definitive or authoritative meanings.

Citations are handled by a special [Citation](#Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

Note for those reading the docstrings metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation]({{ site.baseurl }}/documentation/), but you should have no problem reading them from the help function.





---
<a name="Base Functions"></a>
The functions provided by metaknowledge are:

<ul class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, sourceType='raw', targetType='raw'</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True, byYear=False</i>)</a></article></li>
<li><article><a href="#read_graph"><b>read_graph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#write_edgeList"><b>write_edgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#write_nodeAttributeFile"><b>write_nodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#drop_edges"><b>drop_edges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#drop_nodesByDegree"><b>drop_nodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True</i>)</a></article></li>
<li><article><a href="#drop_nodesByCount"><b>drop_nodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#mergeGraphs"><b>mergeGraphs</b>(<i>targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True</i>)</a></article></li>
<li><article><a href="#write_graph"><b>write_graph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True</i>)</a></article></li>
<li><article><a href="#recordParser"><b>recordParser</b>(<i>paper</i>)</a></article></li>
<li><article><a href="#isiParser"><b>isiParser</b>(<i>isifile</i>)</a></article></li>
<li><article><a href="#tagToFull"><b>tagToFull</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#normalizeToTag"><b>normalizeToTag</b>(<i>val</i>)</a></article></li>
<li><article><a href="#normalizeToName"><b>normalizeToName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isTagOrName"><b>isTagOrName</b>(<i>val</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="filterNonJournals"></a><small></small>**[<ins>filterNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#filterNonJournals)**(_citesLst, invert=False_):

Removes the `Citations` from _citesLst_ that are not journals

###### Parameters

_citesLst_ : `list [Citation]`

 A list of citations to be filtered

_invert_ : `optional [bool]`

 Default `False`, if `True` non-journals will be kept instead of journals

###### Returns

`list [Citation]`

 A filtered list of Citations from _citesLst_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionGraph"></a><small></small>**[<ins>diffusionGraph</ins>]({{ site.baseurl }}{{ page.url }}#diffusionGraph)**(_source, target, sourceType='raw', targetType='raw'_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a graph of the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) in _target_. By default the nodes in the are `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords.

Each node on the output graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `str`

 default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes. If it is a WOS tag then the nodes will be of that type.

_targetType_ : `str`

 default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

###### Returns

`networkx Directed Graph`

 A directed graph of the diffusion network


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionCount"></a><small></small>**[<ins>diffusionCount</ins>]({{ site.baseurl }}{{ page.url }}#diffusionCount)**(_source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True, byYear=False_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a `dict` counting the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `optional [str]`

 default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag the keys will be of that type.

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurrence counts as `"Counts"`. The lists are the same length.

_compareCounts_ : `optional [bool]`

 default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

_byYear_ : `optional [bool]`

default `False`, if `True` the returned dictionary will have Records mapped to maps, these maps will map years ('ints') to counts. If _pandasFriendly_ is also `True` the resultant dictionary will have an additional column called `'year'`. This column will contain the year the citations occurred, in addition the Records entries will be duplicated for each year they occur in.

###### Returns

`dict[:int]`

 A dictionary with the type given by _sourceType_ as keys and integers as values.

 If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

 If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labeled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="read_graph"></a><small></small>**[<ins>read_graph</ins>]({{ site.baseurl }}{{ page.url }}#read_graph)**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by _edgeList_ and _nodeList_ and creates a networkx graph for the files.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()]({{ site.baseurl }}{{ page.url }}#write_graph), if this does not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried as it is aimed at a more general usage.

The read edge list format assumes the column named _eSource_ (default `'From'`) is the source node, then the column _eDest_ (default `'To'`) givens the destination and all other columns are attributes of the edges, e.g. weight.

The read node list format assumes the column _idKey_ (default `'ID'`) is the ID of the node for the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

**Note**: If the names of the columns do not match those given to **read_graph()** a `KeyError` exception will be raised.

**Note**: If nodes appear in the edgelist but not the nodeList they will be created silently with no attributes.

###### Parameters

_edgeList_ : `str`

 a string giving the path to the edge list file

_nodeList_ : `optional [str]`

 default `None`, a string giving the path to the node list file

_directed_ : `optional [bool]`

 default `False`, if `True` the produced network is directed from _eSource_ to _eDest_

_idKey_ : `optional [str]`

 default `'ID'`, the name of the ID column in the node list

_eSource_ : `optional [str]`

 default `'From'`, the name of the source column in the edge list

_eDest_ : `optional [str]`

 default `'To'`, the name of the destination column in the edge list

###### Returns

`networkx Graph`

 the graph described by the input files


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_edgeList"></a><small></small>**[<ins>write_edgeList</ins>]({{ site.baseurl }}{{ page.url }}#write_edgeList)**(_grph, name, extraInfo=True, allSameAttribute=False_):

Writes an edge list of _grph_ at the destination _name_.

The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

**Note**: If any edges are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_edgeInfo_ : `optional [bool]`

 Default `True`, if `True` the attributes of each edge will be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the edges must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_nodeAttributeFile"></a><small></small>**[<ins>write_nodeAttributeFile</ins>]({{ site.baseurl }}{{ page.url }}#write_nodeAttributeFile)**(_grph, name, allSameAttribute=False_):

Writes a node attribute list of _grph_ to the file given by the path _name_.

The node list has one column call `'ID'` with the node ids used by networkx and all other columns are the node attributes.

**Note**: If any nodes are missing an attribute it will be left blank by default, enable _allSameAttribute_ to cause a `KeyError` to be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the nodes must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_edges"></a><small></small>**[<ins>drop_edges</ins>]({{ site.baseurl }}{{ page.url }}#drop_edges)**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Modifies _grph_ by dropping edges whose weight is not within the inclusive bounds of _minWeight_ and _maxWeight_, i.e after running _grph_ will only have edges whose weights meet the following inequality: _minWeight_ <= edge's weight <= _maxWeight_. A `Keyerror` will be raised if the graph is unweighted unless _ignoreUnweighted_ is `True`, the weight is determined by examining the attribute _parameterName_.

**Note**: none of the default options will result in _grph_ being modified so only specify the relevant ones, e.g. `drop_edges(G, dropSelfLoops = True)` will remove only the self loops from `G`.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minWeight_ : `optional [int or double]`

 default `-inf`, the minimum weight for an edge to be kept in the graph.

_maxWeight_ : `optional [int or double]`

 default `inf`, the maximum weight for an edge to be kept in the graph.

_parameterName_ : `optional [str]`

 default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct

_ignoreUnweighted_ : `optional [bool]`

 default `False`, if `True` unweighted edges will kept

_dropSelfLoops_ : `optional [bool]`

 default `False`, if `True` self loops will be removed regardless of their weight


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByDegree"></a><small></small>**[<ins>drop_nodesByDegree</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByDegree)**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True_):

Modifies _grph_ by dropping nodes that do not have a degree that is within inclusive bounds of _minDegree_ and _maxDegree_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minDegree_ <= node's degree <= _maxDegree_.

Degree is determined in two ways, the default _useWeight_ is the weight attribute of the edges to a node will be summed, the attribute's name is _parameterName_ otherwise the number of edges touching the node is used. If _includeUnweighted_ is `True` then _useWeight_ will assign a degree of 1 to unweighted edges.


###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minDegree_ : `optional [int or double]`

 default `-inf`, the minimum degree for an node to be kept in the graph.

_maxDegree_ : `optional [int or double]`

 default `inf`, the maximum degree for an node to be kept in the graph.

_useWeight_ : `optional [bool]`

 default `True`, if `True` the the edge weights will be summed to get the degree, if `False` the number of edges will be used to determine the degree.

_parameterName_ : `optional [str]`

 default `'weight'`, key to weight field in the edge's attribute dictionary, the default is the same as networkx and metaknowledge so is likely to be correct.

_includeUnweighted_ : `optional [bool]`

 default `True`, if `True` edges with no weight will be considered to have a weight of 1, if `False` they will cause a `KeyError` to be raised.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByCount"></a><small></small>**[<ins>drop_nodesByCount</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByCount)**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

Modifies _grph_ by dropping nodes that do not have a count that is within inclusive bounds of _minCount_ and _maxCount_, i.e after running _grph_ will only have nodes whose degrees meet the following inequality: _minCount_ <= node's degree <= _maxCount_.

Count is determined by the count attribute, _parameterName_, and if missing will result in a `KeyError` being raised. _ignoreMissing_ can be set to `True` to suppress the error.

minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input

###### Parameters

_grph_ : `networkx Graph`

 The graph to be modified.

_minCount_ : `optional [int or double]`

 default `-inf`, the minimum Count for an node to be kept in the graph.

_maxCount_ : `optional [int or double]`

 default `inf`, the maximum Count for an node to be kept in the graph.

_parameterName_ : `optional [str]`

 default `'count'`, key to count field in the nodes's attribute dictionary, the default is the same thoughout metaknowledge so is likely to be correct.

_ignoreMissing_ : `optional [bool]`

 default `False`, if `True` nodes missing a count will be kept in the graph instead of raising an exception


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="mergeGraphs"></a><small></small>**[<ins>mergeGraphs</ins>]({{ site.baseurl }}{{ page.url }}#mergeGraphs)**(_targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'_):

A quick way of merging graphs, this is meant to be quick and is only intended for graphs generated by metaknowledge. This does not check anything and as such may cause unexpected results if the source and target were not generated by the same method.

**mergeGraphs**() will **modify** _targetGraph_ in place by adding the nodes and edges found in the second, _addedGraph_. If a node or edge exists _targetGraph_ is given precedence, but the edge and node attributes given by _incrementedNodeVal_ and incrementedEdgeVal are added instead of being overwritten.

###### Parameters

_targetGraph_ : `networkx Graph`

 the graph to be modified, it has precedence.

_addedGraph_ : `networkx Graph`

 the graph that is unmodified, it is added and does **not** have precedence.

_incrementedNodeVal_ : `optional [str]`

 default `'count'`, the name of the count attribute for the graph's nodes. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.

_incrementedEdgeVal_ : `optional [str]`

 default `'weight'`, the name of the weight attribute for the graph's edges. When merging this attribute will be the sum of the values in the input graphs, instead of _targetGraph_'s value.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphStats"></a><small></small>**[<ins>graphStats</ins>]({{ site.baseurl }}{{ page.url }}#graphStats)**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

Returns a string or list containing statistics about the graph _G_.

**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

###### Parameters

_G_ : `networkx Graph`

 The graph for the statistics to be determined of

_stats_ : `optional [list or tuple [str]]`

 Default `('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity')`, a list or tuple containing any number or combination of the strings:

 `"nodes"`, `"edges"`, `"isolates"`, `"loops"`, `"density"` and `"transitivity"``

 At least one occurrence of the corresponding string causes the statistics to be provided in the string output. For the non-string (tuple) output the returned tuple has the same length as the input and each output is at the same index as the string that requested it, e.g.

 `_stats_ = ("edges", "loops", "edges")`

 The return is a tuple with 2 elements the first and last of which are the number of edges and the second is the number of loops

_makeString_ : `optional [bool]`

 Default `True`, if `True` a string is returned if `False` a tuple

###### Returns

`str or tuple [float and int]`

 The type is determined by _makeString_ and the layout by _stats_
 


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_graph"></a><small></small>**[<ins>write_graph</ins>]({{ site.baseurl }}{{ page.url }}#write_graph)**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True_):

Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [read_graph()]({{ site.baseurl }}{{ page.url }}#read_graph) and to write only one type of lsit use [write_edgeList()]({{ site.baseurl }}{{ page.url }}#write_edgeList) or [write_nodeAttributeFile()]({{ site.baseurl }}{{ page.url }}#write_nodeAttributeFile).

**Warning**: this function will overwrite files, if they are in the way of the output, to prevent this set _overwrite_ to `False`

**Note**: If any nodes or edges are missing an attribute a `KeyError` will be raised.

###### Parameters

_grph_ : `networkx Graph`

 A networkx graph of the network to be written.

_name_ : `str`

 The start of the file name to be written, can include a path.

_edgeInfo_ : `optional [bool]`

 Default `True`, if `True` the the attributes of each edge are written to the edge list.

_typing_ : `optional [bool]`

 Default `False`, if `True` the directed ness of the graph will be added to the file names.

_suffix_ : `optional [str]`

 Default `"csv"`, the suffix of the file.

_overwrite_ : `optional [bool]`

 Default `True`, if `True` files will be overwritten silently, otherwise an `OSError` exception will be raised.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="recordParser"></a><small></small>**[<ins>recordParser</ins>]({{ site.baseurl }}{{ page.url }}#recordParser)**(_paper_):

This is function that is used to create [`Records`]({{ site.baseurl }}{{ page.url }}#Record) from files.

**recordParser**() reads the file _paper_ until it reaches 'ER'. For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following two lines in a record:

    AF BREVIK, I
       ANICIN, B

The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

`Record` objects can be created with these dictionaries as the initializer.

###### Parameters

_paper_ : `file stream`

 An open file, with the current line at the beginning of the WOS record.

###### Returns

`OrderedDict[str : List[str]]`

 A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isiParser"></a><small></small>**[<ins>isiParser</ins>]({{ site.baseurl }}{{ page.url }}#isiParser)**(_isifile_):

This is function that is used to create [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) from files.

**isiParser**() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [**recordParser**()]({{ site.baseurl }}{{ page.url }}#recordParser) and converted into [`Records`]({{ site.baseurl }}{{ page.url }}#Record). A list of these `Records` is returned.

`BadISIFile` is raised if an issue is found with the file.

###### Parameters

_isifile_ : `str`

 The path to the target file

###### Returns

`List[Record]`

 All the `Records` found in _isifile_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagToFull"></a><small></small>**[<ins>tagToFull</ins>]({{ site.baseurl }}{{ page.url }}#tagToFull)**(_tag_):

A wrapper for [`tagToFullDict`]({{ site.baseurl }}{{ page.url }}#tagProcessing) it maps 2 character tags to their full names.

###### Parameters

_tag_: `str`

 A two character string giving the tag

###### Returns

`str`

 The full name of _tag_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToTag"></a><small></small>**[<ins>normalizeToTag</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToTag)**(_val_):

Converts tags or full names to 2 character tags, case insensitive

###### Parameters

_val_: `str`

 A two character string giving the tag or its full name

###### Returns

`str`

 The short name of _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToName"></a><small></small>**[<ins>normalizeToName</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToName)**(_val_):

Converts tags or full names to full names, case sensitive

###### Parameters

_val_: `str`

 A two character string giving the tag or its full name

###### Returns

`str`

 The full name of _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isTagOrName"></a><small></small>**[<ins>isTagOrName</ins>]({{ site.baseurl }}{{ page.url }}#isTagOrName)**(_val_):

Checks if _val_ is a tag or full name of tag if so returns `True`

###### Parameters

_val_: `str`

 A string possible forming a tag or name

###### Returns

`bool`

 `True` if _val_ is a tag or name, otherwise `False`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="BadCitation"></a><small></small>**[<ins>BadCitation</ins>]({{ site.baseurl }}{{ page.url }}#BadCitation)**(_Warning_):

Exception thrown by Citation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="BadISIRecord"></a><small></small>**[<ins>BadISIRecord</ins>]({{ site.baseurl }}{{ page.url }}#BadISIRecord)**(_Warning_):

Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.



---
<a name="Citation"></a>
<a name="Citation"></a><small></small>**[<ins>Citation</ins>](#Citation)**(_object_):

<a name="Citation.__init__"></a><small></small>**[<ins>Citation.__init__</ins>](#Citation.__init__)**(_cite_):

A class to hold citation strings and allow for comparison between them.

The initializer takes in a string representing a WOS citation in the form:

    Author, Year, Journal, Volume, Page, DOI

`Author` is the author's name in the form of first last name first initial sometimes followed by a period.
`Year` is the year of publication.
`Journal` being the 29-Character Source Abbreviation of the journal.
`Volume` is the volume number(s) of the publication preceded by a V
`Page` is the page number the record starts on
`DOI` is the DOI number of the cited record preceeded by the letters `'DOI'`
Combined they look like:

    Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

**Note**: any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpreted as any of these it is put in the `misc` attribute. That is the reason to use this class, it gracefully handles missing information while still allowing for  comparison between WOS citation strings.

##### Customizations

Citation's hashing and equality checking are based on [`getID()`](#getID) and use the values of `author`, `year` and `journal`.

When converted to a string a Citation will return the original string.

##### Attributes

As noted above, citations are considered to be divided into six distinct fields (`Author`, `Year`, `Journal`, `Volume`, `Page` and `DOI`) with a seventh `misc` for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a `Citation` created from the string: `'Nunez R., 1998, MATH COGNITION'` would have `author`, `year` and `journal` defined. While one from `'Nunez R.'` would have only the attribute `misc`.

If the parsing of a citation string fails the attribute `bad` is set to `True` and the attribute `error` is created to contain said error, which is a [BadCitation](#BadCitation) object. If no errors occur `bad` is `False`.

The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

##### \_\_Init\_\_

Citations can be created by [Records](#Record) or by giving the initializer a string containing a WOS style citation.

##### Parameters

_cite_ : `str`

 A str containing a WOS style citation.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
The Citation class has the following methods:

<ul class="post-list">
<li><article><a href="#isAnonymous"><b>isAnonymous</b>()</a></article></li>
<li><article><a href="#getID"><b>getID</b>()</a></article></li>
<li><article><a href="#allButDOI"><b>allButDOI</b>()</a></article></li>
<li><article><a href="#getExtra"><b>getExtra</b>()</a></article></li>
<li><article><a href="#isJournal"><b>isJournal</b>(<i>dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#getFullJournalName"><b>getFullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isAnonymous"></a><small>Citation.</small>**[<ins>isAnonymous</ins>]({{ site.baseurl }}{{ page.url }}#isAnonymous)**():

Checks if the author is given as `'[ANONYMOUS]'` and returns `True` if so.

###### Returns

`bool`

 `True` if the author is `'[ANONYMOUS]'` otherwise `False`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getID"></a><small>Citation.</small>**[<ins>getID</ins>]({{ site.baseurl }}{{ page.url }}#getID)**():

Returns all of `author`, `year` and `journal` available separated by `' ,'`. It is for shortening labels when creating networks as the resultant strings are often unique. [**getExtra**()]({{ site.baseurl }}{{ page.url }}#getExtra) gets everything not returned by **getID**().

This is also used for hashing and equality checking.

###### Returns

`str`

 A string to use as the ID of a node.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="allButDOI"></a><small>Citation.</small>**[<ins>allButDOI</ins>]({{ site.baseurl }}{{ page.url }}#allButDOI)**():

Returns a string of the normalized values from the Citation excluding the DOI number. Equivalent to getting the ID with [**getID**()]({{ site.baseurl }}{{ page.url }}#getID) then appending the extra values from [**getExtra**()]({{ site.baseurl }}{{ page.url }}#getExtra) and then removing the substring containing the DOI number.

###### Returns

`str`

 A string containing the data of the Citation.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getExtra"></a><small>Citation.</small>**[<ins>getExtra</ins>]({{ site.baseurl }}{{ page.url }}#getExtra)**():

Returns any `V`, `P`, `DOI` or `misc` values as a string. These are all the values not returned by [**getID**()]({{ site.baseurl }}{{ page.url }}#getID), they are separated by `' ,'`.

###### Returns

`str`

 A string containing the data not in the ID of the `Citation`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isJournal"></a><small>Citation.</small>**[<ins>isJournal</ins>]({{ site.baseurl }}{{ page.url }}#isJournal)**(_dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False_):

Returns `True` if the `Citation`'s `journal` field is a journal abbreviation from the WOS listing found at [http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html), i.e. checks if the citation is citing a journal.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

**Note**: All parameters are used for getting the data base with  [**getj9dict**()]({{ site.baseurl }}{{ page.url }}#getj9dict).

###### Parameters

_dbname_ : `optional [str]`

 The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

_manaulDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_returnDict_ : `optional [str]`

 default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.

###### Returns

`bool`

 `True` if the `Citation` is for a journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getFullJournalName"></a><small>Citation.</small>**[<ins>getFullJournalName</ins>]({{ site.baseurl }}{{ page.url }}#getFullJournalName)**():

Returns the full name of the Citation's journal field. Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

###### Returns

`str`

 The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then `None` is returned


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addToDB"></a><small>Citation.</small>**[<ins>addToDB</ins>]({{ site.baseurl }}{{ page.url }}#addToDB)**(_manualName=None, manaulDB='manualj9Abbreviations', invert=False_):

Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()]({{ site.baseurl }}{{ page.url }}#isJournal) to return `True` for this Citation and all others with its `journal`.

**Note**: Requires the [j9Abbreviations]({{ site.baseurl }}{{ page.url }}#getj9dict) database file and will raise an error if it cannot be found.

###### Parameters

_manualName_ : `optional [str]`

 Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

_manaulDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_invert_ : `optional [bool]`

 Default `False`, if `True` the journal will be removed instead of added



---
<a name="Record"></a>
<a name="Record"></a><small></small>**[<ins>Record</ins>](#Record)**(_object_):

<a name="Record.__init__"></a><small></small>**[<ins>Record.__init__</ins>](#Record.__init__)**(_inRecord, taglist=(), sFile='', sLine=0_):

Class for full WOS records

It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored privately.

The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [**getTag**()](#getTag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

##### Customizations

The `Record`'s hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with `'WOS:'` and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

When converted to a string the records title is used so for a record `R`, `R.TI == R.title == str(R)` and its representation uses the WOS number instead of memory location.

##### Attributes

When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [**citations**()](#citations) from the the [tagProcessing](#tagProcessing) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](#metaknowledge)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

The attribute `authors` is also defined as a connivence and returns the same as 'AF' or if that is not found 'AU'.

##### \_\_Init\_\_

Records are generally create as collections in  [Recordcollections](#RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

##### Parameters

_inRecord_: `files stream, dict, str or itertools.chain`

 If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

 If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](#recordParser) returns.

 For a string the input must be the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in `'ER'`.

 itertools.chain is treated identically to a file stream and is used by [RecordCollections](#RecordCollection).

_sFile_ : `optional [str]`

 Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

_sLine_ : `optional [int]`

 Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
The Record class has the following methods:

<ul class="post-list">
<li><article><a href="#numAuthors"><b>numAuthors</b>()</a></article></li>
<li><article><a href="#getTag"><b>getTag</b>(<i>tag, clean=False</i>)</a></article></li>
<li><article><a href="#createCitation"><b>createCitation</b>(<i>multiCite=False</i>)</a></article></li>
<li><article><a href="#getTagsList"><b>getTagsList</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#getTagsDict"><b>getTagsDict</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#activeTags"><b>activeTags</b>()</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#bibString"><b>bibString</b>(<i>maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True</i>)</a></article></li>
<li><article><a href="#bibTexType"><b>bibTexType</b>()</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="numAuthors"></a><small>Record.</small>**[<ins>numAuthors</ins>]({{ site.baseurl }}{{ page.url }}#numAuthors)**():

Returns the number of authors of the records, i.e. `len(self.authors)`

###### Returns

`int`

 The number of authors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTag"></a><small>Record.</small>**[<ins>getTag</ins>]({{ site.baseurl }}{{ page.url }}#getTag)**(_tag, clean=False_):

Returns a list containing the raw data of the record associated with _tag_. Each line of the record is one string in the list.

###### Parameters

_tag_ : `str`

 _tag_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing). If the string is not found in the original record or after being translated through [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing), `None` is returned.

_clean_ : `optional [bool]`

 Default `False`, if `True` the processed data will be returned instead of the raw data.

###### Returns

`List [str]`

 Each string in the list is a line from the record associated with _tag_ or `None` if not found.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="createCitation"></a><small>Record.</small>**[<ins>createCitation</ins>]({{ site.baseurl }}{{ page.url }}#createCitation)**(_multiCite=False_):

Creates a citation string, using the same format as other WOS citations, for the [Record]({{ site.baseurl }}{{ page.url }}#Record) by reading the relevant tags (`year`, `J9`, `volume`, `beginningPage`, `DOI`) and using it to create a [`Citation`]({{ site.baseurl }}{{ page.url }}#Citation) object.

###### Parameters

_multiCite_ : `optional [bool]`

 Default `False`, if `True` a tuple of Citations is returned with each having a different one of the records authors as the author

###### Returns

`Citation`

 A [`Citation`]({{ site.baseurl }}{{ page.url }}#Citation) object containing a citation for the Record.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTagsList"></a><small>Record.</small>**[<ins>getTagsList</ins>]({{ site.baseurl }}{{ page.url }}#getTagsList)**(_taglst, cleaned=False_):

Returns a list of the results of [**getTag**()]({{ site.baseurl }}{{ page.url }}#getTag) for each tag in _taglist_, the return has the same order as the original.

###### Parameters
_taglst_ : `List[str]`

 Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9',  or it can be one of the full names for a tag with the mappings in [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing). If the string is not found in the original record before or after being translated through [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing), `None` is used instead. Same as in [**getTag()**]({{ site.baseurl }}{{ page.url }}#getTag)

 Then they are compiled into a list in the same order as _taglst_

###### Returns

`List[str]`

 a list of the values for each tag in _taglst_, in the same order


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTagsDict"></a><small>Record.</small>**[<ins>getTagsDict</ins>]({{ site.baseurl }}{{ page.url }}#getTagsDict)**(_taglst, cleaned=False_):

returns a dict of the results of getTag, with the elements of _taglst_ as the keys and the results as the values.

###### Parameters
_taglst_ : `List[str]`

 Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing). If the string is not found in the oriagnal record before or after being translated through [fullToTag]({{ site.baseurl }}{{ page.url }}#tagProcessing), `None` is used instead. Same as in [**getTag**()]({{ site.baseurl }}{{ page.url }}#getTag)

###### Returns

`dict[str : List [str]]`

 a dictionary with keys as the original tags in _taglst_ and the values as the results


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="activeTags"></a><small>Record.</small>**[<ins>activeTags</ins>]({{ site.baseurl }}{{ page.url }}#activeTags)**():

Returns a list of all the tags the original WOS record had. These are all the tags that [**getTag**()]({{ site.baseurl }}{{ page.url }}#getTag) will not return `None` for.

###### Returns

`List[str]`

 a list of WOS tags in the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>Record.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_infile_):

Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections]({{ site.baseurl }}{{ page.url }}#RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file (if utf-8 is used). No newline is inserted above the write but the last character is a newline.

###### Parameters

_infile_ : `file stream`

 An open utf-8 encoded file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bibString"></a><small>Record.</small>**[<ins>bibString</ins>]({{ site.baseurl }}{{ page.url }}#bibString)**(_maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True_):

Makes a string giving the Record as a bibTex entry. If the Record is of a journal article (`PT J`) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

**Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier.

**Note** Record entries that are lists have their values seperated with the string `' and '`

###### Parameters

_maxLength_ : `optional [int]`

 default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

_WOSMode_ : `optional [bool]`

 default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

_restrictedOutput_ : `optional [bool]`

 default `False`, if `True` the tags output will be limited to: `'AF'`, `'BF'`, `'ED'`, `'TI'`, `'SO'`, `'LA'`, `'NR'`, `'TC'`, `'Z9'`, `'PU'`, `'J9'`, `'PY'`, `'PD'`, `'VL'`, `'IS'`, `'SU'`, `'PG'`, `'DI'`, `'D2'`, and `'UT'`

_niceID_ : `optional [bool]`

 default `True`, if `True` the ID used will be derived from the authors, publishing date and title, if `False` it will be the UT tag

###### Returns

`str`

 The bibTex string of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bibTexType"></a><small>Record.</small>**[<ins>bibTexType</ins>]({{ site.baseurl }}{{ page.url }}#bibTexType)**():

Returns the bibTex type corresonding to the record

###### Returns

`str`

 The bibTex type string



---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a><small></small>**[<ins>RecordCollection</ins>](#RecordCollection)**(_object_):

<a name="RecordCollection.__init__"></a><small></small>**[<ins>RecordCollection.__init__</ins>](#RecordCollection.__init__)**(_inCollection=None, name='', extension=''_):

A container for a large number of indivual WOS records.

`RecordCollection` provides ways of creating `[Records`](#Record) from an isi file, string, list of records or directory containing isi files.

When being created if there are issues the Record collection will be declared bad, `bad` wil be set to `False`, it will then mostly return `None` or False. The attribute `error` contains the exception that occurred.

They also possess an attribute `name` also accessed accessed with **__repr__**(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred.

##### Customizations

The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur. The comparison operators `<`, `<=`, `>`, `>=` are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

##### \_\_Init\_\_

_inCollection_ is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

##### Parameters

_inCollection_ : `optional [str] or None`

 the name of the source of WOS records. It can be skipped to produce an empty collection.

 If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

 If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

_name_ : `optional [str]`

 The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

_extension_ : `optional [str]`

 The extension to search for when reading a directory for files. _extension_ is the suffix searched for when a directory is read for files, by default it is empty so all files are read.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
The RecordCollection class has the following methods:

<ul class="post-list">
<li><article><a href="#twoModeNetwork"><b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><b>nModeNetwork</b>(<i>tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
<li><article><a href="#localCiteStats"><b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
<li><article><a href="#pop"><b>pop</b>()</a></article></li>
<li><article><a href="#peak"><b>peak</b>()</a></article></li>
<li><article><a href="#dropWOS"><b>dropWOS</b>(<i>wosNum</i>)</a></article></li>
<li><article><a href="#addRec"><b>addRec</b>(<i>Rec</i>)</a></article></li>
<li><article><a href="#getWOS"><b>getWOS</b>(<i>wosNum, drop=False</i>)</a></article></li>
<li><article><a href="#getBadRecords"><b>getBadRecords</b>()</a></article></li>
<li><article><a href="#dropBadRecords"><b>dropBadRecords</b>()</a></article></li>
<li><article><a href="#dropNonJournals"><b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><b>writeCSV</b>(<i>fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#writeBib"><b>writeBib</b>(<i>fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True</i>)</a></article></li>
<li><article><a href="#makeDict"><b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><b>coAuthNetwork</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
<li><article><a href="#coCiteNetwork"><b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#citationNetwork"><b>citationNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#yearSplit"><b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="twoModeNetwork"></a><small>RecordCollection.</small>**[<ins>twoModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#twoModeNetwork)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None_):

Creates a network of the objects found by two WOS tags _tag1_ and _tag2_, each node marked by which tag spawned it making the resultant graph bipartite.

A **twoModeNetwork()** looks at each Record in the `RecordCollection` and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `'WC'` and `'LA'` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `'WC'` and language tag `'LA'`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. the node `'English'` would have the type attribute be `'LA'`.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

The _directed_ parameter if `True` will cause the network to be directed with the first tag as the source and the second as the destination.

###### Parameters

_tag1_ : `str`

 A two character WOS tag or one of the full names for a tag, the source of edges on the graph

_tag1_ : `str`

 A two character WOS tag or one of the full names for a tag, the target of edges on the graph

_directed_ : `optional [bool]`

 Default `False`, if `True` the returned network is directed

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmerTag1_ : `optional [func]`

 Default `None`, If _stemmerTag1_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node given by _tag1_ in the graph, all IDs are strings.

 For example: the function `f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

_stemmerTag2_ : `optional [func]`

 Default `None`, see _stemmerTag1_ as it is the same but for _tag2_

###### Returns

`networkx Graph or networkx DiGraph`

 A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="nModeNetwork"></a><small>RecordCollection.</small>**[<ins>nModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#nModeNetwork)**(_tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None_):

Creates a network of the objects found by all WOS tags in _tags_, each node is marked by which tag spawned it making the resultant graph n-partite.

A **nModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. if `'LA'` were in _tags_ node `'English'` would have the type attribute be `'LA'`.

For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `'CR'` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called `'count'` that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called `'weight'` that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 Default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, note that all IDs are strings.

 For example: the function `f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCiteStats"></a><small>RecordCollection.</small>**[<ins>localCiteStats</ins>]({{ site.baseurl }}{{ page.url }}#localCiteStats)**(_pandasFriendly=False, keyType='citation'_):

Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

###### Parameters

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `'Citations'` is the citations the other is their occurrence counts as `'Counts'`.

_keyType_ : `optional [str]`

 default `'citation'`, the type of key to use for the dictionary, the valid strings are `'citation'`, `'journal'`, `'year'` or `'author'`. IF changed from `'citation'` all citations matching the requested option will be contracted and their counts added together.

###### Returns

`dict[str, int or Citation : int]`

 A dictionary with keys as given by _keyType_ and integers giving their rates of occurrence in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCitesOf"></a><small>RecordCollection.</small>**[<ins>localCitesOf</ins>]({{ site.baseurl }}{{ page.url }}#localCitesOf)**(_rec_):

Takes in a Record, WOS string, citation string or Citation and returns a RecordCollection of all records that cite it.

###### Parameters

_rec_ : `Record, str or Citation`

 The object that is being cited

###### Returns

`RecordCollection`

 A `RecordCollection` containing only those `Records` that cite _rec_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citeFilter"></a><small>RecordCollection.</small>**[<ins>citeFilter</ins>]({{ site.baseurl }}{{ page.url }}#citeFilter)**(_keyString='', field='all', reverse=False, caseSensitive=False_):

Filters `Records` by some string, _keyString_, in their citations and returns all `Records` with at least one citation possessing _keyString_ in the field given by _field_.

###### Parameters

_keyString_ : `optional [str]`

 Default `''`, gives the string to be searched for, if it is is blank then all citations with the specified field will be matched

_field_ : `optional [str]`

 Default `'all'`, gives the component of the citation to be looked at, it can be one of a few strings. The default is `'all'` which will cause the entire original `Citation` to be searched. It can be used to search across fields, e.g. `'1970, V2'` is a valid keystring
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

 Default `False`, being set to `True` causes all `Records` not matching the query to be returned

_caseSensitive_ : `optional [bool]`

 Default `False`, if `True` causes the search across the original to be case sensitive, **only** the `'all'` option can be case sensitive


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pop"></a><small>RecordCollection.</small>**[<ins>pop</ins>]({{ site.baseurl }}{{ page.url }}#pop)**():

Returns a random `Record` from the `RecordCollection`, the `Record` is deleted from the collection, use [**peak**()]({{ site.baseurl }}{{ page.url }}#peak) for nondestructive, but slower, access

###### Returns

`Record`

 A random `Record` that has been removed from the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="peak"></a><small>RecordCollection.</small>**[<ins>peak</ins>]({{ site.baseurl }}{{ page.url }}#peak)**():

Returns a random `Record` from the `RecordCollection`, the `Record` is kept in the collection, use [**pop**()]({{ site.baseurl }}{{ page.url }}#pop) for faster destructive access.

###### Returns

`Record`

 A random `Record` in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropWOS"></a><small>RecordCollection.</small>**[<ins>dropWOS</ins>]({{ site.baseurl }}{{ page.url }}#dropWOS)**(_wosNum_):

Removes the `Record` with WOS number (ID number) _wosNum_ from the collection. If it cannot be found nothing happens.

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the Record to be dropped. _wosNum_ must begin with `'WOS:'` or a valueError is raise.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addRec"></a><small>RecordCollection.</small>**[<ins>addRec</ins>]({{ site.baseurl }}{{ page.url }}#addRec)**(_Rec_):

Adds a `Record` or `Records` to the collection.

###### Parameters

_Rec_ : `Record or iterable[Record]`

 A Record or some iterable containing `Records` to add


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getWOS"></a><small>RecordCollection.</small>**[<ins>getWOS</ins>]({{ site.baseurl }}{{ page.url }}#getWOS)**(_wosNum, drop=False_):

Gets the `Record` from the collection by its WOS number (ID number) _wosNum_.

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the `Record` to be extracted. _wosNum_ must begin with `'WOS:'` or a valueError is raise.

_drop_ : `optional [bool]`

 Default `False`. If `True` the Record is dropped from the collection after being extract, i.e. if `False` [**getWOS**()]({{ site.baseurl }}{{ page.url }}#getWOS) acts like [**peak**()]({{ site.baseurl }}{{ page.url }}#peak), if `True` it acts like [**pop**()]({{ site.baseurl }}{{ page.url }}#pop)

###### Returns

`metaknowledge.Record`

 The `Record` whose WOS number is _wosNum_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getBadRecords"></a><small>RecordCollection.</small>**[<ins>getBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#getBadRecords)**():

creates a `RecordCollection` containing all the `Record` which have their `bad` attribute set to `True`, i.e. all those removed by [**dropBadRecords**()]({{ site.baseurl }}{{ page.url }}#dropBadRecords).

###### Returns

`RecordCollection`

 All the bad `Records` in one collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropBadRecords"></a><small>RecordCollection.</small>**[<ins>dropBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#dropBadRecords)**():

Removes all `Records` with `bad` attribute `True` from the collection, i.e. drop all those returned by [**getBadRecords**()]({{ site.baseurl }}{{ page.url }}#getBadRecords).
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNonJournals"></a><small>RecordCollection.</small>**[<ins>dropNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#dropNonJournals)**(_ptVal='J', dropBad=True, invert=False_):

Drops the non journal type `Records` from the collection, this is done by checking _ptVal_ against the PT tag

###### Parameters

_ptVal_ : `optional [str]`

 Default `'J'`, The value of the PT tag to be kept, default is `'J'` the journal tag, other tags can be substituted.

_dropBad_ : `optional [bool]`

 Default `True`, if `True` bad `Records` will be dropped as well those that are not journal entries

_invert_ : `optional [bool]`

 Default `False`, Set `True` to drop journals (or the PT tag given by _ptVal_) instead of keeping them. **Note**, it still drops bad Records if _dropBad_ is `True`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeFile"></a><small>RecordCollection.</small>**[<ins>writeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeFile)**(_fname=None_):

Writes the `RecordCollection` to a file, the written file's format is identical to those download from WOS. The order of `Records` written is random.

###### Parameters

_fname_ : `optional [str]`

 Default `None`, if given the output file will written to _fanme_, if `None` the `RecordCollection`'s name's first 200 characters are used with the suffix .isi


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeCSV"></a><small>RecordCollection.</small>**[<ins>writeCSV</ins>]({{ site.baseurl }}{{ page.url }}#writeCSV)**(_fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

Writes all the `Records` from the collection into a csv file with each row a record and each column a tag.

###### Parameters

_fname_ : `optional [str]`

 Default `None`, the name of the file to write to, if `None` it uses the collections name suffixed by .csv.

_onlyTheseTags_ : `optional [iterable]`

 Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

 If you want to use all known tags pass [`metaknowledge.knownTagsList`]({{ site.baseurl }}{{ page.url }}#tagProcessing).

_numAuthors_ : `optional [bool]`

 Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.

_longNames_ : `optional [bool]`

 Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

_firstTags_ : `optional [iterable]`

 Default `None`, if `None` the iterable `['UT', 'PT', 'TI', 'AF', 'CR']` is used. The tags given by the iterable are the first ones in the csv in the order given.

 **Note** if tags are in _firstTags_ but not in _onlyTheseTags_, _onlyTheseTags_ will override _firstTags_

_csvDelimiter_ : `optional [str]`

 Default `','`, the delimiter used for the cells of the csv file.

_csvQuote_ : `optional [str]`

 Default `'"'`, the quote character used for the csv.

_listDelimiter_ : `optional [str]`

 Default `'|'`, the delimiter used between values of the same cell if the tag for that record has multiple outputs.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeBib"></a><small>RecordCollection.</small>**[<ins>writeBib</ins>]({{ site.baseurl }}{{ page.url }}#writeBib)**(_fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True_):

Writes a bibTex entry to _fname_ for each `Record` in the collection.

If the Record is of a journal article (PT J) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

**Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier only.

**Note** Record entries that are lists have their values separated with the string `' and '`, as this is the way bibTex understands

###### Parameters

_fname_ : `optional [str]`

 Default `None`, The name of the file to be written. If not given one will be derived from the collection and the file will be written to .

_maxStringLength_ : `optional [int]`

 Default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

_WOSMode_ : `optional [bool]`

 Default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

_restrictedOutput_ : `optional [bool]`

 Default `False`, if `True` the tags output will be limited to: `'AF'`, `'BF'`, `'ED'`, `'TI'`, `'SO'`, `'LA'`, `'NR'`, `'TC'`, `'Z9'`, `'PU'`, `'J9'`, `'PY'`, `'PD'`, `'VL'`, `'IS'`, `'SU'`, `'PG'`, `'DI'`, `'D2'`, and `'UT'`

_niceID_ : `optional [bool]`

 Default `True`, if `True` the IDs used will be derived from the authors, publishing date and title, if `False` it will be the UT tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="makeDict"></a><small>RecordCollection.</small>**[<ins>makeDict</ins>]({{ site.baseurl }}{{ page.url }}#makeDict)**(_onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True_):

Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

When used with pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

###### Parameters

_onlyTheseTags_ : `optional [iterable]`

 Default `None`, if an iterable (list, tuple, etc) only the tags in _onlyTheseTags_ will be used, if not given then all tags in the records are given.

 If you want to use all known tags pass [`metaknowledge.knownTagsList`]({{ site.baseurl }}{{ page.url }}#tagProcessing).

_longNames_ : `optional [bool]`

 Default `False`, if `True` will convert the tags to their longer names, otherwise the short 2 character ones will be used.

_cleanedVal_ : `optional [bool]`

 Default `True`, if `True` the processed values for each `Record`'s field will be provided, otherwise the raw values are given.

_numAuthors_ : `optional [bool]`

 Default `True`, if `True` adds the number of authors as the column `'numAuthors'`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coAuthNetwork"></a><small>RecordCollection.</small>**[<ins>coAuthNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coAuthNetwork)**(_detailedInfo=False, weighted=True, dropNonJournals=False, count=True_):

Creates a coauthorship network for the RecordCollection.

###### Parameters

_detailedInfo_ : `optional [bool or iterable[WOS tag Strings]]`

 Default `False`, if `True` all nodes will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedInfo_ is an iterable (that evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attributes.

 For each of the selected tags an attribute will be added to the node using the values of those tags on the first `Record` encountered. **Warning** iterating over `RecordCollection` objects is not deterministic the first `Record` will not always be same between runs. The node will be given attributes with the names of the WOS tags for each of the selected tags. The attributes will contain strings of containing the values (with commas removed), if multiple values are encountered they will be comma separated.

 Note: _detailedInfo_ is not identical to the _detailedCore_ argument of [`Recordcollection.coCiteNetwork()`]({{ site.baseurl }}{{ page.url }}#coCiteNetwork) or [`Recordcollection.citationNetwork()`]({{ site.baseurl }}{{ page.url }}#citationNetwork)

_weighted_ : `optional [bool]`

 Default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of co-authorships.

_dropNonJournals_ : `optional [bool]`

 Default `False`, wether to drop authors from non-journals

_count_ : `optional [bool]`

 Default `True`, causes the number of occurrences of a node to be counted

###### Returns

`Networkx Graph`

 A networkx graph with author names as nodes and collaborations as edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coCiteNetwork"></a><small>RecordCollection.</small>**[<ins>coCiteNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coCiteNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False_):

Creates a co-citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{{ page.url }}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

_dropAnon_ : `optional [bool]`

 default `True`, if `True` citations labeled anonymous are removed from the network

_nodeInfo_ : `optional [bool]`

 default `True`, if `True` an extra piece of information is stored with each node. The extra inforamtion is detemined by _nodeType_.

_fullInfo_ : `optional [bool]`

 default `False`, if `True` the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

_weighted_ : `optional [bool]`

 default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

_dropNonJournals_ : `optional [bool]`

 default `False`, wether to drop citations of non-journals

_count_ : `optional [bool]`

 default `True`, causes the number of occurrences of a node to be counted

_keyWords_ : `optional [str] or [list[str]]`

 A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

_detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

 default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`]({{ site.baseurl }}{{ page.url }}#coAuthNetwork)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

_expandedCore_ : `optional [bool]`

 default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

###### Returns

`Networkx Graph`

 A networkx graph with hashes as ID and co-citation as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citationNetwork"></a><small>RecordCollection.</small>**[<ins>citationNetwork</ins>]({{ site.baseurl }}{{ page.url }}#citationNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, coreOnly=False, expandedCore=False_):

Creates a citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{{ page.url }}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

_dropAnon_ : `optional [bool]`

 default `True`, if `True` citations labeled anonymous are removed from the network

_nodeInfo_ : `optional [bool]`

 default `True`, wether an extra piece of information is stored with each node.

_fullInfo_ : `optional [bool]`

 default `False`, wether the original citation string is added to the node as an extra value, the attribute is labeled as fullCite

_weighted_ : `optional [bool]`

 default `True`, wether the edges are weighted. If `True` the edges are weighted by the number of citations.

_dropNonJournals_ : `optional [bool]`

 default `False`, wether to drop citations of non-journals

_count_ : `optional [bool]`

 default `True`, causes the number of occurrences of a node to be counted

_keyWords_ : `optional [str] or [list[str]]`

 A string or list of strings that the citations are checked against, if they contain any of the strings they are removed from the network

_directed_ : `optional [bool]`

 Determines if the output graph is directed, default `True`

_detailedCore_ : `optional [bool or iterable[WOS tag Strings]]`

 default `False`, if `True` all Citations from the core (those of records in the RecordCollection) and the _nodeType_ is `'full'` all nodes from the core will be given info strings composed of information from the Record objects themselves. This is Equivalent to passing the list: `['AF', 'PY', 'TI', 'SO', 'VL', 'BP']`.

 If _detailedCore_ is an iterable (That evaluates to `True`) of WOS Tags (or long names) The values  of those tags will be used to make the info attribute. All

 The resultant string is the values of each tag, with commas removed, seperated by `', '`, just like the info given by non-core Citations. Note that for tags like `'AF'` that return lists only the first entry in the list will be used. Also a second attribute is created for all nodes called inCore wich is a boolean describing if the node is in the core or not.

 Note: _detailedCore_  is not identical to the _detailedInfo_ argument of [`Recordcollection.coAuthNetwork()`]({{ site.baseurl }}{{ page.url }}#coAuthNetwork)

_coreOnly_ : `optional [bool]`

 default `False`, if `True` only Citations from the RecordCollection will be included in the network

_expandedCore_ : `optional [bool]`

 default `False`, if `True` all citations in the ouput graph that are records in the collection will be duplicated for each author. If the nodes are `"full"`, `"original"` or `"author"` this will result in new noded being created for the other options the results are **not** defined or tested. Edges will be created between each of the nodes for each record expanded, attributes will be copied from exiting nodes.

###### Returns

`Networkx DiGraph or Networkx Graph`

 See _directed_ for explanation of returned type

 A networkx digraph with hashes as ID and citations as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="yearSplit"></a><small>RecordCollection.</small>**[<ins>yearSplit</ins>]({{ site.baseurl }}{{ page.url }}#yearSplit)**(_startYear, endYear, dropMissingYears=True_):

Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

###### Parameters

_startYear_ : `int`

 The smallest year to be included in the returned RecordCollection

_endYear_ : `int`

 The largest year to be included in the returned RecordCollection

_dropMissingYears_ : `optional [bool]`

 Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

###### Returns

`RecordCollection`

 A RecordCollection of Records from _startYear_ to _endYear_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="oneModeNetwork"></a><small>RecordCollection.</small>**[<ins>oneModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#oneModeNetwork)**(_mode, nodeCount=True, edgeWeight=True, stemmer=None_):

Creates a network of the objects found by one WOS tag _mode_.

A **oneModeNetwork**() looks are each Record in the RecordCollection and extracts its values for the tag given by _mode_, e.g. the `'AF'` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `'AF'` a co-authorship network is created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()]({{ site.baseurl }}{{ page.url }}#coCiteNetwork) it is more accurate and has more options.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

_stemmer_ : `optional [func]`

 Default `None`, If _stemmer_ is a callable object, basically a function or possibly a class, it will be called for the ID of every node in the graph, all IDs are strings. For example:

 The function ` f = lambda x: x[0]` if given as the stemmer will cause all IDs to be the first character of their unstemmed IDs. e.g. the title `'Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes'` will create the node `'G'`.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges



---
<a name="visual"></a>

# [visual]({{ site.baseurl }}{{ page.url }}#visual)

Two functions based on _matplotlib_ for generating nicer looking graphs

This is the only module that depends on anything besides _networkx_, as it depends on _numpy_, _scipy_ and _matplotlib_ in addition to _networkx_.




The visual module provides the following functions:

<ul class="post-list">
<li><article><a href="#graphDensityContourPlot"><b>graphDensityContourPlot</b>(<i>G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'</i>)</a></article></li>
<li><article><a href="#quickVisual"><b>quickVisual</b>(<i>G, showLabel=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphDensityContourPlot"></a><small>visual.</small>**[<ins>graphDensityContourPlot</ins>]({{ site.baseurl }}{{ page.url }}#graphDensityContourPlot)**(_G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'_):

Creates a 3D plot giving the density of nodes on a 2D layout as a surface in 3 dimensions.

Most of the options are for tweaking the final appearance. _layout_ and _layoutScaleFactor_ allow a pre-layout graph to be provided. If a layout is not provided the [networkx.**spring_layout**()](https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.spring_layout.html) is used after _iters_ iterations. Then, once the graph has been laid out a grid of _axisSamples_ cells by _axisSamples_ cells is overlaid and the number of nodes in each cell is determined. This then forms a surface in 3-space, gaussian blur is applied with a sigma of _blurringFactor_. The surface is then be plotted.

###### Parameters

_G_ : `networkx Graph`

 The graph to be plotted

_iters_ : `optional [int]`

 Default `50`, the number of iterations for the spring layout if _layout_ is not provided.

_layout_ : `optional [networkx layout dictionary]`

 Default `None`, if provided will be used as a layout of the graph, the maximum distance from the origin along any axis must also given as _layoutScaleFactor_, which is by default `1`.

_layoutScaleFactor_ : `optional [double]`

 Default `1`, The maximum distance from the origin allowed along any axis given by _layout_, i.e. the layout must fit in a square centered at the origin with side lengths 2 * _layoutScaleFactor_

_overlay_ : `optional [bool]`

 Default `False`, if `True` the graph will be plotted on the X-Y plane at Z = 0.

_nodeSize_ : `optional [double]`

 Default `10`, the size of the nodes dawn in the overlay

_axisSamples_ : `optional [int]`

 Default 100, the number of cells used along each axis for sampling. A larger number will mean a lower average density.

_blurringFactor_ : `optional [double]`

 Default `0.1`, the sigma value used for smoothing the surface density. The higher this number the smoother the surface.

_contours_ : `optional [int]`

 Default 15, the number of different heights drawn. If this number is low the resultant image will look very banded. It is recommended this be raised above `50` if you want your images to look good, **Warning** this will make them much slower to generate and interact with.

_graphType_ : `optional [str]`

 Default `'coloured'`, if `'coloured'` the image will have a destiny based colourization applied, the only other option is `'solid'` which removes the colourization.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="quickVisual"></a><small>visual.</small>**[<ins>quickVisual</ins>]({{ site.baseurl }}{{ page.url }}#quickVisual)**(_G, showLabel=False_):

just makes a simple matplotlib figure and displays it, with each node coloured by its type. You can add labels with _showLabel_.

###### Parameters

_showLabel_ : `optional [bool]`

 Default `False`, if `True` labels will be added to the nodes giving their IDs.



---
<a name="journalAbbreviations"></a>

# [journalAbbreviations]({{ site.baseurl }}{{ page.url }}#journalAbbreviations)

This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in records, for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function [**updatej9DB**()](#getj9dict) is used to scape and parse the pages, it must be run without error before the other features can be used. _metaknowledge_ will try running it once during the installation but it could easily have been canceled or failed so it is best to it manually. **updatej9DB**() creates a database in the _metaknowledge_ install directory that gives each abbreviation and the titles it corresponds to, note there can be many titles for one abbreviation. The database can be accessed as a dictionary with [**getj9dict**()](#getj9dict).

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool `metaknowledge`, unless you know what you are doing.




The journalAbbreviations module provides the following functions:

<ul class="post-list">
<li><article><a href="#getj9dict"><b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#excludeFromDB"><b>excludeFromDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#updatej9DB"><b>updatej9DB</b>(<i>dbname='j9Abbreviations', saveRawHTML=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getj9dict"></a><small>journalAbbreviations.</small>**[<ins>getj9dict</ins>]({{ site.baseurl }}{{ page.url }}#getj9dict)**(_dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'_):

Returns the dictionary of journal abbreviations mapping to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

###### Parameters

_dbname_ : `optional [str]`

 The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

_manaulDB_ : `optional [str]`

 The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

_returnDict_ : `optional [str]`

 default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addToDB"></a><small>journalAbbreviations.</small>**[<ins>addToDB</ins>]({{ site.baseurl }}{{ page.url }}#addToDB)**(_abbr=None, dbname='manualj9Abbreviations'_):

Adds _abbr_ to the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manaulDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

###### Parameters

_abbr_ : `optional [str or dict[str : str]]`

 The journal abbreviation to be added to the database, it can either be a single string in which case that string will be added with its self as the full name, or a dict can be given with the abbreviations as keys and their names as strings, use pipes (`'|'`) to separate multiple names. Note, if the empty string is given as a name the abbreviation will be considered manually __excluded__, i.e. having excludeFromDB() run on it.

_dbname_ : `optional [str]`

 The name of the database file, default is `metaknowledge.journalAbbreviations.manaulDBname`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="excludeFromDB"></a><small>journalAbbreviations.</small>**[<ins>excludeFromDB</ins>]({{ site.baseurl }}{{ page.url }}#excludeFromDB)**(_abbr=None, dbname='manualj9Abbreviations'_):

Marks _abbr_ to be excluded the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manaulDBname`. To create an empty database run [**addToDB**()]({{ site.baseurl }}{{ page.url }}#addToDB) without an _abbr_ argument.

###### Parameters

_abbr_ : `optional [str or tuple[str] or list[str]`

 The journal abbreviation to be excluded from the database, it can either be a single string in which case that string will be exclude or a list/tuple of strings can be given with the abbreviations.

_dbname_ : `optional [str]`

 The name of the database file, default is `metaknowledge.journalAbbreviations.manaulDBname`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="updatej9DB"></a><small>journalAbbreviations.</small>**[<ins>updatej9DB</ins>]({{ site.baseurl }}{{ page.url }}#updatej9DB)**(_dbname='j9Abbreviations', saveRawHTML=False_):

Updates the database of Journal Title Abbreviations. Requires an internet connection. The data base is saved relative to the source file not the working directory.

###### Parameters

_dbname_ : `optional [str]`

 The name of the database file, default is "j9Abbreviations.db"

_saveRawHTML_ : `optional [bool]`

 Determines if the original HTML of the pages is stored, default `False`. If `True` they are saved in a directory inside j9Raws begining with todays date.



---
<a name="tagProcessing"></a>

# [tagProcessing]({{ site.baseurl }}{{ page.url }}#tagProcessing)

The functions used by metaknowledge to handle WOS tags

Each of the functions in tagProcessing is named after the long name of its tag and is responsible for taking the raw data from a WOS file and returning usable information. The raw data is a list containing each line associated with the tag as a string. So the section of a record:

    TI The Motion Behind the Symbols: A Vital Role for Dynamism in the
      Conceptualization of Limits and Continuity in Expert Mathematics

would be the list:

    ["The Motion Behind the Symbols: A Vital Role for Dynamism in the",
    "Conceptualization of Limits and Continuity in Expert Mathematics"
    ]

The function to process it is called [**title**()](#title) which is determined by looking up the tag in the `tagProcessing.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`](#metaknowledge).

The objects `tagToFullDict`, `fullToTagDict`, `tagNameConverterDict`, `tagsAndNameSet` and `knownTagsList` are also provided. They are the objects used by _metaknowledge_ to keep track of tag names. `tagToFullDict` and `fullToTagDict` are dictionaries that convert from tags to full names and vice versa, respectively, while `tagNameConverterDict` goes both ways. `tagsAndNameSet` is a set of all full names and tags, while `knownTagsList` contains only tags and is a list. For a less raw interface look the functions provided by the base _metaknowledge_ module, e.g. [**tagToFull**()](#tagToFull).

The full list of tags and their long names is provided below followed by the descriptions of the functions, they are ordered by their occurrence in WOS records:

| tag | Name |
|:---|:---|
| [`'PT'`]({{ site.baseurl }}{{ page.url }}#pubType) | [pubType]({{ site.baseurl }}{{ page.url }}#pubType) |
| [`'AF'`]({{ site.baseurl }}{{ page.url }}#authorsFull) | [authorsFull]({{ site.baseurl }}{{ page.url }}#authorsFull) |
| [`'GP'`]({{ site.baseurl }}{{ page.url }}#group) | [group]({{ site.baseurl }}{{ page.url }}#group) |
| [`'BE'`]({{ site.baseurl }}{{ page.url }}#editedBy) | [editedBy]({{ site.baseurl }}{{ page.url }}#editedBy) |
| [`'AU'`]({{ site.baseurl }}{{ page.url }}#authorsShort) | [authorsShort]({{ site.baseurl }}{{ page.url }}#authorsShort) |
| [`'BA'`]({{ site.baseurl }}{{ page.url }}#bookAuthor) | [bookAuthor]({{ site.baseurl }}{{ page.url }}#bookAuthor) |
| [`'BF'`]({{ site.baseurl }}{{ page.url }}#bookAuthorFull) | [bookAuthorFull]({{ site.baseurl }}{{ page.url }}#bookAuthorFull) |
| [`'CA'`]({{ site.baseurl }}{{ page.url }}#groupName) | [groupName]({{ site.baseurl }}{{ page.url }}#groupName) |
| [`'ED'`]({{ site.baseurl }}{{ page.url }}#editors) | [editors]({{ site.baseurl }}{{ page.url }}#editors) |
| [`'TI'`]({{ site.baseurl }}{{ page.url }}#title) | [title]({{ site.baseurl }}{{ page.url }}#title) |
| [`'SO'`]({{ site.baseurl }}{{ page.url }}#journal) | [journal]({{ site.baseurl }}{{ page.url }}#journal) |
| [`'SE'`]({{ site.baseurl }}{{ page.url }}#seriesTitle) | [seriesTitle]({{ site.baseurl }}{{ page.url }}#seriesTitle) |
| [`'BS'`]({{ site.baseurl }}{{ page.url }}#seriesSubtitle) | [seriesSubtitle]({{ site.baseurl }}{{ page.url }}#seriesSubtitle) |
| [`'LA'`]({{ site.baseurl }}{{ page.url }}#language) | [language]({{ site.baseurl }}{{ page.url }}#language) |
| [`'DT'`]({{ site.baseurl }}{{ page.url }}#docType) | [docType]({{ site.baseurl }}{{ page.url }}#docType) |
| [`'CT'`]({{ site.baseurl }}{{ page.url }}#confTitle) | [confTitle]({{ site.baseurl }}{{ page.url }}#confTitle) |
| [`'CY'`]({{ site.baseurl }}{{ page.url }}#confDate) | [confDate]({{ site.baseurl }}{{ page.url }}#confDate) |
| [`'HO'`]({{ site.baseurl }}{{ page.url }}#confHost) | [confHost]({{ site.baseurl }}{{ page.url }}#confHost) |
| [`'CL'`]({{ site.baseurl }}{{ page.url }}#confLocation) | [confLocation]({{ site.baseurl }}{{ page.url }}#confLocation) |
| [`'SP'`]({{ site.baseurl }}{{ page.url }}#confSponsors) | [confSponsors]({{ site.baseurl }}{{ page.url }}#confSponsors) |
| [`'DE'`]({{ site.baseurl }}{{ page.url }}#authKeyWords) | [authKeyWords]({{ site.baseurl }}{{ page.url }}#authKeyWords) |
| [`'ID'`]({{ site.baseurl }}{{ page.url }}#keyWords) | [keyWords]({{ site.baseurl }}{{ page.url }}#keyWords) |
| [`'AB'`]({{ site.baseurl }}{{ page.url }}#abstract) | [abstract]({{ site.baseurl }}{{ page.url }}#abstract) |
| [`'C1'`]({{ site.baseurl }}{{ page.url }}#authAddress) | [authAddress]({{ site.baseurl }}{{ page.url }}#authAddress) |
| [`'RP'`]({{ site.baseurl }}{{ page.url }}#reprintAddress) | [reprintAddress]({{ site.baseurl }}{{ page.url }}#reprintAddress) |
| [`'EM'`]({{ site.baseurl }}{{ page.url }}#email) | [email]({{ site.baseurl }}{{ page.url }}#email) |
| [`'RI'`]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber) | [ResearcherIDnumber]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber) |
| [`'OI'`]({{ site.baseurl }}{{ page.url }}#orcID) | [orcID]({{ site.baseurl }}{{ page.url }}#orcID) |
| [`'FU'`]({{ site.baseurl }}{{ page.url }}#funding) | [funding]({{ site.baseurl }}{{ page.url }}#funding) |
| [`'FX'`]({{ site.baseurl }}{{ page.url }}#fundingText) | [fundingText]({{ site.baseurl }}{{ page.url }}#fundingText) |
| [`'CR'`]({{ site.baseurl }}{{ page.url }}#citations) | [citations]({{ site.baseurl }}{{ page.url }}#citations) |
| [`'NR'`]({{ site.baseurl }}{{ page.url }}#citedRefsCount) | [citedRefsCount]({{ site.baseurl }}{{ page.url }}#citedRefsCount) |
| [`'TC'`]({{ site.baseurl }}{{ page.url }}#wosTimesCited) | [wosTimesCited]({{ site.baseurl }}{{ page.url }}#wosTimesCited) |
| [`'Z9'`]({{ site.baseurl }}{{ page.url }}#totalTimesCited) | [totalTimesCited]({{ site.baseurl }}{{ page.url }}#totalTimesCited) |
| [`'PU'`]({{ site.baseurl }}{{ page.url }}#publisher) | [publisher]({{ site.baseurl }}{{ page.url }}#publisher) |
| [`'PI'`]({{ site.baseurl }}{{ page.url }}#publisherCity) | [publisherCity]({{ site.baseurl }}{{ page.url }}#publisherCity) |
| [`'PA'`]({{ site.baseurl }}{{ page.url }}#publisherAddress) | [publisherAddress]({{ site.baseurl }}{{ page.url }}#publisherAddress) |
| [`'SC'`]({{ site.baseurl }}{{ page.url }}#subjectCategory) | [subjectCategory]({{ site.baseurl }}{{ page.url }}#subjectCategory) |
| [`'SN'`]({{ site.baseurl }}{{ page.url }}#ISSN) | [ISSN]({{ site.baseurl }}{{ page.url }}#ISSN) |
| [`'EI'`]({{ site.baseurl }}{{ page.url }}#eISSN) | [eISSN]({{ site.baseurl }}{{ page.url }}#eISSN) |
| [`'BN'`]({{ site.baseurl }}{{ page.url }}#ISBN) | [ISBN]({{ site.baseurl }}{{ page.url }}#ISBN) |
| [`'J9'`]({{ site.baseurl }}{{ page.url }}#j9) | [j9]({{ site.baseurl }}{{ page.url }}#j9) |
| [`'JI'`]({{ site.baseurl }}{{ page.url }}#isoAbbreviation) | [isoAbbreviation]({{ site.baseurl }}{{ page.url }}#isoAbbreviation) |
| [`'PD'`]({{ site.baseurl }}{{ page.url }}#month) | [month]({{ site.baseurl }}{{ page.url }}#month) |
| [`'PY'`]({{ site.baseurl }}{{ page.url }}#year) | [year]({{ site.baseurl }}{{ page.url }}#year) |
| [`'VL'`]({{ site.baseurl }}{{ page.url }}#volume) | [volume]({{ site.baseurl }}{{ page.url }}#volume) |
| [`'IS'`]({{ site.baseurl }}{{ page.url }}#issue) | [issue]({{ site.baseurl }}{{ page.url }}#issue) |
| [`'PN'`]({{ site.baseurl }}{{ page.url }}#partNumber) | [partNumber]({{ site.baseurl }}{{ page.url }}#partNumber) |
| [`'SU'`]({{ site.baseurl }}{{ page.url }}#supplement) | [supplement]({{ site.baseurl }}{{ page.url }}#supplement) |
| [`'SI'`]({{ site.baseurl }}{{ page.url }}#specialIssue) | [specialIssue]({{ site.baseurl }}{{ page.url }}#specialIssue) |
| [`'MA'`]({{ site.baseurl }}{{ page.url }}#meetingAbstract) | [meetingAbstract]({{ site.baseurl }}{{ page.url }}#meetingAbstract) |
| [`'BP'`]({{ site.baseurl }}{{ page.url }}#beginningPage) | [beginningPage]({{ site.baseurl }}{{ page.url }}#beginningPage) |
| [`'EP'`]({{ site.baseurl }}{{ page.url }}#endingPage) | [endingPage]({{ site.baseurl }}{{ page.url }}#endingPage) |
| [`'AR'`]({{ site.baseurl }}{{ page.url }}#articleNumber) | [articleNumber]({{ site.baseurl }}{{ page.url }}#articleNumber) |
| [`'PG'`]({{ site.baseurl }}{{ page.url }}#pageCount) | [pageCount]({{ site.baseurl }}{{ page.url }}#pageCount) |
| [`'WC'`]({{ site.baseurl }}{{ page.url }}#subjects) | [subjects]({{ site.baseurl }}{{ page.url }}#subjects) |
| [`'DI'`]({{ site.baseurl }}{{ page.url }}#DOI) | [DOI]({{ site.baseurl }}{{ page.url }}#DOI) |
| [`'D2'`]({{ site.baseurl }}{{ page.url }}#bookDOI) | [bookDOI]({{ site.baseurl }}{{ page.url }}#bookDOI) |
| [`'GA'`]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber) | [documentDeliveryNumber]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber) |
| [`'UT'`]({{ site.baseurl }}{{ page.url }}#wosString) | [wosString]({{ site.baseurl }}{{ page.url }}#wosString) |
| [`'PM'`]({{ site.baseurl }}{{ page.url }}#pubMedID) | [pubMedID]({{ site.baseurl }}{{ page.url }}#pubMedID) |




<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubType"></a><small>tagProcessing.</small>**[<ins>pubType</ins>]({{ site.baseurl }}{{ page.url }}#pubType)**(_val_):

######The PT Tag

extracts the type of publication as a character: conference, book, journal, book in series, or patent

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsFull"></a><small>tagProcessing.</small>**[<ins>authorsFull</ins>]({{ site.baseurl }}{{ page.url }}#authorsFull)**(_val_):

######The AF Tag

extracts a list of authors full names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="group"></a><small>tagProcessing.</small>**[<ins>group</ins>]({{ site.baseurl }}{{ page.url }}#group)**(_val_):

######The GP Tag

extracts the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the name of the group


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editedBy"></a><small>tagProcessing.</small>**[<ins>editedBy</ins>]({{ site.baseurl }}{{ page.url }}#editedBy)**(_val_):

######The BE Tag

extracts a list of the editors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of editors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsShort"></a><small>tagProcessing.</small>**[<ins>authorsShort</ins>]({{ site.baseurl }}{{ page.url }}#authorsShort)**(_val_):

######The AU Tag

extracts a list of authors shortened names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthor"></a><small>tagProcessing.</small>**[<ins>bookAuthor</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthor)**(_val_):

######The BA Tag

extracts a list of the short names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthorFull"></a><small>tagProcessing.</small>**[<ins>bookAuthorFull</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthorFull)**(_val_):

######The BF Tag

extracts a list of the long names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="groupName"></a><small>tagProcessing.</small>**[<ins>groupName</ins>]({{ site.baseurl }}{{ page.url }}#groupName)**(_val_):

######The CA Tag

extracts the name of the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The group's name


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editors"></a><small>tagProcessing.</small>**[<ins>editors</ins>]({{ site.baseurl }}{{ page.url }}#editors)**(_val_):

###### Needs Work

currently not well understood, returns _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="title"></a><small>tagProcessing.</small>**[<ins>title</ins>]({{ site.baseurl }}{{ page.url }}#title)**(_val_):

######The TI Tag

extracts the title of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="journal"></a><small>tagProcessing.</small>**[<ins>journal</ins>]({{ site.baseurl }}{{ page.url }}#journal)**(_val_):

######The SO Tag

extracts the full name of the publication and normalizes it to uppercase

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The name of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesTitle"></a><small>tagProcessing.</small>**[<ins>seriesTitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesTitle)**(_val_):

######The SE Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesSubtitle"></a><small>tagProcessing.</small>**[<ins>seriesSubtitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesSubtitle)**(_val_):

######The BS Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The subtitle of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="language"></a><small>tagProcessing.</small>**[<ins>language</ins>]({{ site.baseurl }}{{ page.url }}#language)**(_val_):

######The LA Tag

extracts the languages of the Record as a string with languages separated by ', ', usually there is only one language

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The language(s) of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="docType"></a><small>tagProcessing.</small>**[<ins>docType</ins>]({{ site.baseurl }}{{ page.url }}#docType)**(_val_):

######The DT Tag

extracts the type of document the Record contains

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The type of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confTitle"></a><small>tagProcessing.</small>**[<ins>confTitle</ins>]({{ site.baseurl }}{{ page.url }}#confTitle)**(_val_):

######The CT Tag

extracts the title of the conference associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confDate"></a><small>tagProcessing.</small>**[<ins>confDate</ins>]({{ site.baseurl }}{{ page.url }}#confDate)**(_val_):

######The CY Tag

extracts the date string of the conference associated with the Record, the date is not normalized

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The data of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confHost"></a><small>tagProcessing.</small>**[<ins>confHost</ins>]({{ site.baseurl }}{{ page.url }}#confHost)**(_val_):

######The HO Tag

extracts the host of the conference

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The host


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confLocation"></a><small>tagProcessing.</small>**[<ins>confLocation</ins>]({{ site.baseurl }}{{ page.url }}#confLocation)**(_val_):

######The CL Tag

extracts the sting giving the conference's location

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The conferences address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confSponsors"></a><small>tagProcessing.</small>**[<ins>confSponsors</ins>]({{ site.baseurl }}{{ page.url }}#confSponsors)**(_val_):

######The SP Tag

extracts a list of sponsors for the conference associated with the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the list of of sponsors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authKeyWords"></a><small>tagProcessing.</small>**[<ins>authKeyWords</ins>]({{ site.baseurl }}{{ page.url }}#authKeyWords)**(_val_):

######The DE Tag

extracts the keywords assigned by the author of the Record. The WOS description is:

    Author keywords are included in records of articles from 1991 forward. They are also include in conference proceedings records.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of keywords


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="keyWords"></a><small>tagProcessing.</small>**[<ins>keyWords</ins>]({{ site.baseurl }}{{ page.url }}#keyWords)**(_val_):

######The ID Tag

extracts the WOS keywords of the Record. The WOS description is:

    KeyWords Plus are index terms created by Thomson Reuters from significant, frequently occurring words in the titles of an article's cited references.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The keyWords list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="abstract"></a><small>tagProcessing.</small>**[<ins>abstract</ins>]({{ site.baseurl }}{{ page.url }}#abstract)**(_val_):

######The AB Tag

return abstract of the record, with newlines hopefully in the correct places

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The abstract


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authAddress"></a><small>tagProcessing.</small>**[<ins>authAddress</ins>]({{ site.baseurl }}{{ page.url }}#authAddress)**(_val_):

###### The C1 Tag

extracts the address of the authors as given by WOS. **Warning** the mapping of author to address is not very good and is given in multiple ways.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of addresses


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="reprintAddress"></a><small>tagProcessing.</small>**[<ins>reprintAddress</ins>]({{ site.baseurl }}{{ page.url }}#reprintAddress)**(_val_):

######The RP Tag

extracts the reprint address string

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The reprint address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="email"></a><small>tagProcessing.</small>**[<ins>email</ins>]({{ site.baseurl }}{{ page.url }}#email)**(_val_):

######The EM Tag

extracts a list of emails given by the authors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of emails


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ResearcherIDnumber"></a><small>tagProcessing.</small>**[<ins>ResearcherIDnumber</ins>]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber)**(_val_):

######The RI Tag

extracts a list of the research IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of the research IDs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="orcID"></a><small>tagProcessing.</small>**[<ins>orcID</ins>]({{ site.baseurl }}{{ page.url }}#orcID)**(_val_):

######The OI Tag

extracts a list of orc IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The orc ID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="funding"></a><small>tagProcessing.</small>**[<ins>funding</ins>]({{ site.baseurl }}{{ page.url }}#funding)**(_val_):

######The FU Tag

extracts a list of the groups funding the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of funding groups


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="fundingText"></a><small>tagProcessing.</small>**[<ins>fundingText</ins>]({{ site.baseurl }}{{ page.url }}#fundingText)**(_val_):

######The FX Tag

extracts a string of the funding thanks

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The funding thank-you


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citations"></a><small>tagProcessing.</small>**[<ins>citations</ins>]({{ site.baseurl }}{{ page.url }}#citations)**(_val_):

######The CR Tag

extracts a list of all the citations in the record, the citations are the [metaknowledge.Citation]({{ site.baseurl }}{{ page.url }}#Citation) class.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

` list[metaknowledge.Citation]`

 A list of Citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citedRefsCount"></a><small>tagProcessing.</small>**[<ins>citedRefsCount</ins>]({{ site.baseurl }}{{ page.url }}#citedRefsCount)**(_val_):

######The NR Tag

extracts the number citations, length of CR list

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of CRs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosTimesCited"></a><small>tagProcessing.</small>**[<ins>wosTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#wosTimesCited)**(_val_):

######The TC Tag

extracts the number of times the Record has been cited by records in WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of time the Record has been cited


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="totalTimesCited"></a><small>tagProcessing.</small>**[<ins>totalTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#totalTimesCited)**(_val_):

######The Z9 Tag

extracts the total number of citations of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The total number of citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisher"></a><small>tagProcessing.</small>**[<ins>publisher</ins>]({{ site.baseurl }}{{ page.url }}#publisher)**(_val_):

######The PU Tag

extracts the publisher of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherCity"></a><small>tagProcessing.</small>**[<ins>publisherCity</ins>]({{ site.baseurl }}{{ page.url }}#publisherCity)**(_val_):

######The PI Tag

extracts the city the publisher is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The city of the publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherAddress"></a><small>tagProcessing.</small>**[<ins>publisherAddress</ins>]({{ site.baseurl }}{{ page.url }}#publisherAddress)**(_val_):

######The PA Tag

extracts the publishers address

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjectCategory"></a><small>tagProcessing.</small>**[<ins>subjectCategory</ins>]({{ site.baseurl }}{{ page.url }}#subjectCategory)**(_val_):

######The SC Tag

extracts a list of the subjects associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of the subjects associated with the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISSN"></a><small>tagProcessing.</small>**[<ins>ISSN</ins>]({{ site.baseurl }}{{ page.url }}#ISSN)**(_val_):

######The SN Tag

extracts the ISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The ISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="eISSN"></a><small>tagProcessing.</small>**[<ins>eISSN</ins>]({{ site.baseurl }}{{ page.url }}#eISSN)**(_val_):

######The EI Tag

extracts the EISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The EISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISBN"></a><small>tagProcessing.</small>**[<ins>ISBN</ins>]({{ site.baseurl }}{{ page.url }}#ISBN)**(_val_):

######The BN Tag

extracts a list of ISBNs associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list`

 The ISBNs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="j9"></a><small>tagProcessing.</small>**[<ins>j9</ins>]({{ site.baseurl }}{{ page.url }}#j9)**(_val_):

######The J9 Tag

extracts the J9 (29-Character Source Abbreviation) of the publication

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The 29-Character Source Abbreviation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isoAbbreviation"></a><small>tagProcessing.</small>**[<ins>isoAbbreviation</ins>]({{ site.baseurl }}{{ page.url }}#isoAbbreviation)**(_val_):

######The JI Tag

extracts the iso abbreviation of the journal

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The iso abbreviation of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="month"></a><small>tagProcessing.</small>**[<ins>month</ins>]({{ site.baseurl }}{{ page.url }}#month)**(_val_):

######The PD Tag

extracts the month the record was published in as an int with January as 1, February 2, ...

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 A integer giving the month


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="year"></a><small>tagProcessing.</small>**[<ins>year</ins>]({{ site.baseurl }}{{ page.url }}#year)**(_val_):

######The PY Tag

extracts the year the record was published in as an int

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The year


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="volume"></a><small>tagProcessing.</small>**[<ins>volume</ins>]({{ site.baseurl }}{{ page.url }}#volume)**(_val_):

######The VL Tag

return the volume the record is in as a string, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The volume number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="issue"></a><small>tagProcessing.</small>**[<ins>issue</ins>]({{ site.baseurl }}{{ page.url }}#issue)**(_val_):

######The IS Tag

extracts a string giving the issue or range of issues the Record was in, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The issue number/range


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="partNumber"></a><small>tagProcessing.</small>**[<ins>partNumber</ins>]({{ site.baseurl }}{{ page.url }}#partNumber)**(_val_):

######The PN Tag

return an integer giving the part of the issue the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The part of the issue of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="supplement"></a><small>tagProcessing.</small>**[<ins>supplement</ins>]({{ site.baseurl }}{{ page.url }}#supplement)**(_val_):

######The SU Tag

extracts the supplement number

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The supplement number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialIssue"></a><small>tagProcessing.</small>**[<ins>specialIssue</ins>]({{ site.baseurl }}{{ page.url }}#specialIssue)**(_val_):

######The SI Tag

extracts the special issue value

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The special issue value


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="meetingAbstract"></a><small>tagProcessing.</small>**[<ins>meetingAbstract</ins>]({{ site.baseurl }}{{ page.url }}#meetingAbstract)**(_val_):

######The MA Tag

extracts the ID of the meeting abstract prefixed by 'EPA-'

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The meeting abstract prefixed


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="beginningPage"></a><small>tagProcessing.</small>**[<ins>beginningPage</ins>]({{ site.baseurl }}{{ page.url }}#beginningPage)**(_val_):

######The BP Tag

extracts the first page the record occurs on, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The first page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="endingPage"></a><small>tagProcessing.</small>**[<ins>endingPage</ins>]({{ site.baseurl }}{{ page.url }}#endingPage)**(_val_):

######The EP Tag

return the last page the record occurs on as a string, not aall are intergers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The final page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="articleNumber"></a><small>tagProcessing.</small>**[<ins>articleNumber</ins>]({{ site.baseurl }}{{ page.url }}#articleNumber)**(_val_):

######The AR Tag

extracts a string giving the article number, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The article number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pageCount"></a><small>tagProcessing.</small>**[<ins>pageCount</ins>]({{ site.baseurl }}{{ page.url }}#pageCount)**(_val_):

######The PG Tag

returns an integer giving the number of pages of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The page count


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjects"></a><small>tagProcessing.</small>**[<ins>subjects</ins>]({{ site.baseurl }}{{ page.url }}#subjects)**(_val_):

######The WC Tag

extracts a list of subjects as assigned by WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The subjects list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DOI"></a><small>tagProcessing.</small>**[<ins>DOI</ins>]({{ site.baseurl }}{{ page.url }}#DOI)**(_val_):

######The DI Tag

return the DOI number of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookDOI"></a><small>tagProcessing.</small>**[<ins>bookDOI</ins>]({{ site.baseurl }}{{ page.url }}#bookDOI)**(_val_):

######The D2 Tag

extracts the book DOI of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="documentDeliveryNumber"></a><small>tagProcessing.</small>**[<ins>documentDeliveryNumber</ins>]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber)**(_val_):

######The GA Tag

extracts the document delivery number of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The document delivery number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosString"></a><small>tagProcessing.</small>**[<ins>wosString</ins>]({{ site.baseurl }}{{ page.url }}#wosString)**(_val_):

######The UT Tag

extracts the WOS number of the record as a string preceded by "WOS:"

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The WOS number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubMedID"></a><small>tagProcessing.</small>**[<ins>pubMedID</ins>]({{ site.baseurl }}{{ page.url }}#pubMedID)**(_val_):

######The PM Tag

extracts the pubmed ID of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The pubmed ID



{% include docsFooter.md %}