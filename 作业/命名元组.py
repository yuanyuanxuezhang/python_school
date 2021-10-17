'''

任务描述
命名元组 (namedtuple)
创建命名元组
访问命名元组的元素
修改元素
编程要求
任务描述
本关任务：完成对命名元组的简单操作。

命名元组 (namedtuple)
Python 中提供了基础的不可变数据结构元组tuple，对元组元素的访问需通过索引来完成，对此需要熟记每个下标对应的具体含义。如果元素数量一多，要记清楚这些东西就会比较麻烦了，于是就出现了命名元组namedtuple。

创建命名元组
命名元组的构造函数接受两个参数typename，field_names：

typename：元组的名字；
field_names：元组各个元素的名称，也就是属性名称。
比如：

collections.namedtuple("Point",["x","y"])
这样就创建了一个叫做Point的命名元组类，它拥有两个属性x，y。

第二个参数["x","y"]也可以写成"x y"或者"x,y"，即用空格或者逗号隔开属性名，即：

collections.namedtuple("Point","x y")
collections.namedtuple("Point","x,y")
我们可以将其赋值给一个变量：

Point = collections.namedtuple("Point","x,y")
p = collections.namedtuple("Point","x,y") #变量名不一定要和第一个参数相同
以上得到的变量Point或者p并不直接是一个元组对象，它只是一个类，如果要创建它的实例，则需要像创建类实例一样调用它：

p1 = Point(x = 0, y = 0)
p2 = p(x = 1, y = 1)
这样就创建了两个实例p1，p2，他们的内容分别是x = 0,y = 0，x = 1,y = 1。

访问命名元组的元素
通过collections.namedtuple创建的命名元组类，实际上是元组类的子类，因此命名元组也可以通过索引访问元素：

print(p1[0])
print(p1[1])
得到的结果：
0
0

当然，命名元组也可以通过属性访问：

print(p2.x)
print(p2.y)
得到的结果：
1
1

修改元素
如果需要修改元组的元素，则不能简单的使用p1.x = 1，需要调用成员函数_replace()，它会返回一个包含新值的新实例，比如：

p1 = p1._replace(x = 1) #将p1的x值从0换到1
编程要求
根据右边编辑器中各个函数中的提示，将函数Begin-End区间代码补充完整，使得程序能够正常运行并输出正确的结果。编辑区的3个函数，将按照如下顺序被调用：

    p = CreatePoint()
    PrintPoint(p)
    p = IncX(p)
    PrintPoint(p)
    p = IncY(p)
    PrintPoint(p)
提示：后两个函数需要用到函数_replace()。
####测试说明
正确的补充代码后，应该得到的结果：
当前位置:x = 0,y = 0
当前位置:x = 1,y = 0
当前位置:x = 1,y = 1

开始你的任务吧，祝你成功！
'''


import collections

def CreatePoint():
    # ********** Begin ********** #
    q = collections.namedtuple("text","x,y")
    p = q(x=0,y=0)
    return p

	# ********** End ********** #

def IncX(p):
    # ********** Begin ********** #
    p = p._replace(x=1)
    return p

	# ********** End ********** #

def IncY(p):
    # ********** Begin ********** #
    p = p._replace(y=1)
    return p

	# ********** End ********** #

def PrintPoint(p):
    print("当前位置:x = %d,y = %d" % p)

p = CreatePoint()
PrintPoint(p)
p = IncX(p)
PrintPoint(p)
p = IncY(p)
PrintPoint(p)