
import scrapy
import datetime as dt

from ..items import JobSearchProjectItem
from scrapy.loader import ItemLoader


class JobSearchSpider(scrapy.Spider):
    name = 'job_search'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://www.craigslist.org/about/sites']
    scrapped_jobs = []

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
        jobs = response.css('.result-row')
        for job in jobs:
            job_title = job.css('h3 a::text').get().strip()
            date = job.css('.result-date::attr(datetime)').get().strip()
            job_date = dt.datetime.strptime(date, '%Y-%m-%d %H:%M')
            filter_date = dt.datetime.now() - dt.timedelta(days=2.0)

            if job_title not in self.scrapped_jobs and job_date >= filter_date:
                self.scrapped_jobs.append(job_title)
                job_url = job.css('.hdrlnk::attr(href)').get()
                print(job_title)

                yield scrapy.Request(
                    url=job_url,
                    callback=self.parse_job
                )

    @staticmethod
    def parse_job(response):
        l = ItemLoader(
            item=JobSearchProjectItem(),
            selector=response
        )
        l.add_css('title', '#titletextonly::text')
        l.add_css('salary', 'span:nth-child(1) b::text')
        l.add_css('timing', 'br+ span b::text')
        l.add_css('communication', 'span:nth-child(5)::text')
        l.add_css('job_posted', '#display-date .timeago::attr(datetime)')
        l.add_value('job_url', response.url)
        yield l.load_item()
