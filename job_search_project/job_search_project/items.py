# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobSearchProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    timing = scrapy.Field()
    communication = scrapy.Field()
    job_posted = scrapy.Field()
    job_url = scrapy.Field()
