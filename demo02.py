# 输出python中的关键字
# import keyword
# print(keyword.kwlist)


name = '张三'
age = 20
print('我叫'+name+'我今年'+str(age)+'岁了')
present = input('大圣想要什么礼物呢？\n')
print(present)
a,b,c = 10,20,10
print('a>b吗?',a>b)
print('a<b吗?',a<b)
print('a is b 比较2者之间的id',a is b)
print('a is c 吗?  \n\n',a is c)
print('---------------顺序结构------------------\n')
print('---------------程序开始------------------\n')
print('把大象装进冰箱一共要几步？')
print('1.把冰箱门打开')
print('2.把大象放进冰箱里面')
print("3.把冰箱门关上\n")
print('---------------程序结束--------------------')

money = 1000  #余额
s=int(input('请输入取款金额'))   #取款余额
# 判断余额是否充足

if money>=s:
    money = money-s
    print('取款成功，余额',money)