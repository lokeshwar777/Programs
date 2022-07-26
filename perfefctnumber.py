def pernum(n):
    global k
    if n>0:
        k+=n%10
        return pernum(n//10)
    else:
        if k==l:
            print(l,'is a perfect number')
        else:
            print(l,'is not a perfect number')
n=int(input())
k=0
l=n
p=pernum(n)
print(p)