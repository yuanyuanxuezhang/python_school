

scores = {'张三':100,'李四':98,'王五':59}
#获取所有的key
keys = scores.keys()

print(keys)
print(type(keys))
print(list(keys))
print('----------------------------------------------')

#获取所有的values
values = scores.values()
print(values)
print(type(values))
print(list(values))

print('---------------------------------')
#获取所有的keys-values键值对
items = scores.items();
print(items)
print(type(items))
print(list(items))

print('---------------------------------')
for item in scores :
    print(item,scores[item],scores.get(item))#score[] 和 get方法都是根据键来获取值的方法
    