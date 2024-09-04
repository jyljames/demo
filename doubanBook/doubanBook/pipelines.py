# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DoubanbookPipeline(ImagesPipeline):
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
        with open('bookinfo.csv','a',encoding='utf-8') as f:
            item['book_name'] = item.get('book_name')    #书名
            item['type'] = item.get('type')   #图书类型
            item['isbn'] = item.get('isbn')  # isbn号
            item['author'] = item.get('author')  # 作者
            item['publisher'] = item.get('publisher')  # 出版社
            item['publish_company'] = item.get('publish_company')  # 出版方
            item['ori_name'] = item.get('ori_name')  # 原作名
            item['translator'] = item.get('translator')  # 译者
            item['publish_time'] = item.get('publish_time')  # 出版时间
            item['page_number'] = item.get('page_number')  # 页数
            item['book_price'] = item.get('book_price')  # 图书价格
            item['decorative'] = item.get('decorative')  # 装帧
            item['series'] = item.get('series')  # 丛书
            item['book_introduction'] = item.get('book_introduction')  # 简介
            item['book_score'] = item.get('book_score')  # 评分
            item['img'] = item.get('img')  # 图片
            BookInfo = str.format('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n',item['book_name'],item['type'],item['isbn'],item['author'],item['publisher'],item['publish_company'],item['ori_name'],item['translator'],item['publish_time'],item['page_number'],item['book_price'],item['decorative'],item['series'],item['book_introduction'],item['book_score'],item['img'])
            f.write(BookInfo)
        print(item)
        return item
