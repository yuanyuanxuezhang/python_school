

items = ['Fruits',"Book",'Others']
prices = [96,78,85,1000]

d = {value:key for value,key in zip(items,prices)}
print(d)
d = {value.upper():key for value,key in zip(items,prices)}
print(d)