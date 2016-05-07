---
layout: doc
title: MedlineRecord
categories: docs
excerpt: The object for containing and processing Medline entries
tags: [class]
weight: 2
---
<a name="MedlineRecord"></a>
<a name="MedlineRecord"></a><small></small>**[<ins>MedlineRecord</ins>]({{ site.baseurl }}{{ page.url }}#MedlineRecord)**(_<a href="#ExtendedRecord"><u style="border-bottom: .5px dashed gray;">ExtendedRecord</u></a>_):

<a name="MedlineRecord.__init__"></a><small></small>**[<ins>MedlineRecord.__init__</ins>]({{ site.baseurl }}{{ page.url }}#MedlineRecord.__init__)**(_inRecord, sFile='', sLine=0_):

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

The `__init__` of `ExtendedRecord` takes the same arguments as [`Record`]({{ site.baseurl }}{{ page.url }}#Record)


<h3>
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
        



{% include docsFooter.md %}