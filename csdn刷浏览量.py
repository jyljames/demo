import time

import requests
if __name__ == "__main__":
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    urls = ['https://blog.csdn.net/haokelaicds/article/details/126579966?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/126513101?spm=1001.2014.3001.5502',
           'https://blog.csdn.net/haokelaicds/article/details/125956528?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/125819712?spm=1001.2014.3001.5502',
           'https://blog.csdn.net/haokelaicds/article/details/125684120?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/125280405?spm=1001.2014.3001.5502',
           'https://blog.csdn.net/haokelaicds/article/details/125280405?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/125102735?spm=1001.2014.3001.5502',
           'https://blog.csdn.net/haokelaicds/article/details/124753576?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/124158569?spm=1001.2014.3001.5502',
            'https://blog.csdn.net/haokelaicds/article/details/125162849?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/125067784?spm=1001.2014.3001.5502',
            'https://blog.csdn.net/haokelaicds/article/details/125000356?spm=1001.2014.3001.5502','https://blog.csdn.net/haokelaicds/article/details/124802968?spm=1001.2014.3001.5502',
            'https://blog.csdn.net/haokelaicds/article/details/124761350?spm=1001.2014.3001.5502']

    # #对指定的url发起请求对应的url是携带参数的，并且请求过程中携带了参数
    flag = True
    while flag:
        for url in urls:
            time.sleep(2)
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                print("ok!"+url)
            else:
                print("connected error!")
