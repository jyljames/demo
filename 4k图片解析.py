import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = 'https://dl.lianjia.com/ershoufang/102105978788.html'
    page_text = requests.get(url=url,headers=headers).text
    #实例化tree对象
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[4]/div/div/a[1]/text()')
    print(li_list)
    # for li in li_list:
    #     img_scr = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    #     img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    #     print(img_scr,img_name)

