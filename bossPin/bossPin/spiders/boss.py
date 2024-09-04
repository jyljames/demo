import scrapy
from selenium import webdriver
from bossPin.items import BosspinItem
from bs4 import BeautifulSoup
import os
import json
import time
class BossSpider(scrapy.Spider):
    name = 'boss'
    n = 0
    start_urls = ['https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.6.b_7375626e6176.2#/all/default/0/1/']
    page_urls = [] #用来存储分页的url

    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        for i in range(10):
            i = i+1
            urls = f'https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.6.b_7375626e6176.2#/all/default/0/{i}/'
            self.page_urls.append(urls)

            # 依次对每一个板块对应的页面进行请求
        for url in self.page_urls:
            yield scrapy.Request(url, callback=self.page_list,dont_filter=True)


    def page_list(self,response):
        self.n = self.n+1
        print(self.n)
        list_ul = response.xpath('//*[@id="videolist_box"]/div[2]/ul/li')

        for li in list_ul:
            title = li.xpath('./div/div[@class="r"]/a[@class="title"]/@title').extract_first()
            item = BosspinItem()
            item['title'] = title
            yield item
    def closed(self,spider):
        self.bro.quit()
