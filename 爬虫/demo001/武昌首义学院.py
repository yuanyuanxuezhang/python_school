# -*- coding: utf-8 -*-
# 时          间 : 2022/2/6 22:13
# 高贵的高级工程师 : 元元学长
import requests
import time
url = "http://www.wsyu.edu.cn/"
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
# resp = requests.get(url)
# resp.encoding = "utf-8"
i = 0
while(True):
    resp = requests.get(url,headers=headers)
    resp.encoding = "utf-8"
    # resp.close()
    time.sleep(1)
    # print(resp.close())
    i = i+1
    print("次数",end='\t')
    print(str(i)+ '\t' + str(resp),end='\t')
    print()

print("访客增加一百万成功")

