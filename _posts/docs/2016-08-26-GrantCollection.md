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
<li><article><a href="#networkCoInvestigator"><b>networkCoInvestigator</b>(<i>institutionLevel=False, targetTags=None, tagSeperator=';', count=True, weighted=True</i>)</a></article></li>
</ol>
<hr style="padding: 0;border: none;border-width: 3px;height: 20px;color: #333;text-align: center;border-top-style: solid;border-bottom-style: solid;">

<a name="networkCoInvestigator"></a><small>GrantCollection.</small>**[<ins>networkCoInvestigator</ins>]({{ site.baseurl }}{{ page.url }}#networkCoInvestigator)**(_institutionLevel=False, targetTags=None, tagSeperator=';', count=True, weighted=True_):

Works for only some grant types



{% include docsFooter.md %}