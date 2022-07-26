# Using iteration and list
'''
def fibonacci(n):
    a=[0,1]
    for i in range(n-2):
        a.append(a[i]+a[i+1])
    return a[n-1]

n=int(input())
print(fibonacci(n))

# Using iteration and 2 variables
def operation(s):
    if s=='y':
        a=0
        b=1
        n=int(input("Enter a number:"))
        for i in range(n-1):
            b=a+b
            a=b-a
        print(a)
        #k=input("Do you want to try again?(y/n):")
        return operation('y')
    else:
        return 'End of program'
operation('y')

# Using two functions
def fibonacci(n):
    n=n-1
    global i
    i=0
    a=[0,1]
    def fibo(i,n):
        if i==n:
            return a[n]
        else:
            a.append(a[i]+a[i+1])
            return fibo(i+1,n)
    return fibo(i,n)

n=int(input())
print(fibonacci(n))
'''
def fibonacci(n):
    global a,b
    if n>0:
        b=a+b
        a=b-a
        return fibonacci(n-1)
    else:
        return a
a=0
b=1
n=int(input("Enter a number:"))
k=fibonacci(n-1)
print(k)