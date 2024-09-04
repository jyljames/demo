# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    music_name = scrapy.Field()
    music_another_name = scrapy.Field()
    singer = scrapy.Field()
    music_type = scrapy.Field()
    media = scrapy.Field()
    showtime = scrapy.Field()
    publisher = scrapy.Field()
    music_introduction = scrapy.Field()
    img_url = scrapy.Field()
    img = scrapy.Field()
    music_score = scrapy.Field()
    murl = scrapy.Field()
