a=input("请输入一串字符：")
N=len(a)
english=0#英文字符个数
numbers=0#数字个数
space=0#空格个数
extra=0#其他字符个数
chinese=0
a=a.lower()
for i in range(0,N):
    if a[i]>="a" and a[i]<="z":#此行也可以改成：if a[i].islower():
        english+=1
    elif a[i].isnumeric():
        numbers+=1

    elif a[i].isspace():
        space+=1
    else:
        extra+=1
print("英文字符个数：{}\t数字个数：{}\t空格个数：{}\t其他字符个数：{}".format(english,numbers,space,extra),end="")
