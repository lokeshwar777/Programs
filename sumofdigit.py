def sumofdigit(n):
    global s
    if n>0:
        s+=n%10
        return sumofdigit(n//10)
    else:
        return s
n=int(input())
s=0
print(sumofdigit(n))