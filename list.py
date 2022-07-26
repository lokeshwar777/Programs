if __name__ == '__main__':
    n = int(input())
    k=[]
    for i in range (0,n):
        x=[]
        x = [str(x) for x in input().split()]
        if (x[0]=='insert'):
            a=int(x[1])
            b=int(x[2])
            k.insert(a,b)
        elif(x[0]=='print'):
            print(k)
        elif(x[0]=='remove'):
            a=int(x[1])
            k.remove(a)
        elif(x[0]=='append'):
            a=int(x[1])
            k.append(a)
        elif(x[0]=='sort'):
            k.sort()
        elif(x[0]=='pop'):
            k.pop()
        elif(x[0]=='sort'):
            k.sort(reverse=True)
        i+=1
        

        
            