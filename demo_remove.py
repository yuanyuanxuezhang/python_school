lst = [10,20,30,40,50,30,60,30]
lst.remove(30)
print(lst)  #如果元素重复值移出第一个元素

lst.pop(1)
print(lst)
lst.pop()
print(lst)
print('------------------------------')
new_list = lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)

"""不产生新的列表对象，而是直接删除原来的列表"""
print(lst)
lst[1:3] = []
print(lst)

print('---------------------------------')
"""清楚列表中的所有元素"""
lst.clear()
print(lst)


'''del语句将列表元素对象删除'''
del lst

'''排序'''
lst = [10,20,48,30,29]
#lst.sort()  #使用sort方法排序，默认是升序排列
print(lst)

lst.sort(reverse=True)  #reverse=True 表示降序排列，reverse=False就是升序排列
print(lst)
lst.sort(reverse=False)
print(lst)
print('-----------------------------')
lst1 = [i*i for i in range(1,10)]
print(lst1)
