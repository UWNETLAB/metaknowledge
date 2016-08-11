---
layout: doc
title: ExtendedRecord
categories: docs
excerpt: A Record the processes its contents before returning them
tags: [class]
weight: 2
---
<a name="ExtendedRecord"></a>
<a name="ExtendedRecord"></a><small></small>**[<ins>ExtendedRecord</ins>]({{ site.baseurl }}{{ page.url }}#ExtendedRecord)**(_<a href="#Record"><u style="border-bottom: .5px dashed gray;">Record</u></a>_):

<a name="ExtendedRecord.__init__"></a><small></small>**[<ins>ExtendedRecord.__init__</ins>]({{ site.baseurl }}{{ page.url }}#ExtendedRecord.__init__)**(_fieldDict, idValue, bad, error, sFile='', sLine=0_):

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
<li><article><a href="#getCitations"><b>getCitations</b>(<i>field=None, values=None, pandasFriendly=True</i>)</a></article></li>
<li><article><a href="#subDict"><b>subDict</b>(<i>tags, raw=False</i>)</a></article></li>
<li><article><a href="#createCitation"><b>createCitation</b>(<i>multiCite=False</i>)</a></article></li>
<li><article><a href="#authGenders"><b>authGenders</b>(<i>countsOnly=False, fractionsMode=False</i>)</a></article></li>
<li><article><a href="#bibString"><b>bibString</b>(<i>maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True</i>)</a></article></li>
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

<a name="getCitations"></a><small>ExtendedRecord.</small>**[<ins>getCitations</ins>]({{ site.baseurl }}{{ page.url }}#getCitations)**(_field=None, values=None, pandasFriendly=True_):

# Needs to be written

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


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="authGenders"></a><small>ExtendedRecord.</small>**[<ins>authGenders</ins>]({{ site.baseurl }}{{ page.url }}#authGenders)**(_countsOnly=False, fractionsMode=False_):

# Needs to be written

<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="bibString"></a><small>ExtendedRecord.</small>**[<ins>bibString</ins>]({{ site.baseurl }}{{ page.url }}#bibString)**(_maxLength=1000, WOSMode=False, restrictedOutput=False, niceID=True_):

Makes a string giving the Record as a bibTex entry. If the Record is of a journal article (`PT J`) the bibtext type is set to `'article'`, otherwise it is set to `'misc'`. The ID of the entry is the WOS number and all the Record's fields are given as entries with their long names.

**Note** This is not meant to be used directly with LaTeX none of the special characters have been escaped and there are a large number of unnecessary fields provided. _niceID_ and _maxLength_ have been provided to make conversions easier.

**Note** Record entries that are lists have their values seperated with the string `' and '`

###### Parameters

_maxLength_ : `optional [int]`

 default 1000, The max length for a continuous string. Most bibTex implementation only allow string to be up to 1000 characters ([source](https://www.cs.arizona.edu/~collberg/Teaching/07.231/BibTeX/bibtex.html)), this splits them up into substrings then uses the native string concatenation (the `'#'` character) to allow for longer strings

_WOSMode_ : `optional [bool]`

 default `False`, if `True` the data produced will be unprocessed and use double curly braces. This is the style WOS produces bib files in and mostly macthes that.

_restrictedOutput_ : `optional [bool]`

 default `False`, if `True` the tags output will be limited to tose found in `metaknowledge.commonRecordFields`

_niceID_ : `optional [bool]`

 default `True`, if `True` the ID used will be derived from the authors, publishing date and title, if `False` it will be the UT tag

###### Returns

`str`

 The bibTex string of the Record



{% include docsFooter.md %}