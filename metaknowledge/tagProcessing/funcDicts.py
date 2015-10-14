from .tagFunctions import tagToFunc
from .helpFuncs import reverseDict, makeBiDirectional

tagToFullDict = {k : v.__name__ for k, v in tagToFunc.items()}

fullToTagDict = reverseDict(tagToFullDict) #Reverses tagToFull

tagNameConverterDict = makeBiDirectional(tagToFullDict) #tagToFull made reversible

tagsAndNameSet = set(tagNameConverterDict.keys()) #set of WOS tags and their names

knownTagsList = list(tagToFullDict.keys()) #list of all the known tags

def tagToFull(tag):
    """A wrapper for tagToFullDict
    """
    try:
        return tagToFullDict[tag]
    except KeyError:
        raise("Tag not in list of known tags")


def normalizeToTag(val):
    if val not in tagsAndNameSet:
        raise KeyError("{} is not a tag or name string".format(val))
    else:
        try:
            return fullToTagDict[val]
        except KeyError:
            return val

def normalizeToName(val):
    if val not in tagsAndNameSet:
        raise KeyError("{} is not a tag or name string".format(val))
    else:
        try:
            return tagToFullDict[val]
        except KeyError:
            return val

def isTagOrName(val):
    return val in tagsAndNameSet
