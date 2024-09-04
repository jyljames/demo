# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class FirstbloodDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
    #该方法对无法板块对应的响应对象进行了篡改
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        bro = spider.bro#获取了在爬虫类中定义的浏览器对象

        #挑出指定的url进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:
            bro.get(request.url) #五个板块对应的url进行请求
            sleep(3)
            page_text = bro.page_source #包含了动态加载的新闻数据

            # response #五大板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            # 如何获取动态加载出的新闻数据？
            # 基于selenium便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            return response
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest


    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exczeption
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    class GetFailedUrl(object):
        def process_response(self, response, request, spider):
            if response.status != 200:
                print(111111111111)
                print(response.status)
                print(222222222222)
            else:
                return response

