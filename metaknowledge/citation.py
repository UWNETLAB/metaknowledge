#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from .journalAbbreviations import getj9dict, abrevDBname, manaulDBname, addToDB

abbrevDict = None

class BadCitation(Warning):
    """
    Exception thrown by Citation
    """
    pass

class Citation(object):
    """
    A class to hold citation strings and allow for comparison between them.

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
    def __init__(self, cite):
        #save original
        self.original = cite
        #setup attributes
        self.bad = False
        self._isjourn = None
        self._hash = None
        self.author = None
        self.year = None
        self.P = None
        self.V = None
        self.journal = None
        self.DOI = None
        self.misc = []
        #split by citation seperator
        c = ' '.join(cite.upper().split()).split(', ')
        if 'DOI' in c[-1][:3]:
            self.DOI = c.pop().split(' ')[-1]
        else:
            self.DOI = None
        if len(c) < 2:
            self.bad = True
            self.error = BadCitation("Too few elements")
        while len(c) > 0:
            field = c.pop(0).upper()
            if field.isnumeric():
                self.year = int(field)
            elif not self.author:
                self.author = field.replace('.','').title()
            elif not self.journal:
                self.journal = field
            elif field[0] == 'V' and field[1:].isnumeric():
                self.V = field
            elif 'P' == field[0] and field[1:].isnumeric():
                self.P = field
            else:
                self.misc.append(field)
        if not self.author or not self.year or not self.journal and not self.bad:
            self.bad = True
            self.error = BadCitation("Not a complete set of author, year and journal")

    def __str__(self):
        """
        returns the original string
        """
        return self.original

    def __hash__(self):
        """
        A hash for Citation that should be equal to the hash of other citations that are equal to it. Based on the values returned by [`ID()`](#Citation.ID).
        """
        if self._hash:
            return self._hash
        else:
            self._hash = hash(self.ID())
            return self._hash

    def __eq__(self, other):
        """
        First checks DOI for equality then checks each attribute if any are not equal False is returned
        """
        if not isinstance(other, Citation):
            return NotImplemented
        return hash(self) == hash(other)

    def __ne__(self, other):
        """
        Returns the inverse of equality
        """
        return not self == other

    def __repr__(self):
        """
        the representation of the Citation is its original form
        """
        return self.original

    def isAnonymous(self):
        """
        Checks if the author is given as `'[ANONYMOUS]'` and returns `True` if so.

        # Returns

        `bool`

        > `True` if the author is `'[ANONYMOUS]'` otherwise `False`.
        """
        return self.author == "[Anonymous]"

    def ID(self):
        """
        Returns all of `author`, `year` and `journal` available separated by `' ,'`. It is for shortening labels when creating networks as the resultant strings are often unique. [**Extra**()](#Citation.Extra) gets everything not returned by **ID**().

        This is also used for hashing and equality checking.

        # Returns

        `str`

        > A string to use as the ID of a node.
        """
        if self.bad:
            atrLst = []
            if self.author:
                atrLst.append(self.author)
            if self.year:
                atrLst.append(str(self.year))
            if self.journal:
                atrLst.append(self.journal)
            return ', '.join(atrLst)
        else:
            return "{0}, {1}, {2}".format(self.author, self.year, self.journal)

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

    def isJournal(self, dbname = abrevDBname, manaulDB = manaulDBname, returnDict = 'both', checkIfExcluded = False):
        """Returns `True` if the `Citation`'s `journal` field is a journal abbreviation from the WOS listing found at [http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html), i.e. checks if the citation is citing a journal.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

        **Note**: All parameters are used for getting the data base with  [**getj9dict**()](#journalAbbreviations.getj9dict).

        # Parameters

        _dbname_ : `optional [str]`

        > The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

        _manaulDB_ : `optional [str]`

        > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

        _returnDict_ : `optional [str]`

        > default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.

        # Returns

        `bool`

        > `True` if the `Citation` is for a journal
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict(dbname = dbname, manualDB = manaulDB, returnDict = returnDict)
        if checkIfExcluded and self.journal:
            try:
                if abbrevDict.get(self.journal, [True])[0]:
                    return False
                else:
                    return True
            except IndexError:
                return False
        elif self._isjourn is None:
            if self.journal:
                dictVal = abbrevDict.get(self.journal, [b''])[0]
                if dictVal:
                    self._isjourn = dictVal
                else:
                    self._isjourn = False
            else:
                self._isjourn = False
        return self._isjourn

    def FullJournalName(self):
        """Returns the full name of the Citation's journal field. Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

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

    def addToDB(self, manualName = None, manaulDB = manaulDBname, invert = False):
        """Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()](#Citation.isJournal) to return `True` for this Citation and all others with its `journal`.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

        # Parameters

        _manualName_ : `optional [str]`

        > Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

        _manaulDB_ : `optional [str]`

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
            addToDB(abbr = d, dbname = manaulDB)
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
