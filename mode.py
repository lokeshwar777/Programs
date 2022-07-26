import re
a=[int(a) for a in input().split()]
b=[]
for i in a:
    if i not in b:    
        b.append(i)
b.sort()
c=[]
for i in b:
    k=0
    for j in a:
        if i==j:
            k+=1
    c.append(k)
print('The mode is',end=' ')
for i in range (0,len(c)):
    if c[i]==max(c):
        print(b[i],end=' ')