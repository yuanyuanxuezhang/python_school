import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     #导入matplotlib.pyplot
h, v0, g = 3000, 200, 9.8
for t in [10, 15, 20, 24]:
    xt = v0*t
    yt = h-1/2*g*t**2

    plt.ylim((0, 3000))
    plt.xlim((0, 5000))
    plt.grid('on')
    ######## begin ############
    # 请使用plot函数，绘制一个坐标点
    plt.plot(xt,yt,'ro')
    ######## end ##############
    plt.savefig('./student result/%s秒后.png' % str(t))
    plt.close()
