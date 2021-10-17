# -*- coding: utf-8 -*-
# 时          间 : 2021/10/16 14:42
# 高贵的高级工程师 : 元元学长

# 第一个栗子
a = 520
def aa():
    a = 52
    return a
aa()
print(a)

# 第二个栗子
class1 = 'python'
def w_class():
    global class1
    class2 = 'php'
    class1 = class2
    return class2
print(w_class())

# 第三个栗子
class3 = []
def li3(a):
    class3.append(a)
    return class3
a = li3('java')
print(a,class3)

# 第四个栗子
class4 = []
def li4(b):
    class4 = []
    class4.append(b)
    return class4
b = li4('thinkphp')
print(class4,b)