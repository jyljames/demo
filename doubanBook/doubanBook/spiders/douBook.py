import scrapy
from doubanBook.items import DoubanbookItem
from time import sleep
from redis import Redis
import re
class DoubookSpider(scrapy.Spider):
    name = 'douBook'
    first_type = []
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6']
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse(self, response):
        self.first_type = response.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/a/text()').extract()
        for type in self.first_type:
            for list in range(0,200,20):
                item = DoubanbookItem()
                print(type)
                sleep(4)
                page_url = f'https://book.douban.com/tag/{type}?start={list}&type=T'
                print(page_url)
                item['type'] = type
                yield scrapy.Request(page_url, callback=self.book_parse,meta=({'item': item}))

    def book_parse(self,response):
        detail_url_list = response.xpath('//*[@id="subject_list"]/ul/li/div[2]/h2/a/@href').extract()
        for detail_url in detail_url_list:
            item = response.meta['item']
            item['detail_url'] = detail_url
            state = self.conn.sismember("urls", detail_url)
            if state == False:
                yield scrapy.Request(detail_url, callback=self.info_parse, meta=({'item': item}))
                sleep(2)
                print('该url没有被爬取过，可以进行数据的爬取')
            else:
                print('数据还没有更新，暂无新数据可爬取！')


    def info_parse(self,response):
        str = response.text
        book_score = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        author_ex = '<div id="info".*?作者.*?span>.*?<a.*?>(.*?)</a>'   #提取作者
        publisher_ex = 'div id="info".*?出版社.*?>(.*?)<br'    #提取出版社
        publish_company_ex = 'div id="info".*?出品方.*?>.*?>(.*?)<'   #出品方
        ori_name_ex = 'div id="info".*?原作名.*?>(.*?)<br'    #原始名
        translator_ex = 'div id="info".*?译者.*?>.*?>(.*?)<'    #译者
        publish_time_ex = 'div id="info".*?出版年.*?>(.*?)<br'  #出版年
        page_number_ex = 'div id="info".*?页数.*?>(.*?)<br'   #页数
        book_price_ex = 'div id="info".*?定价.*?>(.*?)<br'   #定价
        decorative_ex = 'div id="info".*?装帧.*?>(.*?)<br'  #装帧
        series_ex = 'div id="info".*?丛书.*?>.*?>(.*?)<'   #丛书
        isbn_ex = 'div id="info".*?ISBN.*?>(.*?)<br'   #isbn号

        book_name = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()  #书名
        author = re.findall(author_ex,str,re.S)[0]
        try:
            if '出版社' in re.findall('div id="info".*?出版社', str, re.S)[0]:
                publisher = re.findall(publisher_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                publisher = ' '
        except:
            publisher = ' '
        try:
            if '出品方' in re.findall('div id="info".*?出版社', str, re.S)[0]:
                publish_company = re.findall(publish_company_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                publish_company = ' '
        except:
            publish_company = ' '
        try:
            if '原作名' in re.findall('div id="info".*?原作名', str, re.S)[0]:
                ori_name = re.findall(ori_name_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                ori_name = ' '
        except:
            ori_name = ' '
        try:
            if '译者' in re.findall('div id="info".*?译者', str, re.S)[0]:
                translator = re.findall(translator_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                translator = ' '
        except:
            translator = ' '
        try:
            if '出版年' in re.findall('div id="info".*?出版年', str, re.S)[0]:
                publish_time = re.findall(publish_time_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                publish_time = ' '
        except:
            publish_time = ' '
        try:
            if '页数' in re.findall('div id="info".*?页数', str, re.S)[0]:
                page_number = re.findall(page_number_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                page_number = ' '
        except:
            page_number = ' '
        try:
            if '定价' in re.findall('div id="info".*?定价', str, re.S)[0]:
                book_price = re.findall(book_price_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                book_price = ' '
        except:
            book_price = ' '
        try:
            if '装帧' in re.findall('div id="info".*?装帧', str, re.S)[0]:
                decorative = re.findall(decorative_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                decorative = ' '
        except:
            decorative = ' '
        try:
            if '丛书' in re.findall('div id="info".*?丛书', str, re.S)[0]:
                series = re.findall(series_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                series = ' '
        except:
            series = ' '
        try:
            if 'ISBN' in re.findall('div id="info".*?ISBN', str, re.S)[0]:
                isbn = re.findall(isbn_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                isbn = ' '
        except:
            isbn = ' '

        book_introduction_data =response.xpath('//*[@id="link-report"]//div[@class="intro"]').xpath('string(.)').extract_first()
        book_introduction = book_introduction_data.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        img_url = response.xpath('//*[@id="mainpic"]/a/img/@src').extract_first()
        img = img_url.split('/')[-1]
        item = response.meta['item']
        item['book_name'] = book_name
        item['book_score'] = book_score
        item['isbn'] = isbn
        item['author'] = author
        item['publisher'] = publisher
        item['publish_company'] = publish_company
        item['ori_name'] = ori_name
        item['translator'] = translator
        item['publish_time'] = publish_time
        item['page_number'] = page_number
        item['decorative'] = decorative
        item['series'] = series
        item['book_price'] = book_price
        item['book_introduction'] = book_introduction
        item['img_url'] = img_url
        item['img'] = img
        flag = self.conn.sadd('book_urls', item['detail_url'])
        if flag == 1:
            print("已加入数据库")
        else:
            print("加入数据库失败")

        yield item









