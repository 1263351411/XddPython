import re
import time
import requests
from urllib import request
from bs4 import BeautifulSoup
import urllib.request

firefoxHead = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
IPRegular = r"(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])"
host = "https://blog.csdn.net"
url = "https://blog.csdn.net/qq_41903671/article/details/{}"

codes = ["90046569", "90046712"]


def parseIPList():
    _RR = re.compile(b"""<td data-title="IP">(?P<ip>[.\d]*)</td>[^<]*<td data-title="PORT">(?P<post>[\w]*)</td>""")
    IPs = []
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    req = request.Request("https://www.kuaidaili.com/free/inha/1", headers=headers)
    html = request.urlopen(req).read()
    # print(html.decode())
    lt = _RR.findall(html)
    for i in lt:
        IPs.append("{}:{}".format(i[0].decode(),i[1].decode()))
    return IPs


def PV(IP):
    s = requests.Session()
    s.headers = firefoxHead

    for i in range(len(codes)):
        print("No.{}\t".format(i), end="\t")
        s.proxies = {"http": "{}:8080".format(IP)}
        s.get(host)
        r = s.get(url.format(codes[i]))
        html = r.text
        print(html)
        soup = BeautifulSoup(html, "html.parser")
        spans = soup.find_all("span")
        print(spans)
        # print(spans[2].string)
        time.sleep(2)


def main():
    IPs = parseIPList()
    print(IPs)
    for i in range(len(IPs)):
        print("正在进行第{}次访问\t".format(i), end="\t")
        PV(IPs[i])


if __name__ == "__main__":
    main()
