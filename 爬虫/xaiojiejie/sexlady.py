# -*- coding: utf-8 -*-
# 时          间 : 2022/2/25 19:34
# 高贵的高级工程师 : 元元学长
import requests
import time


url = "https://api.lyiqk.cn/sexylady"
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
num = 135

while(True):
    resp = requests.get(url, headers=headers)
    img_name = str(num)+".jpg"     #给写入的文件加入拓展名
    num = num + 1
    # print(resp.text)
    with open(r"sexlady/"+img_name,mode="wb") as f:
        f.write(resp.content)   #图片内容写入到文件
        time.sleep(1)       #sleep里面的参数单位为秒
        print("第"+str(num)+"次下载")
