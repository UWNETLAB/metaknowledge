singleLineEntries = {
    #The inverse cannot be done as new tags may be added that occupy mutiple line
    'Author',
    'Title',
    'Advisor',
    'Name',
    'Committee member',
    'Copyright',
    'Country of publication',
    'Database',
    'Degree',
    'Degree date',
    'Department',
    'Dissertation/thesis number',
    'Document type',
    'Language',
    'Number of pages',
    'Place of publication',
    'ProQuest document ID',
    'Publication year',
    'School code',
    'Source',
    'Source type',
    'University location',
    'University/institution',
    'ISBN',
    'Publication subject',
}

def proQuestSubject(value):
    return value[0].split('; ')

def proQuestIdentifier_Keyword(value):
    return value[0].split(', ')

def proQuestClassification(value):
    return [tuple(s.split(': ')) for s in value[0].split('; ')]

customTags = {
    'Classification' : proQuestClassification,
    'Identifier / keyword' : proQuestIdentifier_Keyword,
    'Subject' : proQuestSubject
}

def proQuestTagToFunc(tag):
    if tag in singleLineEntries:
        return lambda x : x[0]
    elif tag in customTags:
        return customTags[tag]
    else:
        return lambda x : x
