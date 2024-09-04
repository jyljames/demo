# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
class BiantuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 处理对象，对item中的图片地址发起请求
        yield Request(item['img_src'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        '''
        处理对象:每张图片
        返回的path是item中每一张图片的路径
        '''
        img_name = request.meta['item']['img_name']
        img_category = request.meta['item']['img_category']

        path = 'images' + '/' + img_category + '/' + img_name + '.jpg'
        return path

    def item_completed(self, results, item, info):
        '''
        处理对象:每组item中的图片
        '''
        image_path = [x['path'] for ok, x in results if ok]

        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item






