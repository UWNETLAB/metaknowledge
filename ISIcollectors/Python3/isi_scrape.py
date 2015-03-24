#!/usr/bin/env python3
"""
Scraper for the ISI Web of Science

See README.md for goals and overview.

Example:
```
S = AnonymizedUWISISession()  #unfortunately, this has only be designed and tested with @uwaterloo.ca
S.login(your, credentials)
Q = S.generalSearch(("TS", "cats"), "OR", ("PY", 2007))
len(Q)
Q.export("manycats.ciw", 22, 78)

from isiparse import reader
p1 = next(iter(reader("manycats.ciw")))
print(p1['TI'])  #display title

Q2 = S.inlinks(p1['UT'])
print(len(Q2), p1['TC']) #ISI's citation counts are inconsistent, hinging on which sub-database getting searched    lov
Q2.rip("catlovers.ciw")
```

Query objects are static for the duration of a session---internally ISI doesn't
let you do anything until it has first made a temporary SQL materialized view
(or something equivalent) and tagged it with a qid number.
The bonus is that there is no concern about accidentally missing records during a long running scrape due to data entry.

Be very very very careful with this. It would be very easy to accidentally start
downloading a million records and find a lawyer-happy Thomson-Reuters pie on your face.
"""

#TODO:
# [ ] rearchitect so that passwords are passed at __init__
# [ ] Rearchitect to use composition instead of inheritence (namely: it's awks that ISISession exposes .post() and .get())
# [ ] advancedSearch()
#   [ ] besides a manual query string, advanced search has a few extra params like "articles only": support these
# [ ] Use logging.debug() instead of print() everywhere
# [x] Outlinks:
#     Using OutboundService.do with "CITREF" in filters
#     WOS's full_record.do has a "Citation Network" div which links to
#     InterService.do which has the export options of the regular page;
#     indeed, clicking this makes a new qid (hidden) number.
#     This route gives a full ISI record for each
# [x] Inlinks:
#     On a query result page, the "Times Cited" links go to
#     CitingArticles.do which provides all the inlinks.
#     Extract these.
#   [ ] Handle the case where a article has zero inlinks (in which
# [ ] Make python2 compatible (probably with liberal use of the python-future module)
# [ ] Make ISIQuery more fully featured; in particular, it should be a lazily-loaded sequence which you can iterate over, extracting the basics (via screen scraping)
# [ ] .rip() is a very scripty function. It basically expects an interactive user with a pristine filesystem; it should be not so noisy!
#       Could it be written as an iterator over the result files? And then that could be combined inline with isijoin.py, and the

# stdlib imports
import sys, os
#import argparse, optparse, ...
from warnings import warn
import traceback

from itertools import count, cycle
from urllib.parse import urlparse, urlunparse, quote as urlquote, parse_qsl, urljoin

# library imports
# (users will need to `pip install` these)
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# local package imports
from isiparse import is_WOS_number
from util import *
from httputil import *


class ISIError(Exception): pass

class ISISession(requests.Session):
    """
    A requests.Session that hardcodes the magic URLs needed to access http://apps.webofknowledge.com/
    """

    def login(self, *args, **kwargs):
        super().login(*args, **kwargs)

        # hit the front page of WoS to extract relevant things that let us pretend to be a Real Browser(TM) better
        r = self.get("http://isiknowledge.com/wos") #go to the front page like a normal person and create a session
        r.raise_for_status()
        # find the WoS SID (which is different than the ezproxy SID!)
        self._SID = qs_parse(urlparse(r.url).query)["SID"]
        self._searchpage = r.url
        # TODO: scrape the search page to extract all the form fields and the form target
        # TODO.. other key things to scrape??

    def request(self, *args, **kwargs):
        return super().request(*args, **kwargs)


    def _generalSearch(self, *fields, timespan=None, editions=["SCI", "SSCI", "AHCI", "ISTP", "ISSHP"], sort='LC.D;PY.A;LD.D;SO.A;VL.D;PG.A;AU.A'):
        """
        Backend for generalSearch(); factored out since some of the other extractions *can only work by first doing a regular search*. ugh.

        returns a BeautifulSoup. TODO: I might need to return the HTTP response as well. Don't need it right now, but keep it in mind.
        """
        max_field_count = 25

        # There are a lot of things that get posted to this form, even though it's just the simple search.
        # most of these were copied raw from a working query
        # most of them are ridiculously unusable and redundant and possibly ignored on the backend
        # but WHEN IN ROME...
        #
        # For readability, I split up the construction of the POST data into a sections, with a generator for each.
        # They are underscored to avoid conflicts with the input arguments.

        def _session():
            """
            This is header stuff needed to convince the search engine to listen to us
            """
            yield 'product', 'WOS' # 'UA' == "all databases", "..." == korean thing, "..." = MedLine, ...; we want WOS because WOS can give us bibliographies, not just
            yield 'action', 'search'
            yield 'search_mode', 'GeneralSearch'
            yield 'SID', self._SID

        def _cruft():
            """
            this is crap ISI probably ignores
            TODO: try commenting this out and seeing if anything breaks. (requires a working test suite, which is annoying because the only server to test against is the real one)
            """
            # (the browser is sending hardcoded error messages as options in its *query*??)
            yield 'input_invalid_notice', 'Search Error: Please enter a search term.'
            yield 'exp_notice', 'Search Error: Patent search term could be found in more than one family (unique patent number required for Expand option) '
            yield 'max_field_notice', 'Notice: You cannot add another field.'
            yield 'input_invalid_notice_limits', ' <br/>Note: Fields displayed in scrolling boxes must be combined with at least one other search field.'
            # LOL what are these for?? "Yes, I Love Descartes Too"
            yield 'x', '0',
            yield 'y', '0',
            # whyyyyyy
            yield 'ss_query_language', 'auto'
            yield 'ss_showsuggestions', 'ON'
            yield 'ss_numDefaultGeneralSearchFields', '1'
            yield 'ss_lemmatization', 'On'
            yield 'limitStatus', 'collapsed'
            yield 'update_back2search_link_param', 'yes'
            #'sa_params': "UA||4ATCGy9dQvV3rtykDa3|http://apps.webofknowledge.com.proxy.lib.uwaterloo.ca|'", #<-- TODO: this seems to repeat things passed elsewhere: product, SID, and URL. The first two I can get, but the URL is tricky because I've abstracted out from coding against the UW proxy directly
                # but I suspect the system won't notice if it's missing...
            yield 'ss_spellchecking', 'Suggest'
            yield 'ssStatus', 'display:none'
            yield 'formUpdated', 'true'

        # This is the actual fields
        # This part is rather complicated. This ISI's fault.
        def _fields():
            """
            this generator walks the input and reformats it into key-value pairs
            returns the number of fields searched (which you need to retrieve from the StopIteration)
            Note: the number of times this yields is larger than the number of fields actually represented, because of ISI cruft, so you can't simply len() the result.
            """
            for i in range(0, len(fields), 2):
                t = (i//2)+1 #terms correspond to every other index, and are themselves indexed from 1

                # the field term
                # TODO: wrap this in a better typecheck, because the user has to pass a complicated
                # datastructure down and, if wrong, will get a crash in this pretty obscure place
                (field, querystring) = fields[i]

                if isinstance(querystring, list): #TODO: be more geneerric
                    # attempt to coerce lists to the format used by GeneralSearch.do for OR'd enumerations
                    # This is to ###-separarate the points
                    # as far as I know, this is *only* used for but we'll leave that up to the user
                    querystring = str.join("###", querystring)

                yield "value(select%d)" % t, field
                yield "value(input%d)" % t, querystring
                yield "value(hidInput%d)" % t, "" #the fantastic spaztastic no-op hidden input field

                # the operand term
                if fields[i+1:]:
                    op = fields[i+1]
                    assert op in ["AND","OR","NOT","SAME","NEAR"], "ISI only knows these operators"
                    yield "value(bool_%d_%d)" % (t,t+1), op
                else:
                    # last field; don't include the operand term
                    assert len(fields)-1 == i, "Double checking I got the if right"

            if t > max_field_count:
                warn("Submitting %d > %d fields to ISI. ISI might balk." % (fieldCount, max_field_count))
            yield 'fieldCount', t  #the number of fields processed
            yield 'max_field_count', max_field_count #uhhhh, and what happens if I ignore this? omg, I bet ISI is full of SQL injections. :(

        def _period():
            """
             the period is actually several sub-fields together; as in fields2isi we re-interpret the python arguments into ISI's crufty form
            """
            #default values, as on the HTML form
            period = "Range Selection" # this decides whether we're using the range drop down or the year dropdowns
            range = "ALL"  #this is the value of the range dropdown
            startYear, endYear = 1900, 2000 #this is the value of the year dropdowns
            # obviously, only one of the latter two actually matters, but we POST both because we want to be as close to a browser as possible to avoid mishaps.

            if timespan is not None:
                try:
                    # (startYear, endYear)
                    startYear, endYear = timespan
                    period = "Year Range"
                except:
                    if isinstance(timespan, int):
                        # (year,)
                        startYear, endYear = timespan, timespan
                        period = "Year Range"
                    else:
                        # special-case ISI timespan
                        assert timespan in ["ALL","Latest5Years","YearToDate","4week","2week","1week"], "ISI only knows these timespans, besides year ranges."
                        range = timespan

            yield ("period", period)
            yield ("startYear", startYear)
            yield ("endYear", endYear)
            yield ("range", range)

        def _sort_order():
            yield 'rs_sort_by', sort

        def _editions():
            for e in editions:
                yield ("editions", e)

        # merge all the sections
        # note: we have to use lists of key-value pairs and not dicts because ISI repeats some parameter names
        # += on a list L and a generator G is the same as .extend(); note that L + G will *not* work.
        form = []
        form += _session()
        form += _cruft()
        form += _fields()
        form += _sort_order()
        form += _editions()

        #print(form) #DEBUG
        #import IPython; IPython.embed() #DEBUG

        # Do the query
        # this causes ISI to create and cache a resultset
        r = self.post("http://apps.webofknowledge.com/WOS_GeneralSearch.do",
                headers={'Referer': "http://apps.webofknowledge.com/WOS_GeneralSearch.do?product=WOS&SID=%s&search_mode=GeneralSearch" % self._SID}, #TODO: base this URL on the data above
                data=form)
        r.raise_for_status()

        soup = BeautifulSoup(r.content)

        # DEBUG
        # being able to see what ISI gives back helps, especially since ISI seems to return 200 OK for *everything*
        #with open("generalSearch()_result.html","w") as what:
        #    what.write(soup.prettify())

        #print("performed a query; dropping to shell; query result is in r and soup")
        #import IPython; IPython.embed()

        # TODO: search for error message in output, translate it to an exception

        err = soup.find("div", id="client_error_input_message") #TODO: this can occur on any(?) request to ISI: to; we should wrap all of them into exceptions; perhaps this means an extra layer of indirection: make isisession speak *only* to the ISI site and put code in post() and get() and put() that wraps screenscraped errors into Exceptions
        assert err is not None, "The result page *always* includes this div, even if there's no error"
        err = err.text.strip()
        if err:
            #TODO: better exception
            raise ISIError("Search failed", err)

        return soup

    def generalSearch(self, *fields, timespan=None, editions=["SCI", "SSCI", "AHCI", "ISTP", "ISSHP"], sort='LC.D;PY.A;LD.D;SO.A;VL.D;PG.A;AU.A'):
        """
        Perform a search of the http://apps.webofknowledge.com/WOS_GeneralSearch_input.do form.

        fields gives the fields to search; the keyword arguments give the other options.

        fields:
            specifies what to search for. This tuple should alternate between fields and operators.
            Specifically, it alternates between:
            - (field, querystring) pairs
              - Field Tags:
                    TS= Topic
                    TI= Title
                    AU= Author
                    AI= Author Identifiers
                    GP= Group Author
                    ED= Editor
                    SO= Publication Name
                    DO= DOI
                    PY= Year Published
                    CF= Conference
                    AD= Address
                    OG= Organization-Enhanced
                    OO= Organization
                    SG= Suborganization
                    SA= Street Address
                    CI= City
                    PS= Province/State
                    CU= Country
                    ZP= Zip/Postal Code
                    FO= Funding Agency
                    FG= Grant Number
                    FT= Funding Text
                    SU= Research Area
                    WC= Web of Science Category
                    IS= ISSN/ISBN
                    UT= Accession Number (aka WOS number: the unique document ID within the WOS database)
                    PMID= PubMed ID
                You can reuse fields, though it's easy to end up with empty resultsets if you do this.
                Reference: http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do
                           http://images.webofknowledge.com/WOKRS5161B5_fast5k/help/WOS/hs_wos_fieldtags.html
                    WARNING: these two pages give inconsistent lists of fields:
                      the first uses "PMID" and the second "PM"
                      the first uses "IS" and the second "BN" to refer to ISBN, much like Harry and Draco.
                      the first doesn't list "DT" and some other fields
                      You apparently can search by anything in the fuller list, regardless.
              - querystring is fed directly into ISI unchecked.
                Anything you can use from the http://isiknowledge.com/wos search engine you can use here (and if things aren't working, try it via the Web UI first).
                ~Generally~ you can use ranges ("2007-2010"), globbing (?, +, *), and boolean operators ("WOS:000348623400019 OR WOS:000348623400022") here, so long as it makes sense.
                Reference: http://images.webofknowledge.com/WOKRS5161B5_fast5k/help/WOS/hs_search_rules.html
                Let it be reiterated that this string is fed into ISI **UNCHECKED**, which makes it both powerful and a pain.
            - operator strings: AND, OR, NOT, NEAR, SAME; also fed into ISI unchecked.
                Reference: http://images.webofknowledge.com/WOKRS5161B5_fast5k/help/WOS/hs_search_operators.html
            The length of fields should be an odd number because there should be exactly one less operator than query pairs.
            It also, apparently, should not contain more than 49 fields.
            This is an awkward format; you're just going to have to DEAL WITH IT. It's better than trying to parse a string before feeding it.
        timespan: optional timespan to restrict results to.
            Can be:
             - "ALL"
             - "Latest5Years"
             - "YearToDate"
             - "4week"
             - "2week"
             - "1week"
             - an integer year
             - or a pair (startYear, endYear)
            The first set correspond to the first radio button on the search page next to a dropdown;
            The last two correspond to second next to the two year range selection dropdowns (a single integer period=y is the same as period=(y,y)).
            If timespan==None, assumes "ALL"
            (yes, this appears to be partially redundant with the "PY" field. Try not to cringe too much.)

        editions: the list of WoS subsections to search:
            #TODO: document what these are
            The default is all known, so you can probably leave it alone mostly.
        sort: the sort order to return
            This isn't actually an option on the form, but it's sent along with the request and is useful
            Currently, passed unchecked to ISI. Thus, it must be given in ISI's internal notation which is this pattern:
            ({field}.{order}(.{lang})?;)*
            * field is a field tag
            * order is "A" for ascending or "D" for descending.
            * lang is an optional 2-letter language code which only applies to certain fields; I don't know what this is for.
            This is essentially a normal table order-by clause:
                records are first sorted by the first field given; ties are broken by looking at the second, if given; ties in that are broken by looking at the third, etc
                Additionally(??) there's extra fields allowed here not listed above? like "LC" which is the citation count (which, confusing, is given as "TC" in the ISI format).
            The default puts most cited and oldest articles first, since those are probbbbbably the articles you care about if you're doing scraping.

        # TODO: if we don't get any results we get sent back to GeneralSearch.do; handle this case

        returns an ISIQuery object. See ISIQuery for how to proceed from there.
        """
        soup = self._generalSearch(*fields, timespan=timespan, editions=editions, sort=sort)

        qid = soup.find("input", {"name": "qid"})['value']
        #count = soup.find(id="hitCount.top").text #this is no good because the count (and most of the rest of the page) are actually loaded *by awful javascript*
        #count = 10*int(soup.find(id="pageCount.top").text) #here's another idea
        count = soup.find(id="footer_formatted_count").text
        estimated = "approximately" in count.lower()
        count = count.split()[-1] #chomp the 'approximately', if it exists
        #locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
        #count = locale.atoi(count) #this should but doesn't work because it assumes *my* locale
        count = parse_american_int(count)

        return ISIQuery(self, 'GeneralSearch', qid, count, estimated)

    def advancedSearch(self, query):
        """
        query should be a string in the form
        """
        raise NotImplementedError

    def search(self, topic):
        """
        perform a simple of the Web of Science
        """
        return self.generalSearch(('TS', topic))

    def outlinks(self, document):
        """
        Given an ISI document ID (aka WOS number aka UT field aka Accession Number),
        get an ISIQuery over all the documents it cites.

        Now, you also get outlinks in the "CR" field, but those are badly mangled
        MLA-esque single line citations; this API actually gives you the full records.
        However, we make no guarantees that these results match up to the "CR" results; that's up
        to ISI (and their database is full of varying formats and inconsistencies).
        In particular, the WOS includes citations to articles which it does not have;
        in this case, the missing records are silently elided during ISIQuery.export().
        If your record counts are not adding up, and especially if you are getting empty .ciw files,
        try the search by hand and see if the results lists "Title: [not available]".

        If you use this across a set of related records, you are likely to get duplicates.
        You will just have to merge them by WOS number.

        This method does not pretend very well to be a proper browser:
         a proper browser would first search for the WOS number with WOS_GeneralSearch.do
         then click on the link to the article's full_record.do page
         then click on the InterService.do link.
        This method goes straight for the jugular.
        """
        assert is_WOS_number(document)

        def _session():
            yield "product", "WOS"
            yield "last_prod", "WOS"
            yield "parentProduct", "WOS"
            yield "toPID", "WOS"
            yield "fromPID", "WOS"
            yield "action", "AllCitationService"
            yield "search_mode", "CitedRefList"
            yield "isLinks", "yes" #maybe this belongs in cruft()
            yield "SID", self._SID

        def _cruft():
            yield "returnLink", "http://gilgamesh" #this is, apparently, ignored. Still, TODO: something reasonable, like maybe the same value as headers.referer
            yield "srcDesc", "RET2WOS"
            yield "srcAlt", 'Back+to+Web+of+Science<span+class="TMMark">TM</span>' #HAHAHAHAH
            yield "parentQid", 1 #this is ignored, apparently
            yield "parentDoc", 1 #this too; though you'd think that this should somehow be linked to the WOS number you're earc
            yield "PREC_REFCOUNT", 1 #wot?
            yield "fromRightPanel", "true"

        def _query():
            yield "UT", document # this is actually irrelevant: this is used to generate the "From:" header on the page, but it does not affect the search results, hilariously
            yield "recid", document #this one controls the actual search results

        form = []
        form += _session()
        form += _cruft()
        form += _query()

        r = self.get("http://apps.webofknowledge.com/InterService.do",
                 #headers={"Referer": "Gilgamesh",}, #TODO
                 params=form) #the outlinks page takes query params, not form POST params; luckily python-requests makes this distinction trivial
        r.raise_for_status()
        soup = BeautifulSoup(r.content)

        qid = soup.find("input", {"name": "qid"})['value']
        count = soup.find(id="hitCount.top").text  #<--unlike the other searches
        count = parse_american_int(count)

        return ISIQuery(self, 'CitedRefList', qid, count, False)

    def inlinks(self, document):
        """
        Given an ISI document ID (aka WOS number aka UT field aka Accession Number),
        get an ISIQuery over all the documents that cites it.
        """
        assert is_WOS_number(document)

        # there is no way to go for the jugular with this one
        # so, first we do once search, then extract the magic link, then hit that
        soup = self._generalSearch(("UT", document))

        records = soup(class_="search-results-item")
        assert len(records) == 1, "Since we searched by WOS number, we should only have one result"
        soup = records[0]

        cites = soup.find(class_="search-results-data-cite")
        link = cites("a")
        if len(link) == 0:
            raise Warning("No in links")
        assert len(link) == 1, "Ditto"
        link = link[0]

        assert link['href'].startswith("/CitingArticles.do"), "The link should be to the inlinks page: CitingArticles.do"
        link = link['href']

        # TODO: this use base = r.url from the _generalSearch() call
        base = "http://apps.webofknowledge.com/"
        link = urljoin(base, link) #resolve the relative link

        r = self.get(link) #we don't need to deal with params cruft
        # appppparently hitting this with GET creates a new qid on the backend
        r.raise_for_status()
        soup = BeautifulSoup(r.content)

        #XXX COPYPASTED FROM ABOVE
        #TODO FACTOR FACTOR FACTOR
        try:
            qid = soup.find("input", {"name": "qid"})['value']
        except Exception:
            raise Warning("Something weird came from WOS, skipping")
        #count = soup.find(id="hitCount.top").text #this is no good because the count (and most of the rest of the page) are actually loaded *by awful javascript*
        #count = 10*int(soup.find(id="pageCount.top").text) #here's another idea
        try:
            count = soup.find(id="footer_formatted_count").text
        except Exception:
            raise Warning("Something weird came from WOS, skipping")
        estimated = "approximately" in count.lower()
        count = count.split()[-1] #chomp the 'approximately', if it exists
        #locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
        #count = locale.atoi(count) #this should but doesn't work because it assumes *my* locale
        count = parse_american_int(count)

        return ISIQuery(self, 'CitingArticles', qid, count, False)

    #def __str__(self):
    #    return "<%s: %s " % (type(self),) #???





class UWISISession(ISISession, UWProxy):
    pass

class AnonymizedUWISISession(AnonymizedUAMixin, UWISISession):
    pass


class ISIQuery:
    """
    You need to create queries in order to extract anything from WOS,
    because their search engine works by first caching result sets.

    This class is a brittle nougat shell around a creamy WoS result set.
    """
    def __init__(self, session, search_mode, qid, N=None, estimated=None):
        """
        N is the number of results in the query set, if known.
        search_mode: 'GeneralSearch', 'AdvancedSearch', 'CitedRefList' or 'CitingArticles'
            This is needed to properly tweak the behaviour of the request
            to match the type of search on the server in qid. Incorrect,
            instead of an error, ISI will simply export an empty UTF-8 file
             (it will have exactly two bytes: the Unicode BOM)
             TODO: perhaps this is a good place to use an inheritence tree instead of an embedded if-else tree?
        """
        self._session = session
        self.SID = session._SID
        self.qid = qid
        self._len = N
        self.estimated = estimated
        self.search_mode = search_mode

    def __len__(self):
        return self._len

    def export(self, fname, start=1, end=500, format="fieldtagged"):
        """
        Request records export via the "Save to Other File Formats" dialog.
        Export records for the current query startinf running start through end-1.

        format:
         - fieldtagged or othersoftware -- ISI Flat File format
         - {win,mac}Tab{Unicode,UTF8}   -- variants of TSV
         - bibtex                       -- for LaTeX junkies
         - html                         -- if you hate yourself

        Returns the HTTP response from ISI's OutboundService.do,
        because I don't want to corner your choices, though this
        does mean you get more information than you expect, probably.
        """
        r = self._export(start, end, format)
        print("Exporting records [%d,%d) to %s" % (start, end, fname), file=sys.stderr) #TODO: if we start multiprocessing with this, we should print the query in here to distinguish who is doing what. Though I suppose printing the filename is equally good.
        with open(fname,"wb") as w:
            w.write(r.content) #.content == binary => "wb"; .text would => "w"

    def _export(self, start, end, format="fieldtagged"):
        """
        backend for export()
        """
        assert start >= 0 and end >= 0
        assert start < end
        assert end - start <= 500, "ISI disallows more than 500 records at a time"

        params = {
                            # export ALL THE THINGS
                            # TODO: make configurable
                            'fields_selection': 'PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ',
                            'filters': 'PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ',


                            # TODO: make configurable
                            'sortBy': 'PY.A;LD.D;SO.A;VL.D;PG.A;AU.A',
                            'locale': 'en_US',

                            # DUPLICATED LOL
                            'markFrom': str(start),
                            'mark_from': str(start),
                            'markTo': str(end),
                            'mark_to': str(end),

                            # just because they didn't already know you were searching the Web of Science
                            'product': 'WOS',
                            'mark_id': 'WOS',
                            'colName': 'WOS',

                            # now this part is important
                            'SID': self._session._SID,
                            'search_mode': self.search_mode,
                            'qid': self.qid,

                            'mode': 'OpenOutputService', # I bet WOS is programmed in Java.
                            'format': 'saveToFile', # this is called 'format'; this corresponds to the ["Save to EndNote Online", "Save to EndNote Desktop", ..., "Save to Other File Formats", ...] dropdown.
                            'save_options': format, # for our purposes, it's not actually the format; we choose "save to other file formats" always and fill in which sub-format via save_options.
                                                    # (format, save_options) = ("saveToRef", _) is identical to both ("saveToFile", {"fieldtagged","othersoftware"}): it gives the ISI Flat File format.
                                                    # the one difference is it sets the extension to .ciw instead of .txt, but we ignore the Content-Disposition header anyway.

                            # cruft?
                            'displayCitedRefs': 'true',
                            'displayTimesCited': 'true',

                            'viewType': 'summary',
                            'view_name': 'WOS-summary',
                            'IncitesEntitled': 'no',
                            'count_new_items_marked': '0',

                            'value(record_select_type)': 'range', #if set to 'pagerecords' then
                            'selectedIds': '',                    #<-- this gives a semicolon-separated list of indexes of which records to extract

                            'rurl': 'http://isiknowledge.com', #yep TODO: this should be generated by a combination of qid, search_mode, and guessing
                            'queryNatural': '<b>TOPIC</b>: EVERYTHING IS AWESOME WHEN YOURE PART OF A TEAM', #..this one is just going to have to be stuck like this
                           }

        # append mode-specific cruft
        # (some of these are actually updates, overwriting the defaults extracted from GeneralSearch
        if self.search_mode == 'GeneralSearch':
            # generalSearch()
            #params.update({})
            pass #defaults above were extracted from GeneralSearch mode
        elif self.search_mode == 'AdvancedSearch':
            # advancedSearch()
            raise NotImplementedError
        elif self.search_mode == 'CitedRefList':
            # outlinks()
            params.update({'view_name': 'WOS-CitedRefList-summary',

                           'mode': 'CitedRefList-OpenOutputService', #without this, the output is empty (but *not* an error, ugh)
                           'mark_id': 'UDB', #???? this seems to be ignored, but is set differently in CitedRefList mode

                           # *undo* the DOWNLOAD ALL THE THINGS option
                           # TODO: experiment with this; can we get ALL THE THINGS even out of CitedRefList-OpenOutputService?
                           'fields_selection': 'AUTHORSIDENTIFIERS ISSN_ISBN ABSTRACT SOURCE TITLE AUTHORS  ',
                           'filters': 'AUTHORSIDENTIFIERS ISSN_ISBN ABSTRACT SOURCE TITLE AUTHORS  ',

                           })
        elif self.search_mode == 'CitingArticles':
            # inlinks()
            params.update({'view_name': 'WOS-CitingArticles-summary',

                            # apparently mode can be left at default here?
                            })
        else:
            raise ValueError("Unknown search_mode '%s'" % (self.search_mode,)) #XXX check this in __init__ instead?

        assert len(params) == 27, "Expected number of params, extracted by hand-counting in Firefox's web inspector"
        # fire!
        r = self._session.post("http://apps.webofknowledge.com/OutboundService.do?action=go",
                           #headers={...},
                           data=params)

        r.raise_for_status()
        #print("performed an export; dropping to shell; query result is in r")
        #import IPython; IPython.embed()
        # translate WOS's happy-go-lucky 302 to a 200 OK with a small little error message into an actual exception
        print("export result:", r.url)
        if "error_display_redirect" in qs_parse(urlparse(r.url).query):
            raise HTTPError("404: invalid export range requested (i guess)")
        return r

    def rip(self, fname, upper_limit=20000):
        """
        Export all records available in this query.

        fname: file name. used as a template: if fname == "fname.ext" then records will be exported to ["fname_0001.ext", "fname_0501.ext", ...]
        upper_limit: the largest record index to export; use this to make an easy guarantee that you won't get stomped by ISI for chewing through their data.
        """

        # TODO:
        # [ ] make Queries record their parameters and write a __str__ which canonicallizes them into a text form, then implicitly use this as fname. Done right, this will really help provenance.
        #   -> or at the very least
        #   -> tricky because there are soooooooooooooooo many parameters;
        # [ ] add random jitter between requests so we don't look so botty

        #note!: the web UI declines to let you export more records than available, however the API will accept such a request and just only give you which records it has available.
        #       Here, the *last record block* is making such an illegal request: it requests 500 even if there's only one; it's currently working but it might break if ISI tightens up their game.
        #       We could use len(self) to determine how many to request, but len(self) is not accurate when self.estimated==True, which happens in large result sets ((on the other hand, you really, really, really should not be ripping large result sets: you'll get yourself banned and/or sued))

        base_name, ext = os.path.splitext(fname)
        for k in count(): #TODO: use range() here to somehow get the upper and low bounds simultanouesly
            block = 500*k + 1 #+1 because ISI starts counting at 1, of course
            if upper_limit and block > upper_limit: break
            fname = "%s_%04d%s" % (base_name, block, ext)
            try:
                r = self.export(fname, block, block+500)
            except HTTPError as exc:
                #print("quitting on block %d due to:" % (k,)) #DEBUG
                #traceback.print_exc()
                break

    def __str__(self):
        return "<%s: %d records%s>" % (type(self).__name__, len(self), " (approximately)" if self.estimated else "") #<-- this could be better


def tos_warning():
    print("In using this to download records from the Web of Science, you should be aware of the terms of service:")
    print()
    print(
    "Thomson Reuters determines a “reasonable amount” of data to download by comparing your download activity\n"
    "against the average annual download rates for all Thomson Reuters clients using the product in question.\n"
    "Thomson Reuters determines an “insubstantial portion” of downloaded data to mean an amount of data taken\n"
    "from the product which (1) would not have significant commercial value of its own; and (2) would not act\n"
    "as a substitute for access to a Thomson Reuters product for someone who does not have access to the product.")
	# but they don't seem to say 'no botting', just 'no excessive downloading', which sort of implies they expect some amount of botting.
    print()
    print("The authors of this software take no responsibility for your use of it. Don't get b&.")
    print("")


# ----------------------------- main

if __name__ == '__main__':
    import argparse, datetime

    # TODO: pass barcode via stdin to hide it from ps auxww
    # TODO: support non-UW logins

    ap = argparse.ArgumentParser(description="Export paper associated metadata from the Web of Science. Currently only works for University of Waterloo members.")
    ap.add_argument('user', type=str, help="Your last name, as you use to log in to the UW library proxy")
    ap.add_argument('barcode', type=str, help="Your 14 digit library card barcode number (not your student ID!)")
    ap.add_argument('query', type=str, nargs="+", help="A query in the form FD=filter where FD is the field and filter is what to search for in that field.")
    ap.add_argument('-q', '--quiet', action="store_true", help="Silence most output")
    ap.add_argument('-d', '--debug', action="store_true", help="Enable debugging")
    ap.epilog = """
    Fields are given by two letter codes as documented at http://images.webofknowledge.com/WOKRS5161B5_fast5k/help/WOS/hs_wos_fieldtags.html.
    Filters support globbing as documented at http://images.webofknowledge.com/WOKRS5161B5_fast5k/help/WOS/hs_search_rules.html.

    If multiple queries are given they will be ANDed together.

    ISI supports more search parameters than exposed here.
    If you need more control you can use this program as a library:
    ```
    import isi_scrape
    help(isi_scrape.UWISISession)
    ```

    All records in the resultset will be automatically exported, 500 at a time, to the current directory.
    Currently, the exported filenames will be the session ID ISI's web framework assigned, in lieu of something more meaningful.
    """ #^TODO: argparse helpfully reflows the text but this fucks up the formatting that I do want. What do?


    args = ap.parse_args()

    #by sorting we enforce that each search has a unique reference for each search
    args.query = sorted(args.query)

    if args.debug: #<-- a bit dangerous, since if -d breaks we won't know it
        print(args) #DEBUG

    def parse_queries(Q):
        for e in Q:

            try:
                field, query = e.split("=")
                yield field, query
            except:
                ap.error("Incorrectly formatted query '%s'" % (e,))
    query = list(parse_queries(args.query))

    if not args.quiet:
        tos_warning()

    try:

        query = flatten(zip(query,  cycle(["AND"]))) #this line is line "AND".join(query)
        query = query[:-1] #chomp the straggling incorrect, "AND"

        S = AnonymizedUWISISession()
        S.login(args.user, args.barcode)

        print("Logged into ISI as UW:%s." % (args.user,))

        print("Querying ISI for %s" % (query,)) #TODO: pretty-print
        Q = S.generalSearch(*query)
        print("Got %s%d results" % ("an estimated " if Q.estimated else "", len(Q)))

        # make a new folder for the results, labelled by the query used to generate them
        strquery = str.join(" ", (args.query))
        results_folder = strquery.replace(" ","_") #TODO: find a generalized make_safe_for_filename() function. That's gotta exist somewhere...
        if not os.path.isdir(results_folder):
            print("Making results folder", results_folder)
            os.mkdir(results_folder)
        os.chdir(results_folder)
        # record the parameters used for replicability
        # this could be dne better
        if os.path.exists("parameters.txt"): #ughhhhhh, this is awkward. TODO: handle this case better.
            warn("Overwriting old parameters.txt")
        with open("parameters.txt","w") as desc:
            print("ISI scrape\n"
                  "==========\n"
                  "\n"
                  "Query: %s\n"
                  "Records: %d\n"
                  "ISI Session: %s\n"
                  "Date: %s\n" %
                  (strquery, len(Q), S._SID, datetime.datetime.now()), file=desc)
        fname = "%s.ciw" % (S._SID,) #name according to the SID; this should be redundant since we're also making a new folder *but* it will help if files get mixed together.
        print("Ripping results.")
        Q.rip(fname)
    except Exception as exc:
        if args.debug:
            print("------ EXCEPTION ------")
            traceback.print_exc()
            print()
            print("placing exception into 'exc' and dropping to a shell")
            print()
            import IPython; IPython.embed()
        else:
            raise
    else:
        if args.debug:
            print("Finished ripping. You may continue to experiment with the session S and query Q.");
            import IPython; IPython.embed()
