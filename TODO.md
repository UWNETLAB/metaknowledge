# Grants
+ **Done** Finish NSERC processor
+ Complete how-to guide
+ **In Progress** Add tests
+ **Done** Integrate with pubmed
+ **Done** Integrate with Records in general
+ **Done** Think about encoding more
    - every option is terrible
    - going with utf-8, because unix
+ Add more methods
+ Performance test
+ **Done** Think about caching
    - Added to GrantCollections
    - Still terrible

# Citations
+ **Will not do** Make a `Record`
    - Doesn't make sense
+ **Done** Integrate with `Grants`
    - Nothing really to do

# Records
+ Allow large files to be read
+ Add tests
+ Complete how-to guide
+ Add ProQuest

# Collections
+ **Done** Think about general collection (Grants and Records and ...)
    - Maybe
+ Add tests
+ **Done** Clean up interfaces of the network generators
+ Add more methods for dealing with mk objects

# Diffusion
+ For the diffusion networks. I am sorry I can’t remember if we have this specific function, but can we make it so that you can create any network you want from the first record collection (e.g. co-citation) where the number of counts each article has in the second collection is an attribute for the nodes in the network from the first collection.
    - For the diffusion, the use scenario is: I want to look at the association between various centrality measures within the POS networks and uptake in the science collection.
    - but it would also be good to have seperate counts for each of the area designations / disciplines they come from.
    - and I assume we could also do this for whatever the level of the network is for the first collection. e.g. if it is documents, then count documents from record collection 2, if it is authors, authors, if it is journals, journals, etc.

+ Add option for including records from network

# General
+ Make installable
+ Add tests
+ Lint
+ Make organization make sense
+ Make names make sense
+ Remove `import *`
+ **Done** Update CLI
+ Update vagrant/notebooks
+ Update docs/website

#Diffusion
+ Differences between journals (in phil of science) that have uptake in the science and those that do not
+ Phil science cites less than most, also slow to publish -> low thresholds
+ Decades should be the final graph size, if not possible, at least 5 years
+ Data set is 60s-00s, max 2014
+ Data set is maximal, based on top/field defining
+ pubs is the publication by an author
+ cites is everything citing them
+ using `'WC'` for classifying, maybe `'ID'`
+ make a list and counts of `'WC'` tags from data set
