#DONE

##Record Class
* If classified as bad most functions will not work, i.e. return None
   - Might be worth reconsidering this
* Contains a dict of tags and values read from the record
* Uses lazy evaluation only reads from tag value dictionary once
* uses WOS number as unique id
* are considered bad if the original record threw and error during parse or was missing WOS number
* meant to be immutable

###Builtins
* \_\_str\_\_ gives title of record
* equality testing
* hashable, uses WOS number for seed, bad Records are likely to cause hash collisions
* copiable and pickle-able, using field tags dict instead of full \_\_dict\_\_

###Methods
(Function return what they stay they return)
* functions that attempt to return clean data:
   - title
   - wosString
   - year
   - month
   - authors
* functions that return unclean data:
   - citations
* general tag extraction:
   - individual
   - by list, returns a dict or list
* writeRecord() writes the file exactly as it was given


##RecordCollection Class
* a set of unique papers
* does not care if the papers are good or not, although many methods will only use the good ones
* can be constructed with a path to a ISI file or a list/set of records
* contains a set of records
* mutable
* duplicate records are deleted when a RecordCollection is formed

###Builtins
* \_\_str\_\_ gives number of records
* \_\_repr\_\_ gives a string with the original name of the record collection and all the modifications made to it in order
* equality, merge, subtract, includes and xor builtins implemented for comparing two collections

##Methods
* dropBadRecords() and getBadRecords() allow removal or analysis of bad records
* yearSplit gets papers with some range of years
* Networks it can produce:
   - co-authorship
   - co-citation
* writeFile() writes the RecordCollection as an WOS file
   - The output is usually identical to a file download from WOS
