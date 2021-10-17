from random import *
random_num = randint(0,100)
user_num = int(input("请输入您猜的数据："))
n = 0;
while(True):
    n = n+1
    if random_num == user_num:
        print("预测{}次，你猜中了".format(n))
        break
    elif user_num > random_num:
        print("遗憾，太大了")
        user_num = int(input("请输入您猜的数据："))
    else:
        print("遗憾，太小了")
        user_num = int(input("请输入您猜的数据："))
