# -*- coding: utf-8 -*-
# 时          间 : 2022/1/30 13:30
# 高贵的高级工程师 : 元元学长
import requests
import chardet
# import bs4
from bs4 import BeautifulSoup
url = "http://www.xinfadi.com.cn/index.html"
resp = requests.get(url,verify=False)
# resp.encoding = 'utf-8'
# resp.encoding = 'GBK'
# print(resp.content)
print()
print(chardet.detect(resp.content))
print(resp.encoding)
# print(resp.text)
print(resp)
page = BeautifulSoup(resp.text,"html.parser")
print(page ,end="\n\n\n\n")
table = page.find("table",class_ = "hq_table")  #class是python关键字，需要用到相同的时候使用class_代替
table1 = page.find("table",border = "0")
print(table1)
trs = table1.find_all("tr")
for tr in trs:
    th = tr.find_all("th")
    # print(len(th))
    print(th[0])
    print(th[0].text)
    print(th[1])
    print(th[1].text)
    print(th[2].text)
    print(th[3].text)
    print(th[4].text)
    print(th[5].text)
    print(th[6].text)
    print(th[7].text)
    # print(th[8].text)  #总长度为8则下标最大为7，len()取的是总长度