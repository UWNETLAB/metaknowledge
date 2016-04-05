#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from .mkExceptions import BadCitation

import abc
try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections
import re

import metaknowledge

class Citation(collections.abc.Hashable):
    """A class to hold citation strings and allow for comparison between them.

    The initializer takes in a string representing a WOS citation in the form:

        Author, Year, Journal, Volume, Page, DOI

    `Author` is the author's name in the form of first last name first initial sometimes followed by a period.
    `Year` is the year of publication.
    `Journal` being the 29-Character Source Abbreviation of the journal.
    `Volume` is the volume number(s) of the publication preceded by a V
    `Page` is the page number the record starts on
    `DOI` is the DOI number of the cited record preceeded by the letters `'DOI'`
    Combined they look like:

        Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

    **Note**: any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpreted as any of these it is put in the `misc` attribute. That is the reason to use this class, it gracefully handles missing information while still allowing for  comparison between WOS citation strings.

    # Customizations

    Citation's hashing and equality checking are based on [`ID()`](#Citation.ID) and use the values of `author`, `year` and `journal`.

    When converted to a string a Citation will return the original string.

    # Attributes

    As noted above, citations are considered to be divided into six distinct fields (`Author`, `Year`, `Journal`, `Volume`, `Page` and `DOI`) with a seventh `misc` for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a `Citation` created from the string: `'Nunez R., 1998, MATH COGNITION'` would have `author`, `year` and `journal` defined. While one from `'Nunez R.'` would have only the attribute `misc`.

    If the parsing of a citation string fails the attribute `bad` is set to `True` and the attribute `error` is created to contain said error, which is a [BadCitation](#metaknowledge.BadCitation) object. If no errors occur `bad` is `False`.

    The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

    # \_\_Init\_\_

    Citations can be created by [Records](#metaknowledge.Record) or by giving the initializer a string containing a WOS style citation.

    # Parameters

    _cite_ : `str`

    > A str containing a WOS style citation.
    """
    #citeRegex = re.compile(r"(([^,]+), )((DOI (.+))?|.+?)")
    citeRegex = re.compile(r"([^0-9,][^,]+)?(, )?(-?[0-9]{1,5})?(, )?([^,]+)?(, (V[^,]+))?(, (P[^,]+))?($|, DOI (.+)|((.+?)(, DOI (.+))?))")
    #citeRegex = re.compile(r"([^0-9,].+?)?(, )?(-?[0-9]{1,5})?(, )?(.+?)?(, (V.+?))?(, (P.+?))?($|, DOI (.+)|((.+?)(, DOI (.+))?))")

    def __init__(self, cite):
        #save original
        #setup attributes
        #Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343
        #Author, Year, Journal, Volume, Page, DOI
        regex = re.match(self.citeRegex, cite.upper())
        if regex is None:
            self.bad = True
            self.error = BadCitation("Regex parsing failed.")
        try:
            self.author = regex.group(1).replace('.', '').title()
        except AttributeError:
            self.author = None
        try:
            self.year = int(regex.group(3))
        except TypeError:
            self.year = None
        self.journal = regex.group(5)
        self.V = regex.group(7)
        self.P = regex.group(9)
        self.DOI = regex.group(11)
        if regex.group(12) is not None:
            self.misc = regex.group(12)
            self.DOI = regex.group(15)
            self.bad = True
            self.error = BadCitation("The citation did not fully match the expected pattern")
            atrLst = []
            if self.author:
                atrLst.append(self.author)
            if self.year:
                atrLst.append(str(self.year))
            if self.journal:
                atrLst.append(self.journal)
            self._id =  ', '.join(atrLst)
        elif self.author is None or self.year is None or self.journal is None:
            self.bad = True
            self.misc = None
            self.error = BadCitation("Not a complete set of author, year and journal")
            atrLst = []
            if self.author:
                atrLst.append(self.author)
            if self.year:
                atrLst.append(str(self.year))
            if self.journal:
                atrLst.append(self.journal)
            self._id =  ', '.join(atrLst)
        else:
            self.bad = False
            self.error = None
            self.misc = None
            self._id =  "{0}, {1}, {2}".format(self.author, self.year, self.journal)
        if not metaknowledge.FAST_CITES:
            self.original = cite
        else:
            self = self._id

    def __str__(self):
        """
        returns the original string
        """
        if metaknowledge.FAST_CITES:
            return self.ID()
        else:
            return self.original

    def __repr__(self):
        """
        the representation of the Citation is its original form
        """
        if metaknowledge.FAST_CITES:
            return "<metaknowledge.{} object {}>".format(type(self).__name__, self.ID())
        else:
            return "<metaknowledge.{} object {}>".format(type(self).__name__, self.original)
    #@profile
    def __hash__(self):
        """
        A hash for Citation that should be equal to the hash of other citations that are equal to it. Based on the values returned by [`ID()`](#Citation.ID).
        """
        try:
            return self._hash
        except AttributeError:
            self._hash = hash(self.ID())
            return self._hash
    #@profile
    def __eq__(self, other):
        """
        First checks DOI for equality then checks each attribute if any are not equal False is returned
        """
        if not isinstance(other, Citation):
            return NotImplemented
        return hash(self) == hash(other)


    def isAnonymous(self):
        """
        Checks if the author is given as `'[ANONYMOUS]'` and returns `True` if so.

        # Returns

        `bool`

        > `True` if the author is `'[ANONYMOUS]'` otherwise `False`.
        """
        return self.author == "[Anonymous]"
    #@profile
    def ID(self):
        """
        Returns all of `author`, `year` and `journal` available separated by `' ,'`. It is for shortening labels when creating networks as the resultant strings are often unique. [**Extra**()](#Citation.Extra) gets everything not returned by **ID**().

        This is also used for hashing and equality checking.

        # Returns

        `str`

        > A string to use as the ID of a node.
        """
        return self._id

    def allButDOI(self):
        """
        Returns a string of the normalized values from the Citation excluding the DOI number. Equivalent to getting the ID with [**ID**()](#Citation.ID) then appending the extra values from [**Extra**()](#Citation.Extra) and then removing the substring containing the DOI number.

        # Returns

        `str`

        > A string containing the data of the Citation.
        """
        extraTags = ['V', 'P', 'misc']
        s = self.ID()
        extras = []
        for tag in extraTags:
            if getattr(self, tag):
                extras.append(str(getattr(self, tag)))
        if len(extras) > 0:
            return "{0}, {1}".format(s, ', '.join(extras))
        else:
            return s

    def Extra(self):
        """
        Returns any `V`, `P`, `DOI` or `misc` values as a string. These are all the values not returned by [**ID**()](#Citation.ID), they are separated by `' ,'`.

        # Returns

        `str`

        > A string containing the data not in the ID of the `Citation`.
        """
        extraTags = ['V', 'P', 'DOI', 'misc']
        retVal = ""
        for tag in extraTags:
            if getattr(self, tag):
                retVal += getattr(self, tag) + ', '
        if len(retVal) > 2:
            return retVal[:-2]
        else:
            return retVal


def filterNonJournals(citesLst, invert = False):
    """Removes the `Citations` from _citesLst_ that are not journals

    # Parameters

    _citesLst_ : `list [Citation]`

    > A list of citations to be filtered

    _invert_ : `optional [bool]`

    > Default `False`, if `True` non-journals will be kept instead of journals

    # Returns

    `list [Citation]`

    > A filtered list of Citations from _citesLst_
    """

    retCites = []
    for c in citesLst:
        if c.isJournal():
            if not invert:
                retCites.append(c)
        elif invert:
            retCites.append(c)
    return retCites
