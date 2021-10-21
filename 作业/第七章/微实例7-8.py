# -*- coding: utf-8 -*-
# 时          间 : 2021/10/21 10:28
# 高贵的高级工程师 : 元元学长
fo = open("prince2021.csv","r")
ls =[]
for line in fo:
    line = line.replace("\n","")
    #ls.append(line.split(",")) #字符串转换成列表，join是列表转换成字符串  生成的是二维列表
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)