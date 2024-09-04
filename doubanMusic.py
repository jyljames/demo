import scrapy


class DoubanmusicSpider(scrapy.Spider):
    name = 'doubanMusic'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass


def items():
    return None