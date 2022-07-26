array=[]
array_size=int(input("Enter the size of the array: "))
for i in range(array_size):
    array.append(int(input("array[%d]="%(i))))
print("The given array is",array)

#Bubble sort using iteration
for i in range(array_size,1,-1):
    for j in range(i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print("The sorted array is",array)

#Bubble sort using recursion
def bubble_sort(array):
    

print(bubble_sort(array))