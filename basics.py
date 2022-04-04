# 1
p = float(input("Enter a principal value:"))
t = int( input("Enter a time period in months:"))
r = float(input("Enter a rate of interest in %:"))
a = int(input("Enter 1 for simple interest or 2 for compound intertest:"))
if a == 1:
	print("The Simple Interest is :", p*t*r/100)
elif a== 2:
	print("The Compound Interest is :", p*((1+(r/100))**t)-p)
else :
	print("Enter a valid number.")
    
    
# 2
m = int(input("Enter the marks obtained in mathematics( out of 100):"))
p = int(input("Enter the marks obtained in physics( out of 100):"))
c = int(input("Enter the marks obtained in chemistry( out of 100):"))
e = int(input("Enter the marks obtained in english( out of 100):'"))
i = int(input("Enter the marks obtained in informatics practices( out of 100):"))
t = m+p+i+e+c
l = t/5
print("The total marks obtained are", t)
print("The percentage you got is", l)
if l >= 90:
	print("The grade obtained by you is A+")
elif l >= 80:
	print("The grade obtained by you is A")
elif l >= 70:
	print("The grade obtained by you is B+")
elif l >= 60:
	print("The grade obtained by you is B")
elif l >= 50:
	print("The grade obtained by you is C+")
elif l >= 40:
	print("The grade obtained by you is C")
elif l >= 33:
	print("The grade obtained by you is D")
else:
	print("The grade obtained by you is E")

#Conditional Looping 
while True:
    username = input('Enter username :')
    if username == 'pypy':
        break
    else:
        continue
else:
    print('Program completed')
    
#sets
a = {'apple', 'banana', 'cherry', 'orange'}

for x in a:
    print(x)
    
'banana' in a

#Dictionaries
d = dict(brand = 'Maruti Suzuki', model = 'i20', year = '2018')
d
d.get('i20)
d.items()

#Nested Dictionaries
myfamily = { 'child1' :{ 'name' : 'Emil', 'year' : 2004},
'child2' :{ 'name' : 'Shyam', 'year' : 2010},
'child3' :{ 'name' : 'Ram', 'year' : 2012}}
myfamily
myfamily.values()

#Numpy special function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)

y = np.sin(x)
#y = np.cos(x)
#y = np.tan(x)

plt.plot(x,y)

plt.show() 

#Numpy test
import numpy as np

a = np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])

print(a.ndim) # to get the no. of dimension
print(a.itemsize) # to get the size of individual item
print(a.dtype) # to get the datatype of elements
print(a.size) # to get the size of an array
print(a.shape) # to get the shape of an array
print(a)
print()

print(a.reshape(4,3)) # to reshape an array
print(a.transpose()) # to transpose an array
print()

print(a[0,2]) # to access an elements
print(a[0:,3]) # array slicing. Include all the rows but display only the element at index 3 in each row.
print(a[0:2,3]) # array slicing. Include row at index 0 and 1 but display only the element at index 3 in each row.
print()

c = np.linspace(1,3,5) # create an array containing 5 elements, equally spaced between 1 and 3.
print(c)
print()

print(a.max()) # give maximum value of an array
print(a.min()) # give minimum value of an array
print(a.sum()) # give the sum of the values of an array
print()

# The rows are called axis 1 and columns are called axis 0
print(a.sum(axis=0)) # the sum of columns
print(a.sum(axis=1)) # the sum of rows
print() 

print(np.sqrt(a)) # To calculate the square root of each of the element in the given array.
print(np.std(a)) # To calculate the stardard deviation. Means how much each element deviates from the mean value.
print() 

b = np.array([(4,3,2,1), (8,7,6,5), (12,11,10,9)])
print(a+b) # To get sum of two arrays element wise.
print(b-a) # To get subtraction of two arrays element wise.
print(a*b) # To get multiplication of two arrays element wise.
print(b/a) # To get division of two arrays element wise.
print()

#Concatenation of Arrays:
print(np.vstack((a,b))) # Vertical stacking
print(np.hstack((a,b))) # Horizontal stacking
print()

# To convert N-D array in a single column
print(a.ravel())

#Numpy time
import numpy as np
import time
import sys

size = 10000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start = time.time()
result = a1 + a2
print((time.time()-start)*1000)

#Numpy exponent and logarithm
import numpy as np

ar = np.array([1,2,3])

print(np.exp(ar)) # exponential of array ar
print()

print(np.log(ar)) # Natural log/log base e of array ar
print()

print(np.log10(ar)) # log base 10 values

#Numpy space
import numpy as np
import time
import sys

s = range(1000)

print(sys.getsizeof(5)*len(s)) # Get the total memory occupied by a list

d = np.arange(1000)

print(d.size*d.itemsize) # Get the total memory occupied by numpy array