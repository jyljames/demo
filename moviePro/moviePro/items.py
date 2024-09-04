# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    actors = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    showtime = scrapy.Field()
    time = scrapy.Field()
    score = scrapy.Field()
    introduction = scrapy.Field()
    img_url = scrapy.Field()
    img = scrapy.Field()
    murl = scrapy.Field()
