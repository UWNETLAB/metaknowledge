import shutil
import collections
import datetime

from .mkExceptions import mkException

glimpseTags = collections.OrderedDict([
    ('Top Authors','authorsFull'),
    ('Top Journals','journal'),
    ('Top Cited','citations'),
    ])

descriptionString1 = 'Columns are ranked by num. of occurrences'
descriptionString2 = 'and are independent of one another'

descriptionStringFull = descriptionString1 + ' ' + descriptionString2

def _glimpse(RC, *tags, compact = False):
    tColumns, tRows = tuple(shutil.get_terminal_size())
    if len(tags) < 1:
        targetTags = glimpseTags
    else:
        targetTags = {t: t for t in tags}
    #If it can't fit just go with the usual settings
    if tColumns < 55:
        tColumns = 80
    if tRows < 6:
        tRows = 24
    glimpseVals = collections.OrderedDict()
    if len(descriptionStringFull) > tColumns:
        maxRows = tRows - 7
    else:
        maxRows = tRows - 6
    for name, tag in targetTags.items():
        glimpseVals[name] = RC.rankedSeries(tag, giveCounts = False, giveRanks = True, pandasMode = False)
    return makeHeader(RC, tColumns, targetTags, compact) + makeTable(glimpseVals, maxRows, tColumns, compact)

def makeHeader(RC, width, glimpseVals, compact):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    firstLine = "{} glimpse made at: {}".format(type(RC).__name__, now)
    secondLine = "{} Records from {}".format(len(RC), RC.name[:30])
    if compact:
        if len(descriptionStringFull) > width - 2:
            thirdLine = '|{1:+<{0}}|\n|{2:+<{0}}|\n'.format(width - 2, descriptionString1, descriptionString2)
        else:
            thirdLine = '|{1:+<{0}}|\n'.format(width - 2, descriptionStringFull)
        return '+{2:+<{0}}\n|{3:+<{1}}|\n{4}'.format(width - 1, width - 2, firstLine, secondLine, thirdLine)
    else:
        return '{}\n{}\n'.format(firstLine, secondLine)

def makeTable(values, height, width, compact):
    retLines = []
    if compact:
        lines = [[] for i in range(height + 1)]
        firstRowString = "|{}" + "+{}" * (len(values) - 1) + '|'
        rowString = "|{}" * len(values) + '|'
        cWidth = (width // len(values)) - 1
        cRemainder = width % len(values) - 1
        for title, rows in values.items():
            if cRemainder > 0:
                heading = "{1:-^{0}}".format(cWidth + 1, title)
                cRemainder -= 1
            elif cRemainder < 0:
                heading = "{1:-^{0}}".format(cWidth - 1, title)
                cRemainder += 1
            else:
                heading = "{1:-^{0}}".format(cWidth, title)
            hWidth = len(heading)
            lines[0].append(heading)
            if len(rows) < height:
                for i in range(height - len(rows)):
                    rows.append(('NA', -1))
            for index, entry in enumerate((prepEntry(hWidth, *s) for s in rows[:height]), start = 1):
                lines[index].append(entry)
        retLines.append(firstRowString.format(*tuple(lines[0])))
        for line in lines[1:]:
            retLines.append(rowString.format(*tuple(line)))
    else:
        for title, rows in values.items():
            retLines.append('')
            retLines.append(title)
            retLines += ['{} {}'.format(c, str(s)[:width - len(str(c)) - 1]) for s, c in rows[:height // 2]]
    return '\n'.join(retLines)

def prepEntry(maxLength, valString, rank):
    valString = str(valString)
    if len(valString) <= maxLength - 2:
        valString = valString.rjust(maxLength - 2, ' ')
    else:
        valString = "{}.".format(valString[:maxLength - 3])
    return "{:<2.0f}{}".format(rank, valString)
