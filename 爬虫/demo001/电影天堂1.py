# -*- coding: utf-8 -*-
# 时          间 : 2022/1/29 20:50
# 高贵的高级工程师 : 元元学长
import requests
import re
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
domain = "https://m.dytt8.net/index2.htm"
# domain = "https://www.dytt89.com/"

resp = requests.get(domain,verify=False,headers=headers)    #verify=False 去掉安全验证
resp.encoding = "gb2312"
# resp.encoding = "ISO-8859-1"
# resp.encoding = "gbk"
# resp.close()
print(resp.content)
resp.close()
