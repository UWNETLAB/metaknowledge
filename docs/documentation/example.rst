##############
Basic Example
##############

*metaknoweldge* is a Python3 package that simplifies bibliometric and computational analysis of Web of Science data.

To load the data from files and make a network: ::
  >>> import metaknowledge as mk
  >>> RC = mk.RecordCollection("records/")
  >>> print(RC)
  Collection of 33 records
  >>> G = RC.coCiteNetwork(nodeType = 'journal')
  Done making a co-citation network of files-from-records                 1.1s
  >>> print(len(G.nodes()))
  223
  >>> mk.writeGraph(G, "Cocitation-Network-of-Journals")

There is also a simple command line program called ``metaknowledge`` that comes with the package. It allows for creating networks without any need to know Python. More information about it can be found `here <../CLI.html>`_.

.. toctree::
   :maxdepth: 2
   :caption: Example:
