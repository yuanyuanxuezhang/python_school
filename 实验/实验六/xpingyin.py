# -*- coding: utf-8 -*-
# 时          间 : 2021/10/23 15:21
# 高贵的高级工程师 : 元元学长
import xpinyin
fo = open('物联网19-1-2班学生名单.csv','r',encoding="utf-8")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
p = xpinyin.Pinyin()
for lss in ls:
    lss.append(p.get_initial(lss[2]))
fw = open("xie_name.csv","w",encoding="utf-8")
for line in s:
    fw.write(",".join(line)+'\n')
fw.close()
fo.close()
