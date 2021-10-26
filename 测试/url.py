# -*- coding: utf-8 -*-
# 时          间 : 2021/10/25 20:20
# 高贵的高级工程师 : 元元学长
import urllib.request
import urllib.parse #将键值对按照一定的方式进行解析
# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# response = urllib.request.urlopen("https://yyxuezhang.top")
# print(response)
# print(response.read())
# print(response.read().decode('utf-8'))

# 获取一个post请求 通过httpbin.org网站的响应
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

