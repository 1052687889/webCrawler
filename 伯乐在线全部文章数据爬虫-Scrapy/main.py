#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Author:taoke
import sys,pathlib
from scrapy.cmdline import execute
sys.path.append(pathlib.Path(__file__).parent)

execute(['scrapy','crawl','jobbole'])
















