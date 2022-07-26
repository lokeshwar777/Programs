for i in range(1,int(input())+1):
    for j in range(1,i+1):
        print(j,end='')
        if j==i:
            while(j>1):
                j-=1
                print(j,end='')
    print()
        
