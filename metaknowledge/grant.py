class Grant(object):
    def __init__(self, grant):
        self.bad = False
        self.error = None
        self.original = grant

        self.agency = ''
        self.number = ''
        self.code = ''
        split = grant.split('/')
        try:
            self.country = split.pop()
            self.agency = split.pop()
        except IndexError:
            self.bad = True
            self.country = grant
        else:
            if len(split) == 1:
                code = split.pop()
                if len(code) == 2:
                    self.code = code
                else:
                    self.number = code
            elif len(split) == 2:
                code = split.pop()
                if len(code) == 2:
                    self.code = code
                    self.number = split.pop()
                else:
                    self.number = "{}/{}".format(split.pop(), code)
            else:
                self.number = '/'.join(split)

    def __str__(self):
        """
        returns the original string
        """
        return self.original

    def __repr__(self):
        """
        the representation of the Grant is its original form
        """
        return "<metaknowledge.{} object {}>".format(type(self).__name__, self.original)

    def __hash__(self):
        return hash(self.ID())

    def __eq__(self, other):
        if not isinstance(other, Grant):
            return NotImplemented
        return self.ID() == other.ID()

    def ID(self):
        if self.number != '':
            return "{}/{}-{}".format(self.number, self.code, self.country)
        else:
            return "{}-{}-{}".format(self.code, self.agency, self.country)
