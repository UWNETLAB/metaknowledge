metaknowledge
=========================================
*A Python3 package for doing computational research on knowledge*

*metaknowledge* is a Python3_ package for doing computational research in bibliometrics, scientometrics, and network analysis. It can also be easily used to simplify the process of doing systematic reviews in any disciplinary context.

*metaknowledge* reads a directory of plain text files containing meta-data on publications and citations, and writes to a variety of data structures that are suitable for longitudinal research, computational text analysis (e.g. topic models and burst analysis), Reference Publication Year Spectroscopy (RPYS), and network analysis (including multi-modal, multi-level, and dynamic). It handles large datasets (e.g. several million records) efficiently.

metaknowledge currently handles data from the Web of Science, PubMed, Scopus, Proquest Dissertations & Theses, and administrative data from the National Science Foundation and the Canadian tri-council granting agencies: SSHRC, CIHR, and NSERC.

Datasets created with metaknowledge can be analyzed using NetworkX_ and the `standard libraries <http://www.scipy.org/about.html>`_ for data analysis in Python. It is also easy to write data to :code:`csv` or :code:`graphml` files for analysis and visualization in `R <http://www.r-project.org>`_, `Stata <http://www.stata.com>`_, `Visone <http://visone.info>`_, `Gephi <http://gephi.github.io>`_, or any other tools for data analysis.

*metaknowledge* also has a simple command line tool for extracting quantitative datasets and network files from Web of Science files. This makes the library more accessible to researchers who do not know Python, and makes it easier to quickly explore new datasets.

Contact
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| **Reid McIlroy-Young**, `reid@reidmcy.com <mailto:reid@reidmcy.com>`_
| *University of Chicago, Chicago, IL, USA*

| **John McLevey**, `john.mclevey@uwaterloo.ca <mailto:john.mclevey@uwaterloo.ca>`_
| *University of Waterloo, Waterloo, ON, Canada*

| **Jillian Anderson**, `jillianderson8@gmail.com <mailto:jillianderson8@gmail.com>`_
| *University of Waterloo, Waterloo, ON, Canada*

Citation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are using metaknowledge for research that will be published or publicly distributed, please acknowledge us with the following citation:

  *Reid McIlroy-Young, John McLevey, and Jillian Anderson. 2015. metaknowledge: open source software for social networks, bibliometrics, and sociology of knowledge research. URL: http://www.networkslab.org/metaknowledge.*

`Download .bib file: <Download .bib file:>`_

License
^^^^^^^
*metaknowledge* is free and open source software, distributed under the GPL License.


.. toctree::
   :maxdepth: 1

   install
   documentation/index
   examples/index
   CLI


Indices and tables
^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Python3: https://www.python.org
.. _NetworkX: https://networkx.github.io