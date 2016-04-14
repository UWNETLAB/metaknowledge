import collections

from .baseGrant import Grant
from ..mkExceptions import BadGrant

class MedlineGrant(Grant):
    def __init__(self, grantString):

        grantDict = collections.OrderedDict()

        bad = False
        error = None

        split = grantString.split('/')
        try:
            grantDict['country'] = split.pop()
            grantDict['agency'] = split.pop()
        except IndexError:
            bad = True
            grantDict['country'] = grantString
            error = BadGrant("The grant string '{}' does not contain enough slashes (/) to be a medline grant.".format(grantString))
        else:
            if len(split) == 1:
                code = split.pop()
                if len(code) == 2:
                    grantDict['code'] = code
                else:
                    grantDict['number'] = code
            elif len(split) == 2:
                code = split.pop()
                if len(code) == 2:
                    grantDict['code'] = code
                    grantDict['number'] = split.pop()
                else:
                    grantDict['number'] = "{}/{}".format(split.pop(), code)
            else:
                grantDict['number'] = '/'.join(split)
        if 'number' in  grantDict:
            idValue = "{}/{}-{}".format(grantDict.get('number', ''), grantDict.get('code', ''), grantDict.get('country', ''))
        else:
            idValue  = "{}-{}-{}".format(grantDict.get('code', ''), grantDict.get('agency', ''), grantDict.get('country', ''))
        Grant.__init__(self, grantString, grantDict, idValue, bad, error)
