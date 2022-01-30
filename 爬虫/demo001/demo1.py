# -*- coding: utf-8 -*-
# 时          间 : 2022/1/20 16:25
# 高贵的高级工程师 : 元元学长
import requests

url = 'http://47.105.73.182:3000/explore/repos'

dic = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

resp = requests.get(url,dic)
print(resp)  #查看响应状态200,404,500
print(resp.text)    #拿到页面源代码
resp.close()    #关闭resp
