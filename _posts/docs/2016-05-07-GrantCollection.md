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



{% include docsFooter.md %}