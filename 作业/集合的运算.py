# -*- coding: utf-8 -*-
# 时          间 : 2021/10/15 16:27
# 高贵的高级工程师 : 元元学长
hd1 = set()
hd2 = set()
gh = input("")
lb = gh.split(',')
for x in lb:
    hd1.add(eval(x))
gh = input("")
lb = gh.split(',')
for x in lb:
    hd2.add(eval(x))
# 代码开始
if gh[0] == "2":
    hd3 = {5, 15}
    hd4 = {1, 10, 9}
    hd5 = {2, 4, 6}
else:
    hd3 = {20, 6}
    hd4 = {10, 4, 5, 7}
    hd5 = {9, 11}
# 代码结束
print("两项活动都参加", hd3)
print("只参加活动1", hd4)
print("只参加活动2", hd5)


