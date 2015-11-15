__author__ = 'SHADOW'

from functions import *
import io
import pycurl
import requests
import stem.process
import concurrent.futures
from stem.util import term
import json
import time
from urllib.parse import unquote
import socks  # SocksiPy module
import socket
import urllib
import stem.process
from stem.util import term
import time
import concurrent.futures
import logging
from random import randint

logger = logging.getLogger()




SOCKS_PORT = 7000
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
# socket.socket = socks.socksocket

urls = ["http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Well-Worn%29",
        "http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Field-Tested%29",
        "http://steamcommunity.com/market/listings/730/P2000%20%7C%20Amber%20Fade%20%28Field-Tested%29",
        "http://steamcommunity.com/market/listings/730/USP-S%20%7C%20Torque%20%28Field-Tested%29",
        "http://steamcommunity.com/market/listings/730/Dual%20Berettas%20%7C%20Cobalt%20Quartz%20%28Field-Tested%29"
        ]


'''def buy(url):
    if url == "https://www.atagar.com/echo.php" or url == "http://canihazip.com/s":
        return requests.get(url).text
    tail = '/render?start=0&count=5&currency=3&language=english&format=json'
    try:
        return requests.get(url + tail).json()
    except:
        print("Unable to reach", url)'''


def curl(url):
    if url == "https://www.atagar.com/echo.php" or url == "http://canihazip.com/s":
        u = url
    else:
        u = url + '/render?start=0&count=5&currency=3&language=english&format=json'
    output = io.BytesIO()
    query = pycurl.Curl()
    query.setopt(pycurl.URL, u)
    query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue().decode('utf-8')
    except pycurl.error as exc:
        print("Unable to reach %s (%s)" % (url, exc))


def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
        print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))
tor_process = stem.process.launch_tor_with_config(
    tor_cmd=r'C:\Users\SHADOW\Desktop\New folder\Tor Browser\Browser\TorBrowser\Tor\tor.exe',
    config={
        'SocksPort': str(SOCKS_PORT),
        'ExitNodes': '{ru}',
    },
    init_msg_handler=print_bootstrap_lines,
)


def main_function(x, y):
    duplicate_check = []
    session = sessionid()
    while True:
        try:
            a = curl(x)
            # print(a)
            if a == "null":
                print("Null")
            b = json.loads(a)
            res = []
            form_data = {}
            for item, key in b['listinginfo'].items():
                try:
                    res.append([item, key['converted_price']])
                    form_data[item] = {"sessionid": session,
                                       "currency": 3,
                                       "subtotal": int(key['converted_price']) - int(key['converted_fee']),
                                       "fee": int(key['converted_fee']),
                                       "total": int(key['converted_price']),
                                       "quantity": 1
                                       }
                except KeyError:
                    res.append("SOLD!")
            print(y, '-->', unquote(x.split("/render")[0]).replace(' ', ''), res)
            # print(form_data)
            # print(' ')
            for price in res:

                if price != 'SOLD!':
                    if price[1] <= int(y):
                        print('GOT ONE')
                        if price[0] not in duplicate_check:
                            buy(x, price[0], form_data[price[0]])
                            duplicate_check.append(price[0])
            # print(res)
        except BaseException as e:
            logger.error('ERR ' + str(e))
            continue
        sleep(randint(10, 20))


def f():
    prices_list = []
    for item in urls:
        prices_list.append(get_buy_price(item))
    print(term.format(curl("https://www.atagar.com/echo.php"), term.Color.YELLOW))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(main_function, urls, prices_list)
        # print(requests.get("http://canihazip.com/s").text)


# one_by_one()
# f()
# print(curl("http://canihazip.com/s"))
# print(curl("http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Well-Worn%29"))

'''
while True:
    f()
    time.sleep(10)'''

if __name__ == '__main__':
    f()


tor_process.kill()  # stops tor'''
