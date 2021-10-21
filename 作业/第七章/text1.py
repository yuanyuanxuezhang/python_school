# -*- coding: utf-8 -*-
# 时          间 : 2021/10/18 15:19
# 高贵的高级工程师 : 元元学长
textfile = open("7.1.txt","rt") #t表示文本文件方式
print(textfile.readline())
textfile.close()
binFile = open("7.1.txt","rb")
print(binFile.readline())
binFile.close()