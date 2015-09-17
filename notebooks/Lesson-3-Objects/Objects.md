# Objects


In _Python_ everything is an object thus everything _metaknowledge_ produces is an object. There are three objects that have been created specifically for it,  objects created this way are call classes. The three are `Record` a single WOS record, `RecordCollection` a group of `Records` and `Citation` a single WOS citation.

Lets import _metaknowledge_ and read a file

[]import metaknowledge as mk
[]RC = mk.RecordCollection('../savedrecs.txt') # '..' is one directory above the current one

Now we can look at how the different objects relate to this file.


# `Record` object


[`Record`](http://networkslab.org/metaknowledge/docs/Record#Record) is an object that contains a simple WOS record, for example a journal article, book, or conference proceedings. They are what [`RecordCollections`](http://networkslab.org/metaknowledge/docs/RecordCollection#RecordCollection) contain. To see an individual [`Record`](http://networkslab.org/metaknowledge/docs/Record#Record) at random from a `RecordCollection` you can use `peak()`

[]R = RC.peak()

A single `Record` can give you all the information it contains about its record. If for example you want its authors.

[]print(R.authorsFull)
[]print(R.AF)

Converting a `Record` to a string will give its title

[]print(R)

If you try to access a tag the `Record` does not have it will return `None`

[]print(R.GP)

There are two ways of getting each tag, one is using the WOS 2 letter abbreviation and the second is to use the human readable name. There is no standard for the human readable names, so they are specific to _metaknowledge_. To see how the WOS names map to the long names look at [tagFuncs](http://networkslab.org/metaknowledge/docs/tagFuncs#tagFuncs). If you want all the tags a `Record` has use [`activeTags()`]((http://networkslab.org/metaknowledge/docs/Record#activeTags).

[]print(R.activeTags())


# `RecordCollection` object


[`RecordCollection`](http://networkslab.org/metaknowledge/docs/RecordCollection#RecordCollection) is the object that _metaknowledge_ uses the most. It is your interface with the data you want.

To iterate over all of the `Records` you can use a for loop

[]for R in RC:
[]    print(R)

The individual `Records` are index by their WOS numbers so you can access a specific one in the collection if you know its number.

[]RC.getWOS("WOS:A1979GV55600001")


# `Citation` object


[`Citation`](http://networkslab.org/metaknowledge/docs/Citation#Citation) is an object to contain the results of parsing a citation. They can be created from a `Record`

[]Cite = R.createCitation()
[]print(Cite)

`Citations` allow for the raw strings of citations to be manipulated easily by _metaknowledge_.

#Filtering


The for loop shown above is the main way to filter a RecordCollection, that said there are a few builtin filters, e.g. [`yearSplit()`](http://networkslab.org/metaknowledge/docs/RecordCollection#yearSplit), but the for loop is an easily generalized way of filtering that is relatively simple to read so it the main way you should filter. An example of the workflow is as follows:


First create a new RecordCollection

[]RCfiltered = mk.RecordCollection()

Then add the records that meet your condition, in this case that their title's start with `'A'`

[1]for R in RC:
[1]    if R.title[0] == 'A':
[1]        RCfiltered.addRec(R)
[2]print(RCfiltered)

Now you have a RecordCollection `RCfiltered` of all the `Records` whose titles begin with `'A'`.

One note about implementing this, the above code does not handle the case in which the title is missing i.e. `R.title` is `None`. You will have to deal with this on your own.


Two builtin functions to filter collections are [`yearSplit()`](http://networkslab.org/metaknowledge/docs/RecordCollection#yearSplit) and [`localCitesOf()`](http://networkslab.org/metaknowledge/docs/RecordCollection#localCitesOf). To get a RecordCollection of all Records between 1970 and 1979:

[]RC70 = RC.yearSplit(1970, 1979)
[]print(RC70)

The second function [`localCitesOf()`](http://networkslab.org/metaknowledge/docs/RecordCollection#localCitesOf) takes in an object that a [Citation](http://networkslab.org/metaknowledge/docs/Citation#Citation) can be created from and returns a RecordCollection of all the Records that cite it. So to see all the records that cite `"Yariv A., 1971, INTRO OPTICAL ELECTR"`.

[]RCintroOpt = RC.localCitesOf("Yariv A., 1971, INTRO OPTICAL ELECTR")
[]print(RCintroOpt)


# Exporting RecordCollections


Now you have a filtered RecordCollection you can write it as a file with [`writeFile()`](http://networkslab.org/metaknowledge/docs/RecordCollection#writeFile)

[] RCfiltered.writeFile("Records_Starting_with_A.txt")

The written file is identical to one of those produced by WOS.


If you wish to have a more useful file use [`writeCSV()`](http://networkslab.org/metaknowledge/docs/RecordCollection#writeCSV) which creates a CSV file of all the tags as columns and the Records as rows. IF you only care about a few tags the `onlyTheseTags` argument allows you to control the tags.

[]selectedTags = ['TI', 'UT', 'CR', 'AF']

This will give only the title, WOS number, citations, and authors.

[]RCfiltered.writeCSV("Records_Starting_with_A.csv", onlyTheseTags = selectedTags)


The last export feature is for using _metaknowledge_ with other packages, in particular [_pandas_](http://pandas.pydata.org/), which you will learn about later, but others should also work. [`makeDict()`](http://networkslab.org/metaknowledge/docs/RecordCollection#makeDict) creates a dictionary with tags as keys and lists as values with each index of the lists corresponding to a Record. _pandas_ can accept these directly to make DataFrames.

[]import pandas
[]recDataFrame = pandas.DataFrame(RC.makeDict())
