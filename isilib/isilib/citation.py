class BadCitation(Warning):
    """
    Exception thrown by Citation
    """
    pass

class Citation(object):
    def __init__(self, cite):
        self.original = cite
        self.bad = False
        c = cite.upper().replace(' ',' ').split(', ')
        if 'DOI' in c[-1][:3]:
            self.DOI = c.pop().split(' ')[-1]
        if len(c) < 3:
            self.bad = True
            self.error = BadCitation("Too few elemets")
            self.misc = ', '.join(c)
        else:
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
        return self.original

    def getID(self):
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
        extraTags = ['journal','V', 'P', 'misc']
        retVal = ""
        for tag in extraTags:
            if hasattr(self, tag):
                retVal += getattr(self, tag) + ', '
        if len(retVal) > 2:
            return retVal[:-2]
        else:
            return retVal
