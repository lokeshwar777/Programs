from lib2to3.pgen2.token import LEFTSHIFTEQUAL


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))