import urllib.request
import string
import os
import datetime
import shelve

abrevDBname = "j9Abbreviations.db"

def j9urlGenerator(nameDict = False):
    """How to get all the urls for the WOS Journal Title Abbreviations. Each is varies by only a few characters. These are the currently in use urls they may change.

    They are of the form:

    > "http://images.webofknowledge.com/WOK46/help/WOS/{VAL}_abrvjt.html"
    > Where {VAL} is a capital letter or the string "0-9"

    # Returns

    `list[str]`

    > A list of all the url's strings
    """
    start = "http://images.webofknowledge.com/WOK46/help/WOS/"
    end = "_abrvjt.html"
    if nameDict:
        urls = {"0-9" : start + "0-9" + end}
        for c in string.ascii_uppercase:
            urls[c] = start + c + end
    else:
        urls = [start + "0-9" + end]
        for c in string.ascii_uppercase:
            urls.append(start + c + end)
    return urls

def _j9SaveCurrent(sDir = '.'):
    """Downloads and saves all the webpages

    For Backend
    """
    dname = os.path.normpath(sDir + '/' +  datetime.datetime.now().strftime("%Y-%m-%d_J9_AbbreviationDocs"))
    if not os.path.isdir(dname):
        os.mkdir(dname)
        os.chdir(dname)
    else:
        os.chdir(dname)
    for urlID , urlString in j9urlGenerator(nameDict = True).items():
        fname = "{}_abrvjt.html".format(urlID)
        f = open(fname, 'wb')
        f.write(urllib.request.urlopen(urlString).read())

def _getDict(j9Page):
    """Parses a Journal Title Abbreviations page

    Note the pages are not well formatted html as the <DT> tags are not closes so html parses (Beautiful Soup) do not work. This is a simple parser that only works on the webpages and may fail if they are changed

    For Backend
    """
    slines = j9Page.read().decode('utf-8').split('\n')
    while slines.pop(0) != "<DL>":
        pass
    currentName = slines.pop(0).split('"></A><DT>')[1]
    currentTag = slines.pop(0).split("<B><DD>\t")[1]
    j9Dict = {}
    while True:
        try:
            j9Dict[currentTag].append(currentName)
        except KeyError:
            j9Dict[currentTag] = [currentName]
        try:
            currentName = slines.pop(0).split('</B><DT>')[1]
            currentTag = slines.pop(0).split("<B><DD>\t")[1]
        except IndexError:
            break
    return j9Dict

def _getCurrentj9Dict():
    """Downloads and parses all the webpages

    For Backend
    """
    urls = j9urlGenerator()
    j9Dict = {}
    for url in urls:
        d = _getDict(urllib.request.urlopen(url))
        if len(d) == 0:
            raise RuntimeError("Parsing failed, this is could require an update of the parser.")
        j9Dict.update(d)
    return j9Dict

def updatej9DB(dbname = abrevDBname, saveRawHTML = False):
    """Updates the database of Journal Title Abbreviations. Requires an internet connection. The data base is saved relative to the source file not the working directory.

    # Parameters

    _dbname_ : `optional [str]`

    > The name of the database file, default is "j9Abbreviations.db"

    _saveRawHTML_ : `optional [bool]`

    > Determines if the original HTML of the pages is stored, default `False`. If `True` they are saved in a directory inside j9Raws begining with todays date.
    """
    if saveRawHTML:
        rawDir = '{}/j9Raws'.format(os.path.dirname(__file__))
        if not os.path.isdir(rawDir):
            os.mkdir(rawDir)
        _j9SaveCurrent(sDir = rawDir)
    dbLoc = os.path.normpath(os.path.dirname(__file__) + '/{}'.format(dbname))
    with shelve.open(dbLoc) as db:
        try:
            j9Dict = _getCurrentj9Dict()
        except urllib.error.URLError:
            raise urllib.error.URLError("Unable to access server, check your connection")
        for k, v in j9Dict.items():
            if k in db:
                for jName in v:
                    if jName not in j9Dict[k]:
                        j9Dict[k].append(jName)
            else:
                db[k] = v

def getj9dict(updateDB = False, requireConnection = True, saveRaw = False, dbname = abrevDBname):
    """Returns the dictionary of journal abbreviations to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

    # Parameters

    _updateDB_ : `optional [bool]`

    > Makes the database be updated, default `True`

    _requireConnection_ : `optional [bool]`

    > Makes an OSError exception be raised if a connection cannot be established, default `True`

    _saveRaw_ : `optional [bool]`

    > Causes the raw HTML files to be saved, default `False`. They are saved in a directory inside j9Raws begining with todays date, j9Raws is in the same directory as this source file.

    _dbname_ : `optional [str]`

    > The name of the database file
    """
    if updateDB:
        try:
            updatej9DB(dbname = dbname, saveRawHTML = saveRaw)
        except urllib.error.URLError:
            if requireConnection:
                raise OSError("Unable to access server, check your connection")
            else:
                pass
    dbLoc = os.path.normpath(os.path.dirname(__file__) + '/{}'.format(dbname))
    with shelve.open(dbLoc) as db:
        return dict(db)
