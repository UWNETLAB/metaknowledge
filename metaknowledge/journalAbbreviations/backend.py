#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import urllib.request
import string
import os
import datetime
import dbm.dumb

from ..mkExceptions import JournalDataBaseError

abrevDBname = "j9Abbreviations"

manualDBname = "manualj9Abbreviations"

def j9urlGenerator(nameDict = False):
    """How to get all the urls for the WOS Journal Title Abbreviations. Each is varies by only a few characters. These are the currently in use urls they may change.

    They are of the form:

    > "https://images.webofknowledge.com/images/help/WOS/{VAL}_abrvjt.html"
    > Where {VAL} is a capital letter or the string "0-9"

    # Returns

    `list[str]`

    > A list of all the url's strings
    """
    start = "https://images.webofknowledge.com/images/help/WOS/"
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
    for urlID, urlString in j9urlGenerator(nameDict = True).items():
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
    dbLoc = os.path.join(os.path.normpath(os.path.dirname(__file__)), dbname)
    try:
        with dbm.dumb.open(dbLoc, flag = 'c') as db:
            try:
                j9Dict = _getCurrentj9Dict()
            except urllib.error.URLError:
                raise urllib.error.URLError("Unable to access server, check your connection")
            for k, v in j9Dict.items():
                if k in db:
                    for jName in v:
                        if jName not in j9Dict[k]:
                            j9Dict[k] += '|' + jName
                else:
                    db[k] = '|'.join(v)
    except dbm.dumb.error as e:
        raise JournalDataBaseError("Something happened with the database of WOS journal names. To fix this you should delete the 1 to 3 files whose names start with {}. If this doesn't work (sorry), deleteing everything in '{}' and reinstalling metaknowledge should.\nThe error was '{}'".format(dbLoc, os.path.dirname(__file__), e))

def getj9dict(dbname = abrevDBname, manualDB = manualDBname, returnDict ='both'):
    """Returns the dictionary of journal abbreviations mapping to a list of the associated journal names. By default the local database is used. The database is in the file _dbname_ in the same directory as this source file

    # Parameters

    _dbname_ : `optional [str]`

    > The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

    _manualDB_ : `optional [str]`

    > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

    _returnDict_ : `optional [str]`

    > default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.
    """
    dbLoc = os.path.normpath(os.path.dirname(__file__))

    retDict = {}
    try:
        if returnDict == 'both' or returnDict == 'WOS':
            with dbm.dumb.open(dbLoc + '/{}'.format(dbname)) as db:
                if len(db) == 0:
                    raise JournalDataBaseError("J9 Database empty or missing, to regenerate it import and run metaknowledge.WOS.journalAbbreviations.updatej9DB().")
                for k, v in db.items():
                    retDict[k.decode('utf-8')] = v.decode('utf-8').split('|')
    except JournalDataBaseError:
        updatej9DB()
        return getj9dict(dbname = dbname, manualDB = manualDB, returnDict = returnDict)
    try:
        if returnDict == 'both' or returnDict == 'manual':
            if os.path.isfile(dbLoc + '/{}.dat'.format(manualDB)):
                with dbm.dumb.open(dbLoc + '/{}'.format(manualDB)) as db:
                    for k, v in db.items():
                        retDict[k.decode('utf-8')] = v.decode('utf-8').split('|')
            else:
                if returnDict == 'manual':
                    raise JournalDataBaseError("Manual J9 Database ({0}) missing, to create it run addToDB(dbname = {0})".format(manualDB))
    except JournalDataBaseError:
        updatej9DB(dbname = manualDB)
        return getj9dict(dbname = dbname, manualDB = manualDB, returnDict = returnDict)
    return retDict

def addToDB(abbr = None, dbname = manualDBname):
    """Adds _abbr_ to the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manualDBname`. To create an empty database run **addToDB** without an _abbr_ argument.

    # Parameters

    _abbr_ : `optional [str or dict[str : str]]`

    > The journal abbreviation to be added to the database, it can either be a single string in which case that string will be added with its self as the full name, or a dict can be given with the abbreviations as keys and their names as strings, use pipes (`'|'`) to separate multiple names. Note, if the empty string is given as a name the abbreviation will be considered manually __excluded__, i.e. having excludeFromDB() run on it.

    _dbname_ : `optional [str]`

    > The name of the database file, default is `metaknowledge.journalAbbreviations.manualDBname`.
    """
    dbLoc = os.path.normpath(os.path.dirname(__file__))
    with dbm.dumb.open(dbLoc + '/' + dbname) as db:
        if isinstance(abbr, str):
            db[abbr] = abbr
        elif isinstance(abbr, dict):
            try:
                db.update(abbr)
            except TypeError:
                raise TypeError("The keys and values of abbr must be strings.")
        elif abbr is None:
            pass
        else:
            raise TypeError("abbr must be a str or dict.")

def excludeFromDB(abbr = None, dbname = manualDBname):
    """Marks _abbr_ to be excluded the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by `metaknowledge.journalAbbreviations.manualDBname`. To create an empty database run [addToDB()](#metaknowledge.journalAbbreviations.backend.addToDB) without an _abbr_ argument.

    # Parameters

    _abbr_ : `optional [str or tuple[str] or list[str]`

    > The journal abbreviation to be excluded from the database, it can either be a single string in which case that string will be exclude or a list/tuple of strings can be given with the abbreviations.

    _dbname_ : `optional [str]`

    > The name of the database file, default is `metaknowledge.journalAbbreviations.manualDBname`.
    """
    dbLoc = os.path.normpath(os.path.dirname(__file__))
    with dbm.dumb.open(dbLoc + '/' + dbname) as db:
        if isinstance(abbr, str):
            db[abbr] = ''
        elif isinstance(abbr, list) or isinstance(abbr, tuple):
            try:
                db.update({k : '' for k in abbr})
            except TypeError:
                raise TypeError("The keys and values of abbr must be strings.")
        elif abbr is None:
            pass
        else:
            raise TypeError("abbr must be a str, list or tuple.")
