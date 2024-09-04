import time
import asyncio

async  def request(url):
    print('now download:',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    #time.sleep(1)
    await asyncio.sleep(2)  #当在asyncio中遇到阻塞操作必须进行手动挂起
    print('successful download',url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.douban.com'
]
#任务列表，存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time()-start)