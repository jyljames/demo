import requests
import json
import time
import random
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }


    proxies = {
        'https': 'https://106.55.15.244:8889'
    }

    url = 'https://movie.douban.com/j/new_search_subjects'
    for i in range(8639,500000,20):
        time.sleep(5)
        movieurl = []
        param = {
            "sort": "U",
            "range": "0,10",
            "tags": "电影",
            "start": i
        }
        #proxie = random.choice(proxies)
        #print(proxie)
        response = requests.get(url=url, params=param, headers=headers)

        dic_obj = response.json()
        print(dic_obj)
        for j in range(len(dic_obj['data'])):
            movieurl.append(dic_obj['data'][j]['url'])
            time.sleep(3)
        print(movieurl)
        with open('movieurls.txt', mode='a', encoding='utf-8') as fp:

            fp.write('\n'.join(movieurl))
            fp.write('\n')
    print("爬取完成！")


    # param = {
    #     "sort": "U",
    #     "range": "0,10",
    #     "tags": "电影",
    #     "start": "0"
    # }

    # response = requests.get(url=url,params=param,headers=headers)
    # dic_obj = response.json()
    # print(dic_obj['data'][0]['url'])

    # fp = open('./doubandata.json','w',encoding='utf-8')
    # json.dump(dic_obj,fp,ensure_ascii=False)
    # print('爬取结束！')
