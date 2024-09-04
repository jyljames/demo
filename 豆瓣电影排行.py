import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '11',
        'interval_id' : '100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }

    response = requests.get(url=url,params=param,headers=headers)
    dic_obj = response.text
    print(dic_obj)
    # fp = open('./doubandata.json','w',encoding='utf-8')
    # json.dump(dic_obj,fp,ensure_ascii=False)
    # print('爬取结束！')
    # for i in range(len(dic_obj)):
    #     print(dic_obj[i]['title'])