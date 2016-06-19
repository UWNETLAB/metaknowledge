scopusSpecialTagToFunc = {
    'year' : lambda R : R['Year'],
    'volume' : lambda R : R['Volume'],
    'beginningPage' : lambda R : R['Page start'],
    #'DOI' : lambda R : R['DOI'], Causese recursion errors if not commented out
    #'address' : lambda R : R[''],
    'j9' : lambda R : R['Abbreviated Source Title'],
    'citations' : lambda R : R['References'],
    #'grants' : lambda R : R['References'],
    'selfCitation' : lambda R : R.createCitation(),
    'authorsShort' : lambda R : R['Authors'],
    'authorsFull' : lambda R : R['Authors'],
    'title' : lambda R : R['Title'],
    'journal' : lambda R : R['Source title'],
    'keywords' : lambda R : R['Index Keywords'],
    'abstract' : lambda R : R['Abstract'],
    'id' : lambda R : R['EID'],
}
