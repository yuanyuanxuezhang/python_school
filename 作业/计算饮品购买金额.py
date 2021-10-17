# -*- coding: utf-8 -*-
# 时          间 : 2021/10/15 16:14
# 高贵的高级工程师 : 元元学长
cp = (("悠哉悠哉", 18), ("人间烟火", 17), ("蔓越阑珊", 17), ("抹茶葡提", 16), ("幽兰拿铁", 16), ("  翠翠  ", 13), ("浮生半日", 15), ("筝筝纸鸢", 16),
      ("声声乌龙", 15), ("风栖绿桂", 12), ("素颜锡兰", 13), ("烟火易冷", 15))
# 代码开始
a = 0
sum = 0
for i in cp:
    a = a + 1
    if a < 10:
        print("", a, end="")
        print(i[0], end="")
        print(i[1])
    else:
        print(a, end="")
        print(i[0], end="")
        print(i[1])

while (True):

    drink = int(input("请选择饮品"))
    if drink == 0:
        print("应付{}元".format(sum - 1))
        break
    else:
        num = int(input("请输入数量"))
    sum = sum + int(cp[drink][1] * num)

# 代码结束