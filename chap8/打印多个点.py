import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot

h, v0, g = 3000, 200, 9.8
t, n = 0, 30        #n为要绘制的坐标点数量，假设为30
tmax = (2*h/g)**0.5
delta = tmax/(n-1)  #delta为相邻两时刻之间的间隔
while t<=tmax:      #t从0变到tmax，每次加delta
    ###### begin ##########
    # 请在此填写表达式，计算时间为t时，x轴与y轴的位置，并命名为xt与yt
    xt = v0*t
    yt = h-1/2*g*t**2
    plt.plot(xt,yt,'ro')
    t = t+delta
    ######### end ############
    plt.plot(xt,yt,'ro')
    t = t+delta
plt.grid('on')
plt.axis([0, 5000, 0, h])
plt.savefig('./student result2/%s个点.png' % str(n))
plt.close()
