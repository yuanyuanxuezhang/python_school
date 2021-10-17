#第一种创建方式使用{}

s = {2,3,4,5,5,6,7,7}#集合中的元素不允许重复
print(s)

#第二种创建方式使用set（）
s1 = set(range(6))
print(s1,type(s1))

s2 = set([1,2,6,2,3,5,56])
print(s2,type(s2))

s3 = set((1,2,3,4,555,4,4))
print(s3,type(s3))

s4 = set("python")
print(s4,type(s4))

s5 = set({1,2,3,6,5,5,6})
print(s5,type(s5))

s6 = set({})
print(s6,type(s6))