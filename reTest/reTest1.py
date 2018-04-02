#!/usr/bin/env python3
# Author:taoke
import re
str = '<link rel="icon" sizes="any" mask href="http://www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg.com">'
pat = '[a-zA-Z0-9]+://[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.com|cn'
p = re.search(pat,str)
print(p)
p = re.compile(pat).findall(str)
print(len(p) , p)
