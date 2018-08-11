#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
import time
from selenium import webdriver

class taobao(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def crawer(self,keyword):
        self.browser.get('https://www.taobao.com/')
        search = self.browser.find_element_by_xpath('//*[@id="q"]')
        search.clear()
        search.send_keys(keyword)
        self.browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
        next_buttom_class = ''
        with open('taobao.inf','w',encoding='utf-8') as file:
            while 'item next next-disabled' != next_buttom_class:
                try:
                    next_buttom_class = self.browser.find_element_by_class_name('next').get_attribute('class')
                    lres = self.browser.find_elements_by_class_name('J_MouserOnverReq')
                    for item in lres:
                        ws  = ' - '.join(item.text.split('\n'))
                        print(ws)
                        file.write(ws+'\n')
                    self.browser.find_element_by_class_name('next').click()
                    time.sleep(0.3)
                except Exception as e:
                    print(e)

if __name__ == "__main__":
    t = taobao()
    t.crawer('男鞋')















