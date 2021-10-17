t = (10,[20,30],40,100)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]),'\n',t[1],type(t[1]),id(t[1]),'\n',t[2],type(t[2]),id(t[2]))
print(id(100))
print(id(t[3]))
#t[1]=100   元组是不允许修改元素的
