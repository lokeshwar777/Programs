arr=[]
b=int(input("Enter the size of the array: "))
for i in range(b):
    arr.append(int(input("arr[%d]="%(i))))
arr.sort()

#Binary Search using recursion
'''
def BinarySearch(low,high):
    if high<low:
        return "The element is not found"
    global arr,n
    mid=high//2
    if n==arr[mid]:
        print("The element is found at %dth position"%(mid+1))
        # if element is found at multiple positions
"""
        if n==arr[mid-1]:
            return BinarySearch(low,mid-1)
        if n==arr[mid+1]:
            return BinarySearch(mid+1,high)
"""    
    elif n>arr[mid]:
        return BinarySearch(mid,high)
    else:
        return BinarySearch(low,mid)
low=0
high=len(arr)
while True:
    n=int(input("Enter a number which is to searched: "))
    BinarySearch(low,high)
    if n=='\n':
        break
'''

# Binary search using iteration

low =0
high=len(arr)
while True:
    n=int(input("Enter a number which is to be searched: "))
    while low<high:
        mid=high//2
        if n==arr[mid]:
            print("The element is found at %dth position"%(mid+1))
            break
        elif n>arr[mid]:
            low=mid
        else:
            high=mid
    else:
        print("The element is not found")