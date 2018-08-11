#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
import requests
import re
def get_maoyan_data(page_num):
    headers = {
        'Host': 'maoyan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    respond = requests.get(url = "http://maoyan.com/board/4?offset=%d"%page_num,headers=headers)
    respond.encoding = respond.apparent_encoding
    patt = '<dd>[\s\S]*?">([\s\S]*?)</i>[\s\S]*?title="([\s\S]*?)"[\s\S]*?class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>[\s\S]*?class="integer">([\s\S]*?)</i><i class="fraction">([\s\S]*?)</i>'
    data = re.findall(patt,respond.text)
    for item in data:
        temp = [i.strip() for i in item]
        temp[-2]+=temp[-1]
        temp.pop(-1)
        yield temp

def main():
    with open('maoyan.txt','w',encoding='utf-8') as file:
        for i in range(10):
            for item in get_maoyan_data(i*10):
                file.write(str(item)+'\n')
if __name__ == "__main__":
    main()
