#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://wenshu.court.gov.cn/content/content?DocID=f05b8b81-b647-11e3-84e9-5cf3fc0c2c18')
element = driver.find_element_by_id('Content')

text = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
with open('1.txt','w',encoding='utf-8') as file:
    file.write(text)










































