import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot


h, v0, g = 3000, 200, 9.8
n = 30
xt, yt = [], []
tmax = (2*h/g)**0.5
delta = tmax/(n-1)
for i in range(n):
    t = delta*i
    xt.append(v0*t)
    yt.append(h-1/2*g*t**2)
#### begin ###########
# 请使用plot函数绘制一条线
plt.plot(xt,yt,'r-')
plt.grid('on')
plt.axis([0, 5000, 0, h])
#### end ##############
plt.grid('on')
plt.axis([0, 5000, 0, h])
plt.savefig('./student result3/轨迹.png')
plt.close()
