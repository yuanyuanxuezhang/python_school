import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot

# 第一题
######## begin ###########
# 请编写函数triArea(a ,b , c)，返回三角形的面积
def triArea(a,b,c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s
######## end #########

S1 = triArea(9.8, 9.3, 6.4)
S2 = triArea(2.9, 4.1, 4.7)
S3 = triArea(2.0, 1.4, 2.3)
print('%.6f' %(S1-S2+S3))

# 第二题
######## begin ###########
# 请编写函数isPrime(x)。判断x是否是素数，返回True或者False
def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,x):
            if x%i==0 or (60-x)%i==0:
                return False
        else:
            return True

#######  end    ############


def Goldbach(N):  # 将N分解成两素数之和
    if N < 6 or N % 2 == 1:  # 若N小于6或N为奇数
        print('N应该是大于等于6的偶数')
    else:
        # 循环判断，得到符合要求的小于N的两个素数，并打印
        for x in range(2, N // 2):  # 想想为什么是从2到N/2
            # 调用isPrime函数，得到符合要求的小于N的两个素数
            ######## begin ###########
                isPrime(x)

            ######## end ###########
                print(N, '=', x, '+', N - x)
                break


N = int(input())
Goldbach(N)

# 第三题
# calBombTrace 函数
def calBombTrace(theta):
    v0, g, n = 300, 9.8, 30
    theta_d = np.radians(theta)     #因numpy中cos、sin的输入为弧度值，故先将theta从度转换为弧度
    v0_x = v0*np.cos(theta_d)       #炮弹水平初速度
    v0_y = v0*np.sin(theta_d)       #炮弹垂直初速度
    tmax = 2*v0_y/g                 #落地时间，即v0_y*t-0.5gtt=0的解
    t = np.linspace(0, tmax, n)     #n个时刻
    xt = v0_x*t                     #n个时刻的横坐标
    yt = v0_y*t-1/2*g*t**2          #n个时刻的纵坐标
    return xt, yt

for theta in [30, 45, 60, 75]:
    ############ begin #########
    # 调用函数，得到theta返回的值，并存储到xt与yt变量
    xt = calBombTrace(theta).xt
    yt = calBombTrace(theta).yt

    ########### end #############
    plt.plot(xt, yt)

plt.grid('on')
plt.axis([0, 10000, 0, 5000])
plt.savefig('./src/step4/res/轨迹.png')

plt.close()
print([round(x,6) for x in xt])
print([round(x,6) for x in yt])

# 第四题
# 在此添加代码，编写函数f(x)，计算f(x)的值
########### begin #############


########### end #############

# 在此添加代码，编写函数pt(a, b)，利用勾股定理计算直角三角形的斜边长
########### begin #############


########### end #############

n = 1000  # 细分成n个子区间
x = np.linspace(0, np.pi, n + 1)  # n个子区间的n+1个端点
l, h = 0, np.pi / n  # l为曲线长度、h为子区间宽度
for i in range(n):  # 对每个子区间
    li = pt(f(x[i + 1]) - f(x[i]), h)  # 曲线在第i个子区间的近似长度
    l = l + li  # 将航渡累加到l中

print('l = %.6f' %l)
