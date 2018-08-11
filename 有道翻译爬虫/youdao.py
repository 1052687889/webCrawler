#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
import random
import requests
import time
import hashlib
import json

def translate(endlish):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {'Host': 'fanyi.youdao.com',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Referer': 'http://fanyi.youdao.com/',
               'Accept-Encoding': 'deflate', }
    formdata = {
    'i':endlish,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15316181854457',
    'sign':'0 acd4f34bbb7de68ee2aec865a6b6297',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web' ,
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false',
    }
    Cookie = { 'OUTFOX_SEARCH_USER_ID':'1483315967@10.169.0.83',
               'OUTFOX_SEARCH_USER_ID_NCOO':'140762844.79632822',
               'fanyi-ad-id':'46607', 'fanyi-ad-closed':'1',
               'JSESSIONID':'aaaJfIzL4g-Ze9BHdOysw',
               '___rl__test__cookies':'%s'%str(int(time.time()*1000))}
    h = hashlib.md5()
    formdata['salt'] = str(int(time.time()*1000))+str((random.randint(0,10)))
    s = ("fanyideskweb" + formdata['i'] + formdata['salt'] + "ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8')
    h.update(s)
    formdata['sign'] = h.hexdigest()
    res = requests.post(url=url,headers=headers,data=formdata,cookies=Cookie).text
    jtg = json.loads(res)
    return jtg['translateResult'][0][0]['tgt']

if __name__ == "__main__":
    '''英翻中'''
    t = translate("what's your name?")
    print(t)




