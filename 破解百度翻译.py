import json
import requests

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    #输入需要查询的单词
    word = input('请输入您想要查询的单词:')
    #post请求参数处理（同get一致）
    data={
        'kw':word
    }
    #请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据，json()方法获取的obj的（如果确认获取的数据类型是json才可以使用.json()）
    dic_obj = response.json()
    #持久化存储
    filename = word+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('结束爬取！')
    print(dic_obj['data'][0]['v'])