# Scrapy settings for gdg_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'gdg_scrapy'

SPIDER_MODULES = ['gdg_scrapy.spiders']
NEWSPIDER_MODULE = 'gdg_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gdg_scrapy.middlewares.GdgScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gdg_scrapy.middlewares.GdgScrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from dotenv import load_dotenv
import os 


BIGQUERY_DATASET = "scrapy_data"
BIGQUERY_TABLE = "test_products"
BIGQUERY_SERVICE_ACCOUNT = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiYmlvbmljLWluc2lnaHQtMzE5NjIzIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiZTI2MDVlZGUxYjQyZGUxOTBiYmZiZTkxNDVkNzcyNTY4NGFkOWM3YiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZnSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFDV3pqZDRwUUR4SmRTWlxuUkUxYnVmSnFHSys2TnE1L045YlZZVU9xOWZqcitKZVZlSFVHQitDejg2SFhjUFZDNmdzRThjbzl6eEd2SGY1VVxubUh2RHFKZTNNQmZIZUc3TWNxaUJSMEdnQ2syODlDR29lOGU2bTFENnc1cVFrMTRRTW5Mdy9td1VFZ2JHN0VLOFxuSHJiWkI2U3R2ODE4RFVKNnVsNFN5L0E0cnFMcGVxaUVaN2ptcWtLOFdiTCtwOUplME00N0k2MHc2ZlZaMXNMa1xuckw1OCt6NVNJb0E5Ymdqa25jMTNVZ3ZXR29oeDE4aUVzaG9iTmhUSWg0WmQyTVo5VnlWRXNmc05kb0dBaEU0NlxucEhhMmhqZk5qaU9DekR1OTJLaHRYaDVCSHdMTXVQbkV1NmIrZ1ZURzVpYlJqOHVlSkdtZnc2ZEo2M3k2blNrWVxuaW1iQWNlM3pBZ01CQUFFQ2dnRUFKTzd6U2ZKTFZVUDVHZUpPK2RpRUJMVHdFTENFc3ZhSGdISFdRMEFEaXpNeVxuV0xLTUlvSjZaMGdUU25MSk5tNmdiVUVVVVdmdHdsQWJzamM0RkhhdFZYbUxVVmh1OWxaY2EzRDZvd255K1FSblxuVzk2WXoxeHJqRWFzaTV6ejdBNlc5T3V5cDRXMHNESTdzOXZuMXlaV2tCRUo3OGhGa0U0bGJRQVNZS2R3a2JLT1xubHdNMGQ3bUFCd3M0WGRIMmJ2S0hZV3NTUE9Vd1lNVzNIS3lvZUpoUlQ4b1Y1L3BBQlRlQ2hlN0xQYVQ3dmZkeVxuWHdtVVdDV2xIZDhpZzdKKytrRVZvVGhnUGZhd2E0ck5ZRHRyUXgrZ081b29UUzE3b3Q4NWtiZUUzSW5EVWxEOVxueFpKOSsxcWhqQWdwUDFaS2tvK0xIdVhVeVVYSTR4ZUhyTTB0R3RiWkNRS0JnUURVMmMvanp0WENPN0drSGhWRlxuaXBEdURKR0ZpU0tScjc5VFBUaVg5a3UzRGlNZno1UlJtTFNnY3hzbDJkbVArdldEN05hK0M3VDJGNTZyQzdBN1xuSkVRSDFNVFVaL3QyalZpVTF6UGRycHFBTVRXL1VxclVoVGg1RW1BcU1oOEdRcU4wak53WXYzQ0E3MGtGQVJxaFxubTJNN0ltSFVlT2wxVzQvTitmc0RQaFcwQ1FLQmdRQzFZSHB5Q2ZKSXI1L1FSakRDT3VEUmlIS3hGQU93ekM2MVxuWTBYSVVzbnhTQUt5OWFqSVVMb25CVExCdFhjemdzVjFITUFPUVNma3JvK2N1cXNZOC9nQ3FTMTE2U29ESzdWelxuWnBua081K1ZkWGhBbVZaK255VDFkNUtIK1kyN3ZCTENldG1DaHBzckg4aGQvZ3lWYVArQWd3ZHhHMitWbnN2YVxudWpEMzNWNnBHd0tCZ1FDcmdhSXdWbTRKSnQ1WmRsLy9lOHFSOVpDZ1A4S2FEem1qMGJXelJLTDNxaTJGS1ZiQ1xuZE1BK2RPRlFHM3hodG41endiZTZ4R1lZMFNscGUyNlNDUVBFSjU0OTVGZEx6Rkt2QThSb0FKTy9iV2Q0ZFJ6dlxuUnpVYzRVQ1pYMjkrTk4zT1FOM3NGdjJJOXNZb2dSNDdUNkNpZW03SHJIRzR2WUZmSCtreFVLcGVPUUtCZ0M2a1xuN3hoZ3duUTY1aWlUeEhwTzFmNU16dUlIT2FPLy9zc2JDcGtuNFZNeHA3QUtTU3VxeHhTOTIzM0JnelEyRHoyOFxuOVE4MVptTURHVisvQ2IxVEVKYnVsd2hadkRvd2hXdDJHV0YraTkzTjVlMEhBaDF5SS9rVWxSUnU4eW95aGNpSlxuKzJINzUrL0JMckF0WTJNUks1UUxIbURTSTNJZzhsLy92aFFnVS9XOUFvR0JBTEJ6MFFENnEwL1VPMUozTkFVaVxub1lIVDVSUkx0UTZ2T05kUmJES0RYUC9KYWxGOGpncTRIMFVudWdFUjZLZWFHS1loNk54bE5jU1pCS2wzaTIwUlxuRkZ4ckJHWkg4MHpWVEpEWmhwS09EOWZqVkY5UWNNT2R6MHNES3doOXBGV2I2SGR0SEQ5Y2hFbWpaR1dPcklzZ1xuSGY2cUp3ZnB3UzJtQ2hnVWNJd2ppQldLXG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAic2NyYXB5LWluamVjdGlvbkBiaW9uaWMtaW5zaWdodC0zMTk2MjMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTA4NTgyOTQ3MzQ2NDU2MjM5NTUwIiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9zY3JhcHktaW5qZWN0aW9uJTQwYmlvbmljLWluc2lnaHQtMzE5NjIzLmlhbS5nc2VydmljZWFjY291bnQuY29tIgp9Cg=="

ITEM_PIPELINES = {
    
    'gdg_scrapy.pipelines.GdgScrapyPipeline': 300,
    "bigquerypipeline.pipelines.BigQueryPipeline": 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
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
