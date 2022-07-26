def factors(i):
    if i==n:
        return n
    else:
        if n%i==0:
            print(i)
        return factors(i+1)
n=int(input())
factors(n)