import scrapy
import random
import time

class CityurlSpider(scrapy.Spider):
    name = 'cityurl'
    start_urls = ['https://aq.lianjia.com/']
    ershou_cities_urls = ['https://aq.lianjia.com/ershoufang', 'https://cz.fang.lianjia.com/ershoufang',
                          'https://fy.lianjia.com/ershoufang', 'https://hf.lianjia.com/ershoufang',
                          'https://mas.lianjia.com/ershoufang', 'https://wuhu.lianjia.com/ershoufang',
                          'https://bj.lianjia.com/ershoufang', 'https://cq.lianjia.com/ershoufang',
                          'https://fz.lianjia.com/ershoufang', 'https://quanzhou.lianjia.com/ershoufang',
                          'https://xm.lianjia.com/ershoufang', 'https://zhangzhou.lianjia.com/ershoufang',
                          'https://dg.lianjia.com/ershoufang', 'https://fs.lianjia.com/ershoufang',
                          'https://gz.lianjia.com/ershoufang', 'https://hui.lianjia.com/ershoufang',
                          'https://jiangmen.lianjia.com/ershoufang', 'https://qy.lianjia.com/ershoufang',
                          'https://sz.lianjia.com/ershoufang', 'https://zh.lianjia.com/ershoufang',
                          'https://zhanjiang.lianjia.com/ershoufang', 'https://zs.lianjia.com/ershoufang',
                          'https://bh.lianjia.com/ershoufang', 'https://fcg.lianjia.com/ershoufang',
                          'https://gl.lianjia.com/ershoufang', 'https://liuzhou.lianjia.com/ershoufang',
                          'https://nn.lianjia.com/ershoufang', 'https://gy.lianjia.com/ershoufang',
                          'https://qxn.fang.lianjia.com/ershoufang', 'https://lz.lianjia.com/ershoufang',
                          'https://tianshui.lianjia.com/ershoufang', 'https://bd.lianjia.com/ershoufang',
                          'https://chengde.lianjia.com/ershoufang', 'https://hd.lianjia.com/ershoufang',
                          'https://lf.lianjia.com/ershoufang', 'https://qhd.fang.lianjia.com/ershoufang',
                          'https://sjz.lianjia.com/ershoufang', 'https://ts.lianjia.com/ershoufang',
                          'https://zjk.lianjia.com/ershoufang', 'https://bt.fang.lianjia.com/ershoufang',
                          'https://cm.lianjia.com/ershoufang', 'https://dz.fang.lianjia.com/ershoufang',
                          'https://hk.lianjia.com/ershoufang', 'https://lg.fang.lianjia.com/ershoufang',
                          'https://ld.fang.lianjia.com/ershoufang', 'https://ls.fang.lianjia.com/ershoufang',
                          'https://qh.fang.lianjia.com/ershoufang', 'https://san.lianjia.com/ershoufang',
                          'https://wzs.fang.lianjia.com/ershoufang', 'https://wc.fang.lianjia.com/ershoufang',
                          'https://wn.fang.lianjia.com/ershoufang', 'https://cs.lianjia.com/ershoufang',
                          'https://changde.lianjia.com/ershoufang', 'https://hy.lianjia.com/ershoufang',
                          'https://xx.lianjia.com/ershoufang', 'https://yy.lianjia.com/ershoufang',
                          'https://zhuzhou.lianjia.com/ershoufang', 'https://jiyuan.fang.lianjia.com/ershoufang',
                          'https://kf.lianjia.com/ershoufang', 'https://luoyang.lianjia.com/ershoufang',
                          'https://pds.lianjia.com/ershoufang', 'https://py.lianjia.com/ershoufang',
                          'https://smx.fang.lianjia.com/ershoufang', 'https://xinxiang.lianjia.com/ershoufang',
                          'https://xc.lianjia.com/ershoufang', 'https://zz.lianjia.com/ershoufang',
                          'https://zk.lianjia.com/ershoufang', 'https://zmd.lianjia.com/ershoufang',
                          'https://ez.lianjia.com/ershoufang', 'https://huangshi.lianjia.com/ershoufang',
                          'https://wh.lianjia.com/ershoufang', 'https://xy.lianjia.com/ershoufang',
                          'https://yichang.lianjia.com/ershoufang', 'https://hrb.lianjia.com/ershoufang',
                          'https://ganzhou.lianjia.com/ershoufang', 'https://jiujiang.lianjia.com/ershoufang',
                          'https://jian.lianjia.com/ershoufang', 'https://nc.lianjia.com/ershoufang',
                          'https://sr.lianjia.com/ershoufang', 'https://changzhou.lianjia.com/ershoufang',
                          'https://changshu.lianjia.com/ershoufang', 'https://danyang.lianjia.com/ershoufang',
                          'https://haimen.lianjia.com/ershoufang', 'https://ha.lianjia.com/ershoufang',
                          'https://jy.lianjia.com/ershoufang', 'https://jr.lianjia.com/ershoufang',
                          'https://ks.lianjia.com/ershoufang', 'https://nj.lianjia.com/ershoufang',
                          'https://nt.lianjia.com/ershoufang', 'https://su.lianjia.com/ershoufang',
                          'https://taicang.lianjia.com/ershoufang', 'https://wx.lianjia.com/ershoufang',
                          'https://xz.lianjia.com/ershoufang', 'https://yc.lianjia.com/ershoufang',
                          'https://zj.lianjia.com/ershoufang', 'https://cc.lianjia.com/ershoufang',
                          'https://jl.lianjia.com/ershoufang', 'https://dl.lianjia.com/ershoufang',
                          'https://dd.lianjia.com/ershoufang', 'https://fushun.lianjia.com/ershoufang',
                          'https://sy.lianjia.com/ershoufang', 'https://baotou.lianjia.com/ershoufang',
                          'https://byne.fang.lianjia.com/ershoufang', 'https://cf.lianjia.com/ershoufang',
                          'https://hhht.lianjia.com/ershoufang', 'https://tongliao.lianjia.com/ershoufang',
                          'https://yinchuan.lianjia.com/ershoufang', 'https://heze.lianjia.com/ershoufang',
                          'https://jn.lianjia.com/ershoufang', 'https://jining.lianjia.com/ershoufang',
                          'https://linyi.lianjia.com/ershoufang', 'https://qd.lianjia.com/ershoufang',
                          'https://ta.lianjia.com/ershoufang', 'https://wf.lianjia.com/ershoufang',
                          'https://weihai.lianjia.com/ershoufang', 'https://yt.lianjia.com/ershoufang',
                          'https://zb.lianjia.com/ershoufang', 'https://cd.lianjia.com/ershoufang',
                          'https://dy.lianjia.com/ershoufang', 'https://dazhou.lianjia.com/ershoufang',
                          'https://guangyuan.lianjia.com/ershoufang', 'https://leshan.fang.lianjia.com/ershoufang',
                          'https://liangshan.lianjia.com/ershoufang', 'https://mianyang.lianjia.com/ershoufang',
                          'https://ms.fang.lianjia.com/ershoufang', 'https://nanchong.lianjia.com/ershoufang',
                          'https://pzh.lianjia.com/ershoufang', 'https://sn.lianjia.com/ershoufang',
                          'https://yibin.lianjia.com/ershoufang', 'https://yaan.lianjia.com/ershoufang',
                          'https://ziyang.lianjia.com/ershoufang', 'https://baoji.lianjia.com/ershoufang',
                          'https://hanzhong.lianjia.com/ershoufang', 'https://xa.lianjia.com/ershoufang',
                          'https://xianyang.lianjia.com/ershoufang', 'https://jz.lianjia.com/ershoufang',
                          'https://ty.lianjia.com/ershoufang', 'https://yuncheng.lianjia.com/ershoufang',
                          'https://sh.lianjia.com/ershoufang', 'https://tj.lianjia.com/ershoufang',
                          'https://wlmq.lianjia.com/ershoufang', 'https://dali.lianjia.com/ershoufang',
                          'https://km.lianjia.com/ershoufang', 'https://xsbn.fang.lianjia.com/ershoufang',
                          'https://hz.lianjia.com/ershoufang', 'https://huzhou.lianjia.com/ershoufang',
                          'https://jx.lianjia.com/ershoufang', 'https://jh.lianjia.com/ershoufang',
                          'https://nb.lianjia.com/ershoufang', 'https://quzhou.lianjia.com/ershoufang',
                          'https://sx.lianjia.com/ershoufang', 'https://taizhou.lianjia.com/ershoufang',
                          'https://wz.lianjia.com/ershoufang', 'https://yw.lianjia.com/ershoufang']
    sleeptime = random.randint(2, 10)
    type_url = ['co32', 'co21', 'co41', 'co11']

    def parse(self, response):
        for city_url in self.ershou_cities_urls:
            if city_url == '':
                continue
            for i in range(1, 101):
                time.sleep(self.sleeptime)
                newcity_url = f'{city_url}/pg{i}/co11'
                yield scrapy.Request(newcity_url, callback=self.detialinfo, dont_filter=True)

    def detialinfo(self, response):
        print('开始执行')
        detail_url_list = response.xpath('//*[@id="content"]/div[1]/ul/li/a/@href').extract()

        print(detail_url_list)
        with open('house_urls.txt', mode='a', encoding='utf-8') as fp:
            fp.write('\n'.join(detail_url_list))
            fp.write('\n')

