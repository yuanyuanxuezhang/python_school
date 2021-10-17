n = int(input("请输入5个数字:"))
one = n // 10000
two = n//1000 - one*10
three = n // 100 - two*10 - one*100
four = n//10 - three*10 - two*100 -one*1000
five = n%10;
if one == five and two == four:
    print(n,'\n','是回文数')
else:
    print(n,'\n','不是回文数')