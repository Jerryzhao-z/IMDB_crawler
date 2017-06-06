# -*- coding: utf-8 -*-

# Scrapy settings for imdb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'imdb'

SPIDER_MODULES = ['imdb.spiders']
NEWSPIDER_MODULE = 'imdb.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imdb (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'imdb.middlewares.ImdbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'imdb.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'imdb.pipelines.ImdbPipeline': 300,
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

# Retry many times since proxies often fail
RETRY_TIMES = 5
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#    'scrapy_proxies.RandomProxy': 100,
    'imdb.middlewares.RandomUserAgent':1,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'imdb.middlewares.ProxyMiddleware': 100,
    #'scrapy_crawlera.CrawleraMiddleware': 600 
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
#PROXY_LIST = '/mnt/d/user/EPFL/QA-project/spider_imdb/scrapy_project/imdb/imdb/proxy.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
#PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"


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

PROXIES = [
    {'ip_port': '94.177.233.247:8080', 'user_pass': ''},
    {'ip_port': '94.177.233.10:1000', 'user_pass': ''},
    {'ip_port': '193.248.154.41:3128', 'user_pass': ''},
    {'ip_port': '89.36.218.91:3128', 'user_pass': ''},
    {'ip_port': '89.40.127.171:8080', 'user_pass': ''},
    {'ip_port': '89.40.127.171:3128', 'user_pass': ''},
    {'ip_port': '89.36.218.91:8080', 'user_pass': ''},
    {'ip_port': '46.101.225.83:3128', 'user_pass': ''},
    {'ip_port': '78.47.27.99:3128', 'user_pass': ''},
    {'ip_port': '213.39.60.100:3128', 'user_pass': ''},
    {'ip_port': '89.38.146.208:80', 'user_pass': ''},
    {'ip_port': '217.61.16.86:80', 'user_pass': ''}
]

'''
    {'ip_port': '46.218.73.162: 80', 'user_pass': ''},
    {'ip_port': '37.187.100.23:3128', 'user_pass': ''},
    {'ip_port': '167.114.241.123:80', 'user_pass': ''},
    {'ip_port': '213.246.39.38:3128', 'user_pass': ''},
    {'ip_port': '149.202.217.218:80', 'user_pass': ''},
    {'ip_port': '5.135.195.166:3128', 'user_pass': ''},
    {'ip_port': '46.218.85.101:3129', 'user_pass': ''},
    {'ip_port': '51.254.127.194:8081', 'user_pass': ''},
    {'ip_port': '178.32.117.226:3128', 'user_pass': ''},

    {'ip_port': '62.210.51.150:80', 'user_pass': ''},
    {'ip_port': '91.121.88.60:80', 'user_pass': ''},
    {'ip_port': '86.253.83.158:80', 'user_pass': ''},
    {'ip_port': '87.98.159.184:3128', 'user_pass': ''},
    {'ip_port': '51.254.252.34:80', 'user_pass': ''},
    {'ip_port': '51.254.252.34:80', 'user_pass': ''},

    {'ip_port': '37.59.80.69:8080', 'user_pass': ''},
    {'ip_port': '151.80.197.192:80', 'user_pass': ''},
'''