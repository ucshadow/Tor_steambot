def get_header(x):
    header = {"Accept": "text/javascript, text/html, application/xml, text/xml, */*",
               "Accept-Encoding": "gzip,deflate,sdch",
               "Accept-Language": "en-US,en;q=0.8",
               "Host": "steamcommunity.com",
               "Referer": x,
               "Origin": "http://steamcommunity.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
               }
    return header
