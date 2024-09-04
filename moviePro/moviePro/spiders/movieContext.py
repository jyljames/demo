import scrapy
from time import sleep
from moviePro.items import MovieproItem
from redis import Redis
class MoviecontextSpider(scrapy.Spider):
    name = 'movieContext'
    start_urls = ['https://movie.douban.com/subject/1295038/']
    movieurls = [] #存储电影详情url
    list = ['/','\n',''] #用来删除扰乱爬取的xpath

    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse(self, response):
        with open('movieurls.txt', 'r', encoding='utf-8') as f:
            self.movieurls = f.read().splitlines()


        for url in self.movieurls:
            if url == '':
                continue
            item = MovieproItem()
            murl = url
            item['murl'] = murl
            state = self.conn.sismember("urls",url)
            if state == False:
                sleep(4)
                yield scrapy.Request(url, callback=self.movie_parse, dont_filter=True, meta=({'item':item}))
                print('该url没有被爬取过，可以进行数据的爬取')
                # ex = self.conn.sadd('urls',url)
                # if ex == 1:
                #     print("已加入数据库")
                # else:
                #     print("加入数据库失败")
            else:
                print('数据还没有更新，暂无新数据可爬取！')

    def movie_parse(self,response):
        title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()  #标题
        director = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first()  #导演
        screenwriterdata = response.xpath('//*[@id="info"]/span[2]/span[2]') #编剧
        screenwriter = screenwriterdata[0].xpath('string(.)').extract()[0]
        actorsdata = response.xpath('//*[@id="info"]/span[3]/span[2]')  #演员
        actors = actorsdata.xpath('string(.)').extract()[0]
        type = response.xpath('//*[@id="info"]/span[5]/text()').extract_first() #电影类型
        areadata = response.xpath('//*[@id="info"]/text()').extract() #制片地区
        arealist = []
        for i in areadata:
            newarea = ''.join(i.split())
            if newarea in self.list:
                continue
            arealist.append(newarea)
        area =arealist[0]
        language = arealist[1]
        showtime = response.xpath('//*[@id="info"]/span[contains(text(),"-")]/text()').extract_first()
        time = response.xpath('//*[@id="info"]/span[contains(text(),"分钟")]/text()').extract_first()
        score = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        introductiondata = response.xpath('//*[@id="link-report"]/span[1]')[0].xpath('string(.)').extract_first()
        introduction = introductiondata.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        img_url = response.xpath('//*[@id="mainpic"]/a/img/@src').extract_first()
        img = img_url.split('/')[-1]

        item = response.meta['item']
        item['title'] = title        #标题
        item['director'] = director           #导演
        item['img_url'] = img_url         #图片地址
        item['screenwriter'] = screenwriter            #编剧
        item['actors'] = actors            #演员
        item['type'] = type              #电影类型
        item['area'] = area             #地区
        item['language'] = language            #语言
        item['showtime'] =showtime          #上映日期
        item['time'] = time           #时长
        item['score'] = score        #评分
        item['introduction'] = introduction            #简介
        item['img'] = img
        ex = self.conn.sadd('urls', item['murl'])
        if ex == 1:
            print("已加入数据库")
        else:
            print("加入数据库失败")

        yield item





