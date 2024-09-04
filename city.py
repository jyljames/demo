import requests
from lxml import etree
if __name__ == "__main__":
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = 'https://aq.lianjia.com/ershoufang/103112691488.html'

    response = requests.get(url=url,headers=headers).text
    tree = etree.HTML(response)

    price = tree.xpath("//span[contains(@class,'unitPriceValue')]/text()")
    '/html/body/div[5]/div[2]/div[3]/div/span[1]'
    total_price = tree.xpath("//span[contains(@class,'total')]/text()")
    '/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span'
    house_type = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()')  #户型
    square = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()')
    village = tree.xpath("//div[contains(@class,'communityName')]/a[contains(@class,'info')]/text()")   #小区
    area = tree.xpath("//div[contains(@class,'areaName')]/span[contains(@class,'info')]/a/text()")  #区域
    city = tree.xpath('/html/body/div[4]/div/div/a[1]/text()')
    floor = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()')
    fitment = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()')  #装修情况
    elevator = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()') #梯户比例
    listing_date = tree.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()') #挂牌时间
    face_to = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()')  #朝向
    used_for  = tree.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()') #房屋用途
    house_type_structure = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()') #户型结构
    building_type = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()')#建筑类型


    print(price)     #1.
    print(total_price)    #2.
    print(house_type)   #3.
    print(square)    #4.
    print(village)    #5.
    print(area)     #6.
    print(city)   #7.
    print(floor)    #8.
    print(fitment)    #9.
    print(elevator)    #10.
    print(listing_date)   #11.
    print(face_to)   #12.
    print(used_for)  #13.
    print(house_type_structure)   #13.
    print(building_type)   #14.

    #
    # li_list2 = [url + "zufang" for url in li_list]
    #
    # print(li_list2)
    # print(len(li_list2))
    # filename = kw+'.html'
    # with open(filename,'w',encoding='utf-8') as fp:
    #     fp.write(page_text)