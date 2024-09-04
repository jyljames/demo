# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hurl = scrapy.Field()
    city = scrapy.Field()   #1.城市
    total_price = scrapy.Field()    #2.房子总价
    house_type = scrapy.Field()   #3.房户类型
    square = scrapy.Field()   #4.面积
    area = scrapy.Field()   #5.区域
    village = scrapy.Field()  #6.小区
    floor = scrapy.Field()  #7.楼层
    fitment = scrapy.Field()  #8.装修情况
    elevator = scrapy.Field()   #9.梯户比例
    face_to = scrapy.Field()   #10.朝向
    used_for = scrapy.Field() #11.房屋用途
    house_type_structure = scrapy.Field() #12.户型结构
    building_type = scrapy.Field() #13.建筑类型
    price = scrapy.Field()   #14.多少钱每平
    listing_date = scrapy.Field()   #15.挂牌时间