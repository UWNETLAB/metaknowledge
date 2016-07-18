import shutil
import collections
import datetime

testTable = {
    'abc' : [1,2,4,5,'657y8u98r54356754'],
    '1234567898765' : list(range(10)),
    'abcd' : ['1',2,4,5,'657y8u98r54356754','sdjsdhsfjsdfsd'],
}

glimpseTags = collections.OrderedDict([
    ('Authors','authorsFull'),
    ('Journals','journal'),
    ('Cited','citations'),
    ])

def _glimpse(RC):
    tColumns, tRows = tuple(shutil.get_terminal_size())
    #If it can't fit just go with the usual settings
    if tColumns < 50:
        tColumns = 80
    if tRows < 6:
        tRows = 24
    maxRows = tRows - 4
    glimpseVals = collections.OrderedDict()
    for name, tag in glimpseTags.items():
        glimpseVals[name] = RC.rankedSeries(tag, giveCounts = False, giveRanks = True)[:maxRows]
    return makeHeader(RC, tColumns) + makeTable(glimpseVals, maxRows + 1, tColumns)

def makeHeader(RC, width):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    firstLine = "{} glimpse made at: {}".format(type(RC).__name__, now)
    return '{1:+^{0}}\n'.format(width, firstLine)

def makeTable(values, height, width):
    lines = [[] for i in range(height + 1)]
    rowString = "|{}" * len(values) + '|'
    cWidth = (width / len(values)) - 1
    cRemainder = width % len(values) - 1
    for heading, rows in values.items():
        if cRemainder > 0:
            heading = "{1: ^{0}}".format(cWidth + 1, heading)
            cRemainder -= 1
        elif cRemainder < 1:
            heading = "{1: ^{0}}".format(cWidth - 1, heading)
            cRemainder += 1
        else:
            heading = "{1: ^{0}}".format(cWidth, heading)
        hWidth = len(heading)
        lines[0].append(heading)
        if len(rows) < height:
            for i in range(height - len(rows)):
                rows.append(('NA', -1))
        for index, entry in enumerate((prepEntry(*s, hWidth) for s in rows[:height]), start = 1):
            lines[index].append(entry)
    retLines = []
    for line in lines:
        retLines.append(rowString.format(*tuple(line)))
    return '\n'.join(retLines)

def prepEntry(valString, rank, maxLength):
    valString = str(valString)
    if len(valString) <= maxLength - 2:
        valString = valString.rjust(maxLength - 2, ' ')
    else:
        valString = "{}.".format(valString[:maxLength - 3])
    return "{:<2.0f}{}".format(rank, valString)
