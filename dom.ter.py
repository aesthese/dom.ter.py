import requests
from bs4 import BeautifulSoup
from netaddr import IPNetwork


def from_mx(domain):
    url = "http://www.dom.ter.dk/?mx=%s" % domain

    req = requests.get(url)
    source = req.text

    soup = BeautifulSoup(source, "lxml")

    links = soup.find_all(name="a", attrs={"class": "extlink"})

    results = []
    for link in links:
        results.append(link["href"][11:-1])

    return results


def from_ns(domain):
    url = "http://www.dom.ter.dk/?ns=%s" % domain

    req = requests.get(url)
    source = req.text

    soup = BeautifulSoup(source, "lxml")

    links = soup.find_all(name="a", attrs={"class": "extlink"})

    results = []
    for link in links:
        results.append(link["href"][11:-1])

    return results


def from_ip(ip):
    url = "http://www.dom.ter.dk/?ip=%s" % ip

    req = requests.get(url)
    source = req.text

    soup = BeautifulSoup(source, "lxml")

    links = soup.find_all(name="a", attrs={"class": "extlink"})

    results = []
    for link in links:
        results.append(link["href"][11:-1])

    return results


def from_ip_range(the_range):
    ip_range = IPNetwork(the_range)
    ip_list = list(ip_range)

    result = []

    for ip in ip_list:
        result += from_ip(ip)

    return result
