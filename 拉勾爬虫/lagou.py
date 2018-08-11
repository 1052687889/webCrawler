#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke

import requests
from urllib.parse import quote
import json
def get_page(keyword,city,page):
    headers = {'Host': 'www.lagou.com',
               'Origin': 'https://www.lagou.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Referer': 'https://www.lagou.com/jobs/list_' + quote(keyword) + '?px=default&city=' + quote(city),
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9'}
    data = {'first': 'true',
            'pn': page,
            'kd': keyword}
    res = requests.post('https://www.lagou.com/jobs/positionAjax.json?px=default&city=' + quote(city) + '&needAddtionalResult=false',data=data, headers=headers)
    try:
        jres = json.loads(res.text)

        return jres['content']['positionResult']['result']
    except Exception as e:
        print(e)
        return []

def get_all(keyword,city):
    with open('jos.txt','w',encoding='utf-8') as file:
        for i in range(1,31):
            res = get_page(keyword,city,i)
            if res == -1:
                continue
            elif res == []:
                break
            else:
                for item in res:
                    print(item)
                    wStr =str([item['companyId'] , item['companyShortName'] , item['positionId'] , item['industryField'] , item['education'] , item['workYear'],item['city'],item['positionAdvantage'],item['createTime'],
                            item['salary'],item['positionName'],item['companySize'],item['companyLogo'],item['financeStage'],item['jobNature'],item['approve'],item['companyLabelList'],item['formatCreateTime']])
                    file.write(wStr+'\n')

get_all('java','北京')
























