x={'a':100,'b':200,'c':300,'d':400}
k=[]
v=[]
for i,j in x.items():
    k.append(i)
    v.append(j)
print(k,'\n',v)
r=int(input("Enter a value from dictionart:"))
for i in x.keys():
    if x[i]==r:
        print(i)