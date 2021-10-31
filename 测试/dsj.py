# -*- coding: utf-8 -*-
# 时          间 : 2021/10/27 19:35
# 高贵的高级工程师 : 元元学长
import urllib.request
import urllib.parse #将键值对按照一定的方式进行解析
# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen("http://47.105.73.182:3000/lyy")
print(response)
print()
print(response.read().decode('utf-8'))