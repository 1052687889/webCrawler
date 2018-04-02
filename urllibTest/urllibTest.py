#!/usr/bin/env python3
# Author:taoke
import pathlib
import urllib.request
url2 = "http://www.hao123.com"
file = urllib.request.urlopen(url2)
data = file.read()
dataline = file.readline()
dirPath = pathlib.Path(__file__).parent
fileHandle = open(dirPath/"testFile.html",'wb')
fileHandle.write(data)
fileHandle.close()
urllib.request.urlcleanup()
# print(file.info())
# print(file.getcode())
# print(data)

print(urllib.request.quote("http://www.sina.com.cn"))
print(urllib.request.unquote("http%3A//www.sina.com.cn"))








