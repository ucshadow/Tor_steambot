import json
import requests

url = 'http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Well-Worn%29'
tail = '/render?start=0&count=5&currency=3&language=english&format=json'


def f():
    r = requests.get(url + tail).json()
    print(r)
    return r

res = []

for item, key in f()['listinginfo'].items():
    res.append([item, key['converted_price']])
print(res)