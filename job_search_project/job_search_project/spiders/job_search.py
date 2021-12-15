import scrapy


class JobSearchSpider(scrapy.Spider):
    name = 'job_search'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://www.craigslist.org/about/sites']

    def parse(self, response):
        countries = response.css('.colmask:nth-child(6) a::attr(href), .colmask:nth-child(4) a::attr(href)').getall()
        print('COUNTRIES LENGTH: ', len(countries))

        for country_link in countries:
            host = country_link[8:-1]
            yield scrapy.Request(
                url=f'{country_link}search/jjj?sort=date&query=python',
                callback=self.parse_search,
                headers={
                    'Host': host,
                }
            )

    def parse_search(self, response):
        print(response)
