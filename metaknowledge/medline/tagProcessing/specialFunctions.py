from ...WOS.tagProcessing.helpFuncs import getMonth

def year(R):
    return R['DP'].split(' ')[0]

def month(R):
    try:
        m = R['DP'].split(' ')[1]
    except IndexError:
        raise KeyError
    else:
        return getMonth(m)

medlineSpecialTagToFunc = {
    'year' : year,
    'month' : month,
}
