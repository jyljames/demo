import requests
import asyncio
import aiohttp
import time

start = time.time()
urls = [
    'https://pic.netbian.com/4kdongman/index_6.html',
    'https://pic.netbian.com/4kdongman/index_6.html',
    'https://pic.netbian.com/4kdongman/index_6.html'
]

async  def get_page(url):
    async with aiohttp.ClientSession() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
        }
        #get()、post();
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url,headers=headers) as response:
            #text()返回的是字符串形式的响应数据
            #read()返回的是二进制形式的响应数据
            #json()返回的数据json对象
            #注意:获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时:',end-start)