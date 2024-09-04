import scrapy
#from selenium import webdriver
from BiAnTu.items import BiantuItem
import os
class BiantuSpider(scrapy.Spider):
    name = 'biantu'
    start_urls = ['https://pic.netbian.com/tupian/1.html']
    photo_urls = [] #用来存储不吐图片对应的url



    # def __init__(self):  #初始化一个浏览器对象
    #     self.bro = webdriver.Chrome()

    def parse(self, response): #获取每一张图片对应的url存储在photo_urls中
        for i in range(20000,27798):
            url = f'https://pic.netbian.com/tupian/{i}.html'
            self.photo_urls.append(url)

        for url in self.photo_urls:
            yield scrapy.Request(url,callback=self.photo_parse,dont_filter=True)

    def photo_parse(self,response):
        photo_url = response.xpath('//*[@id="img"]/img/@src').extract_first() # 取得图片对应的url
        img_src = 'https://pic.netbian.com' + str(photo_url)
        img_name = response.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()').extract_first() # 取得图片对应的名称
        img_category = response.xpath('//*[@id="main"]/div[1]/span/a[2]/text()').extract_first() # 取得图片对应的类别


        item = BiantuItem()
        item['img_src'] = img_src
        item['img_name'] = img_name
        item['img_category'] = img_category
        yield item







