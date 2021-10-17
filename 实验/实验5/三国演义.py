# -*- coding: utf-8 -*-
# 时          间 : 2021/10/16 15:17
# 高贵的高级工程师 : 元元学长
import jieba
txt = open(r'D:\Python\pythonExercise\实验\实验5\171182.txt','r',encoding='utf-8').read()
excludes = {'将军','却说','荆州','二人','不可','不能','如此','商议','如何','主公','左右','军士',\
            '军马','引兵','次日','大喜','天下','东吴','于是','今日','不敢','魏兵','陛下','不知','一人','不敢',\
            '不知','人马','都督','汉中','只见','蜀兵'}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =='诸葛孔明' or word == '孔明曰' or word == '诸葛亮':
        rword = '孔明'
    elif word =='关公' or word == '云长':
        rword = '关羽'
    elif word =='玄德' or word == '玄德曰':
        rword = '刘备'
    elif word =='孟德' or word == '丞相':#丞相也可能是说诸葛亮
        rword = '曹操'
    else:
        rword  = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(30):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))

