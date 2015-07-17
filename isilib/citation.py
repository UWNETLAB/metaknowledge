class BadCitation(Warning):
    """
    Exception thrown by Citation
    """
    pass

class Citation(object):
    """
    A object to hold citation strings and allow for comparison between them.
    It takes in a citation string from the CR tag of a WOS record then attempts to extract the DOI ,author, year, journal, Volume (V) and Page (P) of the citation string, any extra values are put in misc.
    If the citation string does not have 3 comma space separated elements or has 2 or more only numeric elements it is flagged as bad and all of the string is stored in misc

    """

    def __init__(self, cite):
        self.original = cite
        self.bad = False
        c = cite.upper().replace(' ',' ').split(', ')
        if 'DOI' in c[-1][:3]:
            self.DOI = c.pop().split(' ')[-1]
        if len(c) < 3:
            self.bad = True
            self.error = BadCitation("Too few elements")
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

    def isAnonymous(self):
        """
        checks if the author is given as "[ANONYMOUS]" and returns True if so
        """
        if hasattr(self, 'author'):
            return self.author == "[ANONYMOUS]"
        else:
            return True

    def getID(self):
        """
        Returns "author, year" if both available "author" if year is not available and "misc" otherwise
        Use for shortening labels
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
        Returns any journal, V, P or misc values as a string
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
