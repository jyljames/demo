# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import scrapy
class MovieproPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 处理对象，对item中的图片地址发起请求
        yield scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None):
        '''
        处理对象:每张图片
        返回的path是item中每一张图片的路径
        '''
        path = request.url.split('/')[-1]

        return path

    def item_completed(self, results, item, info):
        with open('movieinfo.csv','a') as f:
            item['title'] = item.get('title')  # 标题
            item['director'] = item.get('director')  # 导演
            item['screenwriter'] = item.get('screenwriter')  # 编剧
            item['actors'] = item.get('actors')  # 演员
            item['type'] = item.get('type')  # 电影类型
            item['area'] = item.get('area')  # 地区
            item['language'] = item.get('language')  # 语言
            item['showtime'] = item.get('showtime')  # 上映日期
            item['time'] = item.get('time')  # 时长
            item['score'] = item.get('score')  # 评分
            item['introduction'] = item.get('introduction')  # 简介
            item['img'] = item.get('img')  # 图片
            MovieInfo = str.format('{},{},{},{},{},{},{},{},{},{},{},{}\n',item['title'],item['type'],item['director'],item['img'],item['screenwriter'],item['actors'],item['area'],item['language'],item['showtime'],item['time'],item['score'],item['introduction'])
            f.write(MovieInfo)

        print(item)
        return item
