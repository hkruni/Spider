# -*- coding: utf-8 -*-


import os
import  sys

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, PROJECT_ROOT)

#Scrapy项目实现的bot的名字(也为项目名称),这将用来构造默认 User-Agent，同时也用来log。当您使用 startproject 命令创建项目时其也被自动赋值。
BOT_NAME = 'proxy'

#Scrapy搜索spider的模块列表
SPIDER_MODULES = ['proxy.spiders']
NEWSPIDER_MODULE = 'proxy.spiders'
DOWNLOAD_HANDLERS = {'s3': None,}


#Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值（默认: 100）。
CONCURRENT_ITEMS = 100
#Scrapy downloader 并发请求(concurrent requests)的最大值（默认: 16）。
CONCURRENT_REQUESTS = 20
#对单个网站进行并发请求的最大值（默认：8）。
CONCURRENT_REQUESTS_PER_DOMAIN = 10
#下载器超时时间（单位是秒）
DOWNLOAD_TIMEOUT = 20
#下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数。
DOWNLOAD_DELAY = 1.5
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    'common.middlewares.useragent.UserAgentMiddleware': 730,
    # 'common.middlewares.proxy.ProxyMiddleware': 735,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 740,
}

EXTENSIONS = {
            'scrapy.telnet.TelnetConsole': 200,
#             'scrapy.extensions.statsmailer.StatsMailer': 500,
}

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [{"http": "112.95.43.19:8118"},
{"http": "121.239.104.161:808"},
{"http": "121.226.6.92:808"},
{"http": "116.19.122.196:808"},
{"http": "121.56.189.189:808"},
{"http": "121.56.138.198:8000"},
{"http": "175.180.192.170:8080"},
{"http": "183.141.127.71:3128"},
{"http": "182.203.2.36:8888"},
{"http": "39.1.47.1:8080"},
{"http": "182.90.73.230:80"},
{"http": "175.44.12.102:8888"},
{"http": "39.1.46.108:8080"},
{"http": "171.39.233.49:80"},
{"http": "58.217.11.125:808"}]

try:
    from settings_local import *
except:
    pass