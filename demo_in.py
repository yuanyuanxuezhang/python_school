print("p" in "python")       #true
print("p" not in "python"   )#false

lst=[10,20,"python","hello"]
print(10 in lst)            #ture
print("java" in lst)        #false
print("java" not in lst)    #true
print("--------------------------------------")

for i in lst:
    print(i,end="\t")