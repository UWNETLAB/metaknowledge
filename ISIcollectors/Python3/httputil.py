"""
supporting routines for isi_scrape

"""

import logging

from urllib.parse import urlparse, urlunparse, quote as urlquote, parse_qsl, urljoin

import requests
from requests.exceptions import HTTPError

def qs_parse(s):
    """
    the parse_qs in urllib returns lists of single elements for no obvious reason
    and parse_qsl returns a list of pairs.
    both of these suck.
    """
    return dict(parse_qsl(s))


class UWProxy(requests.Session):
    """
    rewrite requests to go through the UW library
    TODO: is there a better way to write this? as a python-requests plugin of some sort?
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logged_in = False
        self._user = None
    
    def login(self, last_name, card_barcode):
        """
        Login to the UW library proxy. That is, do this page (which you are probably familiar with): https://login.proxy.lib.uwaterloo.ca/login.
        last_name: your "username". Note that the UW library does *not* use your Quest ID.
        card_barcode: your "password" -- the 14 digit barcode number; not your student ID.
        """
        
        try:
            self._logged_in = "logging_in" #workaround the assert in request(). I want to keep that assert for the common case, but it breaks this initial step.
            r = super().post("http://login/login", #this funny URL is because this call itself gets routed through the proxy hackery in self.request()
                data={#"url": "h,
                      #"url": "http://4chan.org",
                        #the proxy optionally will redirect you to
                        # https://login.proxy.lib.uwaterloo.ca/connect?session=s${SID}N&url=${URL} which, if it recognizes the site,
                        # will redirect you to
                        #  http://${HOST}.proxy.lib.uwaterloo.ca/${PATH} ((where ${URL} = http(s)://$HOST/$PATH))
                        # and if it doesn't will just send you to
                        #  $URL
                        #
                        # However, the library proxy doesn't care where you ask to go---you can even go off to 4chan---and it will happily hand out session cookies
                        # So this isn't actually necessary for the sake of the scraper.
                        # (if not given, you get sent to https://login.proxy.lib.uwaterloo.ca/menu)
                      
                      # credentials
                      #yes, the UW proxy reverses the definition of 'username' and 'password':
                      "pass": last_name,
                      "user": card_barcode})
            
            r.raise_for_status() #dirty way to make sure we have 200 OK
            SID = self.cookies["ezproxy"] #make sure that the login process appears to have given us the magic ticket
            
            logging.debug("Started new UW Library Proxy session '%s'" % (SID,)) #DEBUG
            #import IPython; IPython.embed() #DEBUG
            #logging.debug("Library proxy sent us on this goose chase:\n",
            #      "\n->\t".join([p.url for p in r.history] + [r.url]),)
        except Exception as exc:
            # TODO: better exception
            raise Exception("Failed logging in to library proxy", exc)
        
        # if everything is peachy, record who's account we're using
        self._logged_in = True
        self._user = last_name
    
    def request(self, verb, url, *args, **kwargs):
        """
        Rewrite all requests going through this session to go through the library proxy.
        
        Of course, the library proxy is not a standard HTTP proxy at all: it does its own thing.
        Luckily, the protocol is pretty simple: just tack on a domain and make sure to send the right cookie.
        """
        assert self._logged_in == "logging_in" or self._logged_in, "Must be logged in to use the library proxy" #it will 302 to the login page if you're not; since this would be confusing when scripting, just disallow it.
        
        def proxyify(url):
            scheme, host, path, params, query, fragment = urlparse(url)
            proxy_host = host + ".proxy.lib.uwaterloo.ca"
            return urlunparse((scheme, proxy_host, path, params, query, fragment))
        
        proxy_url = proxyify(url)
        
        # rewrite the referer to use the proxy too
        # TODO: where else do we leak URLs?
        if 'headers' in kwargs:
            if 'Referer' in kwargs['headers']:
                kwargs['headers']['Referer'] = proxyify(kwargs['headers']['Referer'])
        
        #*disable* SSL checking because the libary proxy has an out of date cert or something. ugh.
        # TODO: figure out what's going on here; what if I explicitly add UW's cert to the search path (which python-requests lets me do by setting verify to a path instead of a boolean)
        if 'verify' not in kwargs:
            kwargs['verify'] = False 
        return super().request(verb, proxy_url, *args, **kwargs)
        

class AnonymizedUAMixin(requests.Session):
    """
    a requests.Session that tweaks settings to try to anonymize some of our details,
    just because there's no reason not to fly under the radar if we can.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers['User-Agent'] = self.random_UA()

    @staticmethod
    def random_UA():
        """
        
        # TODO: a library that automatically downloads common user agents and picks one
        """
        return "Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0"
    