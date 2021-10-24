# -*- coding: utf-8 -*-
# 时          间 : 2021/10/23 14:41
# 高贵的高级工程师 : 元元学长
fo = open("物联网19-1-2班学生名单.csv","r")
ls =[]
for line in fo:
    # line = line.replace("\n","")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns +="{}\t".format(s)
        print(lns)
fo.close()

