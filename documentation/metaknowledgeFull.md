---
layout: page
title: ""
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
The classes and modules of metaknowledge are:

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
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True</i>)</a></article></li>
<li><article><a href="#read_graph"><b>read_graph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#write_edgeList"><b>write_edgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#write_nodeAttributeFile"><b>write_nodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#drop_edges"><b>drop_edges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#drop_nodesByDegree"><b>drop_nodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True</i>)</a></article></li>
<li><article><a href="#drop_nodesByCount"><b>drop_nodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
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
<li><article><a href="#getExtra"><small>Citation</small>.<b>getExtra</b>()</a></article></li>
<li><article><a href="#isJournal"><small>Citation</small>.<b>isJournal</b>(<i>manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#getFullJournalName"><small>Citation</small>.<b>getFullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><small>Citation</small>.<b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
<li><article><a href="#numAuthors"><small>Record</small>.<b>numAuthors</b>()</a></article></li>
<li><article><a href="#getTag"><small>Record</small>.<b>getTag</b>(<i>tag, clean=False</i>)</a></article></li>
<li><article><a href="#createCitation"><small>Record</small>.<b>createCitation</b>()</a></article></li>
<li><article><a href="#getTagsList"><small>Record</small>.<b>getTagsList</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#getTagsDict"><small>Record</small>.<b>getTagsDict</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#activeTags"><small>Record</small>.<b>activeTags</b>()</a></article></li>
<li><article><a href="#writeRecord"><small>Record</small>.<b>writeRecord</b>(<i>infile</i>)</a></article></li>
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
<li><article><a href="#makeDict"><small>RecordCollection</small>.<b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><small>RecordCollection</small>.<b>coAuthNetwork</b>()</a></article></li>
<li><article><a href="#coCiteNetwork"><small>RecordCollection</small>.<b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None</i>)</a></article></li>
<li><article><a href="#citationNetwork"><small>RecordCollection</small>.<b>citationNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None</i>)</a></article></li>
<li><article><a href="#yearSplit"><small>RecordCollection</small>.<b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><small>RecordCollection</small>.<b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><small>RecordCollection</small>.<b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><small>RecordCollection</small>.<b>nModeNetwork</b>(<i>tags, recordType=True, nodeCount=True, edgeWeight=True</i>)</a></article></li>
<li><article><a href="#graphDensityContourPlot"><small>visual</small>.<b>graphDensityContourPlot</b>(<i>G, layout=None, layoutScaleFactor=1, shifAxis=False, overlay=False, axisSamples=100, blurringFactor=0.1, contours=15, nodeSize=10, graphType='coloured', iters=50</i>)</a></article></li>
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
<li><article><a href="#bookAuthor"><small>tagProcessing</small>.<b>bookAuthor</b>(<i>val</i>)</a></article></li>
<li><article><a href="#reprintAddress"><small>tagProcessing</small>.<b>reprintAddress</b>(<i>val</i>)</a></article></li>
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
<li><article><a href="#authorsFull"><small>tagProcessing</small>.<b>authorsFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#language"><small>tagProcessing</small>.<b>language</b>(<i>val</i>)</a></article></li>
<li><article><a href="#docType"><small>tagProcessing</small>.<b>docType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confTitle"><small>tagProcessing</small>.<b>confTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confDate"><small>tagProcessing</small>.<b>confDate</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confSponsors"><small>tagProcessing</small>.<b>confSponsors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosTimesCited"><small>tagProcessing</small>.<b>wosTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authAddress"><small>tagProcessing</small>.<b>authAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubType"><small>tagProcessing</small>.<b>pubType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confLocation"><small>tagProcessing</small>.<b>confLocation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#j9"><small>tagProcessing</small>.<b>j9</b>(<i>val</i>)</a></article></li>
<li><article><a href="#funding"><small>tagProcessing</small>.<b>funding</b>(<i>val</i>)</a></article></li>
<li><article><a href="#group"><small>tagProcessing</small>.<b>group</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjectCategory"><small>tagProcessing</small>.<b>subjectCategory</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citations"><small>tagProcessing</small>.<b>citations</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherCity"><small>tagProcessing</small>.<b>publisherCity</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISSN"><small>tagProcessing</small>.<b>ISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#articleNumber"><small>tagProcessing</small>.<b>articleNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#issue"><small>tagProcessing</small>.<b>issue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#email"><small>tagProcessing</small>.<b>email</b>(<i>val</i>)</a></article></li>
<li><article><a href="#eISSN"><small>tagProcessing</small>.<b>eISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DOI"><small>tagProcessing</small>.<b>DOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosString"><small>tagProcessing</small>.<b>wosString</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editedBy"><small>tagProcessing</small>.<b>editedBy</b>(<i>val</i>)</a></article></li>
<li><article><a href="#orcID"><small>tagProcessing</small>.<b>orcID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#meetingAbstract"><small>tagProcessing</small>.<b>meetingAbstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isoAbbreviation"><small>tagProcessing</small>.<b>isoAbbreviation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pageCount"><small>tagProcessing</small>.<b>pageCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisher"><small>tagProcessing</small>.<b>publisher</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><small>tagProcessing</small>.<b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#month"><small>tagProcessing</small>.<b>month</b>(<i>val</i>)</a></article></li>
<li><article><a href="#fundingText"><small>tagProcessing</small>.<b>fundingText</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookDOI"><small>tagProcessing</small>.<b>bookDOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#volume"><small>tagProcessing</small>.<b>volume</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsShort"><small>tagProcessing</small>.<b>authorsShort</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ResearcherIDnumber"><small>tagProcessing</small>.<b>ResearcherIDnumber</b>(<i>val</i>)</a></article></li>
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

#### Overview

This package can read the files downloaded from the [Thomson Reuters Web of Science](https://webofknowledge.com) (WOS) as plain text. These files contain metadata about scientific records, such as the authors, language, and citations. The records are saved in groups of up-to 500 individual records in a file.

The [metaknowledge.RecordCollection](#RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](#Record) class that contains the results of the parsing of the record.

The files given by WOS are a flat database containing a series of 2 character tags, e.g. 'TI' is the title. Each WOS tag has one or more values and metaknowledge makes use of them to extract useful information. The approximate meanings of the tags are listed in the [tagProcessing](#tagProcessing) package, if you simply want the mapping [`tagToFull()`](#tagToFull) is a function that maps tags to their full names it as well as a few other similar functions are provided by metaknowledge. There are no full official public listings of tag the meanings available. metaknowledge is not attempting to provide the definitive or authoritative meanings. Some

As citations are of great importance to sociology their handling is done with the [Citation](#Citation) class. This class can parse the citations given by WOS as well as extra details about the full name of their journal and allow simple comparisons.

Note for those reading the docstring metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation](http://networkslab.org/metaknowledge/documentation/).





---
<a name="Base Functions"></a>
The functions provided by metaknowledge are:

<ul class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, sourceType='raw', targetType='raw'</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True</i>)</a></article></li>
<li><article><a href="#read_graph"><b>read_graph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#write_edgeList"><b>write_edgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#write_nodeAttributeFile"><b>write_nodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#drop_edges"><b>drop_edges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#drop_nodesByDegree"><b>drop_nodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True</i>)</a></article></li>
<li><article><a href="#drop_nodesByCount"><b>drop_nodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
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

Removes the Citations from _citesLst_ that are not journals.

###### Parameters

_citesLst_ : `list [Citation]`

 A list of citations to be filtered

_invert_ : `optional [bool]`

 Default `False`, if `True` non-journals will be kept istead of journals

###### Returns

`list [Citation]`

 A filtered list of Citations from _citesLst_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionGraph"></a><small></small>**[<ins>diffusionGraph</ins>]({{ site.baseurl }}{{ page.url }}#diffusionGraph)**(_source, target, sourceType='raw', targetType='raw'_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#RecordCollection) and produces a graph of the citations of the `Records` of _source_ by the `Records` of _target_. By default the graph is of `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords.

Each node on the graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

###### Parameters

_source_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `str`

default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

_targetType_ : `str`

default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes. If it is a WOS tag of the long name of one then the nodes will be of that type.

###### Returns

`networkx Directed Graph`

A directed graph of the diffusion network


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionCount"></a><small></small>**[<ins>diffusionCount</ins>]({{ site.baseurl }}{{ page.url }}#diffusionCount)**(_source, target, sourceType='raw', pandasFriendly=False, compareCounts=False, numAuthors=True_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#RecordCollection) and produces a `dict` counting the citations of the `Records` of _source_ by the `Records` of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

###### Parameters

_source_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `optional [str]`

default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag of the long name of one then the keys will be of that type.

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurence counts as `"Counts"`.

_compareCounts_ : `optional [boo]`

 default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

###### Returns

`dict[:int]`

 A dictionary with the type given by _sourceType_ as keys and integers as values, by default. If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

 If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="read_graph"></a><small></small>**[<ins>read_graph</ins>]({{ site.baseurl }}{{ page.url }}#read_graph)**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by edgeList and if given nodeList. Outputs a networkx graph for the lists.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [write_graph()]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#write_graph), if this dow not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried.

The read edge list format assumes the column named _eSource_ (From) is the source node, then the next column _eDest_ (To) givens the destination and all other columns are attributes of the edge, e.g. weight.

The read nodeList format assumes the column called _idKey_ is the ID of the node as used by the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

If the names of the columns do not match those given to **read_graph()** a KeyError exception will be raised.

**Note**: if nodes appear in the edgelist but not the nodeList they will be created with no attributes.

###### Parameters

_edgeList_ : `str`

 a string giving the path to the edge list file

_nodeList_ : `optional [str]`

 a string giving the path to the node list file

_directed_ : `optional [bool]`

 default `False`, if `True` the produced network is directed instead of undirected

_idKey_ : `optional [str]`

 default `"ID"`, the name of the ID column in the node list

_eSource_ : `optional [str]`

 default `"From"`, the name of the source column in the edge list

_eDest_ : `optional [str]`

 default `"To"`, the name of the destination column in the edge list

###### Returns

`networkx Graph`

 the Graph described by the files


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="write_edgeList"></a><small></small>**[<ins>write_edgeList</ins>]({{ site.baseurl }}{{ page.url }}#write_edgeList)**(_grph, name, extraInfo=True, allSameAttribute=False_):

Writes an edge list of _grph_ at the destination _name_.

The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

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

Writes a node attribute list of _grph_ with filename _name_

The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

**Note**: If any edges are missing an attribute `KeyError` will be raised.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be written to _name_

_name_ : `str`

 The name of the file to be written

_allSameAttribute_ : `optional [bool]`

 Default `False`, if `True` all the nodes must have the same attributes or an exception will be raised. If `False` the missing attributes will be left blank.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_edges"></a><small></small>**[<ins>drop_edges</ins>]({{ site.baseurl }}{{ page.url }}#drop_edges)**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Returns a graph with edges whose weight is within the inclusive bounds of minWeight and maxWeight, i.e minWeight <= edges weight <= maxWeight, will throw a Keyerror if the graph is unweighted

minWeight and maxWeight default to negative and positive infinity respectively so without specifying either the output should be the input

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be ignored


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByDegree"></a><small></small>**[<ins>drop_nodesByDegree</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByDegree)**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', ignoreUnweighted=True_):

Returns a graph whose nodes have a degree that is within inclusive bounds of minDegree and maxDegree, i.e minDegree <= degree <= maxDegree. Degree can be determined in two ways by default it is the total number of edges touching a node, alternative if useWeight is True it is the sum of the weight of all the edges touching a node.

minDegree and maxDegree default to negative and positive infinity respectively so without specifying either the output should be the input

useWeight can be set True to use an alternative method for calculating degree, the total weight of all edges

parameterName is key to weight field in the edge's dictionary, default is weight as that is almost always correct, only used if useWeight is True

ignoreUnweighted can be set False to suppress the KeyError and make unweighted edges be not counted, only used if useWeight is True


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="drop_nodesByCount"></a><small></small>**[<ins>drop_nodesByCount</ins>]({{ site.baseurl }}{{ page.url }}#drop_nodesByCount)**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

Returns a graph whose nodes have a occurrence count that is within inclusive bounds of minCount and maxCount, i.e minCount <= count <= maxCount. Occurrence count is determined by reading the variable associated with the node named parameterName.

minCount and maxCount default to negative and positive infinity respectively so without specifying either the output should be the input


parameterName is key to count field in the node's dictionary, default is count as that is often correct

ignoreMissing can be set False to suppress the KeyError and make nodes missing counts be dropped instead of throwing errors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphStats"></a><small></small>**[<ins>graphStats</ins>]({{ site.baseurl }}{{ page.url }}#graphStats)**(_G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True_):

Returns a string or list containing statistics about the graph _G_.

**graphStats()** gives 6 different statistics: number of nodes, number of edges, number of isolates, number of loops, density and transitivity. The ones wanted can be given to _stats_. By default a string giving a sentence containing all the requested statistics is returned but the raw values can be accessed instead by setting _makeString_ to `False`.

###### Parameters

_G_ : `networkx Graph`

 The graph for the statistics to be determined of

_stats_ : `optional [list or tuple [str]]`

 Default 'nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), a list or tuple containing any number or combination of the strings:

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

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, "From" and "To" respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [read_graph()]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#read_graph) and to write only one type of lsit use [write_edgeList()]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#write_edgeList) or [write_nodeAttributeFile()]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#write_nodeAttributeFile).

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

Reads the file _paper_ until it reaches 'ER'.

For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following string in a record:

"AF BREVIK, I

    ANICIN, B"

The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

[Record]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#Record) objects can be created with these dictionaries as the initializer.

###### Parameters

_paper_ : `file stream`

 An open file, with the current line at the beginning of the record.

###### Returns

`dict[str : List[str]]`

 A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isiParser"></a><small></small>**[<ins>isiParser</ins>]({{ site.baseurl }}{{ page.url }}#isiParser)**(_isifile_):

isiParser() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF.
Each it finds is used to initialize a Record then all Record are returned as a list.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagToFull"></a><small></small>**[<ins>tagToFull</ins>]({{ site.baseurl }}{{ page.url }}#tagToFull)**(_tag_):

A wrapper for [`tagToFullDict`]({{ site.baseurl }}{% post_url /docs/2015-11-05-tagProcessing %}#tagProcessing) it maps 2 character tags to thir full names.

###### Parameters

_tag_: `str`

 A two character string giving the tag

###### Returns

`str`

 The full name of _tag_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToTag"></a><small></small>**[<ins>normalizeToTag</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToTag)**(_val_):

Converts tags or full names to tags

###### Parameters

_val_: `str`

 A two character string giving the tag or its full name

###### Returns

`str`

 The short name of _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="normalizeToName"></a><small></small>**[<ins>normalizeToName</ins>]({{ site.baseurl }}{{ page.url }}#normalizeToName)**(_val_):

Converts tags or full names to full names

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


<a name="BadCitation"></a><small></small>**[<ins>BadCitation</ins>]({{ site.baseurl }}{{ page.url }}#BadCitation)**():

Exception thrown by Citation


The BadCitation class has the following methods:

<ul class="post-list">

</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="BadISIRecord"></a><small></small>**[<ins>BadISIRecord</ins>]({{ site.baseurl }}{{ page.url }}#BadISIRecord)**():

Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * _Missing field on line (line Number):(line)_, which indicates a line was to short, there should have been a tag followed by information

    * _End of file reached before ER_, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * _Duplicate tags in record_, which indicates the record had 2 or more lines with the same tag.

    * _Missing WOS number_, which indicates the record did not have a 'UT' tag.

Records with a BadISIRecord error are likely incomplete or the combination of two or more single records.


The BadISIRecord class has the following methods:

<ul class="post-list">

</ul>

---
<a name="Citation"></a>
<a name="Citation"></a><small></small>**[<ins>Citation</ins>](#Citation)**(_cite_):

A class to hold citation strings and allow for comparison between them.

The initializer takes in a string representing a WOS citation they are in the form:

 Author, Year, Journal, Volume, Page, DOI

Author is the author's name in the form of first last name first initial sometimes followed by a period.
Year is the year of publication.
Journal being the 29-Character Source Abbreviation of the journal.
Volume is the volume number(s) of the publication preceded by a V
Page is the page number the record starts on
DOI is the DOI number of the cited record preceeded by the letters "DOI"
Combined they look like:

 Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

Note that any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpeted as any of these it is put in the `misc` attribute.

The reason for this class is that the WOS data are often irregular. It is designed to allow comparison between WOS citation strings, even when they are missing pieces.

##### Customizations

Citation's hashing and equality checking are based on [`getID()`](#getID) and use the values of `author`, `year` and `journal`.

When converted to a string a Citation will return the original string.

##### Attributes

As noted above, citations are considered to be divided into six distinct fields (Author, Year, Journal, Volume, Page and DOI) with a seventh misc for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a Citation created from the string: "Nunez R., 1998, MATH COGNITION" would have `author`, `year` and `journal` defined. While one from "Nunez R." would have only the attribute `misc`.

If the parsing of a citation string fails the attribute `bad` is set to True and the attribute `error` is created to contain the error, which is a [BadCitation](#BadCitation) object. If no errors occur `bad` is `False`.

The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

##### \_\_Init\_\_

Citations can be created by [Records](#Record) or by giving the initializer a string containing a WOS style citation.

##### Parameters

_cite_ : `str`

 A str containing a WOS style citation.


The Citation class has the following methods:

<ul class="post-list">
<li><article><a href="#isAnonymous"><b>isAnonymous</b>()</a></article></li>
<li><article><a href="#getID"><b>getID</b>()</a></article></li>
<li><article><a href="#getExtra"><b>getExtra</b>()</a></article></li>
<li><article><a href="#isJournal"><b>isJournal</b>(<i>manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#getFullJournalName"><b>getFullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isAnonymous"></a><small>Citation.</small>**[<ins>isAnonymous</ins>]({{ site.baseurl }}{{ page.url }}#isAnonymous)**():

Checks if the author is given as "[ANONYMOUS]" and returns `True` if so.

###### Returns

`bool`

 True if the author is ANONYMOUS otherwise `False`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getID"></a><small>Citation.</small>**[<ins>getID</ins>]({{ site.baseurl }}{{ page.url }}#getID)**():

Returns all of "author, year, journal" available. It is for shortening labels when creating networks as the resultant strings are often unique. [`getExtra()`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#getExtra) gets everything not returned by `getID()`.

This is also used for hashing and equality checking.

###### Returns

`str`

 A string to use as the shortened ID of a node.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getExtra"></a><small>Citation.</small>**[<ins>getExtra</ins>]({{ site.baseurl }}{{ page.url }}#getExtra)**():

Returns any V, P, DOI or misc values as a string. These are all the values not returned by [`getID()`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#getID).

###### Returns

`str`

 A string containing the data not in the ID of the Citation.
 


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isJournal"></a><small>Citation.</small>**[<ins>isJournal</ins>]({{ site.baseurl }}{{ page.url }}#isJournal)**(_manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False_):

Returns `True` if the Citation's journal field is a journal abbreviation given by WOS, i.e. checks if the citation is citing a journal. Requires the j9Abbreviations database file.

###### Returns

`bool`

 `True` if the Citation is for a journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getFullJournalName"></a><small>Citation.</small>**[<ins>getFullJournalName</ins>]({{ site.baseurl }}{{ page.url }}#getFullJournalName)**():

Returns the full name of the Citation's journal field. Requires the j9Abbreviations database file.

###### Returns

`str`

 The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then `None` is returned


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addToDB"></a><small>Citation.</small>**[<ins>addToDB</ins>]({{ site.baseurl }}{{ page.url }}#addToDB)**(_manualName=None, manaulDB='manualj9Abbreviations', invert=False_):

Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#isJournal) to return `True` for this Citation and all others with its `.journal`.

###### Parameters

_manualName_ : `optional [str]`

 Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

_manaulDB_ : `optional [str]`

 The name of the database file, the default is [metaknowledge.journalAbbreviations.manaulDBname]({{ site.baseurl }}{% post_url /docs/2015-11-05-journalAbbreviations %}#manaulDBname)

_invert_ : `optional [bool]`

 Default `False`, if `True` the journal will be removed instead of added



---
<a name="Record"></a>
<a name="Record"></a><small></small>**[<ins>Record</ins>](#Record)**(_inRecord, taglist=(), sFile='', sLine=0_):

Class for full WOS records

It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored in a private dictionary.

The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [getTag()](#getTag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

##### Customizations

The Record's hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with "WOS:" and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

When converted to a string the records title is used so for a record `R`, R.TI == R.title == str(R).

##### Attributes

When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [citations()](#citations) from the the [tagProcessing](#tagProcessing) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull](#metaknowledge)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

The attribute `authors` is also defined as a convience and returns the same as 'AF' or if that is not found 'AU'.

##### \_\_Init\_\_

Records are generally create as collections in  [Recordcollections](#RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

##### Parameters

_inRecord_: `files stream, dict, str or itertools.chain`

 If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

 If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser](#recordParser) returns.

 For a str the input is the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in 'ER'.

 itertools.chain is treated identically to a file stream and is used by [RecordCollections](#RecordCollection).

_sFile_ : `optional [str]`

 Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

_sLine_ : `optional [int]`

 Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.


The Record class has the following methods:

<ul class="post-list">
<li><article><a href="#numAuthors"><b>numAuthors</b>()</a></article></li>
<li><article><a href="#getTag"><b>getTag</b>(<i>tag, clean=False</i>)</a></article></li>
<li><article><a href="#createCitation"><b>createCitation</b>()</a></article></li>
<li><article><a href="#getTagsList"><b>getTagsList</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#getTagsDict"><b>getTagsDict</b>(<i>taglst, cleaned=False</i>)</a></article></li>
<li><article><a href="#activeTags"><b>activeTags</b>()</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="numAuthors"></a><small>Record.</small>**[<ins>numAuthors</ins>]({{ site.baseurl }}{{ page.url }}#numAuthors)**():

Returns the number of authors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTag"></a><small>Record.</small>**[<ins>getTag</ins>]({{ site.baseurl }}{{ page.url }}#getTag)**(_tag, clean=False_):

Returns a list containing the raw data of the record associated with _tag_. Each line of the record is one string in the list.

###### Parameters

_tag_ : `str`

 _tag_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag](#metaknowledge). If the string is not found in the original record or after being translated through [fullToTag](#metaknowledge), `None` is returned.

###### Returns

`List [str]`

 Each string in the list is a line from the record associated with _tag_ or None if not found.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="createCitation"></a><small>Record.</small>**[<ins>createCitation</ins>]({{ site.baseurl }}{{ page.url }}#createCitation)**():

Creates a citation string, using the same format as other WOS citations, for the [Record]({{ site.baseurl }}{% post_url /docs/2015-11-05-Record %}#Record) by reading the relevant tags (year, J9, volume, beginningPage, DOI) and using it to start a [Citation]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#Citation) object.

###### Returns

`Citation`

 A [Citation]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#Citation) object containing a citation for the Record.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTagsList"></a><small>Record.</small>**[<ins>getTagsList</ins>]({{ site.baseurl }}{{ page.url }}#getTagsList)**(_taglst, cleaned=False_):

Returns a list of the results of [`getTag()`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Record %}#getTag) for each tag in _taglist_, the return has the same order as the original.

###### Parameters
_taglst_ : `List[str]`

 Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#metaknowledge). If the string is not found in the original record before or after being translated through [fullToTag]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#metaknowledge), `None` is used instead. Same as in [`getTag()`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Record %}#getTag)

 Then they are compiled into a list in the same order as _taglst_

###### Returns

`List[str]`

 a list of the values for each tag in _taglst_, in the same order


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getTagsDict"></a><small>Record.</small>**[<ins>getTagsDict</ins>]({{ site.baseurl }}{{ page.url }}#getTagsDict)**(_taglst, cleaned=False_):

returns a dict of the results of getTag, with the elements of _taglst_ as the keys and the results as the values.

###### Parameters
_taglst_ : `List[str]`

 Each string in _taglst_ can be a two character string corresponding to a WOS tag e.g. 'J9', the matching is case insensitive so 'j9' is the same as 'J9'. Or it can be one of the full names for a tag with the mappings in [fullToTag]({{ site.baseurl }}{% post_url /docs/2015-11-05-metaknowledge %}#metaknowledge). If the string is not found in the oriagnal record before or after being translated through [fullToTag](#metaknowledge), `None` is used instead. Same as in [`getTag()`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Record %}#getTag)

###### Returns

`dict[str : List [str]]`

 a dictionary with keys as the original tags in _taglst_ and the values as the results


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="activeTags"></a><small>Record.</small>**[<ins>activeTags</ins>]({{ site.baseurl }}{{ page.url }}#activeTags)**():

Returns a list of all the tags the original WOS record had. These are all the tags that ['getTag()']({{ site.baseurl }}{% post_url /docs/2015-11-05-Record %}#getTag) will not return `None` for.

###### Returns

`List[str]`

 a list of WOS tags in the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>Record.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_infile_):

Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file. No newline is inserted above the write but the last character is a newline.

###### Parameters

_infile_ : `file stream`

 An open utf-8 encoded file



---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a><small></small>**[<ins>RecordCollection</ins>](#RecordCollection)**(_inCollection=None, name='', extension=''_):

A way of containing a large number of Record objects, it provides ways of creating them from an isi file, string, list of records or directory containing isi files. The Records are containing within a set and as such many of the set operations are defined, pop, union, in ... also records are hashed with their WOS string so no duplication can occur.
The comparison operators <, <=, >, >= are based strictly on the number of Records within the collection, while equality looks for an exact match on the Records

When being created if there are issues the Record collection will be declared bad (self.bad = True) it will then mostly return nothing or False. The error attribute contains the exception that occurred.

They also possess a name accessed with repr(), this is used to auto generate the names of files and can be set at creation, note though that any operations that modify the RecordCollection's contents will update the name to include what occurred, read __repr__'s doc string for more information

inCollection is the object containing the information about the Records to be constructed it can be an isi file, string, list of records or directory containing isi files

name sets the name of the of the record if left blank name will be generated based on the object that created the Recordcollection

extension controls the extension that __init__ looks for when reading a directory, set it to the extension on the isi files you wish to load, if left blank all files will be tried and any that are not isi files will be silently skipped

##### \_\_Init\_\_

RecordCollections are made from either a single file or directory supplied as _inCollection_.

##### Parameters

_inCollection_ : `optional [str] or None`

 the name of the source of WOS records. It can be skipped to produce an empty collection.

 If a file is provided. First it is checked to see if it is a WOS file (the header is checked). Then records are read from it one by one until the 'EF' string is found indicating the end of the file.

 If a directory is provided. First each file in the directory is checked for the correct header and all those that do are then read like indivual files. The records are then collected into a single set in the RecordCollection.

_name_ : `optional [str]`

 The name of the RecordCollection, defaults to empty string. If left empty the name of the Record collection is set to the name of the file or directory used to create the collection. If provided the name id set to _name_

_extension_ : `optional [str]`

 The extension to search for when reading a directoy for files. _extension_ is the suffix searched for when a direcorty is read for files, by default it is empty so all files are read.


The RecordCollection class has the following methods:

<ul class="post-list">
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
<li><article><a href="#makeDict"><b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><b>coAuthNetwork</b>()</a></article></li>
<li><article><a href="#coCiteNetwork"><b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None</i>)</a></article></li>
<li><article><a href="#citationNetwork"><b>citationNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None</i>)</a></article></li>
<li><article><a href="#yearSplit"><b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><b>nModeNetwork</b>(<i>tags, recordType=True, nodeCount=True, edgeWeight=True</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCiteStats"></a><small>RecordCollection.</small>**[<ins>localCiteStats</ins>]({{ site.baseurl }}{{ page.url }}#localCiteStats)**(_pandasFriendly=False, keyType='citation'_):

Returns a dict with all the citations in the CR field as keys and the number of times they occur as the values

###### Parameters

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one "Citations" is the citations the other is their occurence counts as "Counts".

_keyType_ : `optional [str]`

 default `'citation'`, the type of key to use for the dictionary, the valid strings are `"citation"`, `"journal"`, `"year"` or `"author"`

###### Returns

`dict[str, int or Citataion : int]`

 A dictioanry with keys as given by _keyType_ and integers giving their rates of occurnce in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="localCitesOf"></a><small>RecordCollection.</small>**[<ins>localCitesOf</ins>]({{ site.baseurl }}{{ page.url }}#localCitesOf)**(_rec_):

Takes in a Record, WOS string, citation string or Citation and returns a RecordCollection of all records that cite it.
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citeFilter"></a><small>RecordCollection.</small>**[<ins>citeFilter</ins>]({{ site.baseurl }}{{ page.url }}#citeFilter)**(_keyString='', field='all', reverse=False, caseSensitive=False_):

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pop"></a><small>RecordCollection.</small>**[<ins>pop</ins>]({{ site.baseurl }}{{ page.url }}#pop)**():

Returns a random Record from the recordCollection, the Record is deleted from the collection, use peak for nondestructive access


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="peak"></a><small>RecordCollection.</small>**[<ins>peak</ins>]({{ site.baseurl }}{{ page.url }}#peak)**():

Returns a random Record from the recordCollection, the Record is kept in the collection, use pop for faster destructive access


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropWOS"></a><small>RecordCollection.</small>**[<ins>dropWOS</ins>]({{ site.baseurl }}{{ page.url }}#dropWOS)**(_wosNum_):

Removes the Record with WOS number (ID number) _wosNum_

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the Record to be dropped. _wosNum_ must begin with 'WOS:' or a valueError is raise.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="addRec"></a><small>RecordCollection.</small>**[<ins>addRec</ins>]({{ site.baseurl }}{{ page.url }}#addRec)**(_Rec_):

Adds a Record or Records to the RecordCollection.

###### Parameters

_Rec_ : `Record or iterable[Record]`

 A Record or some iterable containg records to add


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getWOS"></a><small>RecordCollection.</small>**[<ins>getWOS</ins>]({{ site.baseurl }}{{ page.url }}#getWOS)**(_wosNum, drop=False_):

Gets the Record from the collection by its WOS number.

###### Parameters

_wosNum_ : `str`

 _wosNum_ is the WOS number of the Record to be extracted. _wosNum_ must begin with 'WOS:' or a valueError is raise.

_drop_ : `optional [bool]`

 Default `False`. If `True` the Record is dropped from the collection after being extract, i.e. if `False` [getWOS()]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#getWOS) acts like [peak()]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#peak), if `True` it acts like [pop()]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#pop)

###### Returns

`metaknowledge.Record`

 The Record whose WOS number is _wosNum_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getBadRecords"></a><small>RecordCollection.</small>**[<ins>getBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#getBadRecords)**():

returns RecordCollection containing all the Record which have their bad flag set to True, i.e. all those removed by dropBadRecords()


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropBadRecords"></a><small>RecordCollection.</small>**[<ins>dropBadRecords</ins>]({{ site.baseurl }}{{ page.url }}#dropBadRecords)**():

Removes all Records with bad attributes == True from the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropNonJournals"></a><small>RecordCollection.</small>**[<ins>dropNonJournals</ins>]({{ site.baseurl }}{{ page.url }}#dropNonJournals)**(_ptVal='J', dropBad=True, invert=False_):

Drops the non journal type Records from the collection

###### Parameters

_ptVal_ : `optional [str]`

 The value of the PT tag to be kept, default is 'J' the journal tag

_dropBad_ : `optional [bool]`

 Determines if bad Records will be dropped as well, default `True`

_invert_ : `optional [bool]`

 Set `True` to drop journals (or the PT tag given by _ptVal) instead of keeping them. Note, it still drops bad Records if _dropBad_ is `True`, default `False`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeFile"></a><small>RecordCollection.</small>**[<ins>writeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeFile)**(_fname=None_):

Writes the RecordCollection to a file, the written file is identical to those download from WOS. The order of Records written is random.

fname set the name of the file, if blank the RecordCollection's name's first 200 characters are use with the suffix .isi


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeCSV"></a><small>RecordCollection.</small>**[<ins>writeCSV</ins>]({{ site.baseurl }}{{ page.url }}#writeCSV)**(_fname=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

Writes all the Records from the collection into a csv file with each row a record and each column a tag

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="makeDict"></a><small>RecordCollection.</small>**[<ins>makeDict</ins>]({{ site.baseurl }}{{ page.url }}#makeDict)**(_onlyTheseTags=None, longNames=False, cleanedVal=True, numAuthors=True_):

Returns a dict with each key a tag and the values being lists of the values for each of the Records in the collection, `None` is given when there is no value and they are in the same order across each tag.

When used in pandas: `pandas.DataFrame(RC.makeDict())` returns a data frame with each column a tag and each row a Record.

###### Parameters

See writeCSV()


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coAuthNetwork"></a><small>RecordCollection.</small>**[<ins>coAuthNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coAuthNetwork)**():

Creates a coauthorship network for the RecordCollection.

###### Returns

`Networkx Graph`

 A networkx graph with author names as nodes and collaborations as edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="coCiteNetwork"></a><small>RecordCollection.</small>**[<ins>coCiteNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coCiteNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None_):

Creates a co-citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

###### Returns

`Networkx Graph`

 A networkx graph with hashes as ID and co-citation as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citationNetwork"></a><small>RecordCollection.</small>**[<ins>citationNetwork</ins>]({{ site.baseurl }}{{ page.url }}#citationNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None_):

Creates a citation network for the RecordCollection.

###### Parameters

_nodeType_ : `optional [str]`

 One of `"full"`, `"original"`, `"author"`, `"journal"` or `"year"`. Specifies the value of the nodes in the graph. The default `"full"` causes the citations to be compared holistically using the [`metaknowledge.Citation`]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#Citation) builtin comparison operators. `"original"` uses the raw original strings of the citations. While `"author"`, `"journal"` and `"year"` each use the author, journal and year respectively.

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

###### Returns

`Networkx DiGraph or Networkx Graph`

 See _directed_ for explanation of returned type

 A networkx digraph with hashes as ID and citations as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="yearSplit"></a><small>RecordCollection.</small>**[<ins>yearSplit</ins>]({{ site.baseurl }}{{ page.url }}#yearSplit)**(_startYear, endYear, dropMissingYears=True_):

Creates a RecordCollection of Records from the years between _startYear_ and _endYear_ inclusive.

###### Parameters

_startYear_ : `int`

 The smallest year to be included in the retuned RecordCollection

_endYear_ : `int`

 The largest year to be included in the retuned RecordCollection

_dropMissingYears_ : `optional [bool]`

 Default `True`, if `True` Records with missing years will be dropped. If `False` a `TypeError` exception will be raised

###### Returns

`RecordCollection`

 A RecordCollection of Records from _startYear_ to _endYear_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="oneModeNetwork"></a><small>RecordCollection.</small>**[<ins>oneModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#oneModeNetwork)**(_mode, nodeCount=True, edgeWeight=True_):

Creates a network of the objects found by one WOS tag _mode_.

A **oneModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tag given by _mode_, e.g. the `"AF"` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `"AF"` a co-authorship network is created.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

**Note** Do not use this for the construction of co-citation networks use [Recordcollection.coCiteNetwork()]({{ site.baseurl }}{% post_url /docs/2015-11-05-RecordCollection %}#coCiteNetwork) it is more accurate and has more options.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tag _mode_ as nodes and their co-occurrences as edges


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="twoModeNetwork"></a><small>RecordCollection.</small>**[<ins>twoModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#twoModeNetwork)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True_):

Creates a network of the objects found by two WOS tags _tag1_ and _tag2_.

A **twoModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tag1_ and _tag2_, e.g. the `"WC"` and `"LA"` tags. Then for each object returned by each tag and edge is created between it and every other object of the other tag. So the WOS defined subject tag `"WC"` and language tag `"LA"`, will give a two-mode network showing the connections between subjects and languages. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. the node `"English"` would have the type attribute be `"LA"`.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

The _directed_ parameter if `True` will cause the network to be directed with the first tag as the source and the second as the destination.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_directed_ : `optional [bool]`

 Default `False`, if `True` the returned network is directed

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

###### Returns

`networkx Graph or networkx DiGraph`

 A networkx Graph with the objects of the tags _tag1_ and _tag2_ as nodes and their co-occurrences as edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="nModeNetwork"></a><small>RecordCollection.</small>**[<ins>nModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#nModeNetwork)**(_tags, recordType=True, nodeCount=True, edgeWeight=True_):

Creates a network of the objects found by all WOS tags in _tags_.

A **nModeNetwork()** looks are each Record in the RecordCollection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `"type"` that gives the tag that created it or both if both created it, e.g. if `"LA"` were in _tags_ node `"English"` would have the type attribute be `"LA"`.

For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `"CR"` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

###### Parameters

_mode_ : `str`

 A two character WOS tag or one of the full names for a tag

_nodeCount_ : `optional [bool]`

 Default `True`, if `True` each node will have an attribute called "count" that contains an int giving the number of time the object occurred.

_edgeWeight_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute called "weight" that contains an int giving the number of time the two objects co-occurrenced.

###### Returns

`networkx Graph`

 A networkx Graph with the objects of the tags _tags_ as nodes and their co-occurrences as edges



---
<a name="visual"></a>

# [visual]({{ site.baseurl }}{{ page.url }}#visual)

visual docstring




The visual module provides the following functions:

<ul class="post-list">
<li><article><a href="#graphDensityContourPlot"><b>graphDensityContourPlot</b>(<i>G, layout=None, layoutScaleFactor=1, shifAxis=False, overlay=False, axisSamples=100, blurringFactor=0.1, contours=15, nodeSize=10, graphType='coloured', iters=50</i>)</a></article></li>
<li><article><a href="#quickVisual"><b>quickVisual</b>(<i>G, showLabel=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphDensityContourPlot"></a><small>visual.</small>**[<ins>graphDensityContourPlot</ins>]({{ site.baseurl }}{{ page.url }}#graphDensityContourPlot)**(_G, layout=None, layoutScaleFactor=1, shifAxis=False, overlay=False, axisSamples=100, blurringFactor=0.1, contours=15, nodeSize=10, graphType='coloured', iters=50_):

Requires numpy and matplotlib

graphType is either "coloured or "solid"


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="quickVisual"></a><small>visual.</small>**[<ins>quickVisual</ins>]({{ site.baseurl }}{{ page.url }}#quickVisual)**(_G, showLabel=False_):

just makes a simple matplotlib figure and displays it, with each node coloured by its type



---
<a name="journalAbbreviations"></a>

# [journalAbbreviations]({{ site.baseurl }}{{ page.url }}#journalAbbreviations)






The journalAbbreviations module provides the following functions:

<ul class="post-list">
<li><article><a href="#getj9dict"><b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#excludeFromDB"><b>excludeFromDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
<li><article><a href="#updatej9DB"><b>updatej9DB</b>(<i>dbname='j9Abbreviations', saveRawHTML=False</i>)</a></article></li>
</ul>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getj9dict"></a><small>journalAbbreviations.</small>**[<ins>getj9dict</ins>]({{ site.baseurl }}{{ page.url }}#getj9dict)**(_dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'_):

Returns the dictionary of journal abbreviations to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

###### Parameters

_dbname_ : `optional [str]`

 The name of the database file


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

Marks _abbr_ to be excluded the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manaulDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

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

The function to process it is called [`title()`](#title) which is determined by looking up the tag in the `tagProcessing.tagToFunc` dictionary. Which is a dictionary mapping WOS tag strings to their functions. For a simple mapping of tags to their long strings use [`metaknowledge.tagToFull`](#metaknowledge).

The objects `tagToFullDict`, `fullToTagDict`, `tagNameConverterDict`, `tagsAndNameSet` and `knownTagsList` are also provided. They are the objects used by metaknowledge to keep track of tag names. `tagToFullDict` and `fullToTagDict` are dictionaries that convert from tags to full names and vice versa, respectively, while `tagNameConverterDict` goes both ways. `tagsAndNameSet` is a set of all full names and tags, while `knownTagsList` contains only tags and is a list. For a less raw interface look the functions provided by the base metaknowledge module, e.g. [`tagToFull()`](#tagToFull).

The full list of tags and their long names is provided below followed by the descriptions of the functions, they are ordered by their occurrence in WOS records:

| tag | Name |
|:---|:---|
| `'EM'` |[email]({{ site.baseurl }}{{ page.url }}#tagProcessing.email)
| `'BS'` |[seriesSubtitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.seriesSubtitle)
| `'VL'` |[volume]({{ site.baseurl }}{{ page.url }}#tagProcessing.volume)
| `'SO'` |[journal]({{ site.baseurl }}{{ page.url }}#tagProcessing.journal)
| `'PM'` |[pubMedID]({{ site.baseurl }}{{ page.url }}#tagProcessing.pubMedID)
| `'RP'` |[reprintAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.reprintAddress)
| `'PU'` |[publisher]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisher)
| `'GP'` |[group]({{ site.baseurl }}{{ page.url }}#tagProcessing.group)
| `'J9'` |[j9]({{ site.baseurl }}{{ page.url }}#tagProcessing.j9)
| `'CR'` |[citations]({{ site.baseurl }}{{ page.url }}#tagProcessing.citations)
| `'EP'` |[endingPage]({{ site.baseurl }}{{ page.url }}#tagProcessing.endingPage)
| `'C1'` |[authAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.authAddress)
| `'UT'` |[wosString]({{ site.baseurl }}{{ page.url }}#tagProcessing.wosString)
| `'Z9'` |[totalTimesCited]({{ site.baseurl }}{{ page.url }}#tagProcessing.totalTimesCited)
| `'ID'` |[keyWords]({{ site.baseurl }}{{ page.url }}#tagProcessing.keyWords)
| `'PY'` |[year]({{ site.baseurl }}{{ page.url }}#tagProcessing.year)
| `'RI'` |[ResearcherIDnumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.ResearcherIDnumber)
| `'EI'` |[eISSN]({{ site.baseurl }}{{ page.url }}#tagProcessing.eISSN)
| `'BF'` |[bookAuthorFull]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookAuthorFull)
| `'BN'` |[ISBN]({{ site.baseurl }}{{ page.url }}#tagProcessing.ISBN)
| `'BP'` |[beginningPage]({{ site.baseurl }}{{ page.url }}#tagProcessing.beginningPage)
| `'AR'` |[articleNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.articleNumber)
| `'SU'` |[supplement]({{ site.baseurl }}{{ page.url }}#tagProcessing.supplement)
| `'NR'` |[citedRefsCount]({{ site.baseurl }}{{ page.url }}#tagProcessing.citedRefsCount)
| `'LA'` |[language]({{ site.baseurl }}{{ page.url }}#tagProcessing.language)
| `'BA'` |[bookAuthor]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookAuthor)
| `'SN'` |[ISSN]({{ site.baseurl }}{{ page.url }}#tagProcessing.ISSN)
| `'CA'` |[groupName]({{ site.baseurl }}{{ page.url }}#tagProcessing.groupName)
| `'D2'` |[bookDOI]({{ site.baseurl }}{{ page.url }}#tagProcessing.bookDOI)
| `'PA'` |[publisherAddress]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisherAddress)
| `'TC'` |[wosTimesCited]({{ site.baseurl }}{{ page.url }}#tagProcessing.wosTimesCited)
| `'OI'` |[orcID]({{ site.baseurl }}{{ page.url }}#tagProcessing.orcID)
| `'GA'` |[documentDeliveryNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.documentDeliveryNumber)
| `'AU'` |[authorsShort]({{ site.baseurl }}{{ page.url }}#tagProcessing.authorsShort)
| `'PG'` |[pageCount]({{ site.baseurl }}{{ page.url }}#tagProcessing.pageCount)
| `'SI'` |[specialIssue]({{ site.baseurl }}{{ page.url }}#tagProcessing.specialIssue)
| `'WC'` |[subjects]({{ site.baseurl }}{{ page.url }}#tagProcessing.subjects)
| `'CL'` |[confLocation]({{ site.baseurl }}{{ page.url }}#tagProcessing.confLocation)
| `'SP'` |[confSponsors]({{ site.baseurl }}{{ page.url }}#tagProcessing.confSponsors)
| `'PT'` |[pubType]({{ site.baseurl }}{{ page.url }}#tagProcessing.pubType)
| `'AB'` |[abstract]({{ site.baseurl }}{{ page.url }}#tagProcessing.abstract)
| `'BE'` |[editedBy]({{ site.baseurl }}{{ page.url }}#tagProcessing.editedBy)
| `'PI'` |[publisherCity]({{ site.baseurl }}{{ page.url }}#tagProcessing.publisherCity)
| `'HO'` |[confHost]({{ site.baseurl }}{{ page.url }}#tagProcessing.confHost)
| `'DI'` |[DOI]({{ site.baseurl }}{{ page.url }}#tagProcessing.DOI)
| `'AF'` |[authorsFull]({{ site.baseurl }}{{ page.url }}#tagProcessing.authorsFull)
| `'TI'` |[title]({{ site.baseurl }}{{ page.url }}#tagProcessing.title)
| `'SC'` |[subjectCategory]({{ site.baseurl }}{{ page.url }}#tagProcessing.subjectCategory)
| `'FX'` |[fundingText]({{ site.baseurl }}{{ page.url }}#tagProcessing.fundingText)
| `'DT'` |[docType]({{ site.baseurl }}{{ page.url }}#tagProcessing.docType)
| `'CT'` |[confTitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.confTitle)
| `'IS'` |[issue]({{ site.baseurl }}{{ page.url }}#tagProcessing.issue)
| `'PD'` |[month]({{ site.baseurl }}{{ page.url }}#tagProcessing.month)
| `'JI'` |[isoAbbreviation]({{ site.baseurl }}{{ page.url }}#tagProcessing.isoAbbreviation)
| `'CY'` |[confDate]({{ site.baseurl }}{{ page.url }}#tagProcessing.confDate)
| `'DE'` |[authKeyWords]({{ site.baseurl }}{{ page.url }}#tagProcessing.authKeyWords)
| `'FU'` |[funding]({{ site.baseurl }}{{ page.url }}#tagProcessing.funding)
| `'PN'` |[partNumber]({{ site.baseurl }}{{ page.url }}#tagProcessing.partNumber)
| `'ED'` |[editors]({{ site.baseurl }}{{ page.url }}#tagProcessing.editors)
| `'SE'` |[seriesTitle]({{ site.baseurl }}{{ page.url }}#tagProcessing.seriesTitle)
| `'MA'` |[meetingAbstract]({{ site.baseurl }}{{ page.url }}#tagProcessing.meetingAbstract)




<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getMonth"></a><small>tagProcessing.</small>**[<ins>getMonth</ins>]({{ site.baseurl }}{{ page.url }}#getMonth)**(_s_):

Known formats:
Month ("%b")
Month Day ("%b %d")
Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
Season ("%s") --- this gets coerced to use the first month of the given season
Month Day Year ("%b %d %Y")
Month Year ("%b %Y")


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

<a name="pubMedID"></a><small>tagProcessing.</small>**[<ins>pubMedID</ins>]({{ site.baseurl }}{{ page.url }}#pubMedID)**(_val_):

######The PM Tag

extracts the pubmed ID of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The pubmed ID


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

<a name="editors"></a><small>tagProcessing.</small>**[<ins>editors</ins>]({{ site.baseurl }}{{ page.url }}#editors)**(_val_):

###### Needs Work

currently not well understood, returns _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="journal"></a><small>tagProcessing.</small>**[<ins>journal</ins>]({{ site.baseurl }}{{ page.url }}#journal)**(_val_):

######The SO Tag

extracts the full name of the publication

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

<a name="citations"></a><small>tagProcessing.</small>**[<ins>citations</ins>]({{ site.baseurl }}{{ page.url }}#citations)**(_val_):

######The CR Tag

extracts a list of all the citations in the record, the citations are the [metaknowledge.Citation]({{ site.baseurl }}{% post_url /docs/2015-11-05-Citation %}#Citation) class.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

` list[metaknowledge.Citation]`

 A list of Citations


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

<a name="supplement"></a><small>tagProcessing.</small>**[<ins>supplement</ins>]({{ site.baseurl }}{{ page.url }}#supplement)**(_val_):

######The SU Tag

extracts the supplement number

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The supplement number



{% include docsFooter.md %}