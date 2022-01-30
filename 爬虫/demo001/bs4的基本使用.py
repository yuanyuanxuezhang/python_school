# -*- coding: utf-8 -*-
# 时          间 : 2022/1/30 13:30
# 高贵的高级工程师 : 元元学长
import requests
import bs4

url = "http://www.xinfadi.com.cn/index.html"
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.content)