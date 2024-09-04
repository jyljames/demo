import random
from selenium import webdriver
import scrapy
import time

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    sleeptime = random.randint(0, 10)
    start_urls = ['https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1']

    def parse(self, response):
        url = 'https://movie.douban.com/j/new_search_subjects'
        for i in range(200000, 2000000, 20):
            time.sleep(self.sleeptime)
            self.movieurl = []
            param = {
                "sort": "U",
                "range": "0,10",
                "tags": "电影",
                "start": str(i)
            }
            yield scrapy.FormRequest(url,formdata=param,callback=self.write_parse)

    def write_parse(self,response):
        dic_obj = response.json()

        for j in range(len(dic_obj['data'])):
            self.movieurl.append(dic_obj['data'][j]['url'])
        print(self.movieurl)
        with open('movieurls.txt', mode='a', encoding='utf-8') as fp:
            fp.write('\n'.join(self.movieurl))
            fp.write('\n')
