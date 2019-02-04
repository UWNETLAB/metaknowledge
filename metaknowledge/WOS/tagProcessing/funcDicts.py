#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
from .tagFunctions import tagToFunc
from .helpFuncs import reverseDict, makeBiDirectional

tagToFullDict = {k : v.__name__ for k, v in tagToFunc.items()}

fullToTagDict = reverseDict(tagToFullDict) #Reverses tagToFull

fullToTagDictUpper = {k.upper() : v for k,v in fullToTagDict.items()}


tagNameConverterDict = makeBiDirectional(tagToFullDict) #tagToFull made reversible

tagsAndNameSet = set(tagNameConverterDict.keys()) #set of WOS tags and their names

tagsAndNameSetUpper = set(([c.upper() for c in tagsAndNameSet]))

knownTagsList = list(tagToFullDict.keys()) #list of all the known tags

def tagToFull(tag):
    """A wrapper for `tagToFullDict`, it maps 2 character tags to their full names.

    # Parameters

    _tag_: `str`

    > A two character string giving the tag

    # Returns

    `str`

    > The full name of _tag_
    """
    try:
        return tagToFullDict[tag]
    except KeyError:
        raise("Tag not in list of known tags")


def normalizeToTag(val):
    """Converts tags or full names to 2 character tags, case insensitive

    # Parameters

    _val_: `str`

    > A two character string giving the tag or its full name

    # Returns

    `str`

    > The short name of _val_
    """
    try:
        val = val.upper()
    except AttributeError:
        raise KeyError("{} is not a tag or name string".format(val))
    if val not in tagsAndNameSetUpper:
        raise KeyError("{} is not a tag or name string".format(val))
    else:
        try:
            return fullToTagDictUpper[val]
        except KeyError:
            return val

def normalizeToName(val):
    """Converts tags or full names to full names, case sensitive

    # Parameters

    _val_: `str`

    > A two character string giving the tag or its full name

    # Returns

    `str`

    > The full name of _val_
    """
    if val not in tagsAndNameSet:
        raise KeyError("{} is not a tag or name string".format(val))
    else:
        try:
            return tagToFullDict[val]
        except KeyError:
            return val

def isTagOrName(val):
    """Checks if _val_ is a tag or full name of tag if so returns `True`

    # Parameters

    _val_: `str`

    > A string possible forming a tag or name

    # Returns

    `bool`

    > `True` if _val_ is a tag or name, otherwise `False`
    """
    return val in tagsAndNameSet
