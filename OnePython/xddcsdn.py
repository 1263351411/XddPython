import random
from urllib import request
import re

class Xdd_CsdnPC():

    _RR = re.compile(b"""<td data-title="IP">(?P<ip>[.\d]*)</td>[^<]*<td data-title="PORT">(?P<post>[\w]*)</td>""")

    USER_AGENTS = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
    ]

    URL_LIST = [
        "https://blog.csdn.net/u013008795/article/details/91049694",
        "https://blog.csdn.net/u013008795/article/details/91049675"
    ]

    def __init__(self):
        self.page = 0
        self.proxy = []

    def get_proxy(self):
        self.page += 1
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        req = request.Request("https://www.kuaidaili.com/free/inha/"+str(self.page), headers=headers)
        html = request.urlopen(req).read()
        # print(html.decode())
        lt = self._RR.findall(html)
        for i in lt:
            self.proxy.append("{}:{}".format(i[0].decode(),i[1].decode()))
        if self.proxy:
            print("现在使用的是第{}页的代理IP".format(self.page))
            self.spider()

    def spider(self):
        num = 0 #访问技术
        err_num = 0 #异常计数
        headers = {
            # "Host": "blog.csdn.net",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            # "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Referer": "https://blog.csdn.net/qq_41782425/article/details/84934224",
            # "Accept-Encoding": "gzip",
            "Accept-Language": "zh-CN,zh;q=0.9"
            # "Cookie": "your cookie"
        }
        while True:
            #随机选择UA代理
            user_agent = random.choice(self.USER_AGENTS) #header
            proxy = random.choice(self.proxy) #iip:post
            url = random.choice(self.URL_LIST) #url

            # cookie_jar = RequestsCookieJar()
            # cookie_jar.set("dc_session_id", "10_1559897369110.714629", domain=".csdn.net")
            # cookie_jar.set("uuid_tt_dd", "1559897369110", domain=".csdn.net")
            # print(cookie_jar)
            #
            # r = requests.get(url, headers=headers, cookies=cookie_jar)
            # # print(r.content)
            # gziphtml = r.content.decode("utf-8")


            try:
                # 设置request的代理
                httpproxy_handler = request.ProxyHandler({"http": proxy})
                opener = request.build_opener(httpproxy_handler)
                request.install_opener(opener)

                # 访问网页
                headers["User-Agt"] = user_agent
                req = request.Request(url, headers=headers)
                rr = request.urlopen(req)
                gziphtml = rr.read()

            except Exception as resexcp:
                err_num += 1
                print("{}错误信息{}".format(err_num,resexcp))
                if err_num >= 12:
                    self.__init__()
                    break
        print("正在重新获取代理IP...")
        self.get_proxy()

if __name__ == "__main__":
    xddcsdn = Xdd_CsdnPC()
    xddcsdn.get_proxy()