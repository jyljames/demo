# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class DangdangbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    isbn = scrapy.Field()
    desc = scrapy.Field()
    img = scrapy.Field()
