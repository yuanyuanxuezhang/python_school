# i = 0
# result = 0
#
# while i <= 100:
#     result += i
#     i += 1
# print('1+2+3+...+100的和为:%d' % result)

# while True:
#     print('三生三世十里桃花，一心一意百行代码')
# count=0
#
# while count<5:
#     print("我爱python",count)
#     count+=1
# else:
#         print("我爱PHP")
import time

gonzi = 0
a_type = "Python"

if a_type == "Python":
    gonzi = 10000
if a_type == "PHP":
    gonzi = 20000
if a_type == "java":
    gonzi = 30000

print(gonzi)

# "{0:a^10x}".format(520520520502502502)
scale =10
for i in range(scale+1):
    a,b = '**'*i ,'..'*(scale - i)
    c = (i/scale)*100
    print("%{:3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----")
