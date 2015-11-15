import requests
import logging
from time import sleep
from datetime import datetime
logger = logging.getLogger()


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


def get_buy_price(xx):
    """ returns buy price for items """
    try:
        it = xx.split('730')
        it2 = it[1]
        it3 = 'http://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name='
        r = requests.get(it3 + it2[1:], timeout=10)
        # print(r.status_code, r.reason)
        js = r.json()
        med_price = js['median_price']
        qq = med_price.split(',')
        if int(qq[0]) == 0:
            a = list(med_price)
            c = a[2] + a[3]
            d = int(c) * 15 / 100
            e = int(c) * 20 / 100
            if int(c) <= 12:
                print('price for', xx, int(int(c) - d) - 1)
                return int(int(c) - d) - 2
            if int(c) >= 20:
                print('price for', xx, int(int(c) - e) - 1)
                return int(int(c) - e) - 2
            else:
                print('price for', xx, int(int(c) - d) - 1)
                return int(int(c) - d) - 2
        elif int(qq[0]) > 0:
            l = med_price.split('&')[0]
            k = l.split(',')
            m, n = k[0], k[1]
            if n == '--':
                c = int(m + '00')
                d = int(c) * 15 / 100
                print('price for', xx, int(int(c) - d) - 2)
                return int(int(c) - d) - 2
            c = int(m + n)
            d = int(c) * 15 / 100
            print('price for', xx, int(int(c) - d) - 2)
            return int(int(c) - d) - 2
    except BaseException as e:
        logger.error('get_buy_price retrying with error: ' + str(e))
        sleep(12)
        return get_buy_price(xx)


def sessionid():
    """ returns session id from cookies.txt """
    return cookie_cutter()['sessionid']


def buy(url, id_, load):
    # print('buying', url)
    # print('with id ', id_)
    # print('load', load)
    buy_url = 'https://steamcommunity.com/market/buylisting/' + id_
    r = requests.post(buy_url, data=load, headers=get_header(url), cookies=cookie_cutter())
    print(buy_url, '\n', load + '\n', get_header(url), '\n')

    with open('log.txt', 'a') as f:
        f.write(str(datetime.now()) + r.text + r.reason + '\n')

