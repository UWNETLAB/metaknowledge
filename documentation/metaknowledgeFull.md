---
layout: page
title: Full Documentation 2.1.1
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
<h3><a name="objlist"></a>The modules of <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><a href="#contour"><b>contour</b><span class="excerpt">A nicer matplotlib graph visualizer and contour plot</span></a></article></li>
<li><article><a href="#WOS"><b>WOS</b><span class="excerpt">The backend functions and classes associated with the Web of Science</span></a></article></li>
<li><article><a href="#medline"><b>medline</b><span class="excerpt">The backend functions and classes associated with Medline, the format used by Pubmed</span></a></article></li>
<li><article><a href="#proquest"><b>proquest</b><span class="excerpt">The backend functions and classes associated with ProQuest</span></a></article></li>
<li><article><a href="#scopus"><b>scopus</b><span class="excerpt">The backend functions and classes associated with records from scopus</span></a></article></li>
<li><article><a href="#journalAbbreviations"><b>journalAbbreviations</b><span class="excerpt">Handles the abbreviated journal names used by WOS</span></a></article></li>
</ol>
<h3><a name="objlist"></a>The classes of <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><a href="#WOSRecord"><b>WOSRecord</b></a>(<i><a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a></i>)<span class="excerpt">The object for containing and processing WOS entries</span></article></li>
<li><article><a href="#Citation"><b>Citation</b></a>(<i>Hashable</i>)<span class="excerpt">Citation are special, here is how they are handled</span></article></li>
<li><article><a href="#GrantCollection"><b>GrantCollection</b></a>(<i><a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a></i>)<span class="excerpt">A Collection of Grants, this is what does most of the stuff on Grants</span></article></li>
<li><article><a href="#Grant"><b>Grant</b></a>(<i><a href="#Record"><u style="border-bottom: .5px dashed gray;">Record</u></a>, MutableMapping</i>)<span class="excerpt">The base for all the other Grants</span></article></li>
<li><article><a href="#DefaultGrant"><b>DefaultGrant</b></a>(<i><a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a></i>)<span class="excerpt">The Grant used if a file was not identifiable</span></article></li>
<li><article><a href="#CIHRGrant"><b>CIHRGrant</b></a>(<i><a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a></i>)<span class="excerpt">The container for CIHR grant entries</span></article></li>
<li><article><a href="#MedlineGrant"><b>MedlineGrant</b></a>(<i><a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a></i>)<span class="excerpt">The container for grants derived from Medline Records entries</span></article></li>
<li><article><a href="#NSERCGrant"><b>NSERCGrant</b></a>(<i><a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a></i>)<span class="excerpt">The container for NSERC grant entries</span></article></li>
<li><article><a href="#NSFGrant"><b>NSFGrant</b></a>(<i><a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a></i>)<span class="excerpt">The container for NSF grant entries</span></article></li>
<li><article><a href="#MedlineRecord"><b>MedlineRecord</b></a>(<i><a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a></i>)<span class="excerpt">The object for containing and processing Medline entries</span></article></li>
<li><article><a href="#Collection"><b>Collection</b></a>(<i>MutableSet, Hashable</i>)<span class="excerpt">The base of all other Collections, basically a set</span></article></li>
<li><article><a href="#CollectionWithIDs"><b>CollectionWithIDs</b></a>(<i><a href="#Collection"><u style="border-bottom: .5px dashed gray;">Collection</u></a></i>)<span class="excerpt">A Collection that only holds <i>metaknowledge</i> objects</span></article></li>
<li><article><a href="#ExtendedRecord"><b>ExtendedRecord</b></a>(<i><a href="#Record"><u style="border-bottom: .5px dashed gray;">Record</u></a></i>)<span class="excerpt">A Record the processes its contents before returning them</span></article></li>
<li><article><a href="#Record"><b>Record</b></a>(<i>Mapping, Hashable</i>)<span class="excerpt">The base of all the other Records, basically a dict</span></article></li>
<li><article><a href="#ProQuestRecord"><b>ProQuestRecord</b></a>(<i><a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a></i>)<span class="excerpt">The object for containing and processing ProQuest entries</span></article></li>
<li><article><a href="#RecordCollection"><b>RecordCollection</b></a>(<i><a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a></i>)<span class="excerpt">A Collection of Records, this is what does most of the stuff on Records</span></article></li>
<li><article><a href="#ScopusRecord"><b>ScopusRecord</b></a>(<i><a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a></i>)<span class="excerpt">The object for containing and processing Scopus entries</span></article></li>
</ol>
<h3><a name="fulllist"></a>All the functions and methods of <i>metaknowledge</i> and its objects are as follows:</h3>

<ol class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, weighted=True, sourceType='raw', targetType='raw', labelEdgesBy=None</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', extraValue=None, pandasFriendly=False, compareCounts=False, numAuthors=True, useAllAuthors=True, extraMapping=None</i>)</a></article></li>
<li><article><a href="#diffusionAddCountsFromSource"><b>diffusionAddCountsFromSource</b>(<i>grph, source, target, nodeType='citations', extraType=None, diffusionLabel='DiffusionCount', extraKeys=None, countsDict=None, extraMapping=None</i>)</a></article></li>
<li><article><a href="#readGraph"><b>readGraph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#writeEdgeList"><b>writeEdgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeNodeAttributeFile"><b>writeNodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeTnetFile"><b>writeTnetFile</b>(<i>grph, name, modeNameString, weighted=False, sourceMode=None, timeString=None, nodeIndexString='tnet-ID', weightString='weight'</i>)</a></article></li>
<li><article><a href="#dropEdges"><b>dropEdges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#dropNodesByDegree"><b>dropNodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True</i>)</a></article></li>
<li><article><a href="#dropNodesByCount"><b>dropNodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#mergeGraphs"><b>mergeGraphs</b>(<i>targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True</i>)</a></article></li>
<li><article><a href="#writeGraph"><b>writeGraph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><small>WOSRecord</small>.<b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><small>WOSRecord</small>.<b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><small>WOSRecord</small>.<b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#bibString"><small>WOSRecord</small>.<b>bibString</b>(<i>maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True</i>)</a></article></li>
<li><article><a href="#bibTexType"><small>WOSRecord</small>.<b>bibTexType</b>()</a></article></li>
<li><article><a href="#encoding"><small>WOSRecord</small>.<b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><small>WOSRecord</small>.<b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#isAnonymous"><small>Citation</small>.<b>isAnonymous</b>()</a></article></li>
<li><article><a href="#ID"><small>Citation</small>.<b>ID</b>()</a></article></li>
<li><article><a href="#allButDOI"><small>Citation</small>.<b>allButDOI</b>()</a></article></li>
<li><article><a href="#Extra"><small>Citation</small>.<b>Extra</b>()</a></article></li>
<li><article><a href="#isJournal"><small>Citation</small>.<b>isJournal</b>(<i>dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#FullJournalName"><small>Citation</small>.<b>FullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><small>Citation</small>.<b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
<li><article><a href="#update"><small>Grant</small>.<b>update</b>(<i>other</i>)</a></article></li>
<li><article><a href="#pop"><small>Grant</small>.<b>pop</b>(<i>key, default=<object object at 0x10519a050></i>)</a></article></li>
<li><article><a href="#popitem"><small>Grant</small>.<b>popitem</b>()</a></article></li>
<li><article><a href="#clear"><small>Grant</small>.<b>clear</b>()</a></article></li>
<li><article><a href="#setdefault"><small>Grant</small>.<b>setdefault</b>(<i>key, default=None</i>)</a></article></li>
<li><article><a href="#encoding"><small>MedlineRecord</small>.<b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><small>MedlineRecord</small>.<b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><small>MedlineRecord</small>.<b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><small>MedlineRecord</small>.<b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><small>MedlineRecord</small>.<b>writeRecord</b>(<i>f</i>)</a></article></li>
<li><article><a href="#add"><small>Collection</small>.<b>add</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#discard"><small>Collection</small>.<b>discard</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#remove"><small>Collection</small>.<b>remove</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#clear"><small>Collection</small>.<b>clear</b>()</a></article></li>
<li><article><a href="#pop"><small>Collection</small>.<b>pop</b>()</a></article></li>
<li><article><a href="#copy"><small>Collection</small>.<b>copy</b>()</a></article></li>
<li><article><a href="#peek"><small>Collection</small>.<b>peek</b>()</a></article></li>
<li><article><a href="#chunk"><small>Collection</small>.<b>chunk</b>(<i>maxSize</i>)</a></article></li>
<li><article><a href="#split"><small>Collection</small>.<b>split</b>(<i>maxSize</i>)</a></article></li>
<li><article><a href="#containsID"><small>CollectionWithIDs</small>.<b>containsID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#discardID"><small>CollectionWithIDs</small>.<b>discardID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#removeID"><small>CollectionWithIDs</small>.<b>removeID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#getID"><small>CollectionWithIDs</small>.<b>getID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#badEntries"><small>CollectionWithIDs</small>.<b>badEntries</b>()</a></article></li>
<li><article><a href="#dropBadEntries"><small>CollectionWithIDs</small>.<b>dropBadEntries</b>()</a></article></li>
<li><article><a href="#tags"><small>CollectionWithIDs</small>.<b>tags</b>()</a></article></li>
<li><article><a href="#cooccurrenceCounts"><small>CollectionWithIDs</small>.<b>cooccurrenceCounts</b>(<i>keyTag, *countedTags</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><small>CollectionWithIDs</small>.<b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><small>CollectionWithIDs</small>.<b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><small>CollectionWithIDs</small>.<b>nModeNetwork</b>(<i>*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None</i>)</a></article></li>
<li><article><a href="#get"><small>ExtendedRecord</small>.<b>get</b>(<i>tag, default=None, raw=False</i>)</a></article></li>
<li><article><a href="#values"><small>ExtendedRecord</small>.<b>values</b>(<i>raw=False</i>)</a></article></li>
<li><article><a href="#items"><small>ExtendedRecord</small>.<b>items</b>(<i>raw=False</i>)</a></article></li>
<li><article><a href="#writeRecord"><small>ExtendedRecord</small>.<b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#encoding"><small>ExtendedRecord</small>.<b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><small>ExtendedRecord</small>.<b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><small>ExtendedRecord</small>.<b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><small>ExtendedRecord</small>.<b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#subDict"><small>ExtendedRecord</small>.<b>subDict</b>(<i>tags, raw=False</i>)</a></article></li>
<li><article><a href="#createCitation"><small>ExtendedRecord</small>.<b>createCitation</b>(<i>multiCite=False</i>)</a></article></li>
<li><article><a href="#copy"><small>Record</small>.<b>copy</b>()</a></article></li>
<li><article><a href="#encoding"><small>ProQuestRecord</small>.<b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><small>ProQuestRecord</small>.<b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><small>ProQuestRecord</small>.<b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><small>ProQuestRecord</small>.<b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><small>ProQuestRecord</small>.<b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#dropNonJournals"><small>RecordCollection</small>.<b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><small>RecordCollection</small>.<b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><small>RecordCollection</small>.<b>writeCSV</b>(<i>fname=None, splitByTag=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#writeBib"><small>RecordCollection</small>.<b>writeBib</b>(<i>fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True</i>)</a></article></li>
<li><article><a href="#makeDict"><small>RecordCollection</small>.<b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, raw=False, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><small>RecordCollection</small>.<b>coAuthNetwork</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
<li><article><a href="#coCiteNetwork"><small>RecordCollection</small>.<b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#citationNetwork"><small>RecordCollection</small>.<b>citationNetwork</b>(<i>dropAnon=False, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False, recordToCite=True</i>)</a></article></li>
<li><article><a href="#yearSplit"><small>RecordCollection</small>.<b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#localCiteStats"><small>RecordCollection</small>.<b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><small>RecordCollection</small>.<b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><small>RecordCollection</small>.<b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
<li><article><a href="#encoding"><small>ScopusRecord</small>.<b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><small>ScopusRecord</small>.<b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><small>ScopusRecord</small>.<b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><small>ScopusRecord</small>.<b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><small>ScopusRecord</small>.<b>writeRecord</b>(<i>f</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#contour"><u>contour</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#graphDensityContourPlot"><small>contour</small>.<b>graphDensityContourPlot</b>(<i>G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'</i>)</a></article></li>
<li><article><a href="#quickVisual"><small>contour</small>.<b>quickVisual</b>(<i>G, showLabel=False</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#WOS"><u>WOS</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#recordParser"><small>WOS</small>.<b>recordParser</b>(<i>paper</i>)</a></article></li>
<li><article><a href="#getMonth"><small>WOS</small>.<b>getMonth</b>(<i>s</i>)</a></article></li>
<li><article><a href="#confHost"><small>WOS</small>.<b>confHost</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherAddress"><small>WOS</small>.<b>publisherAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#endingPage"><small>WOS</small>.<b>endingPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#year"><small>WOS</small>.<b>year</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authKeywords"><small>WOS</small>.<b>authKeywords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#reprintAddress"><small>WOS</small>.<b>reprintAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthor"><small>WOS</small>.<b>bookAuthor</b>(<i>val</i>)</a></article></li>
<li><article><a href="#totalTimesCited"><small>WOS</small>.<b>totalTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#partNumber"><small>WOS</small>.<b>partNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#specialIssue"><small>WOS</small>.<b>specialIssue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjects"><small>WOS</small>.<b>subjects</b>(<i>val</i>)</a></article></li>
<li><article><a href="#keywords"><small>WOS</small>.<b>keywords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubMedID"><small>WOS</small>.<b>pubMedID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#documentDeliveryNumber"><small>WOS</small>.<b>documentDeliveryNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthorFull"><small>WOS</small>.<b>bookAuthorFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#groupName"><small>WOS</small>.<b>groupName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#title"><small>WOS</small>.<b>title</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editors"><small>WOS</small>.<b>editors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#journal"><small>WOS</small>.<b>journal</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesTitle"><small>WOS</small>.<b>seriesTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesSubtitle"><small>WOS</small>.<b>seriesSubtitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#language"><small>WOS</small>.<b>language</b>(<i>val</i>)</a></article></li>
<li><article><a href="#docType"><small>WOS</small>.<b>docType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsFull"><small>WOS</small>.<b>authorsFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confTitle"><small>WOS</small>.<b>confTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confDate"><small>WOS</small>.<b>confDate</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confSponsors"><small>WOS</small>.<b>confSponsors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosTimesCited"><small>WOS</small>.<b>wosTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authAddress"><small>WOS</small>.<b>authAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confLocation"><small>WOS</small>.<b>confLocation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#j9"><small>WOS</small>.<b>j9</b>(<i>val</i>)</a></article></li>
<li><article><a href="#funding"><small>WOS</small>.<b>funding</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjectCategory"><small>WOS</small>.<b>subjectCategory</b>(<i>val</i>)</a></article></li>
<li><article><a href="#group"><small>WOS</small>.<b>group</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citations"><small>WOS</small>.<b>citations</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherCity"><small>WOS</small>.<b>publisherCity</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISSN"><small>WOS</small>.<b>ISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#articleNumber"><small>WOS</small>.<b>articleNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#issue"><small>WOS</small>.<b>issue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#email"><small>WOS</small>.<b>email</b>(<i>val</i>)</a></article></li>
<li><article><a href="#eISSN"><small>WOS</small>.<b>eISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DOI"><small>WOS</small>.<b>DOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosString"><small>WOS</small>.<b>wosString</b>(<i>val</i>)</a></article></li>
<li><article><a href="#orcID"><small>WOS</small>.<b>orcID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubType"><small>WOS</small>.<b>pubType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editedBy"><small>WOS</small>.<b>editedBy</b>(<i>val</i>)</a></article></li>
<li><article><a href="#meetingAbstract"><small>WOS</small>.<b>meetingAbstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isoAbbreviation"><small>WOS</small>.<b>isoAbbreviation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pageCount"><small>WOS</small>.<b>pageCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisher"><small>WOS</small>.<b>publisher</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><small>WOS</small>.<b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#month"><small>WOS</small>.<b>month</b>(<i>val</i>)</a></article></li>
<li><article><a href="#fundingText"><small>WOS</small>.<b>fundingText</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookDOI"><small>WOS</small>.<b>bookDOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#volume"><small>WOS</small>.<b>volume</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ResearcherIDnumber"><small>WOS</small>.<b>ResearcherIDnumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsShort"><small>WOS</small>.<b>authorsShort</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citedRefsCount"><small>WOS</small>.<b>citedRefsCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#beginningPage"><small>WOS</small>.<b>beginningPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#abstract"><small>WOS</small>.<b>abstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#supplement"><small>WOS</small>.<b>supplement</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosParser"><small>WOS</small>.<b>wosParser</b>(<i>isifile</i>)</a></article></li>
<li><article><a href="#isWOSFile"><small>WOS</small>.<b>isWOSFile</b>(<i>infile, checkedLines=3</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#medline"><u>medline</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#medlineParser"><small>medline</small>.<b>medlineParser</b>(<i>pubFile</i>)</a></article></li>
<li><article><a href="#isMedlineFile"><small>medline</small>.<b>isMedlineFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
<li><article><a href="#medlineRecordParser"><small>medline</small>.<b>medlineRecordParser</b>(<i>record</i>)</a></article></li>
<li><article><a href="#FPS"><small>medline</small>.<b>FPS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TT"><small>medline</small>.<b>TT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PROF"><small>medline</small>.<b>PROF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PHST"><small>medline</small>.<b>PHST</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EFR"><small>medline</small>.<b>EFR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PST"><small>medline</small>.<b>PST</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SPIN"><small>medline</small>.<b>SPIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AU"><small>medline</small>.<b>AU</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FED"><small>medline</small>.<b>FED</b>(<i>val</i>)</a></article></li>
<li><article><a href="#NM"><small>medline</small>.<b>NM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SO"><small>medline</small>.<b>SO</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IP"><small>medline</small>.<b>IP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OABL"><small>medline</small>.<b>OABL</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PUBM"><small>medline</small>.<b>PUBM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRDT"><small>medline</small>.<b>CRDT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DDIN"><small>medline</small>.<b>DDIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MH"><small>medline</small>.<b>MH</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DP"><small>medline</small>.<b>DP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GN"><small>medline</small>.<b>GN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRF"><small>medline</small>.<b>CRF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TI"><small>medline</small>.<b>TI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRI"><small>medline</small>.<b>CRI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OT"><small>medline</small>.<b>OT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ROF"><small>medline</small>.<b>ROF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CN"><small>medline</small>.<b>CN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OTO"><small>medline</small>.<b>OTO</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OID"><small>medline</small>.<b>OID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PT"><small>medline</small>.<b>PT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RPI"><small>medline</small>.<b>RPI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AB"><small>medline</small>.<b>AB</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EN"><small>medline</small>.<b>EN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AD"><small>medline</small>.<b>AD</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LA"><small>medline</small>.<b>LA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MHDA"><small>medline</small>.<b>MHDA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TA"><small>medline</small>.<b>TA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#JT"><small>medline</small>.<b>JT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IRAD"><small>medline</small>.<b>IRAD</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PS"><small>medline</small>.<b>PS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IS"><small>medline</small>.<b>IS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PL"><small>medline</small>.<b>PL</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CTI"><small>medline</small>.<b>CTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FAU"><small>medline</small>.<b>FAU</b>(<i>val</i>)</a></article></li>
<li><article><a href="#VTI"><small>medline</small>.<b>VTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DCOM"><small>medline</small>.<b>DCOM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LID"><small>medline</small>.<b>LID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#BTI"><small>medline</small>.<b>BTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CI"><small>medline</small>.<b>CI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#STAT"><small>medline</small>.<b>STAT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DRIN"><small>medline</small>.<b>DRIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RF"><small>medline</small>.<b>RF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#UIN"><small>medline</small>.<b>UIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LR"><small>medline</small>.<b>LR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IR"><small>medline</small>.<b>IR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SFM"><small>medline</small>.<b>SFM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EIN"><small>medline</small>.<b>EIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AID"><small>medline</small>.<b>AID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EDAT"><small>medline</small>.<b>EDAT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PRIN"><small>medline</small>.<b>PRIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DEP"><small>medline</small>.<b>DEP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AUID"><small>medline</small>.<b>AUID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SI"><small>medline</small>.<b>SI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><small>medline</small>.<b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RN"><small>medline</small>.<b>RN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#JID"><small>medline</small>.<b>JID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GR"><small>medline</small>.<b>GR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OCI"><small>medline</small>.<b>OCI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SB"><small>medline</small>.<b>SB</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DA"><small>medline</small>.<b>DA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMCR"><small>medline</small>.<b>PMCR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PG"><small>medline</small>.<b>PG</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GS"><small>medline</small>.<b>GS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#VI"><small>medline</small>.<b>VI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#UOF"><small>medline</small>.<b>UOF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FIR"><small>medline</small>.<b>FIR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OWN"><small>medline</small>.<b>OWN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ORI"><small>medline</small>.<b>ORI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MID"><small>medline</small>.<b>MID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMID"><small>medline</small>.<b>PMID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMC"><small>medline</small>.<b>PMC</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RIN"><small>medline</small>.<b>RIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RPF"><small>medline</small>.<b>RPF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CIN"><small>medline</small>.<b>CIN</b>(<i>val</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#proquest"><u>proquest</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#proQuestParser"><small>proquest</small>.<b>proQuestParser</b>(<i>proFile</i>)</a></article></li>
<li><article><a href="#isProQuestFile"><small>proquest</small>.<b>isProQuestFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
<li><article><a href="#proQuestRecordParser"><small>proquest</small>.<b>proQuestRecordParser</b>(<i>enRecordFile, recNum</i>)</a></article></li>
<li><article><a href="#proQuestTagToFunc"><small>proquest</small>.<b>proQuestTagToFunc</b>(<i>tag</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#scopus"><u>scopus</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#scopusRecordParser"><small>scopus</small>.<b>scopusRecordParser</b>(<i>record</i>)</a></article></li>
<li><article><a href="#scopusParser"><small>scopus</small>.<b>scopusParser</b>(<i>scopusFile</i>)</a></article></li>
<li><article><a href="#isScopusFile"><small>scopus</small>.<b>isScopusFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
</ol>
<h3>All the functions of the <a href="#journalAbbreviations"><u>journalAbbreviations</u></a> module are as follows:</h3>

<ol class="post-list">
<li><article><a href="#getj9dict"><small>journalAbbreviations</small>.<b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><small>journalAbbreviations</small>.<b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
</ol>

---
<a name="Overview"></a>
_metaknowledge_ is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

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
    >>> mk.writeGraph(G, "Cocitation-Network-of-Journals")

There is also a simple command line program called `metaknowledge` that comes with the package. It allows for creating networks without any need to know Python. More information about it can be found at [networkslab.org/metaknowledge/cli]({{ site.baseurl }}/cli)

#### Overview

This package can read the files downloaded from the Thomson Reuters' [Web of Science](https://webofknowledge.com) (_WOS_), Elsevier's [Scopus](https://www.scopus.com/), [ProQuest](www.proquest.com/) and Medline files from [PubMed](www.ncbi.nlm.nih.gov/pubmed). These files contain entries on the metadata of scientific records, such as authors, title, and citations. _metaknowledge_ can also read grants from various organizations including _NSF_ and _NSERC_ which are handled similarly to records.

The [metaknowledge.RecordCollection](#RecordCollection) class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the [metaknowledge.Record](#Record) class that contains the results of the parsing of the record.

The files read by _metaknowledge_ are a databases containing a series of tags (implicitly or explicitly), e.g. `'TI'` is the title for WOS. Each tag has one or more values and metaknowledge can read them and extract useful information. As the tags differ between providers a small set of values can be accessed by special tags, the tags are listed in `specialRecordFields`. These special tags can act on the whole `Record` and as such may contain information provided by any number of other tags.

Citations are handled by a special [Citation](#Citation) class. This class can parse the citations given by _WOS_ and journals cited by _Scopus_ and allows for better comparisons when they are used in graphs.

Note for those reading the docstrings metaknowledge's docs are written in markdown and are processed to produce the documentation found at [networkslab.org/metaknowledge/documentation]({{ site.baseurl }}/documentation/), but you should have no problem reading them from the help function.





---
<a name="Base Functions"></a>
<h3>The functions provided by <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><a href="#filterNonJournals"><b>filterNonJournals</b>(<i>citesLst, invert=False</i>)</a></article></li>
<li><article><a href="#diffusionGraph"><b>diffusionGraph</b>(<i>source, target, weighted=True, sourceType='raw', targetType='raw', labelEdgesBy=None</i>)</a></article></li>
<li><article><a href="#diffusionCount"><b>diffusionCount</b>(<i>source, target, sourceType='raw', extraValue=None, pandasFriendly=False, compareCounts=False, numAuthors=True, useAllAuthors=True, extraMapping=None</i>)</a></article></li>
<li><article><a href="#diffusionAddCountsFromSource"><b>diffusionAddCountsFromSource</b>(<i>grph, source, target, nodeType='citations', extraType=None, diffusionLabel='DiffusionCount', extraKeys=None, countsDict=None, extraMapping=None</i>)</a></article></li>
<li><article><a href="#readGraph"><b>readGraph</b>(<i>edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'</i>)</a></article></li>
<li><article><a href="#writeEdgeList"><b>writeEdgeList</b>(<i>grph, name, extraInfo=True, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeNodeAttributeFile"><b>writeNodeAttributeFile</b>(<i>grph, name, allSameAttribute=False</i>)</a></article></li>
<li><article><a href="#writeTnetFile"><b>writeTnetFile</b>(<i>grph, name, modeNameString, weighted=False, sourceMode=None, timeString=None, nodeIndexString='tnet-ID', weightString='weight'</i>)</a></article></li>
<li><article><a href="#dropEdges"><b>dropEdges</b>(<i>grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False</i>)</a></article></li>
<li><article><a href="#dropNodesByDegree"><b>dropNodesByDegree</b>(<i>grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True</i>)</a></article></li>
<li><article><a href="#dropNodesByCount"><b>dropNodesByCount</b>(<i>grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False</i>)</a></article></li>
<li><article><a href="#mergeGraphs"><b>mergeGraphs</b>(<i>targetGraph, addedGraph, incrementedNodeVal='count', incrementedEdgeVal='weight'</i>)</a></article></li>
<li><article><a href="#graphStats"><b>graphStats</b>(<i>G, stats=('nodes', 'edges', 'isolates', 'loops', 'density', 'transitivity'), makeString=True</i>)</a></article></li>
<li><article><a href="#writeGraph"><b>writeGraph</b>(<i>grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True, allSameAttribute=False</i>)</a></article></li>
</ol>
<h3>The Exceptions defined by <i>metaknowledge</i> are:</h3>

<ol class="post-list">
<li><article><b>mkException</b>(<i>Exception</i>)</article></li>
<li><article><b>TagError</b>(<i>mkException</i>)</article></li>
<li><article><b>RCValueError</b>(<i>mkException</i>)</article></li>
<li><article><b>BadInputFile</b>(<i>mkException</i>)</article></li>
<li><article><b>BadRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadPubmedRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadPubmedFile</b>(<i>mkException</i>)</article></li>
<li><article><b>BadScopusRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadProQuestRecord</b>(<i>mkException</i>)</article></li>
<li><article><b>BadProQuestFile</b>(<i>mkException</i>)</article></li>
<li><article><b>CollectionTypeError</b>(<i>mkException, TypeError</i>)</article></li>
<li><article><b>RecordsNotCompatible</b>(<i>mkException</i>)</article></li>
<li><article><b>cacheError</b>(<i>mkException</i>)</article></li>
<li><article><b>BadWOSRecord</b>(<i>BadRecord</i>)</article></li>
<li><article><b>BadWOSFile</b>(<i>Warning</i>)</article></li>
<li><article><b>RCTypeError</b>(<i>mkException, TypeError</i>)</article></li>
<li><article><b>BadCitation</b>(<i>Warning</i>)</article></li>
<li><article><b>BadGrant</b>(<i>mkException</i>)</article></li>
<li><article><b>GrantCollectionException</b>(<i>mkException</i>)</article></li>
<li><article><b>UnknownFile</b>(<i>mkException</i>)</article></li>
</ol>
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

<a name="diffusionGraph"></a><small></small>**[<ins>diffusionGraph</ins>]({{ site.baseurl }}{{ page.url }}#diffusionGraph)**(_source, target, weighted=True, sourceType='raw', targetType='raw', labelEdgesBy=None_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a graph of the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) in _target_. By default the nodes in the are `Record` objects but this can be changed with the _sourceType_ and _targetType_ keywords. The edges of the graph go from the target to the source.

Each node on the output graph has two boolean attributes, `"source"` and `"target"` indicating if they are targets or sources. Note, if the types of the sources and targets are different the attributes will not be checked for overlap of the other type. e.g. if the source type is `'TI'` (title) and the target type is `'UT'` (WOS number), and there is some overlap of the targets and sources. Then the Record corresponding to a source node will not be checked for being one of the titles of the targets, only its WOS number will be considered.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_weighted_ : `optional [bool]`

 Default `True`, if `True` each edge will have an attribute `'weight'` giving the number of times the source has referenced the target.

_sourceType_ : `optional [str]`

 Default `'raw'`, if `'raw'` the returned graph will contain `Records` as source nodes.

 If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

_targetType_ : `optional [str]`

 Default `'raw'`, if `'raw'` the returned graph will contain `Records` as target nodes.

 If Records are not wanted then it can be set to a WOS tag, such as `'SO'` (for journals ), to make the nodes into the type of object returned by that tag from Records.

_labelEdgesBy_ : `optional [str]`

 Default `None`, if a WOS tag (or long name of WOS tag) then the edges of the output graph will have a attribute `'key'` that is the value of the referenced tag, of source `Record`, i.e. if `'PY'` is given then each edge will have a `'key'` value equal to the publication year of the source.

 This option will cause the output graph to be an `MultiDiGraph` and is likely to result in parallel edges. If a `Record` has multiple values for at tag (e.g. `'AF'`) the each tag will create its own edge.

###### Returns

`networkx Directed Graph or networkx multi Directed Graph`

 A directed graph of the diffusion network, _labelEdgesBy_ is used the graph will allow parallel edges.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionCount"></a><small></small>**[<ins>diffusionCount</ins>]({{ site.baseurl }}{{ page.url }}#diffusionCount)**(_source, target, sourceType='raw', extraValue=None, pandasFriendly=False, compareCounts=False, numAuthors=True, useAllAuthors=True, extraMapping=None_):

Takes in two [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) and produces a `dict` counting the citations of _source_ by the [`Records`]({{ site.baseurl }}{{ page.url }}#Record) of _target_. By default the `dict` uses `Record` objects as keys but this can be changed with the _sourceType_ keyword to any of the WOS tags.

###### Parameters

_source_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` being cited

_target_ : `RecordCollection`

 A metaknowledge `RecordCollection` containing the `Records` citing those in _source_

_sourceType_ : `optional [str]`

 default `'raw'`, if `'raw'` the returned `dict` will contain `Records` as keys. If it is a WOS tag the keys will be of that type.

_extraValue_ : `optional [str]`

 default `None`, a tag that will split the counts based on entries to it, meaning instead of a single integer a dictionary will be given.

_pandasFriendly_ : `optional [bool]`

 default `False`, makes the output be a dict with two keys one `"Record"` is the list of Records ( or data type requested by _sourceType_) the other is their occurrence counts as `"Counts"`. The lists are the same length.

_compareCounts_ : `optional [bool]`

 default `False`, if `True` the diffusion analysis will be run twice, first with source and target setup like the default (global scope) then using only the source `RecordCollection` (local scope).

_extraValue_ : `optional [str]`

 default `None`, if a tag the returned dictionary will have `Records` mapped to maps, these maps will map the entries for the tag to counts. If _pandasFriendly_ is also `True` the resultant dictionary will have an additional column called `'year'`. This column will contain the year the citations occurred, in addition the Records entries will be duplicated for each year they occur in.

 For example if `'year'` was given then the count for a single `Record` could be `{1990 : 1, 2000 : 5}`

_useAllAuthors_ : `optional [bool]`

 default `True`, if `False` only the first author will be used to generate the `Citations` for the _source_ `Records`

###### Returns

`dict[:int]`

 A dictionary with the type given by _sourceType_ as keys and integers as values.

 If _compareCounts_ is `True` the values are tuples with the first integer being the diffusion in the target and the second the diffusion in the source.

 If _pandasFriendly_ is `True` the returned dict has keys with the names of the WOS tags and lists with their values, i.e. a table with labeled columns. The counts are in the column named `"TargetCount"` and if _compareCounts_ the local count is in a column called `"SourceCount"`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="diffusionAddCountsFromSource"></a><small></small>**[<ins>diffusionAddCountsFromSource</ins>]({{ site.baseurl }}{{ page.url }}#diffusionAddCountsFromSource)**(_grph, source, target, nodeType='citations', extraType=None, diffusionLabel='DiffusionCount', extraKeys=None, countsDict=None, extraMapping=None_):

Does a diffusion using [`diffusionCount()`]({{ site.baseurl }}{{ page.url }}#diffusionCount) and updates _grph_ with it, using the nodes in the graph as keys in the diffusion, i.e. the source. The name of the attribute the counts are added to is given by _diffusionLabel_. If the graph is not composed of citations from the source and instead is another tag _nodeType_ needs to be given the tag string.

###### Parameters

_grph_ : `networkx Graph`

 The graph to be updated

_source_ : `RecordCollection`

 The `RecordCollection` that created _grph_

_target_ : `RecordCollection`

 The `RecordCollection` that will be counted

_nodeType_ : `optional [str]`

 default `'citations'`, the tag that constants the values used to create _grph_

###### Returns

`dict[:int]`

 The counts dictioanry used to add values to _grph_. *Note* _grph_ is modified by the function and the return is done in case you need it.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="readGraph"></a><small></small>**[<ins>readGraph</ins>]({{ site.baseurl }}{{ page.url }}#readGraph)**(_edgeList, nodeList=None, directed=False, idKey='ID', eSource='From', eDest='To'_):

Reads the files given by _edgeList_ and _nodeList_ and creates a networkx graph for the files.

This is designed only for the files produced by metaknowledge and is meant to be the reverse of [writeGraph()]({{ site.baseurl }}{{ page.url }}#writeGraph), if this does not produce the desired results the networkx builtin [networkx.read_edgelist()](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_edgelist.html) could be tried as it is aimed at a more general usage.

The read edge list format assumes the column named _eSource_ (default `'From'`) is the source node, then the column _eDest_ (default `'To'`) givens the destination and all other columns are attributes of the edges, e.g. weight.

The read node list format assumes the column _idKey_ (default `'ID'`) is the ID of the node for the edge list and the resulting network. All other columns are considered attributes of the node, e.g. count.

**Note**: If the names of the columns do not match those given to **readGraph()** a `KeyError` exception will be raised.

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

<a name="writeEdgeList"></a><small></small>**[<ins>writeEdgeList</ins>]({{ site.baseurl }}{{ page.url }}#writeEdgeList)**(_grph, name, extraInfo=True, allSameAttribute=False_):

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

<a name="writeNodeAttributeFile"></a><small></small>**[<ins>writeNodeAttributeFile</ins>]({{ site.baseurl }}{{ page.url }}#writeNodeAttributeFile)**(_grph, name, allSameAttribute=False_):

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

<a name="writeTnetFile"></a><small></small>**[<ins>writeTnetFile</ins>]({{ site.baseurl }}{{ page.url }}#writeTnetFile)**(_grph, name, modeNameString, weighted=False, sourceMode=None, timeString=None, nodeIndexString='tnet-ID', weightString='weight'_):

Writes an edge list designed for reading by the _R_ package [_tnet_](https://toreopsahl.com/tnet/).

The _networkx_ graph provided must be a pure two-mode network, the modes must be 2 different values for the node attribute accessed by _modeNameString_ and all edges must be between different node types. Each node will be given an integer id, stored in the attribute given by _nodeIndexString_, these ids are then written to the file as the endpoints of the edges. Unless _sourceMode_ is given which mode is the source (first column) and which the target (second column) is random.

**Note** the _grph_ will be modified by this function, the ids of the nodes will be written to the graph at the attribute _nodeIndexString_.

###### Parameters

_grph_ : `network Graph`

 The graph that will be written to _name_

_name_ : `str`

 The path of the file to write

_modeNameString_ : `str`

 The name of the attribute _grph_'s modes are stored in

_weighted_ : `optional bool`

 Default `False`, if `True` then the attribute _weightString_ will be written to the weight column

_sourceMode_ : `optional str`

 Default `None`, if given the name of the mode used for the source (first column) in the output file

_timeString_ : `optional str`

 Default `None`, if present the attribute _timeString_ of an edge will be written to the time column surrounded by double quotes (").

**Note** The format used by tnet for dates is very strict it uses the ISO format, down to the second and without time zones.

_nodeIndexString_ : `optional str`

 Default `'tnet-ID'`, the name of the attribute to save the id for each node

_weightString_ : `optional str`

 Default `'weight'`, the name of the weight attribute


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropEdges"></a><small></small>**[<ins>dropEdges</ins>]({{ site.baseurl }}{{ page.url }}#dropEdges)**(_grph, minWeight=-inf, maxWeight=inf, parameterName='weight', ignoreUnweighted=False, dropSelfLoops=False_):

Modifies _grph_ by dropping edges whose weight is not within the inclusive bounds of _minWeight_ and _maxWeight_, i.e after running _grph_ will only have edges whose weights meet the following inequality: _minWeight_ <= edge's weight <= _maxWeight_. A `Keyerror` will be raised if the graph is unweighted unless _ignoreUnweighted_ is `True`, the weight is determined by examining the attribute _parameterName_.

**Note**: none of the default options will result in _grph_ being modified so only specify the relevant ones, e.g. `dropEdges(G, dropSelfLoops = True)` will remove only the self loops from `G`.

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

<a name="dropNodesByDegree"></a><small></small>**[<ins>dropNodesByDegree</ins>]({{ site.baseurl }}{{ page.url }}#dropNodesByDegree)**(_grph, minDegree=-inf, maxDegree=inf, useWeight=True, parameterName='weight', includeUnweighted=True_):

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

<a name="dropNodesByCount"></a><small></small>**[<ins>dropNodesByCount</ins>]({{ site.baseurl }}{{ page.url }}#dropNodesByCount)**(_grph, minCount=-inf, maxCount=inf, parameterName='count', ignoreMissing=False_):

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

<a name="writeGraph"></a><small></small>**[<ins>writeGraph</ins>]({{ site.baseurl }}{{ page.url }}#writeGraph)**(_grph, name, edgeInfo=True, typing=False, suffix='csv', overwrite=True, allSameAttribute=False_):

Writes both the edge list and the node attribute list of _grph_ to files starting with _name_.

The output files start with _name_, the file type (edgeList, nodeAttributes) then if typing is True the type of graph (directed or undirected) then the suffix, the default is as follows:

>  name_fileType.suffix

Both files are csv's with comma delimiters and double quote quoting characters. The edge list has two columns for the source and destination of the edge, `'From'` and `'To'` respectively, then, if _edgeInfo_ is `True`, for each attribute of the node another column is created. The node list has one column call "ID" with the node ids used by networkx and all other columns are the node attributes.

To read back these files use [readGraph()]({{ site.baseurl }}{{ page.url }}#readGraph) and to write only one type of lsit use [writeEdgeList()]({{ site.baseurl }}{{ page.url }}#writeEdgeList) or [writeNodeAttributeFile()]({{ site.baseurl }}{{ page.url }}#writeNodeAttributeFile).

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



---
<a name="WOSRecord"></a>
<a name="WOSRecord"></a><small></small>**[<ins>WOSRecord</ins>](#WOSRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="WOSRecord.__init__"></a><small></small>**[<ins>WOSRecord.__init__</ins>](#WOSRecord.__init__)**(_inRecord, sFile='', sLine=0_):

Class for full WOS records

It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored privately.

The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [**Tag**()](#Tag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The WOSRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#bibString"><b>bibString</b>(<i>maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True</i>)</a></article></li>
<li><article><a href="#bibTexType"><b>bibTexType</b>()</a></article></li>
<li><article><a href="#encoding"><b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><b>getAltName</b>(<i>tag</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagProcessingFunc"></a><small>WOSRecord.</small>**[<ins>tagProcessingFunc</ins>]({{ site.baseurl }}{{ page.url }}#tagProcessingFunc)**(_tag_):

An `abstractmethod`, gives the function for processing _tag_

###### Parameters

_tag_ : `optional [str]`

 The tag in need of processing

###### Returns

`fucntion`

 The function to process the raw tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialFuncs"></a><small>WOSRecord.</small>**[<ins>specialFuncs</ins>]({{ site.baseurl }}{{ page.url }}#specialFuncs)**(_key_):

An `abstractmethod`, process the special tag, _key_ using the whole `Record`

###### Parameters

_key_ : `str`

 One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

###### Returns

 The processed value of _key_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>WOSRecord.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_infile_):

Writes to _infile_ the original contents of the Record. This is intended for use by [RecordCollections]({{ site.baseurl }}{{ page.url }}#RecordCollection) to write to file. What is written to _infile_ is bit for bit identical to the original record file (if utf-8 is used). No newline is inserted above the write but the last character is a newline.

###### Parameters

_infile_ : `file stream`

 An open utf-8 encoded file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bibString"></a><small>WOSRecord.</small>**[<ins>bibString</ins>]({{ site.baseurl }}{{ page.url }}#bibString)**(_maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True_):

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

<a name="bibTexType"></a><small>WOSRecord.</small>**[<ins>bibTexType</ins>]({{ site.baseurl }}{{ page.url }}#bibTexType)**():

Returns the bibTex type corresonding to the record

###### Returns

`str`

 The bibTex type string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="encoding"></a><small>WOSRecord.</small>**[<ins>encoding</ins>]({{ site.baseurl }}{{ page.url }}#encoding)**():

An `abstractmethod`, gives the encoding string of the record.

###### Returns

`str`

 The encoding


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getAltName"></a><small>WOSRecord.</small>**[<ins>getAltName</ins>]({{ site.baseurl }}{{ page.url }}#getAltName)**(_tag_):

An `abstractmethod`, gives the alternate name of _tag_ or `None`

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`str`

 The alternate name of _tag_ or `None`



---
<a name="Citation"></a>
<a name="Citation"></a><small></small>**[<ins>Citation</ins>](#Citation)**(_Hashable_):

<a name="Citation.__init__"></a><small></small>**[<ins>Citation.__init__</ins>](#Citation.__init__)**(_cite, scopusMode=False_):

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

Citation's hashing and equality checking are based on [`ID()`](#ID) and use the values of `author`, `year` and `journal`.

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The Citation class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#isAnonymous"><b>isAnonymous</b>()</a></article></li>
<li><article><a href="#ID"><b>ID</b>()</a></article></li>
<li><article><a href="#allButDOI"><b>allButDOI</b>()</a></article></li>
<li><article><a href="#Extra"><b>Extra</b>()</a></article></li>
<li><article><a href="#isJournal"><b>isJournal</b>(<i>dbname='j9Abbreviations', manaulDB='manualj9Abbreviations', returnDict='both', checkIfExcluded=False</i>)</a></article></li>
<li><article><a href="#FullJournalName"><b>FullJournalName</b>()</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>manualName=None, manaulDB='manualj9Abbreviations', invert=False</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isAnonymous"></a><small>Citation.</small>**[<ins>isAnonymous</ins>]({{ site.baseurl }}{{ page.url }}#isAnonymous)**():

Checks if the author is given as `'[ANONYMOUS]'` and returns `True` if so.

###### Returns

`bool`

 `True` if the author is `'[ANONYMOUS]'` otherwise `False`.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ID"></a><small>Citation.</small>**[<ins>ID</ins>]({{ site.baseurl }}{{ page.url }}#ID)**():

Returns all of `author`, `year` and `journal` available separated by `' ,'`. It is for shortening labels when creating networks as the resultant strings are often unique. [**Extra**()]({{ site.baseurl }}{{ page.url }}#Extra) gets everything not returned by **ID**().

This is also used for hashing and equality checking.

###### Returns

`str`

 A string to use as the ID of a node.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="allButDOI"></a><small>Citation.</small>**[<ins>allButDOI</ins>]({{ site.baseurl }}{{ page.url }}#allButDOI)**():

Returns a string of the normalized values from the Citation excluding the DOI number. Equivalent to getting the ID with [**ID**()]({{ site.baseurl }}{{ page.url }}#ID) then appending the extra values from [**Extra**()]({{ site.baseurl }}{{ page.url }}#Extra) and then removing the substring containing the DOI number.

###### Returns

`str`

 A string containing the data of the Citation.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="Extra"></a><small>Citation.</small>**[<ins>Extra</ins>]({{ site.baseurl }}{{ page.url }}#Extra)**():

Returns any `V`, `P`, `DOI` or `misc` values as a string. These are all the values not returned by [**ID**()]({{ site.baseurl }}{{ page.url }}#ID), they are separated by `' ,'`.

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

<a name="FullJournalName"></a><small>Citation.</small>**[<ins>FullJournalName</ins>]({{ site.baseurl }}{{ page.url }}#FullJournalName)**():

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
<a name="GrantCollection"></a>
<a name="GrantCollection"></a><small></small>**[<ins>GrantCollection</ins>](#GrantCollection)**(_<a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a>_):

<a name="GrantCollection.__init__"></a><small></small>**[<ins>GrantCollection.__init__</ins>](#GrantCollection.__init__)**(_inGrants=None, name='', extension='', cached=False, quietStart=False_):

A [`Collection`](#Collection) with a few extra methods that assume all the contained items have an id attribute and a bad attribute, e.g. [`Records`](#Record) or [`Grants`](#Grant).

\_\_Init\_\_

As `CollectionWithIDs` is mostly meant to be base for other classes all but one of the arguments in the `__init__` are not optional and the optional one is not used. The `__init__()` function is the same as a [`Collection`](#Collection).


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="Grant"></a>
<a name="Grant"></a><small></small>**[<ins>Grant</ins>](#Grant)**(_<a href="#Record"><u style="border-bottom: .5px dashed gray;">Record</u></a>, MutableMapping_):

<a name="Grant.__init__"></a><small></small>**[<ins>Grant.__init__</ins>](#Grant.__init__)**(_original, grantdDict, idValue, bad, error, sFile='', sLine=0_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The Grant class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#update"><b>update</b>(<i>other</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="update"></a><small>Grant.</small>**[<ins>update</ins>]({{ site.baseurl }}{{ page.url }}#update)**(_other_):

Adds all the tag-entry pairs from _other_ to the `Grant`. If there is a conflict _other_ takes precedence.

###### Parameters

_other_ : `Grant`

 Another `Grant` of the same type as _self_



---
<a name="DefaultGrant"></a>
<a name="DefaultGrant"></a><small></small>**[<ins>DefaultGrant</ins>](#DefaultGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="DefaultGrant.__init__"></a><small></small>**[<ins>DefaultGrant.__init__</ins>](#DefaultGrant.__init__)**(_original, grantdDict, sFile='', sLine=0_):

A subclass of [`Grant`](#grant), it has the same attributes and is returned from the default constructor for grants.
    


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="CIHRGrant"></a>
<a name="CIHRGrant"></a><small></small>**[<ins>CIHRGrant</ins>](#CIHRGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="CIHRGrant.__init__"></a><small></small>**[<ins>CIHRGrant.__init__</ins>](#CIHRGrant.__init__)**(_original, grantdDict, sFile, sLine_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="MedlineGrant"></a>
<a name="MedlineGrant"></a><small></small>**[<ins>MedlineGrant</ins>](#MedlineGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="MedlineGrant.__init__"></a><small></small>**[<ins>MedlineGrant.__init__</ins>](#MedlineGrant.__init__)**(_grantString_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="NSERCGrant"></a>
<a name="NSERCGrant"></a><small></small>**[<ins>NSERCGrant</ins>](#NSERCGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="NSERCGrant.__init__"></a><small></small>**[<ins>NSERCGrant.__init__</ins>](#NSERCGrant.__init__)**(_original, grantdDict, sFile, sLine_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="NSFGrant"></a>
<a name="NSFGrant"></a><small></small>**[<ins>NSFGrant</ins>](#NSFGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="NSFGrant.__init__"></a><small></small>**[<ins>NSFGrant.__init__</ins>](#NSFGrant.__init__)**(_grantdDict, sFile_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">
---
<a name="MedlineRecord"></a>
<a name="MedlineRecord"></a><small></small>**[<ins>MedlineRecord</ins>](#MedlineRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="MedlineRecord.__init__"></a><small></small>**[<ins>MedlineRecord.__init__</ins>](#MedlineRecord.__init__)**(_inRecord, sFile='', sLine=0_):

Class for full Medline(Pubmed) entries.

This class is an [`ExtendedRecord`](#ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [`medlineParser()`](#medlineParser) on a medline file.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The MedlineRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#encoding"><b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>f</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="encoding"></a><small>MedlineRecord.</small>**[<ins>encoding</ins>]({{ site.baseurl }}{{ page.url }}#encoding)**():

An `abstractmethod`, gives the encoding string of the record.

###### Returns

`str`

 The encoding


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getAltName"></a><small>MedlineRecord.</small>**[<ins>getAltName</ins>]({{ site.baseurl }}{{ page.url }}#getAltName)**(_tag_):

An `abstractmethod`, gives the alternate name of _tag_ or `None`

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`str`

 The alternate name of _tag_ or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagProcessingFunc"></a><small>MedlineRecord.</small>**[<ins>tagProcessingFunc</ins>]({{ site.baseurl }}{{ page.url }}#tagProcessingFunc)**(_tag_):

An `abstractmethod`, gives the function for processing _tag_

###### Parameters

_tag_ : `optional [str]`

 The tag in need of processing

###### Returns

`fucntion`

 The function to process the raw tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialFuncs"></a><small>MedlineRecord.</small>**[<ins>specialFuncs</ins>]({{ site.baseurl }}{{ page.url }}#specialFuncs)**(_key_):

An `abstractmethod`, process the special tag, _key_ using the whole `Record`

###### Parameters

_key_ : `str`

 One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

###### Returns

 The processed value of _key_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>MedlineRecord.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_f_):

This is nearly identical to the original the FAU tag is the only tag not writen in the same place, doing so would require changing the parser and lots of extra logic.
        



---
<a name="Collection"></a>
<a name="Collection"></a><small></small>**[<ins>Collection</ins>](#Collection)**(_MutableSet, Hashable_):

<a name="Collection.__init__"></a><small></small>**[<ins>Collection.__init__</ins>](#Collection.__init__)**(_inSet, allowedTypes, collectedTypes, name, bad, errors, quietStart=False_):

A named hashable set with some error reporting.

`Collections` have all the methods of builtin `sets` as well as error reporting with _bad_ and _error_, and control over the contained items with _allowedTypes_ and _collectedTypes_.

##### Customizations

When created _name_ should be a string that allows users to easily determine the source of the `Collection`

When created the you must provided a set of types, _allowedTypes_, when new items are added they will be checked and if they are not instances of any of the types an `CollectionTypeError` exception will be raised. The _collectedTypes_ set that is provided should be a set of only the types in the `Collection`.

If any of the elements in the `Collection` are bad then _bad_ should be set to `True` and the `dict` _errors_ should map the item to it's exception.

All of these customizations are managed when operations occur on the `Collection` and if 2 `Collections` are modified with one of the binary operators (`|`, `-`, etc) the `_collectedTypes` and `errors` attributes will be modified the same way. `name` will be updated to explain the operation(s) that occurred.

\_\_Init\_\_

As `Collection` is mostly meant to be base for other classes all but one of the arguments in the \_\_Init\_\_ are not optional and the optional one is not used.

##### Parameters

_inSet_ : `set`

 The objects to be contained

_allowedTypes_ : `set[type]`

 A set of types, `{object}` will allow virtually everything

_collectedTypes_ : `set[type]`

 The types (or supertypes) of the objects in _inSet_

_name_ : `str`

 The name of the `Collection`

_bad_ : `bool`

 If any of the elements are bad

_errors_ : `dict[:Exception]`

 A mapping from items to their errors

_quietStart_ : `optional [bool]`

 Default `False`, does nothing. This is here for use as a interface by subclasses


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The Collection class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#add"><b>add</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#discard"><b>discard</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#remove"><b>remove</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#clear"><b>clear</b>()</a></article></li>
<li><article><a href="#pop"><b>pop</b>()</a></article></li>
<li><article><a href="#copy"><b>copy</b>()</a></article></li>
<li><article><a href="#peek"><b>peek</b>()</a></article></li>
<li><article><a href="#chunk"><b>chunk</b>(<i>maxSize</i>)</a></article></li>
<li><article><a href="#split"><b>split</b>(<i>maxSize</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="add"></a><small>Collection.</small>**[<ins>add</ins>]({{ site.baseurl }}{{ page.url }}#add)**(_elem_):

Adds _elem_ to the collection.

###### Parameters

_elem_ : `object`

 The object to be added


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="discard"></a><small>Collection.</small>**[<ins>discard</ins>]({{ site.baseurl }}{{ page.url }}#discard)**(_elem_):

Removes _elem_ from the collection, will not raise an Exception if _elem_ is missing

###### Parameters

_elem_ : `object`

 The object to be removed


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="remove"></a><small>Collection.</small>**[<ins>remove</ins>]({{ site.baseurl }}{{ page.url }}#remove)**(_elem_):

Removes _elem_ from the collection, will raise a KeyError is _elem_ is missing

###### Parameters

_elem_ : `object`

 The object to be removed


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="clear"></a><small>Collection.</small>**[<ins>clear</ins>]({{ site.baseurl }}{{ page.url }}#clear)**():

"Removes all elements from the collection and resets the error handling
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pop"></a><small>Collection.</small>**[<ins>pop</ins>]({{ site.baseurl }}{{ page.url }}#pop)**():

Removes a random element from the collection and returns it

###### Returns

`object`

 A random object from the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="copy"></a><small>Collection.</small>**[<ins>copy</ins>]({{ site.baseurl }}{{ page.url }}#copy)**():

Creates a shallow copy of the collection

###### Returns

`Collection`

 A copy of the `Collection`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="peek"></a><small>Collection.</small>**[<ins>peek</ins>]({{ site.baseurl }}{{ page.url }}#peek)**():

returns a random element from the collection. If ran twice the same element will usually be returned

###### Returns

`object`

 A random object from the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="chunk"></a><small>Collection.</small>**[<ins>chunk</ins>]({{ site.baseurl }}{{ page.url }}#chunk)**(_maxSize_):

Splits the `Collection` into _maxSize_ size or smaller `Collections`

###### Parameters

_maxSize_ : `int`

 The maximum number of elements in a retuned `Collection`


###### Returns

`list [Collection]`

 A list of `Collections` that if all merged (`|` operator) would create the original


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="split"></a><small>Collection.</small>**[<ins>split</ins>]({{ site.baseurl }}{{ page.url }}#split)**(_maxSize_):

Destructively, splits the `Collection` into _maxSize_ size or smaller `Collections`. The source `Collection` will be empty after this operation

###### Parameters

_maxSize_ : `int`

 The maximum number of elements in a retuned `Collection`

###### Returns

`list [Collection]`

 A list of `Collections` that if all merged (`|` operator) would create the original



---
<a name="CollectionWithIDs"></a>
<a name="CollectionWithIDs"></a><small></small>**[<ins>CollectionWithIDs</ins>](#CollectionWithIDs)**(_<a href="#Collection"><u style="border-bottom: .5px dashed gray;">Collection</u></a>_):

<a name="CollectionWithIDs.__init__"></a><small></small>**[<ins>CollectionWithIDs.__init__</ins>](#CollectionWithIDs.__init__)**(_inSet, allowedTypes, collectedTypes, name, bad, errors, quietStart=False_):

A [`Collection`](#Collection) with a few extra methods that assume all the contained items have an id attribute and a bad attribute, e.g. [`Records`](#Record) or [`Grants`](#Grant).

\_\_Init\_\_

As `CollectionWithIDs` is mostly meant to be base for other classes all but one of the arguments in the `__init__` are not optional and the optional one is not used. The `__init__()` function is the same as a [`Collection`](#Collection).


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The CollectionWithIDs class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#containsID"><b>containsID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#discardID"><b>discardID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#removeID"><b>removeID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#getID"><b>getID</b>(<i>idVal</i>)</a></article></li>
<li><article><a href="#badEntries"><b>badEntries</b>()</a></article></li>
<li><article><a href="#dropBadEntries"><b>dropBadEntries</b>()</a></article></li>
<li><article><a href="#tags"><b>tags</b>()</a></article></li>
<li><article><a href="#cooccurrenceCounts"><b>cooccurrenceCounts</b>(<i>keyTag, *countedTags</i>)</a></article></li>
<li><article><a href="#oneModeNetwork"><b>oneModeNetwork</b>(<i>mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None</i>)</a></article></li>
<li><article><a href="#twoModeNetwork"><b>twoModeNetwork</b>(<i>tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None</i>)</a></article></li>
<li><article><a href="#nModeNetwork"><b>nModeNetwork</b>(<i>*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="containsID"></a><small>CollectionWithIDs.</small>**[<ins>containsID</ins>]({{ site.baseurl }}{{ page.url }}#containsID)**(_idVal_):

Checks if the collected items contains the give _idVal_

###### Parameters

_idVal_ : `str`

 The queried id string

###### Returns

`bool`

 `True` if the item is in the collection


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="discardID"></a><small>CollectionWithIDs.</small>**[<ins>discardID</ins>]({{ site.baseurl }}{{ page.url }}#discardID)**(_idVal_):

Checks if the collected items contains the give _idVal_ and discards it if it is found, will not raise an exception if item is not found

###### Parameters

_idVal_ : `str`

 The discarded id string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="removeID"></a><small>CollectionWithIDs.</small>**[<ins>removeID</ins>]({{ site.baseurl }}{{ page.url }}#removeID)**(_idVal_):

Checks if the collected items contains the give _idVal_ and removes it if it is found, will raise a `KeyError` if item is not found

###### Parameters

_idVal_ : `str`

 The removed id string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getID"></a><small>CollectionWithIDs.</small>**[<ins>getID</ins>]({{ site.baseurl }}{{ page.url }}#getID)**(_idVal_):

Looks up an item with _idVal_ and returns it if it is found, returns `None` if it does not find the item

###### Parameters

_idVal_ : `str`

 The requested item's id string

###### Returns

`object`

 The requested object or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="badEntries"></a><small>CollectionWithIDs.</small>**[<ins>badEntries</ins>]({{ site.baseurl }}{{ page.url }}#badEntries)**():

Creates a new collection of the same type with only the bad entries

###### Returns

`CollectionWithIDs`

 A collection of only the bad entries


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="dropBadEntries"></a><small>CollectionWithIDs.</small>**[<ins>dropBadEntries</ins>]({{ site.baseurl }}{{ page.url }}#dropBadEntries)**():

Removes all the bad entries from the collection
        


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tags"></a><small>CollectionWithIDs.</small>**[<ins>tags</ins>]({{ site.baseurl }}{{ page.url }}#tags)**():

Creates a list of all the tags of the contained items

###### Returns

`list [str]`

 A list of all the tags


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="cooccurrenceCounts"></a><small>CollectionWithIDs.</small>**[<ins>cooccurrenceCounts</ins>]({{ site.baseurl }}{{ page.url }}#cooccurrenceCounts)**(_keyTag, *countedTags_):

Counts the number of times values from any of the _countedTags_ occurs with _keyTag_. The counts are retuned as a dictionary with the values of _keyTag_ mapping to dictionaries with each of the _countedTags_ values mapping to thier counts.

###### Parameters

_keyTag_ : `str`

 The tag used as the key for the returned dictionary

_*countedTags_ : `str, str, str, ...`

 The tags used as the key for the returned dictionary's values

###### Returns

`dict[str:dict[str:int]]`

 The dictionary of counts


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="oneModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>oneModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#oneModeNetwork)**(_mode, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None, nodeAttribute=None_):

Creates a network of the objects found by one tag _mode_.

A **oneModeNetwork**() looks are each entry in the collection and extracts its values for the tag given by _mode_, e.g. the `'authorsFull'` tag. Then if multiple are returned an edge is created between them. So in the case of the author tag `'authorsFull'` a co-authorship network is created.

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="twoModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>twoModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#twoModeNetwork)**(_tag1, tag2, directed=False, recordType=True, nodeCount=True, edgeWeight=True, stemmerTag1=None, stemmerTag2=None, edgeAttribute=None_):

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

<a name="nModeNetwork"></a><small>CollectionWithIDs.</small>**[<ins>nModeNetwork</ins>]({{ site.baseurl }}{{ page.url }}#nModeNetwork)**(_*tags, recordType=True, nodeCount=True, edgeWeight=True, stemmer=None, edgeAttribute=None_):

Creates a network of the objects found by all tags in _tags_, each node is marked by which tag spawned it making the resultant graph n-partite.

A **nModeNetwork()** looks are each item in the collection and extracts its values for the tags given by _tags_. Then for all objects returned an edge is created between them, regardless of their type. Each node will have an attribute call `'type'` that gives the tag that created it or both if both created it, e.g. if `'LA'` were in _tags_ node `'English'` would have the type attribute be `'LA'`.

For example if _tags_ was set to `['CR', 'UT', 'LA']`, a three mode network would be created, composed of a co-citation network from the `'CR'` tag. Then each citation would also have edges to all the languages of Records that cited it and to the WOS number of the those Records.

The number of times each object occurs is count if _nodeCount_ is `True` and the edges count the number of co-occurrences if _edgeWeight_ is `True`. Both are`True` by default.

###### Parameters

_tags_ : `str`, `str`, `str`, ... or `list [str]`

 Any number of tags, or a list of tags

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



---
<a name="ExtendedRecord"></a>
<a name="ExtendedRecord"></a><small></small>**[<ins>ExtendedRecord</ins>](#ExtendedRecord)**(_<a href="#Record"><u style="border-bottom: .5px dashed gray;">Record</u></a>_):

<a name="ExtendedRecord.__init__"></a><small></small>**[<ins>ExtendedRecord.__init__</ins>](#ExtendedRecord.__init__)**(_fieldDict, idValue, bad, error, sFile='', sLine=0_):

A subclass of `Record` that adds processing to the dictionary. It also cannot be use directly and must be subclassed.

The `ExtendedRecord` class is a extension of `Record` that is intended for use with the records on scientific papers provided by different organizations such as WOS or Pubmed. The 5 abstract (virtual) methods must be defined for each subclass and define how the data in the different fields is processed and how the record can be rewritten to a file.

##### Processing fields

When an `ExtendedRecord` is created a dictionary, _fieldDict_, must be provided this contains the raw data from the file reader, usually as lists of strings. `tagProcessingFunc` is a `staticmethod` function that takes in a tag string an returns another function to process it.

Each tag may also be given a second name, as usually what the they are called in the raw data are not very easy to understand (e.g. `'SO'` is the journal name for WOs records). The mapping from the raw tag (`'SO'`) to the human friendly string (`'journal'`)  is done with the `getAltName` `staticmethod`. `getAltName` takes in a tag string and returns either `None` or the other name for that string. Note, `getAltName` must go both directions `WOSRecord.getAltName(WOSRecord.getAltName('SO')) == 'SO'`.

The last method for processing entries is `specialFuncs` The following are the special keys for `ExtendedRecords`. These must be the alternate names of tags or strings accepted by the `specialFuncs` method.

+ `'authorsFull'`
+ `'keywords'`
+ `'grants'`
+ `'j9'`
+ `'authorsShort'`
+ `'volume'`
+ `'selfCitation'`
+ `'citations'`
+ `'address'`
+ `'abstract'`
+ `'title'`
+ `'month'`
+ `'year'`
+ `'journal'`
+ `'beginningPage'`
+ `'DOI'`

`specialFuncs` when given one of these must raise a `KeyError` or return an object of the same type as that returned by the `MedlineRecord` or `WOSRecord`. e.g. `'title'` would return a string giving the title of the record.

For an example of how this works lets first look at the `'SO'` tag on a `WOSRecord` accessed with the alternate name `'journal'`.

    t = R['journal']

First the private dictionary `_computedFields` is checked for the key `'title'`, which will fail if this is the first time `'journal'` or `'SO'` has been requested, after this the results will be added to the dictionary to speed up future requests.

Then the _fieldDict_ will be checked for the key and when that fails the key will go through `getAltName` and be checked again. If the record had a journal entry this will succeed and the raw data will be given to the `tagProcessingFunc` using the same key as _fieldDict_, in this case `SO`.

The results will then be written to `_computedFields` and returned.

If the requested key was instead `'grants'` (`g = R['grants']`)the both lookups to _fieldDict_ would have failed and the string `'grants'` would have been given to `specialFuncs` which would return a list of all the grants in the `WOSRecord` (this is always `[]` as WOS does not provided grant information).

What if the key were not present anywhere? Then the `specialFuncs` should raise a `KeyError` which will be caught then re-raised like a dictionary would with an invalid key look up.

##### File Handling fields

The two other required methods `encoding` and `writeRecord` define how the records can be rewritten to a file. `encoding` is should return a string giving the encoding python would use, e.g. `'utf-8'` or `'latin-1'`. This is the same encoding that the files written by `writeRecord` should have, `writeRecord` when called should write the original record to the provided open file, _infile_. The opening, closing, header and footer of the file will be handled by `RecordCollection`'s `writeFile` function which should me modified accordingly. If the order of the fields in a record is important you can use a [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict) for _fieldDict_.

##### \_\_Init\_\_

The `__init__` of `ExtendedRecord` takes the same arguments as [`Record`](#Record)


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The ExtendedRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#get"><b>get</b>(<i>tag, default=None, raw=False</i>)</a></article></li>
<li><article><a href="#values"><b>values</b>(<i>raw=False</i>)</a></article></li>
<li><article><a href="#items"><b>items</b>(<i>raw=False</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
<li><article><a href="#encoding"><b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#subDict"><b>subDict</b>(<i>tags, raw=False</i>)</a></article></li>
<li><article><a href="#createCitation"><b>createCitation</b>(<i>multiCite=False</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="get"></a><small>ExtendedRecord.</small>**[<ins>get</ins>]({{ site.baseurl }}{{ page.url }}#get)**(_tag, default=None, raw=False_):

Allows access to the raw values or is an Exception safe wrapper to `__getitem__`.

###### Parameters

_tag_ : `str`

 The requested tag

_default_ : `optional [Object]`

 Default `None`, the object returned when _tag_ is not found

_raw_ : `optional [bool]`

 Default `False`, if `True` the unprocessed value of _tag_ is returned

###### Returns

`Object`

 The processed value of _tag_ or _default_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="values"></a><small>ExtendedRecord.</small>**[<ins>values</ins>]({{ site.baseurl }}{{ page.url }}#values)**(_raw=False_):

Like `values` for dicts but with a `raw` option

###### Parameters

_raw_ : `optional [bool]`

 Default `False`, if `True` the `ValuesView` contains the raw values

###### Returns

`ValuesView`

 The values of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="items"></a><small>ExtendedRecord.</small>**[<ins>items</ins>]({{ site.baseurl }}{{ page.url }}#items)**(_raw=False_):

Like `items` for dicts but with a `raw` option

###### Parameters

_raw_ : `optional [bool]`

 Default `False`, if `True` the `KeysView` contains the raw values as the values

###### Returns

`KeysView`

 The key-value pairs of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>ExtendedRecord.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_infile_):

An `abstractmethod`, writes the record in its original form to _infile_

###### Parameters

_infile_ : `writable file`

 The file to be written to


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="encoding"></a><small>ExtendedRecord.</small>**[<ins>encoding</ins>]({{ site.baseurl }}{{ page.url }}#encoding)**():

An `abstractmethod`, gives the encoding string of the record.

###### Returns

`str`

 The encoding


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getAltName"></a><small>ExtendedRecord.</small>**[<ins>getAltName</ins>]({{ site.baseurl }}{{ page.url }}#getAltName)**(_tag_):

An `abstractmethod`, gives the alternate name of _tag_ or `None`

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`str`

 The alternate name of _tag_ or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagProcessingFunc"></a><small>ExtendedRecord.</small>**[<ins>tagProcessingFunc</ins>]({{ site.baseurl }}{{ page.url }}#tagProcessingFunc)**(_tag_):

An `abstractmethod`, gives the function for processing _tag_

###### Parameters

_tag_ : `optional [str]`

 The tag in need of processing

###### Returns

`fucntion`

 The function to process the raw tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialFuncs"></a><small>ExtendedRecord.</small>**[<ins>specialFuncs</ins>]({{ site.baseurl }}{{ page.url }}#specialFuncs)**(_key_):

An `abstractmethod`, process the special tag, _key_ using the whole `Record`

###### Parameters

_key_ : `str`

 One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

###### Returns

 The processed value of _key_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subDict"></a><small>ExtendedRecord.</small>**[<ins>subDict</ins>]({{ site.baseurl }}{{ page.url }}#subDict)**(_tags, raw=False_):

Creates a dict of values of _tags_ from the Record. The tags are the keys and the values are the values. If the tag is missing the value will be `None`.

###### Parameters

_tags_ : `list[str]`

 The list of tags requested

_raw_ : `optional [bool]`

default `False` if `True` the retuned values of the dict will be unprocessed

###### Returns

`dict`

 A dictionary with the keys _tags_ and the values from the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="createCitation"></a><small>ExtendedRecord.</small>**[<ins>createCitation</ins>]({{ site.baseurl }}{{ page.url }}#createCitation)**(_multiCite=False_):

Creates a citation string, using the same format as other WOS citations, for the [Record]({{ site.baseurl }}{{ page.url }}#Record) by reading the relevant special tags (`'year'`, `'J9'`, `'volume'`, `'beginningPage'`, `'DOI'`) and using it to create a [`Citation`]({{ site.baseurl }}{{ page.url }}#Citation) object.

###### Parameters

_multiCite_ : `optional [bool]`

 Default `False`, if `True` a tuple of Citations is returned with each having a different one of the records authors as the author

###### Returns

`Citation`

 A [`Citation`]({{ site.baseurl }}{{ page.url }}#Citation) object containing a citation for the Record.



---
<a name="Record"></a>
<a name="Record"></a><small></small>**[<ins>Record</ins>](#Record)**(_Mapping, Hashable_):

<a name="Record.__init__"></a><small></small>**[<ins>Record.__init__</ins>](#Record.__init__)**(_fieldDict, idValue, bad, error, sFile='', sLine=0_):

A dictionary with error handling and an id string.

`Record` is the base class of the all objects in _metaknowledge_ that contain information as key-value pairs, these are the grants and the records from different sources.

The error handling of the `Record` is done with the `bad` attribute. If there is some issue with the data _bad_ should be `True` and _error_ given an `Exception` that was caused by or explains the error.

##### Customizations

`Record` is a subclass of `abc.collections.Mapping` which means it has almost all the methods a dictionary does, the missing ones are those that modify entries. So to access the value of the key `'title'` from a `Record` `R`, you would use either the square brace notation `t = R['title']` or the `get()` function `t = R.get('title')` just like a dictionary. The other methods like `keys()` or `copy()` also work.

In addition to being a mapping `Records` are also hashable with their hashes being based on a unique id string they are given on creation, usually some kind of accession number the source gives them. The two optional arguments _sFile_ and _sLine_, which should be given the name of the file the records came from and the line it started on respectively, are used to make the errors more useful.

##### \_\_Init\_\_

_fieldDict_ is the dictionary the `Record` will use and _idValue_ is the unique identifier of the `Record`.

##### Parameters

_fieldDict_ : `dict[str:]`

 A dictionary that maps from strings to values

_idValue_ : `str`

 A unique identifier string for the `Record`

_bad_ : `bool`

 `True` if there are issues with the `Record`, otherwise `False`

_error_ : `Exception`

 The `Exception` that caused whatever error made the record be marked as bad or `None`

_sFile_ : `str`

 A string that gives the source file of the original records

_sLine_ : `int`

 The first line the original record is found on in the source file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The Record class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#__eq__"><b>__eq__</b>(<i>other</i>)</a></article></li>
<li><article><a href="#__str__"><b>__str__</b>()</a></article></li>
<li><article><a href="#__repr__"><b>__repr__</b>()</a></article></li>
<li><article><a href="#copy"><b>copy</b>()</a></article></li>
<li><article><a href="#__hash__"><b>__hash__</b>()</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="__eq__"></a><small>Record.</small>**[<ins>__eq__</ins>]({{ site.baseurl }}{{ page.url }}#__eq__)**(_other_):

Compares `Records` using their hashes if their hashes are the same then `True` is returned.

###### Parameters

_other_ : `Record`

 Another `Record` to be compared against

###### Returns

`bool`

 If the `records` are the same then `True` is returned


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="__str__"></a><small>Record.</small>**[<ins>__str__</ins>]({{ site.baseurl }}{{ page.url }}#__str__)**():

Makes a string with the title of the file as given by self.title, if there is not one it returns "Untitled record"

###### Returns

`str`

 The title of the `Record`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="__repr__"></a><small>Record.</small>**[<ins>__repr__</ins>]({{ site.baseurl }}{{ page.url }}#__repr__)**():

Makes a string with the id of the file and its type

###### Returns

`str`

 The representation of the `Record`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="copy"></a><small>Record.</small>**[<ins>copy</ins>]({{ site.baseurl }}{{ page.url }}#copy)**():

Correctly copies the `Record`

###### Returns

`Record`

 A completely decoupled copy of the original


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="__hash__"></a><small>Record.</small>**[<ins>__hash__</ins>]({{ site.baseurl }}{{ page.url }}#__hash__)**():

Gives a hash of the id or if `bad` returns a hash of the fields combined with the error messages, either of these could be blank

`bad` Records are more likely to cause hash collisions due to their lack of entropy when created.

###### Returns

`int`

 A hopefully unique random number



---
<a name="ProQuestRecord"></a>
<a name="ProQuestRecord"></a><small></small>**[<ins>ProQuestRecord</ins>](#ProQuestRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="ProQuestRecord.__init__"></a><small></small>**[<ins>ProQuestRecord.__init__</ins>](#ProQuestRecord.__init__)**(_inRecord, recNum=None, sFile='', sLine=0_):

Class for full ProQuest entries.

This class is an [`ExtendedRecord`](#ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [`proQuestParser()`](#proQuestParser) on a ProQuest file.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The ProQuestRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#encoding"><b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="encoding"></a><small>ProQuestRecord.</small>**[<ins>encoding</ins>]({{ site.baseurl }}{{ page.url }}#encoding)**():

An `abstractmethod`, gives the encoding string of the record.

###### Returns

`str`

 The encoding


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getAltName"></a><small>ProQuestRecord.</small>**[<ins>getAltName</ins>]({{ site.baseurl }}{{ page.url }}#getAltName)**(_tag_):

An `abstractmethod`, gives the alternate name of _tag_ or `None`

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`str`

 The alternate name of _tag_ or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagProcessingFunc"></a><small>ProQuestRecord.</small>**[<ins>tagProcessingFunc</ins>]({{ site.baseurl }}{{ page.url }}#tagProcessingFunc)**(_tag_):

An `abstractmethod`, gives the function for processing _tag_

###### Parameters

_tag_ : `optional [str]`

 The tag in need of processing

###### Returns

`fucntion`

 The function to process the raw tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialFuncs"></a><small>ProQuestRecord.</small>**[<ins>specialFuncs</ins>]({{ site.baseurl }}{{ page.url }}#specialFuncs)**(_key_):

An `abstractmethod`, process the special tag, _key_ using the whole `Record`

###### Parameters

_key_ : `str`

 One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

###### Returns

 The processed value of _key_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>ProQuestRecord.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_infile_):

An `abstractmethod`, writes the record in its original form to _infile_

###### Parameters

_infile_ : `writable file`

 The file to be written to



---
<a name="RecordCollection"></a>
<a name="RecordCollection"></a><small></small>**[<ins>RecordCollection</ins>](#RecordCollection)**(_<a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a>_):

<a name="RecordCollection.__init__"></a><small></small>**[<ins>RecordCollection.__init__</ins>](#RecordCollection.__init__)**(_inCollection=None, name='', extension='', cached=False, quietStart=False_):

A container for a large number of indivual records.

`RecordCollection` provides ways of creating [`Records`](#Record) from an isi file, string, list of records or directory containing isi files.

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

_cached_ : `optional [bool]`

 Default `False`, if `True` and the _inCollection_ is a directory (a string giving the path to a directory) then the initialized `RecordCollection` will be saved in the directory as a Python pickle with the suffix `'.mkDirCache'`. Then if the `RecordCollection` is initialized a second time it will be recovered from the file, which is much faster than reprising every file in the directory.

 _metaknowledge_ saves the names of the parsed files as well as their last modification times and will check these when recreating the `RecordCollection`, so modifying existing files or adding new ones will result in the entire directory being reanalyzed and a new cache file being created. The extension given to **__init__**() is taken into account as well and each suffix is given its own cache.

 **Note** The pickle allows for arbitrary python code exicution so only use caches that you trust.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The RecordCollection class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#dropNonJournals"><b>dropNonJournals</b>(<i>ptVal='J', dropBad=True, invert=False</i>)</a></article></li>
<li><article><a href="#writeFile"><b>writeFile</b>(<i>fname=None</i>)</a></article></li>
<li><article><a href="#writeCSV"><b>writeCSV</b>(<i>fname=None, splitByTag=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'</i>)</a></article></li>
<li><article><a href="#writeBib"><b>writeBib</b>(<i>fname=None, maxStringLength=1000, wosMode=False, reducedOutput=False, niceIDs=True</i>)</a></article></li>
<li><article><a href="#makeDict"><b>makeDict</b>(<i>onlyTheseTags=None, longNames=False, raw=False, numAuthors=True</i>)</a></article></li>
<li><article><a href="#coAuthNetwork"><b>coAuthNetwork</b>(<i>detailedInfo=False, weighted=True, dropNonJournals=False, count=True</i>)</a></article></li>
<li><article><a href="#coCiteNetwork"><b>coCiteNetwork</b>(<i>dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False</i>)</a></article></li>
<li><article><a href="#citationNetwork"><b>citationNetwork</b>(<i>dropAnon=False, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False, recordToCite=True</i>)</a></article></li>
<li><article><a href="#yearSplit"><b>yearSplit</b>(<i>startYear, endYear, dropMissingYears=True</i>)</a></article></li>
<li><article><a href="#localCiteStats"><b>localCiteStats</b>(<i>pandasFriendly=False, keyType='citation'</i>)</a></article></li>
<li><article><a href="#localCitesOf"><b>localCitesOf</b>(<i>rec</i>)</a></article></li>
<li><article><a href="#citeFilter"><b>citeFilter</b>(<i>keyString='', field='all', reverse=False, caseSensitive=False</i>)</a></article></li>
</ol>
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

<a name="writeCSV"></a><small>RecordCollection.</small>**[<ins>writeCSV</ins>]({{ site.baseurl }}{{ page.url }}#writeCSV)**(_fname=None, splitByTag=None, onlyTheseTags=None, numAuthors=True, longNames=False, firstTags=None, csvDelimiter=',', csvQuote='"', listDelimiter='|'_):

Writes all the `Records` from the collection into a csv file with each row a record and each column a tag.

###### Parameters

_fname_ : `optional [str]`

 Default `None`, the name of the file to write to, if `None` it uses the collections name suffixed by .csv.

_splitByTag_ : `optional [str]`

 Default `None`, if a tag is given the output will be divided into different files according to the value of the tag, with only the records associated with that tag. For example if `'authorsFull'` is given then each file will only have the lines for `Records` that author is named in.

 The file names are the values of the tag followed by a dash then the normale name for the file as given by _fname_, e.g. for the year 2016 the file could be called `'2016-fname.csv'`.

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

<a name="makeDict"></a><small>RecordCollection.</small>**[<ins>makeDict</ins>]({{ site.baseurl }}{{ page.url }}#makeDict)**(_onlyTheseTags=None, longNames=False, raw=False, numAuthors=True_):

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

<a name="coCiteNetwork"></a><small>RecordCollection.</small>**[<ins>coCiteNetwork</ins>]({{ site.baseurl }}{{ page.url }}#coCiteNetwork)**(_dropAnon=True, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False_):

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

<a name="citationNetwork"></a><small>RecordCollection.</small>**[<ins>citationNetwork</ins>]({{ site.baseurl }}{{ page.url }}#citationNetwork)**(_dropAnon=False, nodeType='full', nodeInfo=True, fullInfo=False, weighted=True, dropNonJournals=False, count=True, directed=True, keyWords=None, detailedCore=None, detailedCoreAttributes=False, coreOnly=False, expandedCore=False, recordToCite=True_):

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



---
<a name="ScopusRecord"></a>
<a name="ScopusRecord"></a><small></small>**[<ins>ScopusRecord</ins>](#ScopusRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="ScopusRecord.__init__"></a><small></small>**[<ins>ScopusRecord.__init__</ins>](#ScopusRecord.__init__)**(_inRecord, sFile='', sLine=0_):

Class for full Scopus entries.

This class is an [`ExtendedRecord`](#ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [`scopusParser()`](#scopusParser) on a scopus **CSV** file.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;"><h3>
The ScopusRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#encoding"><b>encoding</b>()</a></article></li>
<li><article><a href="#getAltName"><b>getAltName</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>f</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="encoding"></a><small>ScopusRecord.</small>**[<ins>encoding</ins>]({{ site.baseurl }}{{ page.url }}#encoding)**():

An `abstractmethod`, gives the encoding string of the record.

###### Returns

`str`

 The encoding


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="getAltName"></a><small>ScopusRecord.</small>**[<ins>getAltName</ins>]({{ site.baseurl }}{{ page.url }}#getAltName)**(_tag_):

An `abstractmethod`, gives the alternate name of _tag_ or `None`

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`str`

 The alternate name of _tag_ or `None`


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="tagProcessingFunc"></a><small>ScopusRecord.</small>**[<ins>tagProcessingFunc</ins>]({{ site.baseurl }}{{ page.url }}#tagProcessingFunc)**(_tag_):

An `abstractmethod`, gives the function for processing _tag_

###### Parameters

_tag_ : `optional [str]`

 The tag in need of processing

###### Returns

`fucntion`

 The function to process the raw tag


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialFuncs"></a><small>ScopusRecord.</small>**[<ins>specialFuncs</ins>]({{ site.baseurl }}{{ page.url }}#specialFuncs)**(_key_):

An `abstractmethod`, process the special tag, _key_ using the whole `Record`

###### Parameters

_key_ : `str`

 One of the special tags: `'authorsFull'`, `'keywords'`, `'grants'`, `'j9'`, `'authorsShort'`, `'volume'`, `'selfCitation'`, `'citations'`, `'address'`, `'abstract'`, `'title'`, `'month'`, `'year'`, `'journal'`, `'beginningPage'` and `'DOI'`

###### Returns

 The processed value of _key_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="writeRecord"></a><small>ScopusRecord.</small>**[<ins>writeRecord</ins>]({{ site.baseurl }}{{ page.url }}#writeRecord)**(_f_):

An `abstractmethod`, writes the record in its original form to _infile_

###### Parameters

_infile_ : `writable file`

 The file to be written to



---
<a name="contour"></a>

# [contour]({{ site.baseurl }}{{ page.url }}#contour)

Two functions based on _matplotlib_ for generating nicer looking graphs

This is the only module that depends on anything besides _networkx_, it depends on [_numpy_](http://www.numpy.org/), [_scipy_](https://www.scipy.org/) and [_matplotlib_](http://matplotlib.org/).




<h3><a name="contour">The <a href="#contour"><u>contour</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#graphDensityContourPlot"><b>graphDensityContourPlot</b>(<i>G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'</i>)</a></article></li>
<li><article><a href="#quickVisual"><b>quickVisual</b>(<i>G, showLabel=False</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="graphDensityContourPlot"></a><small>contour.</small>**[<ins>graphDensityContourPlot</ins>]({{ site.baseurl }}{{ page.url }}#graphDensityContourPlot)**(_G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured'_):

Creates a 3D plot giving the density of nodes on a 2D plane, as a surface in 3D.

Most of the options are for tweaking the final appearance. _layout_ and _layoutScaleFactor_ allow a pre-layout graph to be provided. If a layout is not provided the [networkx.**spring_layout**()](https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.spring_layout.html) is used after _iters_ iterations. Then, once the graph has been laid out a grid of _axisSamples_ cells by _axisSamples_ cells is overlaid and the number of nodes in each cell is determined, a gaussian blur is then applied with a sigma of _blurringFactor_. This then forms a surface in 3 dimensions, which is then plotted.

If you find the resultant image looks too banded raise the the _contours_ number to ~50.

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

 Default `False`, if `True` the 2D graph will be plotted on the X-Y plane at Z = 0.

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

<a name="quickVisual"></a><small>contour.</small>**[<ins>quickVisual</ins>]({{ site.baseurl }}{{ page.url }}#quickVisual)**(_G, showLabel=False_):

Just makes a simple _matplotlib_ figure and displays it, with each node coloured by its type. You can add labels with _showLabel_. This looks a bit nicer than the one provided my _networkx_'s defaults.

###### Parameters

_showLabel_ : `optional [bool]`

 Default `False`, if `True` labels will be added to the nodes giving their IDs.



---
<a name="WOS"></a>

# [WOS]({{ site.baseurl }}{{ page.url }}#WOS)

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.




<h3><a name="WOS">The <a href="#WOS"><u>WOS</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#recordParser"><b>recordParser</b>(<i>paper</i>)</a></article></li>
<li><article><a href="#getMonth"><b>getMonth</b>(<i>s</i>)</a></article></li>
<li><article><a href="#confHost"><b>confHost</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherAddress"><b>publisherAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#endingPage"><b>endingPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#year"><b>year</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authKeywords"><b>authKeywords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#reprintAddress"><b>reprintAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthor"><b>bookAuthor</b>(<i>val</i>)</a></article></li>
<li><article><a href="#totalTimesCited"><b>totalTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#partNumber"><b>partNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#specialIssue"><b>specialIssue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjects"><b>subjects</b>(<i>val</i>)</a></article></li>
<li><article><a href="#keywords"><b>keywords</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubMedID"><b>pubMedID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#documentDeliveryNumber"><b>documentDeliveryNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookAuthorFull"><b>bookAuthorFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#groupName"><b>groupName</b>(<i>val</i>)</a></article></li>
<li><article><a href="#title"><b>title</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editors"><b>editors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#journal"><b>journal</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesTitle"><b>seriesTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#seriesSubtitle"><b>seriesSubtitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#language"><b>language</b>(<i>val</i>)</a></article></li>
<li><article><a href="#docType"><b>docType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsFull"><b>authorsFull</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confTitle"><b>confTitle</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confDate"><b>confDate</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confSponsors"><b>confSponsors</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosTimesCited"><b>wosTimesCited</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authAddress"><b>authAddress</b>(<i>val</i>)</a></article></li>
<li><article><a href="#confLocation"><b>confLocation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#j9"><b>j9</b>(<i>val</i>)</a></article></li>
<li><article><a href="#funding"><b>funding</b>(<i>val</i>)</a></article></li>
<li><article><a href="#subjectCategory"><b>subjectCategory</b>(<i>val</i>)</a></article></li>
<li><article><a href="#group"><b>group</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citations"><b>citations</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisherCity"><b>publisherCity</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISSN"><b>ISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#articleNumber"><b>articleNumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#issue"><b>issue</b>(<i>val</i>)</a></article></li>
<li><article><a href="#email"><b>email</b>(<i>val</i>)</a></article></li>
<li><article><a href="#eISSN"><b>eISSN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DOI"><b>DOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosString"><b>wosString</b>(<i>val</i>)</a></article></li>
<li><article><a href="#orcID"><b>orcID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pubType"><b>pubType</b>(<i>val</i>)</a></article></li>
<li><article><a href="#editedBy"><b>editedBy</b>(<i>val</i>)</a></article></li>
<li><article><a href="#meetingAbstract"><b>meetingAbstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#isoAbbreviation"><b>isoAbbreviation</b>(<i>val</i>)</a></article></li>
<li><article><a href="#pageCount"><b>pageCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#publisher"><b>publisher</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#month"><b>month</b>(<i>val</i>)</a></article></li>
<li><article><a href="#fundingText"><b>fundingText</b>(<i>val</i>)</a></article></li>
<li><article><a href="#bookDOI"><b>bookDOI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#volume"><b>volume</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ResearcherIDnumber"><b>ResearcherIDnumber</b>(<i>val</i>)</a></article></li>
<li><article><a href="#authorsShort"><b>authorsShort</b>(<i>val</i>)</a></article></li>
<li><article><a href="#citedRefsCount"><b>citedRefsCount</b>(<i>val</i>)</a></article></li>
<li><article><a href="#beginningPage"><b>beginningPage</b>(<i>val</i>)</a></article></li>
<li><article><a href="#abstract"><b>abstract</b>(<i>val</i>)</a></article></li>
<li><article><a href="#supplement"><b>supplement</b>(<i>val</i>)</a></article></li>
<li><article><a href="#wosParser"><b>wosParser</b>(<i>isifile</i>)</a></article></li>
<li><article><a href="#isWOSFile"><b>isWOSFile</b>(<i>infile, checkedLines=3</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="recordParser"></a><small>WOS.</small>**[<ins>recordParser</ins>]({{ site.baseurl }}{{ page.url }}#recordParser)**(_paper_):

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

<a name="getMonth"></a><small>WOS.</small>**[<ins>getMonth</ins>]({{ site.baseurl }}{{ page.url }}#getMonth)**(_s_):

Known formats:
Month ("%b")
Month Day ("%b %d")
Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
Season ("%s") --- this gets coerced to use the first month of the given season
Month Day Year ("%b %d %Y")
Month Year ("%b %Y")


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confHost"></a><small>WOS.</small>**[<ins>confHost</ins>]({{ site.baseurl }}{{ page.url }}#confHost)**(_val_):

###### The HO Tag

extracts the host of the conference

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The host


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherAddress"></a><small>WOS.</small>**[<ins>publisherAddress</ins>]({{ site.baseurl }}{{ page.url }}#publisherAddress)**(_val_):

###### The PA Tag

extracts the publishers address

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="endingPage"></a><small>WOS.</small>**[<ins>endingPage</ins>]({{ site.baseurl }}{{ page.url }}#endingPage)**(_val_):

###### The EP Tag

return the last page the record occurs on as a string, not aall are intergers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The final page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="year"></a><small>WOS.</small>**[<ins>year</ins>]({{ site.baseurl }}{{ page.url }}#year)**(_val_):

###### The PY Tag

extracts the year the record was published in as an int

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The year


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authKeywords"></a><small>WOS.</small>**[<ins>authKeywords</ins>]({{ site.baseurl }}{{ page.url }}#authKeywords)**(_val_):

###### The DE Tag

extracts the keywords assigned by the author of the Record. The WOS description is:

    Author keywords are included in records of articles from 1991 forward. They are also include in conference proceedings records.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of keywords


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="reprintAddress"></a><small>WOS.</small>**[<ins>reprintAddress</ins>]({{ site.baseurl }}{{ page.url }}#reprintAddress)**(_val_):

###### The RP Tag

extracts the reprint address string

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The reprint address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthor"></a><small>WOS.</small>**[<ins>bookAuthor</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthor)**(_val_):

###### The BA Tag

extracts a list of the short names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="totalTimesCited"></a><small>WOS.</small>**[<ins>totalTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#totalTimesCited)**(_val_):

###### The Z9 Tag

extracts the total number of citations of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The total number of citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="partNumber"></a><small>WOS.</small>**[<ins>partNumber</ins>]({{ site.baseurl }}{{ page.url }}#partNumber)**(_val_):

###### The PN Tag

return an integer giving the part of the issue the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The part of the issue of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="specialIssue"></a><small>WOS.</small>**[<ins>specialIssue</ins>]({{ site.baseurl }}{{ page.url }}#specialIssue)**(_val_):

###### The SI Tag

extracts the special issue value

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The special issue value


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjects"></a><small>WOS.</small>**[<ins>subjects</ins>]({{ site.baseurl }}{{ page.url }}#subjects)**(_val_):

###### The WC Tag

extracts a list of subjects as assigned by WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The subjects list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="keywords"></a><small>WOS.</small>**[<ins>keywords</ins>]({{ site.baseurl }}{{ page.url }}#keywords)**(_val_):

###### The ID Tag

extracts the WOS keywords of the Record. The WOS description is:

    KeyWords Plus are index terms created by Thomson Reuters from significant, frequently occurring words in the titles of an article's cited references.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The keyWords list


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubMedID"></a><small>WOS.</small>**[<ins>pubMedID</ins>]({{ site.baseurl }}{{ page.url }}#pubMedID)**(_val_):

###### The PM Tag

extracts the pubmed ID of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The pubmed ID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="documentDeliveryNumber"></a><small>WOS.</small>**[<ins>documentDeliveryNumber</ins>]({{ site.baseurl }}{{ page.url }}#documentDeliveryNumber)**(_val_):

###### The GA Tag

extracts the document delivery number of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The document delivery number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookAuthorFull"></a><small>WOS.</small>**[<ins>bookAuthorFull</ins>]({{ site.baseurl }}{{ page.url }}#bookAuthorFull)**(_val_):

###### The BF Tag

extracts a list of the long names of the authors of a book Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="groupName"></a><small>WOS.</small>**[<ins>groupName</ins>]({{ site.baseurl }}{{ page.url }}#groupName)**(_val_):

###### The CA Tag

extracts the name of the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The group's name


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="title"></a><small>WOS.</small>**[<ins>title</ins>]({{ site.baseurl }}{{ page.url }}#title)**(_val_):

###### The TI Tag

extracts the title of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editors"></a><small>WOS.</small>**[<ins>editors</ins>]({{ site.baseurl }}{{ page.url }}#editors)**(_val_):

###### Needs Work

currently not well understood, returns _val_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="journal"></a><small>WOS.</small>**[<ins>journal</ins>]({{ site.baseurl }}{{ page.url }}#journal)**(_val_):

###### The SO Tag

extracts the full name of the publication and normalizes it to uppercase

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The name of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesTitle"></a><small>WOS.</small>**[<ins>seriesTitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesTitle)**(_val_):

###### The SE Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="seriesSubtitle"></a><small>WOS.</small>**[<ins>seriesSubtitle</ins>]({{ site.baseurl }}{{ page.url }}#seriesSubtitle)**(_val_):

###### The BS Tag

extracts the title of the series the Record is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The subtitle of the series


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="language"></a><small>WOS.</small>**[<ins>language</ins>]({{ site.baseurl }}{{ page.url }}#language)**(_val_):

###### The LA Tag

extracts the languages of the Record as a string with languages separated by ', ', usually there is only one language

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The language(s) of the record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="docType"></a><small>WOS.</small>**[<ins>docType</ins>]({{ site.baseurl }}{{ page.url }}#docType)**(_val_):

###### The DT Tag

extracts the type of document the Record contains

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The type of the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsFull"></a><small>WOS.</small>**[<ins>authorsFull</ins>]({{ site.baseurl }}{{ page.url }}#authorsFull)**(_val_):

###### The AF Tag

extracts a list of authors full names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confTitle"></a><small>WOS.</small>**[<ins>confTitle</ins>]({{ site.baseurl }}{{ page.url }}#confTitle)**(_val_):

###### The CT Tag

extracts the title of the conference associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The title of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confDate"></a><small>WOS.</small>**[<ins>confDate</ins>]({{ site.baseurl }}{{ page.url }}#confDate)**(_val_):

###### The CY Tag

extracts the date string of the conference associated with the Record, the date is not normalized

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The data of the conference


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confSponsors"></a><small>WOS.</small>**[<ins>confSponsors</ins>]({{ site.baseurl }}{{ page.url }}#confSponsors)**(_val_):

###### The SP Tag

extracts a list of sponsors for the conference associated with the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the list of of sponsors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosTimesCited"></a><small>WOS.</small>**[<ins>wosTimesCited</ins>]({{ site.baseurl }}{{ page.url }}#wosTimesCited)**(_val_):

###### The TC Tag

extracts the number of times the Record has been cited by records in WOS

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of time the Record has been cited


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authAddress"></a><small>WOS.</small>**[<ins>authAddress</ins>]({{ site.baseurl }}{{ page.url }}#authAddress)**(_val_):

###### The C1 Tag

extracts the address of the authors as given by WOS. **Warning** the mapping of author to address is not very good and is given in multiple ways.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of addresses


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="confLocation"></a><small>WOS.</small>**[<ins>confLocation</ins>]({{ site.baseurl }}{{ page.url }}#confLocation)**(_val_):

###### The CL Tag

extracts the sting giving the conference's location

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The conferences address


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="j9"></a><small>WOS.</small>**[<ins>j9</ins>]({{ site.baseurl }}{{ page.url }}#j9)**(_val_):

###### The J9 Tag

extracts the J9 (29-Character Source Abbreviation) of the publication

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The 29-Character Source Abbreviation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="funding"></a><small>WOS.</small>**[<ins>funding</ins>]({{ site.baseurl }}{{ page.url }}#funding)**(_val_):

###### The FU Tag

extracts a list of the groups funding the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of funding groups


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="subjectCategory"></a><small>WOS.</small>**[<ins>subjectCategory</ins>]({{ site.baseurl }}{{ page.url }}#subjectCategory)**(_val_):

###### The SC Tag

extracts a list of the subjects associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of the subjects associated with the Record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="group"></a><small>WOS.</small>**[<ins>group</ins>]({{ site.baseurl }}{{ page.url }}#group)**(_val_):

###### The GP Tag

extracts the group associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A the name of the group


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citations"></a><small>WOS.</small>**[<ins>citations</ins>]({{ site.baseurl }}{{ page.url }}#citations)**(_val_):

###### The CR Tag

extracts a list of all the citations in the record, the citations are the [metaknowledge.Citation]({{ site.baseurl }}{{ page.url }}#Citation) class.

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

` list[metaknowledge.Citation]`

 A list of Citations


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisherCity"></a><small>WOS.</small>**[<ins>publisherCity</ins>]({{ site.baseurl }}{{ page.url }}#publisherCity)**(_val_):

###### The PI Tag

extracts the city the publisher is in

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The city of the publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISSN"></a><small>WOS.</small>**[<ins>ISSN</ins>]({{ site.baseurl }}{{ page.url }}#ISSN)**(_val_):

###### The SN Tag

extracts the ISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The ISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="articleNumber"></a><small>WOS.</small>**[<ins>articleNumber</ins>]({{ site.baseurl }}{{ page.url }}#articleNumber)**(_val_):

###### The AR Tag

extracts a string giving the article number, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The article number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="issue"></a><small>WOS.</small>**[<ins>issue</ins>]({{ site.baseurl }}{{ page.url }}#issue)**(_val_):

###### The IS Tag

extracts a string giving the issue or range of issues the Record was in, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The issue number/range


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="email"></a><small>WOS.</small>**[<ins>email</ins>]({{ site.baseurl }}{{ page.url }}#email)**(_val_):

###### The EM Tag

extracts a list of emails given by the authors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of emails


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="eISSN"></a><small>WOS.</small>**[<ins>eISSN</ins>]({{ site.baseurl }}{{ page.url }}#eISSN)**(_val_):

###### The EI Tag

extracts the EISSN of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The EISSN string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DOI"></a><small>WOS.</small>**[<ins>DOI</ins>]({{ site.baseurl }}{{ page.url }}#DOI)**(_val_):

###### The DI Tag

return the DOI number of the record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosString"></a><small>WOS.</small>**[<ins>wosString</ins>]({{ site.baseurl }}{{ page.url }}#wosString)**(_val_):

###### The UT Tag

extracts the WOS number of the record as a string preceded by "WOS:"

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The WOS number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="orcID"></a><small>WOS.</small>**[<ins>orcID</ins>]({{ site.baseurl }}{{ page.url }}#orcID)**(_val_):

###### The OI Tag

extracts a list of orc IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The orc ID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pubType"></a><small>WOS.</small>**[<ins>pubType</ins>]({{ site.baseurl }}{{ page.url }}#pubType)**(_val_):

###### The PT Tag

extracts the type of publication as a character: conference, book, journal, book in series, or patent

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 A string


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="editedBy"></a><small>WOS.</small>**[<ins>editedBy</ins>]({{ site.baseurl }}{{ page.url }}#editedBy)**(_val_):

###### The BE Tag

extracts a list of the editors of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of editors


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="meetingAbstract"></a><small>WOS.</small>**[<ins>meetingAbstract</ins>]({{ site.baseurl }}{{ page.url }}#meetingAbstract)**(_val_):

###### The MA Tag

extracts the ID of the meeting abstract prefixed by 'EPA-'

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The meeting abstract prefixed


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isoAbbreviation"></a><small>WOS.</small>**[<ins>isoAbbreviation</ins>]({{ site.baseurl }}{{ page.url }}#isoAbbreviation)**(_val_):

###### The JI Tag

extracts the iso abbreviation of the journal

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The iso abbreviation of the journal


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pageCount"></a><small>WOS.</small>**[<ins>pageCount</ins>]({{ site.baseurl }}{{ page.url }}#pageCount)**(_val_):

###### The PG Tag

returns an integer giving the number of pages of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The page count


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="publisher"></a><small>WOS.</small>**[<ins>publisher</ins>]({{ site.baseurl }}{{ page.url }}#publisher)**(_val_):

###### The PU Tag

extracts the publisher of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The publisher


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISBN"></a><small>WOS.</small>**[<ins>ISBN</ins>]({{ site.baseurl }}{{ page.url }}#ISBN)**(_val_):

###### The BN Tag

extracts a list of ISBNs associated with the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list`

 The ISBNs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="month"></a><small>WOS.</small>**[<ins>month</ins>]({{ site.baseurl }}{{ page.url }}#month)**(_val_):

###### The PD Tag

extracts the month the record was published in as an int with January as 1, February 2, ...

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 A integer giving the month


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="fundingText"></a><small>WOS.</small>**[<ins>fundingText</ins>]({{ site.baseurl }}{{ page.url }}#fundingText)**(_val_):

###### The FX Tag

extracts a string of the funding thanks

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The funding thank-you


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bookDOI"></a><small>WOS.</small>**[<ins>bookDOI</ins>]({{ site.baseurl }}{{ page.url }}#bookDOI)**(_val_):

###### The D2 Tag

extracts the book DOI of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The DOI number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="volume"></a><small>WOS.</small>**[<ins>volume</ins>]({{ site.baseurl }}{{ page.url }}#volume)**(_val_):

###### The VL Tag

return the volume the record is in as a string, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The volume number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ResearcherIDnumber"></a><small>WOS.</small>**[<ins>ResearcherIDnumber</ins>]({{ site.baseurl }}{{ page.url }}#ResearcherIDnumber)**(_val_):

###### The RI Tag

extracts a list of the research IDs of the Record

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 The list of the research IDs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authorsShort"></a><small>WOS.</small>**[<ins>authorsShort</ins>]({{ site.baseurl }}{{ page.url }}#authorsShort)**(_val_):

###### The AU Tag

extracts a list of authors shortened names

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`list[str]`

 A list of shortened author's names


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="citedRefsCount"></a><small>WOS.</small>**[<ins>citedRefsCount</ins>]({{ site.baseurl }}{{ page.url }}#citedRefsCount)**(_val_):

###### The NR Tag

extracts the number citations, length of CR list

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`int`

 The number of CRs


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="beginningPage"></a><small>WOS.</small>**[<ins>beginningPage</ins>]({{ site.baseurl }}{{ page.url }}#beginningPage)**(_val_):

###### The BP Tag

extracts the first page the record occurs on, not all are integers

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The first page number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="abstract"></a><small>WOS.</small>**[<ins>abstract</ins>]({{ site.baseurl }}{{ page.url }}#abstract)**(_val_):

###### The AB Tag

return abstract of the record, with newlines hopefully in the correct places

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The abstract


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="supplement"></a><small>WOS.</small>**[<ins>supplement</ins>]({{ site.baseurl }}{{ page.url }}#supplement)**(_val_):

###### The SU Tag

extracts the supplement number

###### Parameters

_val_: `list[str]`

 The raw data from a WOS file

###### Returns

`str`

 The supplement number


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="wosParser"></a><small>WOS.</small>**[<ins>wosParser</ins>]({{ site.baseurl }}{{ page.url }}#wosParser)**(_isifile_):

This is function that is used to create [`RecordCollections`]({{ site.baseurl }}{{ page.url }}#RecordCollection) from files.

**wosParser**() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [**recordParser**()]({{ site.baseurl }}{{ page.url }}#recordParser) and converted into [`Records`]({{ site.baseurl }}{{ page.url }}#Record). A list of these `Records` is returned.

`BadWOSFile` is raised if an issue is found with the file.

###### Parameters

_isifile_ : `str`

 The path to the target file

###### Returns

`List[Record]`

 All the `Records` found in _isifile_


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isWOSFile"></a><small>WOS.</small>**[<ins>isWOSFile</ins>]({{ site.baseurl }}{{ page.url }}#isWOSFile)**(_infile, checkedLines=3_):

Determines if _infile_ is the path to a WOS file. A file is considerd to be a WOS file if it has the correct encoding (`utf-8` with a BOM) and within the first _checkedLines_ a line starts with `"VR 1.0"`.

###### Parameters

_infile_ : `str`

 The path to the targets file

_checkedLines_ : `optional [int]`

 default 2, the number of lines to check for the header

###### Returns

`bool`

 `True` if the file is a WOS file



---
<a name="medline"></a>

# [medline]({{ site.baseurl }}{{ page.url }}#medline)

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.




<h3><a name="medline">The <a href="#medline"><u>medline</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#medlineParser"><b>medlineParser</b>(<i>pubFile</i>)</a></article></li>
<li><article><a href="#isMedlineFile"><b>isMedlineFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
<li><article><a href="#medlineRecordParser"><b>medlineRecordParser</b>(<i>record</i>)</a></article></li>
<li><article><a href="#FPS"><b>FPS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TT"><b>TT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PROF"><b>PROF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PHST"><b>PHST</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EFR"><b>EFR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PST"><b>PST</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SPIN"><b>SPIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AU"><b>AU</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FED"><b>FED</b>(<i>val</i>)</a></article></li>
<li><article><a href="#NM"><b>NM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SO"><b>SO</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IP"><b>IP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OABL"><b>OABL</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PUBM"><b>PUBM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRDT"><b>CRDT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DDIN"><b>DDIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MH"><b>MH</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DP"><b>DP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GN"><b>GN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRF"><b>CRF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TI"><b>TI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CRI"><b>CRI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OT"><b>OT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ROF"><b>ROF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CN"><b>CN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OTO"><b>OTO</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OID"><b>OID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PT"><b>PT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RPI"><b>RPI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AB"><b>AB</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EN"><b>EN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AD"><b>AD</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LA"><b>LA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MHDA"><b>MHDA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#TA"><b>TA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#JT"><b>JT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IRAD"><b>IRAD</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PS"><b>PS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IS"><b>IS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PL"><b>PL</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CTI"><b>CTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FAU"><b>FAU</b>(<i>val</i>)</a></article></li>
<li><article><a href="#VTI"><b>VTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DCOM"><b>DCOM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LID"><b>LID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#BTI"><b>BTI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CI"><b>CI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#STAT"><b>STAT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DRIN"><b>DRIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RF"><b>RF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#UIN"><b>UIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#LR"><b>LR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#IR"><b>IR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SFM"><b>SFM</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EIN"><b>EIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AID"><b>AID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#EDAT"><b>EDAT</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PRIN"><b>PRIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DEP"><b>DEP</b>(<i>val</i>)</a></article></li>
<li><article><a href="#AUID"><b>AUID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SI"><b>SI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ISBN"><b>ISBN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RN"><b>RN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#JID"><b>JID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GR"><b>GR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OCI"><b>OCI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#SB"><b>SB</b>(<i>val</i>)</a></article></li>
<li><article><a href="#DA"><b>DA</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMCR"><b>PMCR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PG"><b>PG</b>(<i>val</i>)</a></article></li>
<li><article><a href="#GS"><b>GS</b>(<i>val</i>)</a></article></li>
<li><article><a href="#VI"><b>VI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#UOF"><b>UOF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#FIR"><b>FIR</b>(<i>val</i>)</a></article></li>
<li><article><a href="#OWN"><b>OWN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#ORI"><b>ORI</b>(<i>val</i>)</a></article></li>
<li><article><a href="#MID"><b>MID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMID"><b>PMID</b>(<i>val</i>)</a></article></li>
<li><article><a href="#PMC"><b>PMC</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RIN"><b>RIN</b>(<i>val</i>)</a></article></li>
<li><article><a href="#RPF"><b>RPF</b>(<i>val</i>)</a></article></li>
<li><article><a href="#CIN"><b>CIN</b>(<i>val</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="medlineParser"></a><small>medline.</small>**[<ins>medlineParser</ins>]({{ site.baseurl }}{{ page.url }}#medlineParser)**(_pubFile_):

Parses a medline file, _pubFile_, to extract the individual entries as [`MedlineRecords`]({{ site.baseurl }}{{ page.url }}#MedlineRecord).

A medline file is a series of entries, each entry is a series of tags. A tag is a 2 to 4 character string each tag is padded with spaces on the left to make it 4 characters which is followed by a dash and a space (`'- '`). Everything after the tag and on all lines after it not starting with a tag is considered associated with the tag. Each entry's first tag is `PMID`, so a first line looks something like `PMID- 26524502`. Entries end with a single blank line.

###### Parameters

_pubFile_ : `str`

 A path to a valid medline file, use [`isMedlineFile`]({{ site.baseurl }}{{ page.url }}#isMedlineFile) to verify

###### Returns

`set[MedlineRecord]`

 Records for each of the entries


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isMedlineFile"></a><small>medline.</small>**[<ins>isMedlineFile</ins>]({{ site.baseurl }}{{ page.url }}#isMedlineFile)**(_infile, checkedLines=2_):

Determines if _infile_ is the path to a Medline file. A file is considerd to be a Medline file if it has the correct encoding (`latin-1`) and within the first _checkedLines_ a line starts with `"PMID- "`.

###### Parameters

_infile_ : `str`

 The path to the targets file

_checkedLines_ : `optional [int]`

 default 2, the number of lines to check for the header

###### Returns

`bool`

 `True` if the file is a Medline file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="medlineRecordParser"></a><small>medline.</small>**[<ins>medlineRecordParser</ins>]({{ site.baseurl }}{{ page.url }}#medlineRecordParser)**(_record_):

The parser [`MedlineRecord`]({{ site.baseurl }}{{ page.url }}#MedlineRecord) use. This takes an entry from [`medlineParser()`]({{ site.baseurl }}{{ page.url }}#medlineParser) and parses it a part of the creation of a `MedlineRecord`.

###### Parameters

_record_ : `enumerate object`

 a file wrapped by `enumerate()`

###### Returns

`collections.OrderedDict`

 An ordered dictionary of the key-vaue pairs in the entry


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="FPS"></a><small>medline.</small>**[<ins>FPS</ins>]({{ site.baseurl }}{{ page.url }}#FPS)**(_val_):

FullPersonalNameSubject


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="TT"></a><small>medline.</small>**[<ins>TT</ins>]({{ site.baseurl }}{{ page.url }}#TT)**(_val_):

TransliteratedTitle


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PROF"></a><small>medline.</small>**[<ins>PROF</ins>]({{ site.baseurl }}{{ page.url }}#PROF)**(_val_):

PartialRetractionOf


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PHST"></a><small>medline.</small>**[<ins>PHST</ins>]({{ site.baseurl }}{{ page.url }}#PHST)**(_val_):

PublicationHistoryStatus


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="EFR"></a><small>medline.</small>**[<ins>EFR</ins>]({{ site.baseurl }}{{ page.url }}#EFR)**(_val_):

ErratumFor


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PST"></a><small>medline.</small>**[<ins>PST</ins>]({{ site.baseurl }}{{ page.url }}#PST)**(_val_):

PublicationStatus


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="SPIN"></a><small>medline.</small>**[<ins>SPIN</ins>]({{ site.baseurl }}{{ page.url }}#SPIN)**(_val_):

SummaryForPatients


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="AU"></a><small>medline.</small>**[<ins>AU</ins>]({{ site.baseurl }}{{ page.url }}#AU)**(_val_):

Author


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="FED"></a><small>medline.</small>**[<ins>FED</ins>]({{ site.baseurl }}{{ page.url }}#FED)**(_val_):

Editor


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="NM"></a><small>medline.</small>**[<ins>NM</ins>]({{ site.baseurl }}{{ page.url }}#NM)**(_val_):

SubstanceName


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="SO"></a><small>medline.</small>**[<ins>SO</ins>]({{ site.baseurl }}{{ page.url }}#SO)**(_val_):

Source


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="IP"></a><small>medline.</small>**[<ins>IP</ins>]({{ site.baseurl }}{{ page.url }}#IP)**(_val_):

Issue


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OABL"></a><small>medline.</small>**[<ins>OABL</ins>]({{ site.baseurl }}{{ page.url }}#OABL)**(_val_):

OtherAbstract


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PUBM"></a><small>medline.</small>**[<ins>PUBM</ins>]({{ site.baseurl }}{{ page.url }}#PUBM)**(_val_):

PublishingModel


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CRDT"></a><small>medline.</small>**[<ins>CRDT</ins>]({{ site.baseurl }}{{ page.url }}#CRDT)**(_val_):

CreateDate


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DDIN"></a><small>medline.</small>**[<ins>DDIN</ins>]({{ site.baseurl }}{{ page.url }}#DDIN)**(_val_):

DatasetIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="MH"></a><small>medline.</small>**[<ins>MH</ins>]({{ site.baseurl }}{{ page.url }}#MH)**(_val_):

MeSHTerms


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DP"></a><small>medline.</small>**[<ins>DP</ins>]({{ site.baseurl }}{{ page.url }}#DP)**(_val_):

DatePublication


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="GN"></a><small>medline.</small>**[<ins>GN</ins>]({{ site.baseurl }}{{ page.url }}#GN)**(_val_):

GeneralNote


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CRF"></a><small>medline.</small>**[<ins>CRF</ins>]({{ site.baseurl }}{{ page.url }}#CRF)**(_val_):

CorrectedRepublishedFrom


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="TI"></a><small>medline.</small>**[<ins>TI</ins>]({{ site.baseurl }}{{ page.url }}#TI)**(_val_):

Title
only one per record


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CRI"></a><small>medline.</small>**[<ins>CRI</ins>]({{ site.baseurl }}{{ page.url }}#CRI)**(_val_):

CorrectedRepublishedIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OT"></a><small>medline.</small>**[<ins>OT</ins>]({{ site.baseurl }}{{ page.url }}#OT)**(_val_):

OtherTerm
Nothing needs to be done


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ROF"></a><small>medline.</small>**[<ins>ROF</ins>]({{ site.baseurl }}{{ page.url }}#ROF)**(_val_):

RetractionOf


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CN"></a><small>medline.</small>**[<ins>CN</ins>]({{ site.baseurl }}{{ page.url }}#CN)**(_val_):

CorporateAuthor


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OTO"></a><small>medline.</small>**[<ins>OTO</ins>]({{ site.baseurl }}{{ page.url }}#OTO)**(_val_):

OtherTermOwner
one line field


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OID"></a><small>medline.</small>**[<ins>OID</ins>]({{ site.baseurl }}{{ page.url }}#OID)**(_val_):

OtherID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PT"></a><small>medline.</small>**[<ins>PT</ins>]({{ site.baseurl }}{{ page.url }}#PT)**(_val_):

PublicationType


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="RPI"></a><small>medline.</small>**[<ins>RPI</ins>]({{ site.baseurl }}{{ page.url }}#RPI)**(_val_):

RepublishedIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="AB"></a><small>medline.</small>**[<ins>AB</ins>]({{ site.baseurl }}{{ page.url }}#AB)**(_val_):

Abstract
basically a one liner after parsing


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="EN"></a><small>medline.</small>**[<ins>EN</ins>]({{ site.baseurl }}{{ page.url }}#EN)**(_val_):

Edition


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="AD"></a><small>medline.</small>**[<ins>AD</ins>]({{ site.baseurl }}{{ page.url }}#AD)**(_val_):

Affiliation
Undoing what the parser does then splitting at the semicolons and dropping newlines extra fitlering is required beacuse some AD's end with a semicolon


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="LA"></a><small>medline.</small>**[<ins>LA</ins>]({{ site.baseurl }}{{ page.url }}#LA)**(_val_):

Language


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="MHDA"></a><small>medline.</small>**[<ins>MHDA</ins>]({{ site.baseurl }}{{ page.url }}#MHDA)**(_val_):

MeSHDate


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="TA"></a><small>medline.</small>**[<ins>TA</ins>]({{ site.baseurl }}{{ page.url }}#TA)**(_val_):

JournalTitleAbbreviation
One line only


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="JT"></a><small>medline.</small>**[<ins>JT</ins>]({{ site.baseurl }}{{ page.url }}#JT)**(_val_):

JournalTitle
One line only


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="IRAD"></a><small>medline.</small>**[<ins>IRAD</ins>]({{ site.baseurl }}{{ page.url }}#IRAD)**(_val_):

InvestigatorAffiliation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PS"></a><small>medline.</small>**[<ins>PS</ins>]({{ site.baseurl }}{{ page.url }}#PS)**(_val_):

PersonalNameSubject


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="IS"></a><small>medline.</small>**[<ins>IS</ins>]({{ site.baseurl }}{{ page.url }}#IS)**(_val_):

ISSN


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PL"></a><small>medline.</small>**[<ins>PL</ins>]({{ site.baseurl }}{{ page.url }}#PL)**(_val_):

PlacePublication


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CTI"></a><small>medline.</small>**[<ins>CTI</ins>]({{ site.baseurl }}{{ page.url }}#CTI)**(_val_):

CollectionTitle


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="FAU"></a><small>medline.</small>**[<ins>FAU</ins>]({{ site.baseurl }}{{ page.url }}#FAU)**(_val_):

FullAuthor


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="VTI"></a><small>medline.</small>**[<ins>VTI</ins>]({{ site.baseurl }}{{ page.url }}#VTI)**(_val_):

VolumeTitle


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DCOM"></a><small>medline.</small>**[<ins>DCOM</ins>]({{ site.baseurl }}{{ page.url }}#DCOM)**(_val_):

DateCompleted


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="LID"></a><small>medline.</small>**[<ins>LID</ins>]({{ site.baseurl }}{{ page.url }}#LID)**(_val_):

LocationIdentifier


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="BTI"></a><small>medline.</small>**[<ins>BTI</ins>]({{ site.baseurl }}{{ page.url }}#BTI)**(_val_):

BookTitle


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CI"></a><small>medline.</small>**[<ins>CI</ins>]({{ site.baseurl }}{{ page.url }}#CI)**(_val_):

CopyrightInformation


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="STAT"></a><small>medline.</small>**[<ins>STAT</ins>]({{ site.baseurl }}{{ page.url }}#STAT)**(_val_):

Status


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DRIN"></a><small>medline.</small>**[<ins>DRIN</ins>]({{ site.baseurl }}{{ page.url }}#DRIN)**(_val_):

DatasetUseReportedIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="RF"></a><small>medline.</small>**[<ins>RF</ins>]({{ site.baseurl }}{{ page.url }}#RF)**(_val_):

NumberReferences


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="UIN"></a><small>medline.</small>**[<ins>UIN</ins>]({{ site.baseurl }}{{ page.url }}#UIN)**(_val_):

UpdateIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="LR"></a><small>medline.</small>**[<ins>LR</ins>]({{ site.baseurl }}{{ page.url }}#LR)**(_val_):

DateLastRevised


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="IR"></a><small>medline.</small>**[<ins>IR</ins>]({{ site.baseurl }}{{ page.url }}#IR)**(_val_):

Investigator


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="SFM"></a><small>medline.</small>**[<ins>SFM</ins>]({{ site.baseurl }}{{ page.url }}#SFM)**(_val_):

SpaceFlightMission


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="EIN"></a><small>medline.</small>**[<ins>EIN</ins>]({{ site.baseurl }}{{ page.url }}#EIN)**(_val_):

ErratumIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="AID"></a><small>medline.</small>**[<ins>AID</ins>]({{ site.baseurl }}{{ page.url }}#AID)**(_val_):

ArticleIdentifier
The given values do not require any work


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="EDAT"></a><small>medline.</small>**[<ins>EDAT</ins>]({{ site.baseurl }}{{ page.url }}#EDAT)**(_val_):

EntrezDate


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PRIN"></a><small>medline.</small>**[<ins>PRIN</ins>]({{ site.baseurl }}{{ page.url }}#PRIN)**(_val_):

PartialRetractionIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DEP"></a><small>medline.</small>**[<ins>DEP</ins>]({{ site.baseurl }}{{ page.url }}#DEP)**(_val_):

DateElectronicPublication


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="AUID"></a><small>medline.</small>**[<ins>AUID</ins>]({{ site.baseurl }}{{ page.url }}#AUID)**(_val_):

AuthorIdentifier
one line only just need to undo the parser's effects


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="SI"></a><small>medline.</small>**[<ins>SI</ins>]({{ site.baseurl }}{{ page.url }}#SI)**(_val_):

SecondarySourceID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ISBN"></a><small>medline.</small>**[<ins>ISBN</ins>]({{ site.baseurl }}{{ page.url }}#ISBN)**(_val_):

ISBN


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="RN"></a><small>medline.</small>**[<ins>RN</ins>]({{ site.baseurl }}{{ page.url }}#RN)**(_val_):

RegistryNumber


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="JID"></a><small>medline.</small>**[<ins>JID</ins>]({{ site.baseurl }}{{ page.url }}#JID)**(_val_):

NLMID


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="GR"></a><small>medline.</small>**[<ins>GR</ins>]({{ site.baseurl }}{{ page.url }}#GR)**(_val_):

GrantNumber


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OCI"></a><small>medline.</small>**[<ins>OCI</ins>]({{ site.baseurl }}{{ page.url }}#OCI)**(_val_):

OtherCopyright


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="SB"></a><small>medline.</small>**[<ins>SB</ins>]({{ site.baseurl }}{{ page.url }}#SB)**(_val_):

Subset


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="DA"></a><small>medline.</small>**[<ins>DA</ins>]({{ site.baseurl }}{{ page.url }}#DA)**(_val_):

DateCreated


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PMCR"></a><small>medline.</small>**[<ins>PMCR</ins>]({{ site.baseurl }}{{ page.url }}#PMCR)**(_val_):

PubMedCentralRelease


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PG"></a><small>medline.</small>**[<ins>PG</ins>]({{ site.baseurl }}{{ page.url }}#PG)**(_val_):

Pagination
all pagination seen so far seems to be only on one line


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="GS"></a><small>medline.</small>**[<ins>GS</ins>]({{ site.baseurl }}{{ page.url }}#GS)**(_val_):

GeneSymbol


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="VI"></a><small>medline.</small>**[<ins>VI</ins>]({{ site.baseurl }}{{ page.url }}#VI)**(_val_):

Volume
The volumes as a string as volume is single line


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="UOF"></a><small>medline.</small>**[<ins>UOF</ins>]({{ site.baseurl }}{{ page.url }}#UOF)**(_val_):

UpdateOf


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="FIR"></a><small>medline.</small>**[<ins>FIR</ins>]({{ site.baseurl }}{{ page.url }}#FIR)**(_val_):

InvestigatorFull


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="OWN"></a><small>medline.</small>**[<ins>OWN</ins>]({{ site.baseurl }}{{ page.url }}#OWN)**(_val_):

Owner


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="ORI"></a><small>medline.</small>**[<ins>ORI</ins>]({{ site.baseurl }}{{ page.url }}#ORI)**(_val_):

OriginalReportIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="MID"></a><small>medline.</small>**[<ins>MID</ins>]({{ site.baseurl }}{{ page.url }}#MID)**(_val_):

ManuscriptIdentifier


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PMID"></a><small>medline.</small>**[<ins>PMID</ins>]({{ site.baseurl }}{{ page.url }}#PMID)**(_val_):

PubMedUniqueIdentifier


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="PMC"></a><small>medline.</small>**[<ins>PMC</ins>]({{ site.baseurl }}{{ page.url }}#PMC)**(_val_):

PubMedCentralIdentifier


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="RIN"></a><small>medline.</small>**[<ins>RIN</ins>]({{ site.baseurl }}{{ page.url }}#RIN)**(_val_):

RetractionIn


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="RPF"></a><small>medline.</small>**[<ins>RPF</ins>]({{ site.baseurl }}{{ page.url }}#RPF)**(_val_):

RepublishedFrom


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="CIN"></a><small>medline.</small>**[<ins>CIN</ins>]({{ site.baseurl }}{{ page.url }}#CIN)**(_val_):

CommentIn



---
<a name="proquest"></a>

# [proquest]({{ site.baseurl }}{{ page.url }}#proquest)

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.




<h3><a name="proquest">The <a href="#proquest"><u>proquest</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#proQuestParser"><b>proQuestParser</b>(<i>proFile</i>)</a></article></li>
<li><article><a href="#isProQuestFile"><b>isProQuestFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
<li><article><a href="#proQuestRecordParser"><b>proQuestRecordParser</b>(<i>enRecordFile, recNum</i>)</a></article></li>
<li><article><a href="#proQuestTagToFunc"><b>proQuestTagToFunc</b>(<i>tag</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="proQuestParser"></a><small>proquest.</small>**[<ins>proQuestParser</ins>]({{ site.baseurl }}{{ page.url }}#proQuestParser)**(_proFile_):

Parses a ProQuest file, _proFile_, to extract the individual entries.

A ProQuest file has three sections, first a list of the contained entries, second the full metadata and finally a bibtex formatted entry for the record. This parser only uses the first two as the bibtex contains no information the second section does not. Also, the first section is only used to verify the second section. The returned [`ProQuestRecords`]({{ site.baseurl }}{{ page.url }}#ProQuestRecord) contains the data from the second section, with the same key strings as ProQuest uses and the unlabeled sections are called in order, `'Name'`, `'Author'` and `'url'`.

###### Parameters

_proFile_ : `str`

 A path to a valid ProQuest file, use [`isProQuestFile`]({{ site.baseurl }}{{ page.url }}#isProQuestFile) to verify

###### Returns

`set[ProQuestRecord]`

 Records for each of the entries


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isProQuestFile"></a><small>proquest.</small>**[<ins>isProQuestFile</ins>]({{ site.baseurl }}{{ page.url }}#isProQuestFile)**(_infile, checkedLines=2_):

Determines if _infile_ is the path to a ProQuest file. A file is considered to be a Proquest file if it has the correct encoding (`utf-8`) and within the first _checkedLines_ the following starts.

    ____________________________________________________________

    Report Information from ProQuest

###### Parameters

_infile_ : `str`

 The path to the targets file

_checkedLines_ : `optional [int]`

 default 2, the number of lines to check for the header

###### Returns

`bool`

 `True` if the file is a valid ProQuest file


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="proQuestRecordParser"></a><small>proquest.</small>**[<ins>proQuestRecordParser</ins>]({{ site.baseurl }}{{ page.url }}#proQuestRecordParser)**(_enRecordFile, recNum_):

The parser [`ProQuestRecords`]({{ site.baseurl }}{{ page.url }}#ProQuestRecord) use. This takes an entry from [`proQuestParser()`]({{ site.baseurl }}{{ page.url }}#proQuestParser) and parses it a part of the creation of a `ProQuestRecord`.

###### Parameters

_enRecordFile_ : `enumerate object`

 a file wrapped by `enumerate()`

_recNum_ : `int`

 The number given to the entry in the first section of the ProQuest file

###### Returns

`collections.OrderedDict`

 An ordered dictionary of the key-vaue pairs in the entry


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="proQuestTagToFunc"></a><small>proquest.</small>**[<ins>proQuestTagToFunc</ins>]({{ site.baseurl }}{{ page.url }}#proQuestTagToFunc)**(_tag_):

Takes a tag string, _tag_, and returns the processing function for its data. If their is not a predefined function returns the identity function (`lambda x : x`).

###### Parameters

_tag_ : `str`

 The requested tag

###### Returns

`function`

 A function to process the tag's data



---
<a name="scopus"></a>

# [scopus]({{ site.baseurl }}{{ page.url }}#scopus)

These are the functions used to process scopus csv files at the backend. They are meant for use internal use by metaknowledge.




<h3><a name="scopus">The <a href="#scopus"><u>scopus</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#scopusRecordParser"><b>scopusRecordParser</b>(<i>record</i>)</a></article></li>
<li><article><a href="#scopusParser"><b>scopusParser</b>(<i>scopusFile</i>)</a></article></li>
<li><article><a href="#isScopusFile"><b>isScopusFile</b>(<i>infile, checkedLines=2</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="scopusRecordParser"></a><small>scopus.</small>**[<ins>scopusRecordParser</ins>]({{ site.baseurl }}{{ page.url }}#scopusRecordParser)**(_record_):

The parser [`ScopusRecords`]({{ site.baseurl }}{{ page.url }}#ScopusRecord) use. This takes a line from [`scopusParser()`]({{ site.baseurl }}{{ page.url }}#scopusParser) and parses it as a part of the creation of a `ScopusRecord`.

**Note** this is for csv files downloaded from scopus _not_ the text records as those are less complete. Also, Scopus uses double quotes (`"`) to quote strings, such as abstracts, in the csv so double quotes in the string must be escaped. For reasons not fully understandable by mortals they choose to use two double quotes in a row (`""`) to represent an escaped double quote. This parser does not unescape these quotes, but it does correctly handle their interacts with the outer double quotes.

###### Parameters

_record_ : `str`

 string ending with a newline containing the record's entry

###### Returns

`dict`

 A dictionary of the key-vaue pairs in the entry


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="scopusParser"></a><small>scopus.</small>**[<ins>scopusParser</ins>]({{ site.baseurl }}{{ page.url }}#scopusParser)**(_scopusFile_):

Parses a scopus file, _scopusFile_, to extract the individual lines as [`ScopusRecords`]({{ site.baseurl }}{{ page.url }}#ScopusRecord).

A Scopus file is a csv (Comma-separated values) with a complete header, see [`scopus.scopusHeader`]({{ site.baseurl }}{{ page.url }}#scopus) for the entries, and each line after it containing a record's entry. The string valued entries are quoted with double quotes which means double quotes inside them can cause issues, see [`scopusRecordParser()`]({{ site.baseurl }}{{ page.url }}#scopusRecordParser) for more information.

###### Parameters

_scopusFile_ : `str`

 A path to a valid scopus file, use [`isScopusFile()`]({{ site.baseurl }}{{ page.url }}#isScopusFile) to verify

###### Returns

`set[ScopusRecord]`

 Records for each of the entries


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="isScopusFile"></a><small>scopus.</small>**[<ins>isScopusFile</ins>]({{ site.baseurl }}{{ page.url }}#isScopusFile)**(_infile, checkedLines=2_):

Determines if _infile_ is the path to a Scopus csv file. A file is considerd to be a Scopus file if it has the correct encoding (`utf-8` with BOM (Byte Order Mark)) and within the first _checkedLines_ a line contains the complete header, the list of all header entries in order is found in [`scopus.scopusHeader`]({{ site.baseurl }}{{ page.url }}#scopus).

**Note** this is for csv files _not_ plain text files from scopus, plain text files are not complete.

###### Parameters

_infile_ : `str`

 The path to the targets file

_checkedLines_ : `optional [int]`

 default 2, the number of lines to check for the header

###### Returns

`bool`

 `True` if the file is a Scopus csv file



---
<a name="journalAbbreviations"></a>

# [journalAbbreviations]({{ site.baseurl }}{{ page.url }}#journalAbbreviations)

This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in WOS Records and for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function [**updatej9DB**()](#getj9dict) is used to scape and parse the pages, it must be run without error before the other features can be used. _metaknowledge_. If the database is requested by `getj9dict()`, which is what [`Citations`](#Citation) use, and the database is not found or is corrupted then [`updatej9DB()`](#updatej9DB) will be run to download the database if this fails an `mkException` will be raised, the download and parsing usually takes less than a second on a good internet connection.

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool `metaknowledge` instead of with a script.




<h3><a name="journalAbbreviations">The <a href="#journalAbbreviations"><u>journalAbbreviations</u></a> module provides the following functions:</a></h3>

<ol class="post-list">
<li><article><a href="#getj9dict"><b>getj9dict</b>(<i>dbname='j9Abbreviations', manualDB='manualj9Abbreviations', returnDict='both'</i>)</a></article></li>
<li><article><a href="#addToDB"><b>addToDB</b>(<i>abbr=None, dbname='manualj9Abbreviations'</i>)</a></article></li>
</ol>
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



{% include docsFooter.md %}