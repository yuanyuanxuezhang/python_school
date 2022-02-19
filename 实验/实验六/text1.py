# -*- coding: utf-8 -*-
# 时          间 : 2021/11/19 15:36
# 高贵的高级工程师 : 元元学长
from  random import *
m=eval(input("请输入一个整数:"))
n=True
for i in range(2,m-1):

    if m%i==0:
        print("{}不是质数".format(m))
        n=False
        break
if n!=False:
    print("{}是质数".format(m))
# a=['123','asd']
# list(a)
# print(a.index("123"))
# a={'name':'zhangs','age':'1'}
# for i in a:
#     print(i)
# a['name']='hh'
# a.popitem()
# print(a)
# print(a.values())

# while(1):
#     a = randint(1, 2)
#     print(a)