#! /usr/bin/env python3
# Author:taoke
# _*_ coding:utf-8 _*_
"""
爬取某个网站的所有连接
time:2018年4月2日 21:06:04
"""

import urllib.request
import os
import pathlib
import re

url = 'http://www.hao123.com'
def get_UrlAllLink(url):
    pat = '[a-zA-Z]+://[\w./]*'
    # 打开网站读取byte数据
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    # urllib.request.urlretrieve(url,filename=pathlib.Path(__file__).parent/"file.html")
    linksAll = re.compile(pat).findall(html1)
    links = []
    for link in linksAll:
        if link not in links:
            links.append(link)
    print(links)
    fileDirPath = pathlib.Path(__file__).parent/'link'
    if not os.path.exists(fileDirPath):
        os.mkdir(fileDirPath)
    file = open(fileDirPath/'linkfile.txt','w')
    for l in links:
        file.write(l+'\n')
    file.close()

if __name__ == "__main__":
    get_UrlAllLink(url)






