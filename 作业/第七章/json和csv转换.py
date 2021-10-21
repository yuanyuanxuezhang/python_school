# -*- coding: utf-8 -*-
# 时          间 : 2021/10/21 11:13
# 高贵的高级工程师 : 元元学长
import json
fr = open("price2016.cs","r")

ls =[]

for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw = open("prince2016.csv","w")
for i in range(1,len(ls)):
    ls[i] = dict(zip(ls[0],ls[i]))
json.dumps(ls[1:],fw,sort_keys=True,indent=4)
fw.close()