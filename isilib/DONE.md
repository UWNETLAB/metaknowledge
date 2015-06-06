#DONE

##Citation Class
* a way of containing citation strings to allow comparison and manipulation
* initialized with a string, the string is then parsed and used to create the Citation object
* will be set to bad if the citation appears malformed, too many numbers only fields or to few fields

###Builtins
* equality testing is possible, it first checks DOIs if one or both are missing, then all the other fields, if any fields disagree the result is False else if anything but volume and page number are absent in only one the result is False
* hashable, hashes of equal Citations are not always equal
* if the author is "\[ANONYMOUS\]" the citation's author will nit beused for equality checking
* \_\_str\_\_ gives the original string
* Citations can have the following properties obtained from the original:
   - DOI
   - author
   - journal
   - V
   - P
   - misc
      + catchall for everything the preceding ones did not contain
* if misc has anything it is likely the citation is not of the usual form
* bad property is set True if the source string had issues, then the error property can be used to determine the exact issue

###Methods
* isAnonymous, returns True if the Citation has an ANONYMOUS author
* getID, returns a string of author, year. This is for creating simple networks
* getExtra, returns everything getID does not as a string

###Usual citation form
````
"author, year, journal, V#, P#, DOI #"
"THURSTON WP, 1994, B AM MATH SOC, V30, P161, DOI 10.1090/S0273-0979-1994-00502-6"
````


##Record Class
* If classified as bad most functions will not work, i.e. return None
   - Might be worth reconsidering this
* Contains a dict of tags and values read from the record
* Uses lazy evaluation only reads from tag value dictionary once
* uses WOS number as unique id
* are considered bad if the original record threw and error during parse or was missing WOS number
* meant to be immutable
* can be tagged by any number of strings

###Builtins
* \_\_str\_\_ gives title of record
* equality testing
* hashable, uses WOS number for seed, bad Records are likely to cause hash collisions
* copiable and pickle-able, using field tags dict instead of full \_\_dict\_\_
* Can be initialized with tags

###Methods
(Function return what they stay they return)
* functions that attempt to return clean data:
   - title
   - wosString
   - year
   - month
   - authors
      + full name
      + shortend name
   - citations
   - journal
      + full name
      + J9
   - first page
   - last page
   - volume number
   - DOI
   - abstract

* general WOS tag extraction:
   - Needs a better wrapper but works
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
* inequalities use number of records for comparison
* work as iterators, iterating over the records

##Methods
* dropBadRecords() and getBadRecords() allow removal or analysis of bad records
* yearSplit gets papers with some range of years
* extracttagged allows removing records with some tag
* Networks it can produce:
   - co-authorship
   - co-citation
      + drop anonymous records
      + use authorship instead of citations
      + write full citations as extra information
      + can be weighted
   - citation
      + drop anonymous records
      + use authorship instead of citations
      + write full citations as extra information
      + can be weighted
* writeFile() writes the RecordCollection as an WOS file
   - The output is usually bit for bit identical to a file download from WOS, although record order is not maintained
* pop, returns a random record and removes it from the collection


##Profiling
- in progress
