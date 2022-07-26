n=int(input('Enter a number:'))
# Prime numbers upto the number
a=[]
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        a.append(i)
print('The prime factors of',n,'are :')
# Factors of the number
b=[]
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
for i in b:
    if i in a:
        print(i,end=' ')
