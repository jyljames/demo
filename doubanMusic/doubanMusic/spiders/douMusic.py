import scrapy
from time import sleep
from redis import Redis
from ..items import DoubanmusicItem
import re

class DoumusicSpider(scrapy.Spider):
    name = 'douMusic'
    musicurls = [] #存储音乐详情url
    start_urls = ['https://music.douban.com/tag/']
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse(self, response):
        with open('musicurls.txt', 'r', encoding='utf-8') as f:
            self.musicurls = f.read().splitlines()

        for url in self.musicurls:
            item = DoubanmusicItem()
            murl = url
            item['murl'] = murl
            state = self.conn.sismember("music_urls",murl)
            if state == False:
                sleep(4)
                yield scrapy.Request(url, callback=self.music_parse, dont_filter=True, meta=({'item':item}))
                print('该url没有被爬取过，可以进行数据的爬取')
            else:
                print('数据还没有更新，暂无新数据可爬取！')

    def music_parse(self,response):
        str = response.text
        music_name = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        music_another_name_ex = 'div id="info" class="ckd-collect".*?又名.*?>(.*?)<'   #提取又名
        singer_ex = 'div id="info" class="ckd-collect".*?表演者.*?>(.*?)<'             #提取歌手
        music_type_ex = 'div id="info" class="ckd-collect".*?流派.*?>(.*?)<'           #提取类型
        media_ex = 'div id="info" class="ckd-collect".*?介质.*?>(.*?)<'                #提取介质媒体
        showtime_ex = 'div id="info" class="ckd-collect".*?发行时间.*?>(.*?)<'          #提取发行时间
        publisher_ex = 'div id="info" class="ckd-collect".*?出版者.*?>(.*?)<'           #提取出版者


        try:
            if '又名' in re.findall('div id="info" class="ckd-collect".*?又名', str, re.S)[0]:
                music_another_name = re.findall(music_another_name_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                music_another_name = ' '
        except:
            music_another_name = ' '
        try:
            if '表演者' in re.findall('div id="info" class="ckd-collect".*?表演者', str, re.S)[0]:
                singer = re.findall(singer_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                singer = ' '
        except:
            singer = ' '
        try:
            if '流派' in re.findall('div id="info" class="ckd-collect".*?流派', str, re.S)[0]:
                music_type = re.findall(music_type_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                music_type = ' '
        except:
            music_type = ' '
        try:
            if '介质' in re.findall('div id="info" class="ckd-collect".*?介质', str, re.S)[0]:
                media = re.findall(media_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                media = ' '
        except:
            media = ' '
        try:
            if '发行时间' in re.findall('div id="info" class="ckd-collect".*?发行时间', str, re.S)[0]:
                showtime = re.findall(showtime_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                showtime = ' '
        except:
            showtime = ' '
        try:
            if '出版者' in re.findall('div id="info" class="ckd-collect".*?出版者', str, re.S)[0]:
                publisher = re.findall(publisher_ex, str, re.S)[0].replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            else:
                publisher = ' '
        except:
            publisher = ' '
        try:
            music_introduction_data = response.xpath('//*[@id="link-report"]').xpath(
                'string(.)').extract_first()
            music_introduction = music_introduction_data.replace(u'\u3000', u'').replace('\n', '').replace('\r',
                                                                                                           '').replace(
                " ", "")
        except:
            music_introduction = ' '

        img_url = response.xpath('//*[@id="mainpic"]/span/a/img/@src').extract_first()
        img = img_url.split('/')[-1]
        music_score = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        item = response.meta['item']

        item['music_name'] = music_name
        item['music_another_name'] = music_another_name
        item['singer'] = singer
        item['music_type'] = music_type
        item['media'] = media
        item['showtime'] = showtime
        item['publisher'] = publisher
        item['music_introduction'] = music_introduction
        item['img_url'] = img_url
        item['img'] = img
        item['music_score'] = music_score

        ex = self.conn.sadd('music_urls', item['murl'])
        if ex == 1:
            print("已加入数据库")
        else:
            print("加入数据库失败")

        yield item

        yield item



