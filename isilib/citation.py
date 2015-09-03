from .journalAbbreviations import getj9dict, manaulDBname, addToDB

abbrevDict = None

class BadCitation(Warning):
    """
    Exception thrown by Citation
    """
    pass

class Citation(object):
    """
    A class to hold citation strings and allow for comparison between them.

    The initializer takes in a string representing a WOS citation they are in the form:

    > Author, Year, Journal, Volume, Page, DOI

    Author is the author's name in the form of first last name first initial sometimes followed by a period.
    Year is the year of publication.
    Journal being the 29-Character Source Abbreviation of the journal.
    Volume is the volume number(s) of the publication preceded by a V
    Page is the page number the record starts on
    DOI is the DOI number of the cited record preceeded by the letters "DOI"
    Combined they look like:

    > Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

    Note that any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpeted as any of these it is put in the `misc` attribute.

    The reason for this class is that the WOS data are often irregular. It is designed to allow comparison between WOS citation strings, even when they are missing pieces.

    # Customizations

    Citation's hashing and equality checking are based on what data they have. The equality checking first checks both Citation's DOI's and if either is missing moves to the other fields. If any of the fields disagree `False` is returned (note, authors are not compared if one is anonymous) if they all agree, including the `misc` field, then True is returned.

    Unfortunately this type of equality checking precludes hashes being identical so to compare Citation objects always use ==. Hashes, if identical, indicate the Citations are identical (excluding collisions), but the converse is not True.

    When converted to a string a Citation will return the original string.

    # Attributes

    As noted above, citations are considered to be divided into six distinct fields (Author, Year, Journal, Volume, Page and DOI) with a seventh misc for anything not in those. Records thus have an attribute with a name corresponding to each `author`, `year`, `journal`, `V`, `P`, `DOI` and `misc` respectively. These are created if there is anything in the field. So a Citation created from the string: "Nunez R., 1998, MATH COGNITION" would have `author`, `year` and `journal` defined. While one from "Nunez R." would have only the attribute `misc`.

    If the parsing of a citation string fails the attribute `bad` is set to True and the attribute `error` is created to contain the error, which is a [BadCitation](#isilib.BadCitation) object. If no errors occur `bad` is `False`.

    The attribute `original` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with `str()`.

    # \_\_Init\_\_

    Citations can be created by [Records](#isilib.Record) or by giving the initializer a string containing a WOS style citation.

    # Parameters

    _cite_ : `str`

    > A str containing a WOS style citation.
    """
    def __init__(self, cite):
        self.original = cite
        self.bad = False
        self._isjourn = None
        c = ' '.join(cite.upper().split()).split(', ')
        if 'DOI' in c[-1][:3]:
            self.DOI = c.pop().split(' ')[-1]
        if len(c) < 3:
            self.bad = True
            self.error = BadCitation("Too few elements")
            if len(c) == 2:
                self.author = c.pop(0).replace('.','')
            self.misc = ', '.join(c)
        else:
            if not c[0].isnumeric():
                self.author = c.pop(0).replace('.','')
            if c[0].isnumeric():
                self.year = c.pop(0)
            if not c[0].isnumeric():
                self.journal = c.pop(0)
            else:
                self.misc = c.pop(0)
                self.bad = True
                self.error = BadCitation("Too many numbers")
            for field in c:
                if 'V' == field[0] and field[1:].isnumeric():
                    self.V = field
                elif 'P' == field[0] and field[1:].isnumeric():
                    self.P = field
                else:
                    if hasattr(self, 'misc'):
                        self.misc += ', ' + field
                    else:
                        self.misc = field

    def __str__(self):
        """
        returns the original string
        """
        return self.original

    def __hash__(self):
        """
        A hash for Citation that should be equal to the hash of other citations that are equal to it
        """
        if hasattr(self, 'DOI'):
            return hash(self.DOI)
        elif self.bad and getattr(self, 'misc', False):
            return hash(getattr(self, 'misc'))
        else:
            hashedString = getattr(self, 'author', '')
            hashedString += getattr(self, 'year', '')
            hashedString += getattr(self, 'journal', '')
            hashedString += getattr(self, 'V', '')
            hashedString += getattr(self, 'P', '')
            return hash(hashedString)

    def __eq__(self, other):
        """
        First checks DOI for equality then checks each attribute if any are not equal False is returned
        """
        if not isinstance(other, Citation):
            return NotImplemented
        elif getattr(self, 'DOI', None) == getattr(other, 'DOI', False):
            return True
        elif getattr(self, 'author', None) != getattr(other, 'author', None) and getattr(self, 'author', None) != '[ANONYMOUS]' and getattr(other, 'author', False) != '[ANONYMOUS]':
            return False
        elif getattr(self, 'year', None) != getattr(other, 'year', None):
            return False
        elif  getattr(self, 'journal', None) != getattr(other, 'journal', None):
            return False
        elif getattr(self, 'V', None) and getattr(other, 'V', False) and getattr(self, 'V', None) != getattr(other, 'V', False):
            return False
        elif getattr(self, 'P', False) and getattr(other, 'P', False) and getattr(self, 'P', None) != getattr(other, 'P', False):
            return False
        elif self.bad and other.bad and not getattr(self, 'misc', None) == getattr(other, 'misc', None):
            return False
        else:
            return True

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
        Checks if the author is given as "[ANONYMOUS]" and returns `True` if so.

        # Returns

        `bool`

        > True if the author is ANONYMOUS otherwise `False`.
        """
        if hasattr(self, 'author'):
            return self.author == "[ANONYMOUS]"
        else:
            return False

    def getID(self):
        """
        Returns "author, year" if both available, "author" if year is not available, and "misc" otherwise. It is for shortening labels when creating networks as the resultant strings are often unique. [`getExtra()`](#Citation.getExtra) gets everthing not returned by `getID()`.

        # Returns

        `str`

        > A string to use as the shortened ID of a node.
        """
        if not self.bad:
            return self.author + ', ' + self.year
        elif hasattr(self, 'author'):
            retid = self.author
            if hasattr(self, 'year'):
                retid += ', '  + self.year
            return retid
        else:
            return self.misc

    def getExtra(self):
        """
        Returns any journal, V, P or misc values as a string. These are all the values not returned by [`getID()`](#Citation.getID).

        # Returns

        `str`

        > A string containing the data not in the ID of the Citation.
         """
        extraTags = ['journal','V', 'P', 'misc']
        retVal = ""
        for tag in extraTags:
            if hasattr(self, tag):
                retVal += getattr(self, tag) + ', '
        if len(retVal) > 2:
            return retVal[:-2]
        else:
            return retVal

    def isJournal(self, manaulDB = manaulDBname, returnDict = 'both', checkIfExcluded = False):
        """Returns `True` if the Citation's journal field is a journal abbreviation given by WOS, i.e. checks if the citation is citing a journal. Requires the j9Abbreviations database file.

        # Returns

        `bool`

        > `True` if the Citation is for a journal
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict(manualDB = manaulDB, returnDict = returnDict)
        if checkIfExcluded and hasattr(self, 'journal'):
            try:
                if abbrevDict.get( self.journal, [True])[0]:
                    return False
                else:
                    return True
            except IndexError:
                return False
        elif self._isjourn is None:
            if hasattr(self, 'journal'):
                dictVal = abbrevDict.get(self.journal, [b''])[0]
                if dictVal:
                    self._isjourn = dictVal
                else:
                    self._isjourn = False
            else:
                self._isjourn = False
        return self._isjourn

    def getFullJournalName(self):
        """Returns the full name of the Citation's journal field. Requires the j9Abbreviations database file.

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
            global abbrevDict
            abbrevDict.update(d)

def filterNonJournals(citesLst, invert = False):
    retCites = []
    for c in citesLst:
        if c.isJournal():
            if not invert:
                retCites.append(c)
        elif invert:
            retCites.append(c)
    return retCites
