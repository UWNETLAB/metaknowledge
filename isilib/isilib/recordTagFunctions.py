from .constants import tagToFull

def pubType(v):
    return v

def authorsFull(v):
    return v


class tagWrapper(object):
    def __init__(self, parent, tag):
        self.tag = tag
        self.data = None
        try:
            self.name = tagToFull[tag]
            setattr(parent, self.name, self)
        except KeyError:
            pass
        except AttributeError:
            pass

    def __get__(self, instance, owner):
        print("Calling")
        if self.data == None:
            try:
                self.data = tagToFunc[self.tag](instance._fieldDict[self.tag])
            except KeyError:
                self.data = instance._fieldDict[self.tag]
        return self.data

tagToFunc = {
            'PT' : pubType,
            'AF' : authorsFull,
            }
