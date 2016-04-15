---
layout: doc
title: Collection
categories: docs
excerpt: The base of all other Collections, basically a set
tags: [class]
weight: 2
---
<a name="Collection"></a>
<a name="Collection"></a><small></small>**[<ins>Collection</ins>]({{ site.baseurl }}{{ page.url }}#Collection)**(_MutableSet, Hashable_):

<a name="Collection.__init__"></a><small></small>**[<ins>Collection.__init__</ins>]({{ site.baseurl }}{{ page.url }}#Collection.__init__)**(_inSet, allowedTypes, collectedTypes, name, bad, errors, quietStart=False_):

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


<h3>
The Collection class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#add"><b>add</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#discard"><b>discard</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#remove"><b>remove</b>(<i>elem</i>)</a></article></li>
<li><article><a href="#clear"><b>clear</b>()</a></article></li>
<li><article><a href="#pop"><b>pop</b>()</a></article></li>
<li><article><a href="#copy"><b>copy</b>()</a></article></li>
<li><article><a href="#peak"><b>peak</b>()</a></article></li>
<li><article><a href="#chunk"><b>chunk</b>(<i>maxSize</i>)</a></article></li>
<li><article><a href="#split"><b>split</b>(<i>maxSize</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="add"></a><small>Collection.</small>**[<ins>add</ins>]({{ site.baseurl }}{{ page.url }}#add)**(_elem_):

Add an element.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="discard"></a><small>Collection.</small>**[<ins>discard</ins>]({{ site.baseurl }}{{ page.url }}#discard)**(_elem_):

Remove an element.  Do not raise an exception if absent.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="remove"></a><small>Collection.</small>**[<ins>remove</ins>]({{ site.baseurl }}{{ page.url }}#remove)**(_elem_):

Remove an element. If not a member, raise a KeyError.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="clear"></a><small>Collection.</small>**[<ins>clear</ins>]({{ site.baseurl }}{{ page.url }}#clear)**():

This is slow (creates N new iterators!) but effective.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="pop"></a><small>Collection.</small>**[<ins>pop</ins>]({{ site.baseurl }}{{ page.url }}#pop)**():

Return the popped value.  Raise KeyError if empty.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="copy"></a><small>Collection.</small>**[<ins>copy</ins>]({{ site.baseurl }}{{ page.url }}#copy)**():

# Needs to be written

<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="peak"></a><small>Collection.</small>**[<ins>peak</ins>]({{ site.baseurl }}{{ page.url }}#peak)**():

# Needs to be written

<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="chunk"></a><small>Collection.</small>**[<ins>chunk</ins>]({{ site.baseurl }}{{ page.url }}#chunk)**(_maxSize_):

# Needs to be written

<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="split"></a><small>Collection.</small>**[<ins>split</ins>]({{ site.baseurl }}{{ page.url }}#split)**(_maxSize_):

destructive



{% include docsFooter.md %}