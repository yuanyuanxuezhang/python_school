# -*- coding: utf-8 -*-
# 时          间 : 2022/1/20 16:05
# 高贵的高级工程师 : 元元学长
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open("mybaidu.html",mode="w",encoding='utf-8') as f:
    f.write(resp.read().decode("utf-8"))
    f.close()
resp.close()
print("over!")