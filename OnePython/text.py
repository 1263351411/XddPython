import random
from urllib import request
import requests
import re
import time

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
        "https://blog.csdn.net/u013008795/article/details/91049675",
        "https://blog.csdn.net/u013008795/article/details/90741950",
        "https://blog.csdn.net/u013008795/article/details/90731526",
        "https://blog.csdn.net/u013008795/article/details/90730818"

    ]

    def __init__(self):
        self.page = 0
        self.proxy = []

    def get_proxy(self):
        self.page += 1
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        req = request.Request("https://www.kuaidaili.com/free/inha/"+str(self.page)+"/", headers=headers)
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
        }
        while True:
            #随机选择UA代理
            user_agent = random.choice(self.USER_AGENTS) #header
            proxy = random.choice(self.proxy) #iip:post
            url = random.choice(self.URL_LIST) #url

            try:
                # 设置request的代理
                httpproxy_handler = request.ProxyHandler({"http": proxy})
                opener = request.build_opener(httpproxy_handler)
                request.install_opener(opener)

                #伪装访问获取cookies
                res = requests.get("https://blog.csdn.net/u013008795/article/details/91049675")
                # time.sleep(0.5)
                cookies = requests.utils.dict_from_cookiejar(res.cookies)
                for k,v in cookies.items():
                    # print(k,v,cookies["uuid_tt_dd"],cookies["dc_session_id"])
                    print(k,v)
                break

                # 访问网页
                headers["User-Agt"] = user_agent
                # headers["Cookie"] = "TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Farticle%252Fdetails%22%2C%22tid%22%3A%22a138c5106d34ca%22%2C%22q%22%3A0%2C%22a%22%3A301%7D; uuid_tt_dd=10_37330046790-1553678136450-721657; dc_session_id=10_1553678136450.722856; acw_tc=276082a915598985313753273eb68123e21008ff68f1d6fd6822bc81de7b6b; acw_sc__v2=5cfa5cd3fa449b509b3eb1008898cefa53682f1b; dc_tos=psqbiy; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1559898533,1559906358,1559909208; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1559911644; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37330046790-1553678136450-721657; c-login-auto=14"
                data = "TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Farticle%252Fdetails%22%2C%22tid%22%3A%22a138c5106d34ca%22%2C%22q%22%3A0%2C%22a%22%3A301%7D;"
                headers["Cookie"] = data + "uuid_tt_dd="+cookies["uuid_tt_dd"]+"; dc_session_id="+cookies["dc_session_id"]+"; acw_tc=276082a915598985313753273eb68123e21008ff68f1d6fd6822bc81de7b6b; acw_sc__v2=5cfa5cd3fa449b509b3eb1008898cefa53682f1b; acw_sc__v3=5cfa535594af5906d9dc8fcb5e7da05aa94bf9e5; dc_tos=psqbiy; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1559898533,1559906358,1559909208; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1559911644; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*"+cookies["uuid_tt_dd"]+"; c-login-auto="+str(num)
                # headers["Cookie"] = self._cok.format(num)
                # headers["Cookie"] = cook

                req = request.Request(url, headers=headers)
                repose = request.urlopen(req).read()
                # print(repose)
                renum = re.compile(b"""<span class="read-count">[^\w<]*([\w]*)</span>""")
                print("{}阅读数量：{}".format(url,renum.findall(repose)[0].decode()))
                num += 1

                # break
            except Exception as resexcp:
                err_num += 1
                print("{}错误信息{}".format(err_num,resexcp))
                if err_num >= 12:
                    self.__init__()
                    break
        # print("正在重新获取代理IP...")
        # self.get_proxy()

if __name__ == "__main__":
    xddcsdn = Xdd_CsdnPC()
    xddcsdn.get_proxy()