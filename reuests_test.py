import requests
from header import get_header


def cookie_cutter():
    """ returns login cookies in dict format """
    sweets = open('cookies.txt', 'r').read().splitlines()
    cookie = {}
    for i in sweets:
        x = i.split()
        l = list(x[4])
        if l[0] in '1234567890':
            x[4], x[5] = x[5], x[4]
        # domain = x[0]
        # secure = x[1]
        name = x[4]
        try:
            value = x[6]
        except IndexError:
            value = x[5]
        # path = x[2]
        cookie[name] = value
    return cookie

d = {"sessionid": "f40247e2d924e43a7dab6b56",
                       "currency": 3,
                       "subtotal": 1,
                       "fee": 2,
                       "total": 3,
                       "quantity": 1}
url = 'https://steamcommunity.com/market/buylisting/726564084060013124'
h = headers = {"Accept": "text/javascript, text/html, application/xml, text/xml, */*",
               "Accept-Encoding": "gzip,deflate,sdch",
               "Accept-Language": "en-US,en;q=0.8",
               "Host": "steamcommunity.com",
               "Referer": "http://steamcommunity.com/market/listings/730/P250%20|%20Boreal%20Forest%20%28Field-Tested%29",
               "Origin": "http://steamcommunity.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
               }

r = requests.post(url, data=d, headers=get_header("http://steamcommunity.com/market/listings/730/P250%20|"
                                                  "%20Boreal%20Forest%20%28Field-Tested%29"), cookies=cookie_cutter())

print(r.status_code)
print(r.text)
