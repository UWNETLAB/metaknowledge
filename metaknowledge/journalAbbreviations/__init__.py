#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in records, for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function [**updatej9DB**()](#journalAbbreviations.getj9dict) is used to scape and parse the pages, it must be run without error before the other features can be used. _metaknowledge_ will try running it once during the installation but it could easily have been canceled or failed so it is best to it manually. **updatej9DB**() creates a database in the _metaknowledge_ install directory that gives each abbreviation and the titles it corresponds to, note there can be many titles for one abbreviation. The database can be accessed as a dictionary with [**getj9dict**()](#journalAbbreviations.getj9dict).

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool `metaknowledge`, unless you know what you are doing.
"""

from .backend import getj9dict, abrevDBname, manaulDBname, addToDB
