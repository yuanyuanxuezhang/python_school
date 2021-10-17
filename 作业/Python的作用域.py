# 测试说明
# 本关的测试文件是src/step3/scope.py，测试过程如下：
#
# 平台自动编译生成scope.exe;
# 平台运行scope.exe，并以标准输入方式提供测试输入；
# 平台获取scope.exe输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。
# 以下是平台对src/step3/scope.py的样例测试集：
#
# 测试输入：
# 5
# 6
# 预期输出：
# 30
#
# 测试输入：
# 8
# 10
# 预期输出：
# 40
#
# 测试输入：
# 16
# 24
# 预期输出：
# 48
#
# 测试输入：
# 132
# 214
# 预期输出：
# 14124

#coding=utf-8

#输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加一个private函数_gcd()求两个正整数的最大公约数
#********** Begin *********#
def _private_gcd(a,b):
    if b == 0 :
        return a
    return gcd(b,a%b)

#********** End **********#

#请在此添加一个public函数lcm()，在lcm()函数中调用_gcd()函数，求两个正整数的最小公倍数
#********** Begin *********#
def lcm(a,b):
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    return a*b//gcd(a,b)

#********** End **********#


#调用函数，并输出a,b的最小公倍数
print(lcm(a,b))