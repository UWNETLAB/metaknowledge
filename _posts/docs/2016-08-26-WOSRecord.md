---
layout: doc
title: WOSRecord
categories: docs
excerpt: The object for containing and processing WOS entries
tags: [class]
weight: 2
---
<a name="WOSRecord"></a>
<a name="WOSRecord"></a><small></small>**[<ins>WOSRecord</ins>]({{ site.baseurl }}{{ page.url }}#WOSRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="WOSRecord.__init__"></a><small></small>**[<ins>WOSRecord.__init__</ins>]({{ site.baseurl }}{{ page.url }}#WOSRecord.__init__)**(_inRecord, sFile='', sLine=0_):

Class for full WOS records

It is meant to be immutable; many of the methods and attributes are evaluated when first called, not when the object is created, and the results are stored privately.

The record's meta-data is stored in an ordered dictionary labeled by WOS tags. To access the raw data stored in the original record the [**Tag**()]({{ site.baseurl }}{{ page.url }}#Tag) method can be used. To access data that has been processed and cleaned the attributes named after the tags are used.

##### Customizations

The `Record`'s hashing and equality testing are based on the WOS number (the tag is 'UT', and also called the accession number). They are strings starting with `'WOS:'` and followed by 15 or so numbers and letters, although both the length and character set are known to vary. The numbers are unique to each record so are used for comparisons. If a record is `bad`  all equality checks return `False`.

When converted to a string the records title is used so for a record `R`, `R.TI == R.title == str(R)` and its representation uses the WOS number instead of memory location.

##### Attributes

When a record is created if the parsing of the WOS file failed it is marked as `bad`. The `bad` attribute is set to True and the `error` attribute is created to contain the exception object.

Generally, to get the information from a Record its attributes should be used. For a Record `R`, calling `R.CR` causes [**citations**()]({{ site.baseurl }}{{ page.url }}#citations) from the the [tagProcessing]({{ site.baseurl }}{{ page.url }}#tagProcessing) module to be called on the contents of the raw 'CR' field. Then the result is saved and returned. In this case, a list of Citation objects is returned. You can also call `R.citations` to get the same effect, as each known field tag has a longer name (currently there are 61 field tags). These names are meant to make accessing tags more readable and mapping from tag to name can be found in the tagToFull dict. If a tag is known (in [tagToFull]({{ site.baseurl }}{{ page.url }}#metaknowledge)) but not in the raw data `None` is returned instead. Most tags when cleaned return a string or list of strings, the exact results can be found in the help for the particular function.

The attribute `authors` is also defined as a convenience and returns the same as 'AF' or if that is not found 'AU'.

##### \_\_Init\_\_

Records are generally create as collections in  [Recordcollections]({{ site.baseurl }}{{ page.url }}#RecordCollection), and not as individual objects. If you wish to create one on its own it is possible, the arguments are as follows.

##### Parameters

_inRecord_: `files stream, dict, str or itertools.chain`

 If it is a file stream the file must be open at the location of the first tag in the record, usually 'PT', and the file will be read until 'ER' is found, which indicates the end of the record in the file.

 If a dict is passed the dictionary is used as the database of fields and tags, so each key is considered a WOS tag and each value a list of the lines of the original associated with the tag. This is the same form of dict that [recordParser]({{ site.baseurl }}{{ page.url }}#recordParser) returns.

 For a string the input must be the raw textual data of a single record in the WOS style, like the file stream it must start at the first tag and end in `'ER'`.

 itertools.chain is treated identically to a file stream and is used by [RecordCollections]({{ site.baseurl }}{{ page.url }}#RecordCollection).

_sFile_ : `optional [str]`

 Is the name of the file the raw data was in, by default it is blank. It is mostly used to make error messages more informative.

_sLine_ : `optional [int]`

 Is the line the record starts on in the raw data file. It is mostly used to make error messages more informative.


<h3>
The WOSRecord class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#tagProcessingFunc"><b>tagProcessingFunc</b>(<i>tag</i>)</a></article></li>
<li><article><a href="#specialFuncs"><b>specialFuncs</b>(<i>key</i>)</a></article></li>
<li><article><a href="#writeRecord"><b>writeRecord</b>(<i>infile</i>)</a></article></li>
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



{% include docsFooter.md %}