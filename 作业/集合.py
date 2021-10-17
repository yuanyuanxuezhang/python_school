s = {10,290,30,404,60}
'''集合元素的判断操作'''
print(10 in s)
print(10 not in s)
print(500 not in s)
print(500 in s)
'''集合元素的新增操作'''
s.add(50)
print(s)
s.update({1,2,3})
print(s)
s.update([4,5,6])
s.update((7,8,9))
print(s)

'''集合元素的删除操作'''
s.remove(290)
print(s)