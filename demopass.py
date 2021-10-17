#pass语句，什么都不做，只是一个占位符，用到需要写语句的地方
'''answer = input('您是会员吗？y/n')
if answer == 'y':
    pass
else:
    pass'''
#range()的三种创建方式
'''第一种创建方式，只有一个参数'''
r = range(10)
print(r)
print(list(r),type(r),'\n')
'''第二种创建方式，给了两个参数(小括号中有两个数值)'''
r=range(1,10)
print(r,'\n',list(r))

'''第三种创建方式，带有三个参数，分别为star,stop,step'''
a=0
sum=0
while a<5:
    sum+=a
    a=a+1
    print('\n',sum)
print('\n')
'''for...in...循环'''
for item in 'python':
    print(item)


for i in range(10):
    print(i)


for password in range(3):
    pwd = input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误请重新输入')
else:
    print('对不起,三次密码均输入错误。账号已被冻结')