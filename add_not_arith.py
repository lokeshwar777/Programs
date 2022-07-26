def not_arith(a,b):
    for i in range(b):
        a+=1
    return a
a=int(input())
b=int(input())
print(not_arith(a,b))