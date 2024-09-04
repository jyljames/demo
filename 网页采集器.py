import requests
if __name__ == "__main__":
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = 'https://www.baidu.com/s'
    kw = input("please input:")
    param = {
        'wd':kw
    }
    #对指定的url发起请求对应的url是携带参数的，并且请求过程中携带了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename+'保存成功')