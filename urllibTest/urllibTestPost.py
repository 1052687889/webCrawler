#!/usr/bin/env python3
# Author:taoke
import urllib.request
import urllib.parse
import pathlib
url = 'http://www.iqianyue.com/mypost'
postdata = urllib.parse.urlencode({
    "name":"1234567890@qq.ccc",
    "pass":"123456"
}).encode('utf-8')
Header = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
req = urllib.request.Request(url,postdata)
req.add_header(*Header)
data = urllib.request.urlopen(url).read()
fHandle = open(pathlib.Path(__file__).parent/"5.html",'wb')
fHandle.write(data)
fHandle.close()










