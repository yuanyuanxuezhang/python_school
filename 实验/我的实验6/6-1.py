import xpinyin
import json
fo = open("物联网19-1-2班学生名单.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
p = xpinyin.Pinyin()
for line in ls:
    line.append(p.get_initials(line[2]))
fw = open("xin.csv","w")
for line in ls:
    fw.write(",".join(line)+'\n')
fw.close()
fo.close()

fr = open("xin.csv","r")
lss=[]
for line in fr:
    line=line.replace("\n","")
    lss.append(line.split(','))
fr.close()
fw=open("xin.json","w")
for i in range(1,len(lss)):
    lss[i]=dict(zip(lss[0],lss[i]))
json.dump(ls[1:],fw,sort_keys=True,indent=4,ensure_ascii=False)
fw.close()
