---
layout: doc
title: GrantCollection
categories: docs
excerpt: A Collection of Grants, this is what does most of the stuff on Grants
tags: [class]
weight: 2
---
<a name="GrantCollection"></a>
<a name="GrantCollection"></a><small></small>**[<ins>GrantCollection</ins>]({{ site.baseurl }}{{ page.url }}#GrantCollection)**(_<a href="#CollectionWithIDs"><u style="border-bottom: .5px dashed gray;">CollectionWithIDs</u></a>_):

<a name="GrantCollection.__init__"></a><small></small>**[<ins>GrantCollection.__init__</ins>]({{ site.baseurl }}{{ page.url }}#GrantCollection.__init__)**(_inGrants=None, name='', extension='', cached=False, quietStart=False_):

A [`Collection`]({{ site.baseurl }}{{ page.url }}#Collection) with a few extra methods that assume all the contained items have an id attribute and a bad attribute, e.g. [`Records`]({{ site.baseurl }}{{ page.url }}#Record) or [`Grants`]({{ site.baseurl }}{{ page.url }}#Grant).

\_\_Init\_\_

As `CollectionWithIDs` is mostly meant to be base for other classes all but one of the arguments in the `__init__` are not optional and the optional one is not used. The `__init__()` function is the same as a [`Collection`]({{ site.baseurl }}{{ page.url }}#Collection).


<h3>
The GrantCollection class has the following methods:</h3>

<ol class="post-list">
<li><article><a href="#networkCoInstitution"><b>networkCoInstitution</b>(<i>targetTags=None, tagSeperator=';', count=True, weighted=True</i>)</a></article></li>
<li><article><a href="#networkCoInvestigator"><b>networkCoInvestigator</b>(<i>targetTags=None, tagSeperator=';', count=True, weighted=True</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCoInstitution"></a><small>GrantCollection.</small>**[<ins>networkCoInstitution</ins>]({{ site.baseurl }}{{ page.url }}#networkCoInstitution)**(_targetTags=None, tagSeperator=';', count=True, weighted=True_):

This works the same as [`networkCoInvestigator()`]({{ site.baseurl }}{{ page.url }}#networkCoInvestigator) see it for details.


<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCoInvestigator"></a><small>GrantCollection.</small>**[<ins>networkCoInvestigator</ins>]({{ site.baseurl }}{{ page.url }}#networkCoInvestigator)**(_targetTags=None, tagSeperator=';', count=True, weighted=True_):

Creates a co-investigator from the collection

Most grants do not have a known investigator tag so it must be provided by the user in _targetTags_ and the separator character if it is not a semicolon should also be given.

###### Parameters

 _targetTags_ : `optional list[str]`

 A list of all the Grant tags to check for investigators

_tagSeperator_ : `optional str`

 The character that separates the individual investigator's names

_count_ : `optional bool`

 Default `True`, if `True` the number of time a name occurs will be given

_weighted_ : `optional bool`

 Default `True`, if `True` the edge weights will be calculated and added to the edges

###### Returns

`networkx Graph`

 The graph of co-investigator



{% include docsFooter.md %}