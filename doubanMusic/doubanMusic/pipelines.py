# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class DoubanmusicPipeline(ImagesPipeline):
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
        with open('musicinfo.csv', 'a') as f:
            item['music_name'] = item.get('music_name')  # 歌名
            item['music_another_name'] = item.get('music_another_name')  # 又名
            item['singer'] = item.get('singer')  # 歌手
            item['music_type'] = item.get('music_type')  # 类型
            item['media'] = item.get('media')  # 媒介
            item['showtime'] = item.get('showtime')  # 出版时间
            item['publisher'] = item.get('publisher')  # 出版社
            item['music_introduction'] = item.get('music_introduction')  # 简介
            item['img'] = item.get('img')  # 图片
            item['music_score'] = item.get('music_score')  #得分
            MovieInfo = str.format('{},{},{},{},{},{},{},{},{},{},{}\n', item['music_name'], item['music_another_name'],
                                   item['singer'], item['music_type'], item['media'], item['showtime'], item['publisher'],
                                   item['music_introduction'], item['showtime'], item['music_score'], item['img'])
            f.write(MovieInfo)

        print(item)
        return item
