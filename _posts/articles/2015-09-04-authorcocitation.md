---
layout: post
title: "Contruct an Author Co-Citation Network"
excerpt: "You want to construct a weighted co-citation network of authors."
categories: articles
tags: [preprocessing, dataframe]
author: john
comments: true
share: false
image:
  feature:
  credit:
  creditlink:
---

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{% highlight python %}
import metaknowledge as mk
import networkx as nx 
import matplotlib.pyplot as plt 

RC = mk.RecordCollection('/path/to/directory/with/WoS/files')

print(RC)

tags = ['AU', 'TI','AB', 'SO', 'LA', 'C1', 'RP', 'CR', 'TC', 'PY']
RC.writeCSV('data/rc_can_soc.csv', onlyTheseTags = tags) 
{% endhighlight %}

Filter to a subset of records that cite a specific author...

{% highlight python %}
authorname = RC.citeFilter(keyString='someauthor',  field='all', reverse=False, caseSensitive=False)
print(len(authorname))

authorname.writeCSV('authorname.csv', onlyTheseTags = tags) 
{% endhighlight %}
