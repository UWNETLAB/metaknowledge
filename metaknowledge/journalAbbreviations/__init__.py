#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in WOS Records and for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function [updatej9DB()](#metaknowledge.journalAbbreviations.backend.getj9dict) is used to scape and parse the pages, it must be run without error before the other features can be used. _metaknowledge_. If the database is requested by `getj9dict()`, which is what [Citations](../classes/Citation.html#metaknowledge.citation.Citation) use, and the database is not found or is corrupted then [updatej9DB()](#metaknowledge.journalAbbreviations.backend.updatej9DB) will be run to download the database if this fails an `mkException` will be raised, the download and parsing usually takes less than a second on a good internet connection.

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool `metaknowledge` instead of with a script.
"""

from .backend import getj9dict, abrevDBname, manualDBname, addToDB
