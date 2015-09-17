# Reading Files


First we need to import _metaknowledge_ like we saw in lesson 1.

[]import metaknowledge as mk

we only need _metaknowledge_ for now so no need to import everything


The files from the Web of Science (WOS) can be loaded into a [`RecordCollections`](http://networkslab.org/metaknowledge/docs/RecordCollection#RecordCollection) by creating a `RecordCollection` with the path to the files given to it as a string.

[]RC = mk.RecordCollection("savedrecs.txt")
[]repr(RC)

You can also read a whole directory, in this case it is reading the current working directory

[]RC = mk.RecordCollection(".")
[]repr(RC)

_metaknowledge_ can detect if a file is a valid WOS file or not and will read the entire directory and load only those that have the right header. You can also tell it to only read a certain type of file, by using the extension argument.

[]RC = mk.RecordCollection(".", extension = "txt")
[]repr(RC)

Now you have a `RecordCollection` composed of all the WOS records in the selected file(s).

[]print("RC is a " + str(RC))

You might have noticed I used two different ways to display the `RecordCollection`. `repr(RC)` will give you where _metaknowledge_ thinks the collection came from. While `str(RC)` will give you a nice string containing the number of `Records`.
