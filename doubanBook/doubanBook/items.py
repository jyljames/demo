# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    detail_url = scrapy.Field()
    type = scrapy.Field()
    book_name = scrapy.Field()
    book_introduction = scrapy.Field()
    isbn = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    publish_company = scrapy.Field()
    ori_name = scrapy.Field()
    translator = scrapy.Field()
    publish_time = scrapy.Field()
    page_number = scrapy.Field()
    decorative = scrapy.Field()
    series = scrapy.Field()
    book_price = scrapy.Field()
    book_score = scrapy.Field()
    img_url = scrapy.Field()
    img = scrapy.Field()


