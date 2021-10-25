# -*- coding: utf-8 -*-
# 时          间 : 2021/10/24 20:42
# 高贵的高级工程师 : 元元学长
import random
count = int(input("count:"))
rang = int(input("range:"))
s=set()
for i in range(count):
    num = random.randint(1,rang)
    s.add(num)
print(sorted(s))