import io
import pycurl
import json
from header import get_header


h = ["Accept:text/javascript, text/html, application/xml, text/xml, */*",
               "Accept-Encoding:gzip,deflate,sdch",
               "Accept-Language:en-US,en;q=0.8",
               "Host:steamcommunity.com",
               "Referer:http://steamcommunity.com/market/listings/730/P250%20|%20Boreal%20Forest%20%28Field-Tested%29'"
               "Origin:http://steamcommunity.com",
               "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
               ]


def query():
    """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

    url = 'https://steamcommunity.com/market/buylisting/797495778193078869'
    data = json.dumps({"sessionid": "f40247e2d924e43a7dab6b56",
                       "currency": "3",
                       "subtotal": "1",
                       "fee": "2",
                       "total": "3",
                       "quantity": "1"})
    output = io.BytesIO()

    query = pycurl.Curl()
    query.setopt(pycurl.COOKIEFILE, 'cookies.txt')
    query.setopt(pycurl.URL, url)
    #query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, 8000)
    query.setopt(pycurl.HTTPHEADER, h)
    query.setopt(pycurl.POST, 1)
    query.setopt(pycurl.POSTFIELDS, data)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
    query.setopt(pycurl.VERBOSE, True)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s)" % (url, exc)


print(query())
