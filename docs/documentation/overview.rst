########
Overview
########

This package can read the files downloaded from the Thomson Reuters’ `Web of Science <https://webofknowledge.com>`_ (*WOS*), Elsevier’s `Scopus <https://www.scopus.com/>`_, `ProQuest <http://www.proquest.com/>`_ and Medline files from `PubMed <http://www.ncbi.nlm.nih.gov/pubmed>`_. These files contain entries on the metadata of scientific records, such as authors, title, and citations. *metaknowledge* can also read grants from various organizations including *NSF* and *NSERC* which are handled similarly to records.

The `metaknowledge.RecordCollection <./classes/RecordCollection.html#recordcollection-collectionwithids>`_ class can take a path to one or more of these files load and parse them. The object is the main way for work to be done on multiple records. For each individual record it creates an instance of the `metaknowledge.Record <./classes/Record.html#record-mapping-hashable>`_ class that contains the results of the parsing of the record.

The files read by *metaknowledge* are a databases containing a series of tags (implicitly or explicitly), e.g. ``'TI'`` is the title for WOS. Each tag has one or more values and metaknowledge can read them and extract useful information. As the tags differ between providers a small set of values can be accessed by special tags, the tags are listed in ``commonRecordFields``. These special tags can act on the whole ``Record`` and as such may contain information provided by any number of other tags.

Citations are handled by a special `Citation <./classes/Citation.html#module-metaknowledge.citation>`_ class. This class can parse the citations given by *WOS* and journals cited by *Scopus* and allows for better comparisons when they are used in graphs.

Note for those reading the docstrings metaknowledge’s docs are written in markdown and are processed to produce the documentation found at `metaknowledge.readthedocs.io <https://metaknowledge.readthedocs.io/en/latest/>`_, but you should have no problem reading them from the help function.


.. toctree::
   :maxdepth: 2
   :caption: Overview:
