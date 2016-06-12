---
layout: doc
title: ScopusRecord
categories: docs
excerpt: The object for containing and processing Scopus entries
tags: [class]
weight: 2
---
<a name="ScopusRecord"></a>
<a name="ScopusRecord"></a><small></small>**[<ins>ScopusRecord</ins>]({{ site.baseurl }}{{ page.url }}#ScopusRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="ScopusRecord.__init__"></a><small></small>**[<ins>ScopusRecord.__init__</ins>]({{ site.baseurl }}{{ page.url }}#ScopusRecord.__init__)**(_inRecord, sFile='', sLine=0_):

Class for full Scopus entries.

This class is an [`ExtendedRecord`]({{ site.baseurl }}{{ page.url }}#ExtendedRecord) capable of generating its own id number. You should not create them directly, but instead use [`scopusParser()`]({{ site.baseurl }}{{ page.url }}#scopusParser) on a scopus **CSV** file.


<h3>
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



{% include docsFooter.md %}