import scrapy
from selenium import webdriver
from dangdangbook.items import DangdangbookItem
class DangbookSpider(scrapy.Spider):
    name = 'dangBook'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://search.dangdang.com/?key=%CD%BC%CA%E9&act=input&page_index=1']
    page_urls = [] #用来存放分页的url

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        # li_list = response.xpath('//*[@id="component_59"]/li')
        # for li in li_list:
        for i in range(1,3):
            url = f'http://search.dangdang.com/?key=%CD%BC%CA%E9&act=input&page_index={i}'
            self.page_urls.append(url)

        for url in self.page_urls:
            yield scrapy.Request(url,callback=self.page_detailed)

    def page_detailed(self,response):
        li_list = response.xpath('//*[@id="component_59"]/li')

        for li in li_list:
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = 'http:' + detail_url
            print(detail_url)

            yield scrapy.Request(detail_url, callback=self.model)
    def model(self,response):
        title = response.xpath('//*[@id="product_info"]/div[1]/h1/@title').extract_first()
        title = ''.join(title.split())
        category = response.xpath('//*[@id="breadcrumb"]/a[3]/text()').extract_first()
        category = ''.join(category.split())
        date = response.xpath('//*[@id="product_info"]/div[2]/span[3]/text()').extract_first()
        date = ''.join(date.split())
        price = response.xpath('//*[@id="dd-price"]/text()').extract()
        price = ''.join(price)
        price = ''.join(price.split())
        author = response.xpath('//*[@id="author"]/a/text()').extract_first()
        author = ''.join(author.split())
        publisher = response.xpath('//*[@id="product_info"]/div[2]/span[2]/a/text()').extract_first()
        publisher = ''.join(publisher.split())
        isbn = response.xpath('//*[@id="detail_describe"]/ul/li[5]/text()').extract_first()
        isbn = ''.join(isbn.split())
        img = response.xpath('//*[@id="largePic"]/@src').extract_first()
        img = 'https:' + img
        desc = response.xpath('//*[@id="product_info"]/div[1]/h2/span[1]/text()').extract_first()
        desc = ''.join(desc.split())

        item = DangdangbookItem()

        item['title'] = title
        item['category'] = category
        item['date'] = date
        item['price'] = price
        item['author'] = author
        item['publisher'] = publisher
        item['isbn'] = isbn
        item['desc'] = desc
        item['img'] = img

        yield item


