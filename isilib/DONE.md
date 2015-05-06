#DONE

##Record Class
* If classified as bad no most functions will not work
* Contains a dict of tags and values read from the record
* Uses lazy evaluation only reads from tag value dictionary once
* uses WOS number as unique id
* are considered bad if the original record threw and error during parse or was missing WOS number
* meant to be immutable

###Builtins
* \_\_str\_\_ gives title of record
* equality testing
* hashable, uses WOS number for seed, bad Records are likely to cause hash collisions
* copiable and pickleable, using field tags dict instead of full \_\_dict\_\_

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

##RecordCollection Class
* a set of unique papers
* does not care if the papers are good or not, although many methods will only use the good ones
* can be constructed with a path to a ISI file or a list/set of records
* contains a set of records
* mutable

###Builtins
* \_\_str\_\_ gives number of records
* equality, merge, subtract, includes and xor builtins implemented for comparing two collections


##Methods
* dropBadRecords and getBadRecords allow removal or analysis of bad records
* yearSplit gets papers with some range of years
* Networks it can produce:
   - co-authorship
   - co-citation
