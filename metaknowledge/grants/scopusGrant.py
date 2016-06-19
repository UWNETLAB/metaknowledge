import collections

from .baseGrant import Grant
from ..mkExceptions import BadGrant

class ScopusGrant(Grant):
    def __init__(self, grantString):

        grantDict = collections.OrderedDict()

        bad = False
        error = None

        split = grantString.split(', ')
        try:
            grantDict['agency'] = split.pop()
        except IndexError:
            bad = True
            grantDict['agency'] = grantString
            error = BadGrant("The grant string '{}' does not contain enough comma-spaces (', ') to be a scopus grant.".format(grantString))
        else:
            try:
                grantDict['agencyCode'] = split.pop()
            except IndexError:
                pass
            else:
                try:
                    grantDict['code'] = split.pop()
                except IndexError:
                    pass
        idValue  = "{}-{}-{}".format(grantDict.get('code', ''), grantDict.get('agencyCode', ''), grantDict.get('agency', ''))
        Grant.__init__(self, grantString, grantDict, idValue, bad, error)
