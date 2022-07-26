array=[]
array_size=int(input("Enter the size of the array: "))
for i in range(array_size):
    array.append(int(input("array[%d]="%(i))))

#Selection sort using iteration
for i in range(array_size):
    for j in range(i,array_size):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
print(array)