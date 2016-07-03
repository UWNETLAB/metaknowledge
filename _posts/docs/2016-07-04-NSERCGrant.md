---
layout: doc
title: NSERCGrant
categories: docs
excerpt: The container for NSERC grant entries
tags: [class]
weight: 2
---
<a name="NSERCGrant"></a>
<a name="NSERCGrant"></a><small></small>**[<ins>NSERCGrant</ins>]({{ site.baseurl }}{{ page.url }}#NSERCGrant)**(_<a href="#Grant"><u style="border-bottom: .5px dashed gray;">Grant</u></a>_):

<a name="NSERCGrant.__init__"></a><small></small>**[<ins>NSERCGrant.__init__</ins>]({{ site.baseurl }}{{ page.url }}#NSERCGrant.__init__)**(_original, grantdDict, sFile, sLine_):

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



{% include docsFooter.md %}