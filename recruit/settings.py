# -*- coding: utf-8 -*-

# Scrapy settings for recruit project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'recruit'

SPIDER_MODULES = ['recruit.spiders']
NEWSPIDER_MODULE = 'recruit.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'recruit (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

CLOSESPIDER_TIMEOUT = 30

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    #'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    #'Content-Type': 'application/x-www-form-urlencoded',
    #'Host': 'http://bbs.ngacn.cc',
    #'Origin': 'https://passport.csdn.net',
    #'Referer': 'https://passport.csdn.net/account/login',
    #'Upgrade-Insecure-Requests': 1,
    #'Host': 'bbs.ngacn.cc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    #'Cookie': 'bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/0a001e494662a12b19fdb530e318%22%2C1%3A1493701482%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-43%2C1%3A1493139684%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1493139684%7D%7D; CNZZDATA30039253=cnzz_eid%3D175419729-1469427320-%26ntime%3D1493095966; CNZZDATA30043604=cnzz_eid%3D1770945354-1469428374-%26ntime%3D1493097569; __utma=240585808.2050012559.1469522546.1493026894.1493096691.63; __utmz=240585808.1487312719.51.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; CNZZDATA1256638858=8220914-1472989817-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1479979790; CNZZDATA1256638851=1122129359-1475132538-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1492646600; CNZZDATA1256638828=664457739-1482284745-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1491528706; CNZZDATA1256638874=1420002279-1487224733-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1491612097; UM_distinctid=15b465a569ba1-010239ebbab367-41544131-15f900-15b465a569c2d4; CNZZDATA1256638820=434122517-1491530851-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1493093232; ngaPassportUid=guest058fed8e8e6d04; guestJs=1493097431; __utmb=240585808',
    'Connection': 'keep-alive'
    }


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'recruit.middlewares.recruitSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'recruit.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'recruit.pipelines.RecruitPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
