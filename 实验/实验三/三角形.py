# -*- coding: utf-8 -*-
# 时          间 : 2021/10/10 20:02
# 高贵的高级工程师 : 元元学长
from turtle import*  #从turtle中导出所有模块
for i in range(3):#采用for循环
  seth(i*120)#转角，注意fd和seth必须前面至少空一格，提示为for循环内容。
  fd(200)#forward，向前200像素，即边长为200像素
done()#结束，暂停
