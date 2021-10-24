# -*- coding: utf-8 -*-
# 时          间 : 2021/10/16 15:03
# 高贵的高级工程师 : 元元学长
def judge(list):
    s = set()
    lenth = len(list)
    for i in range(lenth):
        s.add(list[i])
        if len(s) != (i+1):
            return True
    return False
a = [1,12,2,2]
print(judge(a))