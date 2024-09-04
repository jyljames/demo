from lxml import etree
if __name__ == "__main__":
    #实例化一个etree对象，且将被解析的源码加载到该对象中
    tree = etree.parse('胡歌.html')#parse用于本地的的解析
    #获取到body下的div标签
    r = tree.xpath('/html/body/div')
    #作用同上
    r = tree.xpath('/html//div')
    #获取所有的div标签
    r = tree.xpath('//div')
    #获取class值为#的div
    r = tree.xpath('//div[@class="#]')
    #获取class值为#的div标签下的第三p标签
    r = tree.xpath('//div[@class="#"]/p[3]')
    #获取class值为?的div标签下的第五个li标签下的a标签的文本内容
    r = tree.xpath('//div[@class="?"]//li[5]/a/text()')[0]
    #获取class值为song的div标签下的img标签的src值
    r = tree.xpath('//div[@class="song"]/img/@src')