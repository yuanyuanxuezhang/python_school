lst = [10,20,30]
print("添加之前的元素",lst)
# lst.append(100)
print("添加之后的元素",lst)

lst2 = ["python",'java']

lst3 = [True,False,'hello']
# lst.append(lst2)

#extend 添加多个元素
# lst.extend(lst2)

#insert 在指定的位置上添加一个元素
# lst.insert(1,90)

#切片： 在任意位置添加N个元素
lst[1:] = lst3
print("添加之后的元素",lst)