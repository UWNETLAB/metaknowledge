import shutil

testTable = {
    'abc' : [1,2,4,5,'657y8u98r54356754'],
    '1234567898765' : list(range(10)),
    'abcd' : ['1',2,4,5,'657y8u98r54356754','sdjsdhsfjsdfsd'],
}

glimpseTags = {
    '     Authors    ' : 'authorsFull',
    '    Journals    ' : 'journal',
    '      Cited     ' : 'citations'
}

def _glimpse(RC):
    tColumns, tRows = tuple(shutil.get_terminal_size())
    maxRows = tRows - 4
    glimpseVals = {}
    for name, tag in glimpseTags.items():
        glimpseVals[name] = RC.rankedSeries(tag, giveCounts = False)[:maxRows]
    return makeTable(glimpseVals, maxRows + 1, tColumns)

def makeTable(values, height, width):
    lines = [[] for i in range(height + 1)]
    rowString = "|{}" * len(values) + '|'
    for heading, rows in values.items():
        hWidth = len(heading)
        lines[0].append(heading)
        if len(rows) < height:
            for i in range(height - len(rows)):
                rows.append('NA')
        for index, entry in enumerate((str(s).strip() for s in rows[:height]), start = 1):
            if len(entry) <= hWidth:
                entry = entry.rjust(hWidth, ' ')
            else:
                entry = "{}.".format(entry[:hWidth - 1])
            lines[index].append(entry)
    retLines = []
    for line in lines:
        retLines.append(rowString.format(*tuple(line)))
    return '\n'.join(retLines)
