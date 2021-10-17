# -*- coding: utf-8 -*-
# @Time : 2021/10/6 10:58
# @Author : 元元学长
s = 'hello,python'
print('1.',s.isidentifier())    #False
print("2.",'hello'.isidentifier())  #True
print('3.','张三_'.isidentifier())    #True
print('4.','张三_123'.isidentifier()) #True

print('5.','\t'.isidentifier())     #False
print('6.','\t'.isspace())  #True

print('7.','abc'.isalpha()) #是否全部由字母组成