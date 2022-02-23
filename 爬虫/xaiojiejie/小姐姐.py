# -*- coding: utf-8 -*-
# 时          间 : 2022/2/23 18:14
# 高贵的高级工程师 : 元元学长
import requests
import time
import re

url = "https://api.muxiaoguo.cn/api/meinvtu?num=1"
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
num = 1
while(True):
    resp = requests.get(url,headers=headers)
    obj = re.compile(r'"imgurl":"(?P<imgurl>.*?)"}]}',re.S)
    # print(obj.finditer(resp.text))
    result = obj.finditer(resp.text)
    for it in result:
        i_url = it.group("imgurl")
        print(it.group("imgurl"))
    i_url_name = i_url
    i_url_name = i_url_name.replace(':',"a")
    i_url_name = i_url_name.replace('/','a')
    i_url_name = i_url_name.replace('?','a')
    i_url_name = i_url_name.replace('=','a')

    img_resp = requests.get(i_url,headers=headers)

    img_name = i_url_name+".jpg"     #给写入的文件加入拓展名
    num = num + 1
    # print(resp.text)
    with open(r"img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)   #图片内容写入到文件
        time.sleep(1)       #sleep里面的参数单位为秒
        print("第"+str(num)+"次下载")
