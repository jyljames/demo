import scrapy
from selenium import webdriver
from testUrl.items import TesturlItem
class TestSpider(scrapy.Spider):
    name = 'test'

    start_urls = ['https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.6.b_7375626e6176.2#/all/default/0/8/']

    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        list_ul = response.xpath('//*[@id="videolist_box"]/div[2]/ul/li')

        for li in list_ul:
            title = li.xpath('./div/div[@class="r"]/a[@class="title"]/@title').extract_first()
            item = TesturlItem()
            item['title'] = title

            yield item

    def closed(self,spider):
        self.bro.quit()
