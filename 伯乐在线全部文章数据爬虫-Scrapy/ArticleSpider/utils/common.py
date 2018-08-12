#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
import hashlib
def get_md5(url):
    if isinstance(url,bytes):
        m = hashlib.md5()
        m.update(url)
        return m.hexdigest()
    else:
        raise ValueError(__file__)





if __name__ == '__main__':
    print(get_md5('http://jobbole.com'.encode()))

















