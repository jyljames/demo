# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import scrapy
class HomeproPipeline(object):

    def process_item(self, item, spider):
        with open('houseinfo.csv','a',encoding='utf-8') as f:
            item['city'] = item.get('city') #1.
            item['total_price'] = item.get('total_price') #2.
            item['house_type'] = item.get('house_type')#3.
            item['square'] = item.get('square')#4.
            item['area'] = item.get('area')#5.
            item['village'] = item.get('village')#6.
            item['floor'] = item.get('floor')#7.
            item['fitment'] = item.get('fitment')#8.
            item['elevator'] = item.get('elevator')#9.
            item['face_to'] = item.get('face_to')#10.
            item['used_for'] = item.get('used_for')#11.
            item['house_type_structure'] = item.get('house_type_structure')  #12.
            item['building_type'] = item.get('building_type')  # 13.
            item['price'] = item.get('price')  # 14.
            item['listing_date'] = item.get('listing_date')  # 15.
            HouseInfo = str.format('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n',item['city'],item['total_price'],item['house_type'],item['square'],item['area'],item['village'],item['floor'],item['fitment'],item['elevator'],item['face_to']
                                   ,item['used_for'],item['house_type_structure'],item['building_type'],item['price'],item['listing_date'])
            f.write(HouseInfo)

        print(item)
        return item

