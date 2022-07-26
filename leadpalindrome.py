def lpal(x):
    if int(x)<0:
        print('Invalid input')
    else:
        s=int(x[::-1])
        x=int(x)
        while x%10==0:
            x=int(x/10)
        if x==s:
            print('YES')
        else:
            print('NO')
n=input()
lpal(n)