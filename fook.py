import requests
import logging
logger = logging.getLogger()
from time import sleep

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


get_buy_price("http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Well-Worn%29")