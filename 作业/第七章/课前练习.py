# -*- coding: utf-8 -*-
# 时          间 : 2021/10/21 10:00
# 高贵的高级工程师 : 元元学长
y = 1
z = 3

# x = (y = z + 1) 错误

def f2(p1,*p2):
    print(p1)
    print(p2)
f2(1,2,3,4)

def f3(p1,**p2):
    print(p1)
    print(p2)
f3(1,x=2,y=3,z=4)

# 平均值
def func(*c):
    # ls =[]
    l = len(c)
    sum = 0
    for i in c:
        sum = sum +i
    d = sum/l
    print(d)
    for i in c:
        if d < i:
            print(i)
func(1,2,3,34)