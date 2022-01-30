# -*- coding: utf-8 -*-
# 时          间 : 2022/1/29 16:40
# 高贵的高级工程师 : 元元学长
import requests
import re

url = 'https://movie.douban.com/chart'
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
page_content = requests.get(url,headers=headers)
# print(page_content)
#解析数据
obj = re.compile(r'  class="">(?P<name>.*?)/ <span style="font-size:13px;">',re.S)
result = obj.finditer(page_content.text)
for it in result:
    print(it.group("name").strip(),end="\t")