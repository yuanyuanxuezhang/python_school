# 测试说明
# 本关的测试文件是src/Step1/plus.py，测试过程如下：
#
# 平台自动编译生成plus.exe;
# 平台运行plus.exe，并以标准输入方式提供测试输入；
# 平台获取plus.exe输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。
# 以下是平台对src/Step1/plus.py的样例测试集：
#
# 测试输入：
# 1 2 3 4 5
# 预期输出：
# 15
#
# 测试输入：
# 1 3 5 7 9 11
# 预期输出：
# 36
#
# 测试输入：
# 2 4 6 8 10 12 14 16
# 预期输出：
# 72

#coding=utf-8

#创建一个空列表numbers
numbers = []

#str用来存储输入的数字字符串，lst1是将输入的字符串用空格分割，存储为列表
str = input()
lst1 = str.split(' ')

#将输入的数字字符串转换为整型并赋值给numbers列表
for i in range(len(lst1)):
   numbers.append(int(lst1.pop()))

# 请在此添加函数plus的代码，函数参数为一个列表，对列表中的数值元素进行累加求和
#********** Begin *********#
def plus(*numbers):
   sum = 1
   summ = 1
   a = len(numbers)
   s = 1
   for i in range(0,a):
      sum *=  numbers[i]
   num = len(sum)
   for j in range(0,num):
      summ +=sum[j]
   return summ-1

#********** End **********#

#调用plus函数，并将返回结果存储到变量d中
d = plus(numbers)
print(d)
