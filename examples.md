---
layout: page
title: Examples
---
isilib is intended to be user friendly and most arguments have many default options  

```python
import isilib

RC = isilib.RecordCollection("example_file.isi") #loading an WOS file
print(RC) #Collection of 100 records
G = RC.twoModeNetwork('title', 'CR') #Generating a title-citation
isilib.write_graph(G, "title-citation_Network") #Writing the edge list and the node attribute file of the network
```

## Command Line Tool

In progress
