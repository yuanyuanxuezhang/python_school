s1 = {1,2,3,4}
s2 = {4,3,2,1}
print(s1 == s2) #True
print(s1 != s2) #False

"""一个集合是另一个集合的子集"""
s1 = {1,2,3,4,5,6}
s2 = {1,2,3}
s3 = {1,2,9}
print(s2.issubset(s1)) #s2是s1的子集True
print(s3.issubset(s1)) #s3是s1的子集False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))

'''两个集合是否没有交集'''
print(s2.isdisjoint(s3)) #False
s4 = {10,20,33,44}

print(s2.isdisjoint(s4)) #True
