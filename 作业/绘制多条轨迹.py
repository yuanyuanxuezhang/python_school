import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot

def calBombTrace(h, v0):
    g, n = 9.8, 30
    tmax = (2*h/g)**0.5
    t = np.linspace(0, tmax, n)
    xt = v0*t
    yt = h-1/2*g*t**2
    ##### begin ############
    # 函数bia返回xt，yt
    return xt,yt
    ###### end #############

H, V0 = [3000, 2000], [200, 260]
for h in H:
    for v0 in V0:
        xt, yt = calBombTrace(h, v0)
        plt.plot(xt, yt)
plt.grid('on')
plt.axis([0, 6500, 0, 3000])
plt.savefig('./student result5/轨迹.png')
plt.close()

