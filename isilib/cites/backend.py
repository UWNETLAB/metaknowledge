from bs4 import BeautifulSoup
import urllib.request
import string
import os
import datetime

def j9urlGenerator(nameDict = False):
    """How to get all the urls for the Journal Title Abbreviations

    Each is varies by only a few characters. These are the currently in use urls they may change."""

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

def j9Opened():
    ulrlst = []
    for urlString in j9urlGenerator():
        ulrlst.append(urllib.request.urlopen(urlString))
    return ulrlst

def j9SaveCurrent():
    dname = datetime.datetime.now().strftime("%Y-%m-%d_J9_AbbreviationDocs")
    if not os.path.isdir(dname):
        os.mkdir(dname)
        os.chdir(dname)
    else:
        os.chdir(dname)
    for urlID , urlString in j9urlGenerator(nameDict = True).items():
        fname = "{}_abrvjt.html".format(urlID)
        f = open(fname, 'wb')
        f.write(urllib.request.urlopen(urlString).read())

def getDict(j9Page):
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

def getj9Dict():
    urls = j9Opened()
    j9Dict = {}
    for url in urls:
        j9Dict.update(getDict(url))
    return j9Dict


def j9urlSouped():
    soupLst = []
    for urlString in j9urlGenerator():
        soupLst.append(BeautifulSoup(urllib.request.urlopen(urlString), 'html.parser'))
    return soupLst
