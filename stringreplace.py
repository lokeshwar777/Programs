a=input()
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in a:
    if i in b:
        b.remove(i)
        print(i,end='')
    else:
        print('$',end='')