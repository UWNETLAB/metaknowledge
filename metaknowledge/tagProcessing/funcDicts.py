from .tagFunctions import tagToFunc
from .helpFuncs import reverseDict, makeBiDirectional

tagToFullDict = {k : v.__name__ for k, v in tagToFunc.items()}

fullToTagDict = reverseDict(tagToFullDict) #Reverses tagToFull

tagNameConverterDict = makeBiDirectional(tagToFullDict) #tagToFull made reversible

tagsAndNameSet = set(tagNameConverterDict.keys()) #set of WOS tags and their names

knownTagsList = list(tagToFullDict.keys()) #list of all the known tags

def tagToFull(tag):
    """A wrapper for [`tagToFullDict`](#tagProcessing.tagProcessing) it maps 2 character tags to thir full names.

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
    """Converts tags or full names to tags

    # Parameters

    _val_: `str`

    > A two character string giving the tag or its full name

    # Returns

    `str`

    > The short name of _val_
    """
    if val not in tagsAndNameSet:
        raise KeyError("{} is not a tag or name string".format(val))
    else:
        try:
            return fullToTagDict[val]
        except KeyError:
            return val

def normalizeToName(val):
    """Converts tags or full names to full names

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
