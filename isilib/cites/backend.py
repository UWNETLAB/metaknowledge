from bs4 import BeautifulSoup
import urllib.request
import string

def urlListGenerator():
    """Currently how to get all the urls for the Journal Title Abbreviations

    Each is varies by only a few characters."""

    start = "http://images.webofknowledge.com/WOK46/help/WOS/"
    end = "_abrvjt.html"
    urlList = [start + "0-9" + end]
    for c in string.ascii_uppercase:
        urlList.append(start + c + end)
    return urlList
