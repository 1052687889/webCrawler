#!/usr/bin/env python3
# Author:taoke
import urllib.request
import pathlib

keyword = '饕客 博客园'
url = "http://www.baidu.com/s?wd="+urllib.request.quote(keyword)
data = urllib.request.urlopen(url).read()
filrHandle = open(pathlib.Path(__file__).parent/"4.html",'wb')
filrHandle.write(data)
filrHandle.close()




