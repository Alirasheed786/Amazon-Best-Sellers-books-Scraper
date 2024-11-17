import scraper_helper as sh
# Scrapy settings for amazon_bs_books project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amazon_bs_books'

SPIDER_MODULES = ['amazon_bs_books.spiders']
NEWSPIDER_MODULE = 'amazon_bs_books.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# CLOSESPIDER_ITEMCOUNT = 20

LOG_FILE = 'spider.log'

# DEFAULT_REQUEST_HEADERS = sh.get_dict(
#     '''
#     accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
#     accept-encoding: gzip, deflate, br
#     accept-language: en-US,en;q=0.9
#     cache-control: no-cache
#     cookie: session-id=135-0977884-7912814; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=134-8892929-3300361; lc-main=en_US; session-token=+2pmzzMqgPw6KEOY6CiandbMvwnCrlbA25xRnf6tHFJaArtl88ApjbtQ+s9ZhRHH45fH6Ngdp/fg/zHfC7up8TSF1UO/0wOjFX2t4SoNSc2c/6pgLh2eY35fcBaxbulDwsZ3hPz2mLx/ED+1sT4RMCN+4ZItenqymcBSGEXNEruw105zYgONWLPHIy36ZRPi; csm-hit=tb:8QCT5J68S0VPD43XDD03+s-4854Q6ZNY1KX2KPW74GD|1624962978059&t:1624962978059&adb:adblk_no
#     downlink: 1.3
#     ect: 3g
#     pragma: no-cache
#     rtt: 300
#     sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
#     sec-ch-ua-mobile: ?0
#     sec-fetch-dest: document
#     sec-fetch-mode: navigate
#     sec-fetch-site: same-origin
#     sec-fetch-user: ?1
#     upgrade-insecure-requests: 1
#     user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
#     '''
# )


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
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

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'amazon_bs_books.middlewares.AmazonBsBooksSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610,
# }

# ZYTE_SMARTPROXY_ENABLED = True
# ZYTE_SMARTPROXY_APIKEY = '496e9c4ced6d49308b465c44c7289562'

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'amazon_bs_books.pipelines.AmazonBsBooksPipeline': 300,
}

SCRAPINGBEE_API_KEY = 'Scrapingbee API key'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_scrapingbee.ScrapingBeeMiddleware': 725,
}

CONCURRENT_REQUESTS = 5

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# AUTOTHROTTLE_ENABLED = True