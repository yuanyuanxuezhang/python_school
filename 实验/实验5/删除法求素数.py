# -*- coding: utf-8 -*-
# 时          间 : 2021/10/18 14:36
# 高贵的高级工程师 : 元元学长
print("素数：列表删除法测试")
n = 30
ls = list(range(2,n+1))
print(ls)
for i in ls:
    for j in range(2,(i//2)+1):
        if i%j == 0:
            ls.remove(i)
        break
print(ls)