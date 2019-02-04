#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import abc
try:
    import collections.abc
except ImportError:
    import collections
    collections.abc = collections
import re

from .mkExceptions import BadCitation
from .journalAbbreviations import getj9dict, abrevDBname, manualDBname, addToDB

import metaknowledge

#For journalAbbreviations, to reduce the number of times we read the dict
abbrevDict = None

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

    Citation's hashing and equality checking are based on [ID()](#metaknowledge.citation.Citation.ID) and use the values of `author`, `year` and `journal`.

    When converted to a string a Citation will return the original string.

    # Attributes

    As noted above, citations are considered to be divided into six distinct fields (`Author`, `Year`, `Journal`, `Volume`, `Page` and `DOI`) with a seventh `misc` for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a `Citation` created from the string: `'Nunez R., 1998, MATH COGNITION'` would have `author`, `year` and `journal` defined. While one from `'Nunez R.'` would have only the attribute `misc`.

    If the parsing of a citation string fails the attribute `bad` is set to `True` and the attribute `error` is created to contain said error, which is a [BadCitation](../exceptions/index.html#metaknowledge.mkExceptions.BadCitation) object. If no errors occur `bad` is `False`.

    The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

    # \_\_Init\_\_

    Citations can be created by [Records](./Record.html#metaknowledge.Record) or by giving the initializer a string containing a WOS style citation.

    # Parameters

    _cite_ : `str`

    > A str containing a WOS style citation.
    """
    wosCiteRegex = re.compile(r"([^0-9,][^,]+)?(, )?(-?[0-9]{1,5})?(, )?([^,]+)?(, (V[^,]+))?(, (P[^,]+))?($|, DOI (.+)|((.+?)(, DOI (.+))?))")

    scopusCiteRegex = re.compile(r"([\w\- ]+,? [\w\.\-]+\.), (([\w\- ]+,? [\w\-\.]+\., )+)?([^(]+? )?\((\d{2,5})\) ([^,]+)(, ([\w-]+)( \(([\w-]*)\))?)?(, P?P\. ([\w-]*))?(.*)")


    #(.*?, )?[^,(]*\((\d{2,5}\))[^,]*(, [^,(]*( \(\d+\))?)?(, (p?p\. .*))?")

    def __init__(self, cite, scopusMode = False):
        #save original
        #setup attributes
        #Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343
        #Author, Year, Journal, Volume, Page, DOI
        if scopusMode:
            regex = re.match(self.scopusCiteRegex, cite.upper())
            if regex is None:
                self.bad = True
                self.error = BadCitation("Regex parsing failed on a Scopus Citation this means the Citation is likely for a non-journal.")
                self._id = cite
            else:
                self.author = regex.group(1)
                self.extraAuthors = regex.group(2)
                self.name = regex.group(4)
                self.year = int(regex.group(5))
                self.journal = regex.group(6)
                self.V = regex.group(8)
                self.issue = regex.group(10)
                self.P = regex.group(12)
                self.misc = regex.group(13)
                if self.author and self.journal and self.year:
                    self.bad = False
                    self.error = None
                    self._id =  "{0}, {1}, {2}".format(self.author, self.year, self.journal)
                else:
                    self.bad = True
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
            regex = re.match(self.wosCiteRegex, cite.upper())
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
        A hash for Citation that should be equal to the hash of other citations that are equal to it. Based on the values returned by [ID()](#metaknowledge.citation.Citation.ID).
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
        try:
            return self.author == "[Anonymous]"
        except AttributeError:
            return True

    def ID(self):
        """
        Returns all of `author`, `year` and `journal` available separated by `' ,'`. It is for shortening labels when creating networks as the resultant strings are often unique. [Extra()](#metaknowledge.citation.Citation.Extra) gets everything not returned by **ID**().

        This is also used for hashing and equality checking.

        # Returns

        `str`

        > A string to use as the ID of a node.
        """
        return self._id

    def allButDOI(self):
        """
        Returns a string of the normalized values from the Citation excluding the DOI number. Equivalent to getting the ID with [ID()](#metaknowledge.citation.Citation.ID) then appending the extra values from [Extra()](#metaknowledge.citation.Citation.Extra) and then removing the substring containing the DOI number.

        # Returns

        `str`

        > A string containing the data of the Citation.
        """
        extraTags = ['extraAuthors', 'V', 'issue', 'P', 'misc']
        s = self.ID()
        extras = []
        for tag in extraTags:
            if getattr(self, tag, False):
                extras.append(str(getattr(self, tag)))
        if len(extras) > 0:
            return "{0}, {1}".format(s, ', '.join(extras))
        else:
            return s

    def Extra(self):
        """
        Returns any `V`, `P`, `DOI` or `misc` values as a string. These are all the values not returned by [ID()](#metaknowledge.citation.Citation.ID), they are separated by `' ,'`.

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

    def isJournal(self, dbname = abrevDBname, manualDB = manualDBname, returnDict ='both', checkIfExcluded = False):
        """Returns `True` if the `Citation`'s `journal` field is a journal abbreviation from the WOS listing found at [http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html), i.e. checks if the citation is citing a journal.

        **Note**: Requires the [j9Abbreviations](../modules/journalAbbreviations.html#metaknowledge.journalAbbreviations.backend.getj9dict) database file and will raise an error if it cannot be found.

        **Note**: All parameters are used for getting the data base with [getj9dict](../modules/journalAbbreviations.html#metaknowledge.journalAbbreviations.backend.getj9dict).

        # Parameters

        _dbname_ : `optional [str]`

        > The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

        _manualDB_ : `optional [str]`

        > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

        _returnDict_ : `optional [str]`

        > default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.

        # Returns

        `bool`

        > `True` if the `Citation` is for a journal
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict(dbname = dbname, manualDB = manualDB, returnDict = returnDict)
        if not hasattr(self, 'journal'):
            return False
        elif checkIfExcluded and self.journal:
            try:
                if abbrevDict.get(self.journal, [True])[0]:
                    return False
                else:
                    return True
            except IndexError:
                return False
        else:
            if self.journal:
                dictVal = abbrevDict.get(self.journal, [b''])[0]
                if dictVal:
                    return dictVal
                else:
                    return False
            else:
                return False

    def FullJournalName(self):
        """Returns the full name of the Citation's journal field. Requires the [j9Abbreviations](../modules/journalAbbreviations.html#metaknowledge.journalAbbreviations.backend.getj9dict) database file.

        **Note**: Requires the [j9Abbreviations](../modules/journalAbbreviations.html#metaknowledge.journalAbbreviations.backend.getj9dict) database file and will raise an error if it cannot be found.

        # Returns

        `str`

        > The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then `None` is returned
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict()
        if self.isJournal():
            return abbrevDict[self.journal][0]
        else:
            return None

    def addToDB(self, manualName = None, manualDB = manualDBname, invert = False):
        """Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()](#metaknowledge.citation.Citation.isJournal) to return `True` for this Citation and all others with its `journal`.

        **Note**: Requires the [j9Abbreviations](../modules/journalAbbreviations.html#metaknowledge.journalAbbreviations.backend.getj9dict) database file and will raise an error if it cannot be found.

        # Parameters

        _manualName_ : `optional [str]`

        > Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

        _manualDB_ : `optional [str]`

        > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

        _invert_ : `optional [bool]`

        > Default `False`, if `True` the journal will be removed instead of added
        """
        try:
            if invert:
                d = {self.journal : ''}
            elif manualName is None:
                d = {self.journal : self.journal}
            else:
                d = {self.journal : manualName}
            addToDB(abbr = d, dbname = manualDB)
        except KeyError:
            raise KeyError("This citation does not have a journal field.")
        else:
            abbrevDict.update(d)

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
