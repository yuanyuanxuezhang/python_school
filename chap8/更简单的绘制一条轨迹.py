import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot

h, v0, g, n = 3000, 200, 9.8, 30
tmax = (2*h/g)**0.5
########### begin ##############
# 请使用numpy的linspace函数，在[0, tmax]上平均取30个点
t = np.linspace(0, tmax, n)
########## end #################
xt = v0*t                       #计算n个点的横坐标
yt = h-1/2*g*t**2               #计算n个点的纵坐标

plt.plot(xt, yt, 'r-')
plt.grid('on')
plt.axis([0, 5000, 0, h])
plt.savefig('./student result4/轨迹.png')
plt.close()
