# -*- coding: utf-8 -*-
# 时          间 : 2021/10/16 15:40
# 高贵的高级工程师 : 元元学长
import random
random.seed(0x1010)
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
ls = []            #把十个密码放入列表ls中
excludes = ""      #存放每个密码的首字符
while len(ls) < 10:
    pwd = ""               #生成一个10字符的密码
    for i in range(10):
        pwd += s[random.randint(0, len(s)-1)]
    if pwd[0] in excludes:   #首字符重复，重新再生成新密码
        continue
    else:                    #首字符不重复，把它添加到列表中
        ls.append(pwd)
        excludes += pwd[0]

# 直接打印
print("\n".join(ls))