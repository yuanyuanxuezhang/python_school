# -*- coding: utf-8 -*-
# 时          间 : 2022/1/29 18:12
# 高贵的高级工程师 : 元元学长
import requests
import re
import csv


url = 'https://movie.douban.com/chart'
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
page_content = requests.get(url,headers=headers)
# print(page_content)
#解析数据
obj = re.compile(r'  class="">(?P<name>.*?)  / <span style="font-size:13px;">.*?<p class="pl">'
                 r'(?P<year>.*?) / .*?<span class="rating_nums">(?P<nums>.*?)</span>',re.S)
result = obj.finditer(page_content.text)
f = open("data.csv",mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group())
    print(it.group("name").strip(),end="\t\t\t\t\t")
    print(it.group("year").strip(), end="\t")
    print(it.group("nums").strip(), end="\t")
    print()
    dic = it.groupdict()
    dic['name'] = dic['name'].strip()
    csvwriter.writerow(dic.values())

f.close()
print("数据已写入data.csv文件中")
