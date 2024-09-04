import scrapy
import random
import time

from redis import Redis

from ..items import HomeproItem
class HomepriceSpider(scrapy.Spider):
    name = 'homeprice'
    start_urls = ['https://aq.lianjia.com/']
    houseurls = []  # 存储房子详情url
    sleeptime = random.randint(0, 5)
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse(self, response):
        with open('house_urls.txt', 'r', encoding='utf-8') as f:
            self.houseurls = f.read().splitlines()
        item = HomeproItem()
        for url in self.houseurls:
            item['hurl'] = url
            if url == '':
                continue

            state = self.conn.sismember("houseurls", url)
            if state == False:
                time.sleep(self.sleeptime)
                yield scrapy.Request(url, callback=self.house_parse, dont_filter=True,meta=({'item':item}))
                print('该url没有被爬取过，可以进行数据的爬取')

            else:
                print('数据还没有更新，暂无新数据可爬取！')

    def house_parse(self, response):

        price = response.xpath("//span[contains(@class,'unitPriceValue')]/text()").extract_first()
        total_price = response.xpath("//span[contains(@class,'total')]/text()").extract_first()
        '/html/body/div[5]/div[2]/div[2]/div/span[1]'
        house_type = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').extract_first()  # 户型
        square = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').extract_first()
        village = response.xpath("//div[contains(@class,'communityName')]/a[contains(@class,'info')]/text()").extract_first()  # 小区
        area = response.xpath("//div[contains(@class,'areaName')]/span[contains(@class,'info')]/a/text()").extract_first()  # 区域
        city = response.xpath('/html/body/div[4]/div/div/a[1]/text()').extract_first()
        floor = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').extract_first()
        fitment = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract_first()  # 装修情况
        elevator = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').extract_first()  # 梯户比例
        listing_date = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract_first()  # 挂牌时间
        face_to = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract_first()  # 朝向
        used_for = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').extract_first()  # 房屋用途
        house_type_structure = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').extract_first()  # 户型结构
        building_type = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract_first()  # 建筑类型

        item = response.meta['item']
        item['price'] = price  # 标
        item['total_price'] = total_price # 导演
        item['house_type'] = house_type
        item['square'] = square
        item['village'] = village
        item['area'] = area
        item['city'] = city
        item['floor'] = floor
        item['fitment'] = fitment
        item['elevator'] = elevator
        item['listing_date'] = listing_date
        item['face_to'] = face_to
        item['used_for'] = used_for
        item['house_type_structure'] = house_type_structure
        item['building_type'] = building_type
        ex = self.conn.sadd('houseurls', item['hurl'])
        if ex == 1:
            print("已加入数据库")
        else:
            print("加入数据库失败")

        yield item



