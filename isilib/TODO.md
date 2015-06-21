#TODO

##Unknown tags
- GP
   + Group?
- BF
   + book something
- GA might have two meanings, groupAuthors or documentDeliveryNumber

## Implementation
### Add more documentation
###remove general exceptions
### Record class
* add methods for every important tag
* maybe do geocoding
* Fix Lazy eval
### RecordCollection class
* extract subset from more ranges
* add more methods to create networks
* look a error handling
   - addition needs work
* Consider making network checks more in depth
* reconsider how directories are handled

### Citation
* mark paper's citaions in CiteNetwork
* example edge case
   - Centraal Bureau voor de Statistiek, 2010, 200 JAAR STAT TIJDR

## Cleaning and Preprocessing WOS data

* [reconcile journal names](http://cishell.wiki.cns.iu.edu/Reconcile+Journal+Names). link includes a link to the source code, and a download to an Excel file with journal names.

* Add graph handling helper functions

### citation, co-citation, co-author, bibliographic coupling, etc.  

* extract citation networks DONE

    - Filter by within record set only *or* "core and references" / unrestricted
        + paper citation networks
        + author citation networks
        + source citation networks

* extract co-citation networks DONE
      - filter by
        + author co-citation
        + source co-citation

* extract co-author networks DONE
    - again, this is *great,* but would be even better if it could be based on a specific time frame specified by the researcher

* bibliographic coupling
    - Mainly to get location
    - to get institutional collaboration networks
    - to group records based on similar bibliographies (this is less important to me than getting institutional networks)

* two-mode networks
    - paper and: SO, WC, SC, or keywords
    - author and: SO, WC, SC, or keywords
    - looks like there is a link to Sci^2 source code for 2 mode networks [here](http://cishell.wiki.cns.iu.edu/Bipartite+Network+Graph)

* community detection for all ^ networks
    - the Blondel / Louvain community detection algorithm is not available in iGraph, but Sci^2 has the Blondel version, and NetworkX has the Louvain version. can you include it in the scripts above so community membership attributes are included in the graphml file? however it would be good if this was easy to quickly turn off if I want to speed things up. I prefer Blondel (2008), but Louvain is fine. **Note that this should only work for 1 mode networks. There are different methods for community detection in 2 mode networks. Perhaps you can look into them.**

* whenever a new network is created (e.g. by co-citeMaker.py), print:
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

##Make Study plans/examples
