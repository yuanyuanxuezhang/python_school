# -*- coding: utf-8 -*-
# 时          间 : 2021/10/30 14:42
# 高贵的高级工程师 : 元元学长
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 100, 9999)
y=0
for k in range(1, 10, 1):
    y=y+4*np.sin((2*k-1)*x)/((2*k-1)*np.pi)
plt.plot(x,y,'k',color='pink',label="w=",linewidth=3)
plt.axis([0,10,-1.5,1.5])
plt.legend()
plt.show()
