import scrapy
from firstblood.items import FirstbloodItem
from selenium import webdriver


class FirstSpider(scrapy.Spider):
    name = 'first'

    start_urls = ['https://news.163.com/']
    models_urls = []  #储存几个对应的详情页url

    #实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7]
        for i in alist:
            model_url = li_list[i].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

            #依次对每一个板块对应的页面进行请求
        for url in self.models_urls:
            yield scrapy.Request(url,callback=self.parse_model)

    def parse_model(self,response): #解析每一个板块页面中对应新闻的标题和新闻详情页url
        print(response.text)
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = FirstbloodItem()
            item['title'] = title
            #对新闻详情页面发起请求
            # yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
            yield item

    # def parse_detail(self,response): #解析新闻内容
    #     content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
    #     content = ''.join(content)
    #     item = response.meta['item']
    #     item['content'] = content
    #
    #     yield item

    def closed(self,spider):
        self.bro.quit()








