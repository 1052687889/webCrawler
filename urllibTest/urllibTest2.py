#!/usr/bin/env python3
# Author:taoke
'''
模拟浏览器访问网站，避免出现403错误


'''
import urllib.request
import pathlib
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
file = urllib.request.urlopen(url)
headers =("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
path = pathlib.Path(__file__)
fileHandle = open(path.parent/"3.html","wb")
fileHandle.write(data)
fileHandle.close()




