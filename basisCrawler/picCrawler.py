#!/usr/bin/env python3
# Author:taoke
import re
import urllib.request
import pathlib
#导入 re urllib.request pathlib 模块
def craw(url,page):
    # 打开网站读取byte数据
    html1 = urllib.request.urlopen(url).read()
    # 将读取到的byte数据转换为字符串
    html1=str(html1)
    # 正则表达式，过滤信息
    pat1 = '<div id="plist".+?<div class="page clearfix">'
    # 将所有符合pat1的数据提取出来
    result1 = re.compile(pat1).findall(html1)
    # 只有一个符合的
    result1=result1[0]
    # 正则表达式，过滤信息
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    # 将所有符合pat2的数据提取出来
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        # 生成文件保存路径
        path = pathlib.Path(__file__).parent/"img"/"pic1"
        # 生成文件名字
        imagename = path/(str(page)+"_"+str(x)+".jpg")
        #生成文件
        imageurl = "http://"+imageurl
        # 打印文件名
        print(imagename)
        try:
            # 将文件保存至本地
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            # 如果含有reason属性表明是URLError，如果含有code属性表明是HTTPError
            # 判断是否包含‘code’属性
            if hasattr(e,"HTTPError"):
                x+=1
            # 判断是否包含‘URLError’属性
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,5):
    url='https://list.jd.com/list.html?cat=9987,653,655&page={page}&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=6#J_main'.format(page = i)
    # html1 = urllib.request.urlopen(url).read()
    # print(type(html1))
    craw(url,i)