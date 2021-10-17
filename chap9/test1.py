# -*- coding: utf-8 -*-
# 时          间 : 2021/10/9 10:13
# 高贵的高级工程师 : 元元学长
vlist = list(range(10))

# vlist[1:3] = 0 不可以这么写的
vlist[1:3] =[0]

print(vlist)
s = "他是个小伙子"
ls = list(s)
print(ls)
ls.insert(1,'真')
print(ls)
print(''.join(ls))
a="how are you"
print(a[0])