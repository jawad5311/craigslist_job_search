import scrapy


class JobSearchSpider(scrapy.Spider):
    name = 'job_search'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://www.craigslist.org/about/sites']

    def parse(self, response):
        print(response)
