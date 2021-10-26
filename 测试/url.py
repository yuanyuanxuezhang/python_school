# -*- coding: utf-8 -*-
# 时          间 : 2021/10/25 20:20
# 高贵的高级工程师 : 元元学长
import urllib.request
# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


response = urllib.request.urlopen("https://yyxuezhang.top")
# print(response)
# print(response.read())
print(response.read().decode('utf-8'))

# 获取一个post请求 通过httpbin.org网站的响应

