n,a,b,c,d = 9,"－－","┼","∣       "," "
m = n // 2
for i in range(n):
    if i in [0,m,n-1]:
        print("{0}{1}{0}{1}{0}".format(b,a*(m-1)))
    else:
        print("{0}{1}{0}{1}{0}".format(c,d*(m-1)))