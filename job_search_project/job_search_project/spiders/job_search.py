import scrapy


class JobSearchSpider(scrapy.Spider):
    name = 'job_search'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://craigslist.org/']

    def parse(self, response):
        pass
