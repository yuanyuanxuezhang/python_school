# NixieTube.py

import turtle, time

def drawGap():

    turtle.penup()

    turtle.fd(5)

def drawLine(draw):      #绘制单段数码管

    drawGap()

    turtle.pendown() if draw else turtle.penup()    #如果draw为真值则画，如果不是则抬起画笔移动

    turtle.fd(40)     #向该方向行进40像素

    drawGap()

    turtle.right(90)  #转向90度

def drawDigit(digit):    #根据数字绘制七段数码管

    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,6,8] else drawLine(False)

    turtle.left(90)

    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)

    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)

    turtle.left(180)

    turtle.penup()    #为绘制后续数字确定位置

    turtle.fd(20)     #...

def drawDate(date):   #获得要输出的数字，日期格式为：'%Y-%m=%d+'

    turtle.pencolor("red")

    for i in date:

        if i == '-':

            turtle.write('年',font=("Arial",18,"normal"))

            turtle.pencolor("green")

            turtle.fd(40)

        elif i == '=':

            turtle.write('月',font=("Arial",18,"normal"))

            turtle.pencolor("blue")

            turtle.fd(40)

        elif i == '+':

            turtle.write('日',font=("Arial",18,"normal"))

        else:

            drawDigit(eval(i))   #通过eval()函数将数字变为整数

def main():

    turtle.setup(800, 350, 200, 200)     #设置画布大小

    turtle.penup()

    turtle.fd(-300)      #当前画笔初始绘制所在位置

    turtle.pensize(5)

    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))   #调用函数

    turtle.hideturtle()

    turtle.done()

main()