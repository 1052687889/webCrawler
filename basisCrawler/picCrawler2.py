#!/usr/bin/env python3
# Author:taoke
import urllib.request
import  re
import pathlib
ppicPath = pathlib.Path(__file__).parent/"img"/"pic2"
def crawler(url,page):
    # 打开网站读取byte数据
    html1 = urllib.request.urlopen(url).read()
    # 将读取到的byte数据转换为字符串
    html1=str(html1)
    pat1 = r'''\'imgData\\\', {    "queryEnc":"iu%E5%9B%BE%E7%89%87",    .*?\}\,\{\}\]\}\);'''
    # data = re.search(pat1,html1)
    data = re.compile(pat1).findall(html1)
    print(data)
    pat2 = r'\"[a-zA-Z]*URL\":\"(.*?)\",'#.jpeg"
    data = re.compile(pat2).findall(data[0])
    x=0
    for p in data:
        if p.find('http')==-1:
            data.remove(p)
        else:
            imagename = ppicPath / (str(page) + "_" + str(x) + ".jpg")
            print(p)
            x+=1
            try:
                headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
                opener = urllib.request.build_opener()
                opener.addheaders = [headers]
                urllib.request.install_opener(opener)
                # data = urllib.request.urlopen(p).read()
                urllib.request.urlretrieve(p, filename=imagename)
                # data = str(data)
                # req.add_header(*headers)
                # 将文件保存至本地
                # urllib.request.urlopen(req).read()

                # urllib.request.urlretrieve(p, filename=imagename)
            except urllib.error.URLError as e:
                # 如果含有reason属性表明是URLError，如果含有code属性表明是HTTPError
                # 判断是否包含‘code’属性
                if hasattr(e, "HTTPError"):
                    print("HTTPError"+p)
                    print(e)
                # 判断是否包含‘URLError’属性
                if hasattr(e, "reason"):
                    print("reason" + p)
                    print(e)


for i in range(0,1):
    URL= "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=iu%E5%9B%BE%E7%89%87&pn={pn}&gsm=0&ct=&ic=0&lm=-1&width=0&height=0".format(pn = i*20)
    crawler(URL,i)














