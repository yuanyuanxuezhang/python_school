from random import *
import os, sys
random_num = randint(0,9)
user_num = input("请输入您猜的数据：")
n = 0;
while(True):
    n = n+1
    if user_num.isnumeric():
        while(True):
            if random_num == int(user_num):
                print("预测{}次，你猜中了".format(n))
                sys.exit()
            elif int(user_num) > random_num:
                print("遗憾，太大了")
                user_num = int(input("请输入您猜的数据："))
            else:
                print("遗憾，太小了")
                user_num = int(input("请输入您猜的数据："))
    else:
        print("输入类容必须为整数！")
        user_num = input("请输入您猜的数据：")
