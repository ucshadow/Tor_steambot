import io
import pycurl
import stem.process
from stem.util import term
import json

SOCKS_PORT = 7000

u = "http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Elite%20Build%20%28Well-Worn%29"
t = '/render?start=0&count=5&currency=3&language=english&format=json'


def query(url):
    """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

    output = io.BytesIO()

    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue().decode('utf-8')
    except pycurl.error as exc:
        return "Unable to reach %s (%s)" % (url, exc)


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


def m():
    r = query(u + t)
    print(r)
    a = json.loads(r)
    res = []
    for item, key in a['listinginfo'].items():
        try:
            res.append([item, key['converted_price']])
        except KeyError:
            res.append("SOLD!")
    # print(unquote(x.split("/render")[0]).replace(' ', ''), res)
    return res

print(m())

tor_process.kill()  # stops tor
