# -*- coding: utf-8 -*-
# 时          间 : 2022/1/20 20:33
# 高贵的高级工程师 : 元元学长
import requests #导入库
import os #导入os库
os.system("clear") #清屏
while True:
  print("")
  qq = input("请输入对方QQ：")      #设置输入框
  url = "http://api.qb-api.com/qbtxt-api.php?qq="+qq      #设置接口
  cha = requests.get(url)      #爬虫
  print(cha)
  print(cha.text)      #把结果打印出来
  print("查询完毕 ") #没了
