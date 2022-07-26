array=[]
array_size=int(input("Enter the size of the array: "))
for i in range(array_size):
    array.append(int(input("array[%d]="%(i))))
search_element=int(input("Enter the number that you want to search: "))
'''
#Linear Search using iteration
k=0
for i in range(array_size):
    if array[i]==search_element:
        k=1
        print("The required element is found at %dth position"%(i+1))
if k==0:
    print("The required element is not found")
'''
#Linear Search using recursion
def linear_search(array,search_element,k=0):
    if k==array_size:
        return "The required element is not found",k
    elif array[k]==search_element:
        return "The required element is found at %dth position"%(k+1)
    else:
        return linear_search(array,search_element,k+1)

print(linear_search(array,search_element))