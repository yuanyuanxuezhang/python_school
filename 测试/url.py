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
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode("utf-8"))

# data = bytes(urllib.parse.urlencode({"hahaha":'ok'}),encoding="utf-8")
# try:
#     response = urllib.request.urlopen('http://httpbin.org/post',timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.HTTPError as e:
#     print('time out!')


# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)


# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders()) #获取全部的头部信息
# print()
# print(response.getheader("Bdqid")) #获取其中一个值






#爬取的时候不然服务器知道自己是爬虫
# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"hello":'ok'}),encoding="utf-8")
# headers = {
# "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
# }
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url = "https://www.douban.com"
# data = bytes(urllib.parse.urlencode({"hello":'ok'}),encoding="utf-8")
headers = {
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))












