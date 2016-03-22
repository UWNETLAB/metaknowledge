---
layout: page
title: Command Line Tool
excerpt: "How to use the metaknowledge command line tool."
tags: CLI
---

The metaknowledge comes with a command-line application named `metaknowledge`. This provides a simple interface to the python package an allows the generation of most of networks along with ways to manage the records themselves.

## Overview

To start the tool run:

{% highlight bash %}
$ metaknowledge
{% endhighlight %}

You will be asked for the location of the file or files to use. These can be given by paths to the files or paths to directories with the files. Note, if a directory is used all files the the proper header will be read.

You will then be asked what to do with the records:

    A collection of 537 WOS records has been created
    What do you wish to do with it:
    1) Make a graph
    2) Write the collection as a single WOS style file
    3) Write the collection as a single WOS style file and make a graph
    4) Write the collection as a single csv file
    5) Write the collection as a single csv file and make a graph
    6) Write all the citations to a single file
    7) Go over non-journal citations
    i) open python console
    q) quit
    What is your selection:

Select the option you want by typing the corresponding number or character and pressing enter. The menus after this step are controlled this way as well.

The second last option `i)` will start an interactive python session will all the objects you have created thus far accessible, their names will be given when it starts.

The last option `q)` will cause the program to exit. You can also quit at any time by pressing `ctr-c`.


{% include docsFooter.md %}
