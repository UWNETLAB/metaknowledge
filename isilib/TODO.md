#TODO

## Implementation
### Add more documentation
###remove general exceptions
### Record class

* maybe do geocoding

### RecordCollection class
* extract subset from more ranges
* add more methods to create networks
* extract Locations

## Cleaning and Preprocessing WOS data

* [reconcile journal names](http://cishell.wiki.cns.iu.edu/Reconcile+Journal+Names). link includes a link to the source code, and a download to an Excel file with journal names.

* Add graph handling helper functions
 + Drop edges
 + drop nodes

### citation, co-citation, co-author, bibliographic coupling, etc.  

+ Make output networks from subsets of Collection

* bibliographic coupling
    - Mainly to get location
    - to get institutional collaboration networks
    - to group records based on similar bibliographies (this is less important to me than getting institutional networks)

* community detection for all ^ networks
   - Blondel community detection algorithm seems to be the best

* whenever a new network is created, print info:
    - whether directed or undirected
    - number of nodes and edges
    - number of nodes in the giant component
    - number of isolates

## Content: Burst Detection, Topics, etc.

### Burst Detection XXXXXX

Sci^2 is capable of burst detection, which was originally implemented in C, and then rewritten by the Sci^2 team in Java. You can read about it [here](http://cishell.wiki.cns.iu.edu/Burst+Detection). There is a link to their source code (which fails on my machine), and to the original C implementation. Burst detection is *really* useful for identifying changes over time.

* burst detection for keywords
* burst detection for authors
* burst detection for documents
* burst detection for references

##Make Lessons
- Write more lessons

##WOS
- 61 tags found so far
   + most still need functions
- Write up known information about each in some user friendly way, i.e. md or pdf of all the tags
