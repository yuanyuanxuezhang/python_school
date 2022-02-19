# -*- coding: utf-8 -*-
# 时          间 : 2022/2/5 21:58
# 高贵的高级工程师 : 元元学长
import urllib.request
import requests
from bs4 import BeautifulSoup
url = "https://www.umeitu.com/"
# resp = urllib.request.urlopen(url)
# print(resp.read().decode("utf-8"))
# print(resp.read().getheaders())
resp = requests.get(url)
resp.encoding = "utf-8"
# resp.encoding = 'gbk'
# print(resp.text)
# 把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
# print(main_page)
alist = main_page.find("div",class_="PicListTxt").find_all("img")
print(alist)
for a in alist:
    print(a.get("alt"))      #get获取的是标签内部的属性
    print(a.get("src"))     #直接通过get就可以拿到属性的值
    print()