import numpy as np  
import pandas as pd

ser = pd.Series() #creating an empty series
print(ser)

data = np.array(['f','r','i','d','a','y']) # simple array
ser = pd.Series(data)
print(ser)

df = pd.DataFrame() # Calling dataframe constructor
print(df)

lst = ['Geeks', 'For', 'Geeks', 'is', 'a', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst) # Calling dataframe constructor on list
print(df)

# Creating an empty series 
ser = pd.Series(dtype=object) 
ser

data = np.array(['g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data)
print(ser) 

lst = [10,20,30,40,50] 
ser = pd.Series(lst) 
print(ser) 

ser = pd.Series(range(5)) 
ser 

ser.index = [10,20,30,40,50] # is used to change the index. 
ser

s = pd.Series(range(5), dtype='float') 
s

lst = [11,22,33,44,55,66] 
i = ['a', 'b', 'c', 'd', 'e', 'f'] 
s = pd.Series(lst, i) 
s 

print(s[0]) # for value at index 0 
s[:3] # for first 3 index values
s[-3:] # for last 3 index values
s[-1:1] 

i = ['a', 'b', 'c', 'd', 'e', 'f'] 
s = pd.Series(lst, i) 
s 

s.iloc[1:4] # values at index 1 to 3 
s.iloc[:3] # for first 3 index values 
s[:3] 
s['b':'e'] # for values at index b to e 
s.loc['b':'e'] # for values at index b to e 

ser = pd.Series(55, ['a', 'b', 'c', 'd', 'e']) 
ser 

s = 'Welcome to IP Class' i = ['Raju', 'Akshay', 'John', 'Anand', 'Meghana', 'Saileela'] 
ser = pd.Series(s,i) 
ser 

i = [x for x in 'abcde'] 
ser = pd.Series(range(1,15,3), i) 
ser 

ser['d'] # calling the value with the name of the index 
ser[3] # calling the value with the index number 

# Creating a series from two different lists. 
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'] # as index 
days = [31, 28, 31, 30, 31, 30, 31] # as data 
ser = pd.Series(days, months) 
ser

ser[31] 
ser.iloc[2] 

# Creating a series using misssing values (NaN) 
ser = pd.Series([7.5, 5.4, np.NaN, -34.5]) 
ser 

# Creatition of series using dictionary 
import pandas as pd dic = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30} 
ser = pd.Series(dic) 
ser.name = 'Days' 
ser.index.name = 'Month' 
ser 
 
#Creation of series using mathematical expression 
s1 = np.arange(10,15) 
ser = pd.Series(index = s1, data = s1/2) 
ser 

#Creation of series using mathematical function 
s1 = np.arange(10,15) 
ser = pd.Series(index = s1, data = s1*np.pi) 
ser 

s1 = np.arange(1,11) 
ser = pd.Series(index = s1, data = s1*np.pi) 
ser 
 
ser.index 
ser.values 
ser.dtype 
ser.shape 
ser.nbytes 
ser.ndim 
ser.size # returns the no. of elements in the series 
ser.hasnans 

s = pd.Series([7.5, 5.4, np.NaN, -34.5]) 
s 
s.hasnans 
ser.empty 

s1 = pd.Series(dtype=object) 
s1 
s1.empty 
ser.head() 
ser.tail() 
ser.head() 

s1 = np.arange(1,10) 
ser = pd.Series(index = s1, data = s1*np.pi) 
ser 
ser.head() 
ser.tail() 
ser.tail(3) 

a = pd.Series([1,3,5,7]) 
b = pd.Series([2,4,6,8]) 
a.add(b) # for adding two series 
b.sub(a) #for subtraction 
a.mul(b) # for multiplication 
b.div(a) #for division 
a.sum() # to add the elements of the series. 
b.sum() 
a.prod() # to get the product of all the elements of the series. 
a.mean() # To find the average of the values 
a.pow(b) # Method is used to put each element of passed series(b) 

# as exponential power of caller series elements. 
c = pd.Series(np.linspace(1,2,5)) 
c 
 
c.abs() # It is used to get the absolute numeric value of each element in the series. 
 
d = a.sub(b) 
d.abs() 
# It is used to get the absolute numeric value of each element in the series. 

# list 1 
a = [2, 3, 2.7, 3.2, 4.1] 

# list 2 
b = [10, 14, 12, 15, 20] 

# storing average of a 
av_a = sum(a)/len(a) 

# storing average of b 
av_b = sum(b)/len(b) 

# making series from list a 
a = pd.Series(a)

# making series from list b 
b = pd.Series(b) 

# covariance through pandas method 
covar = a.cov(b) 

# printing results 
print("Results from Pandas method: ", covar)

#practice 1
l = [23, 43, 76, 92, 42, 23, 34, 45]
m = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug']
s1 = pd.Series(l, index=m)
s1
n = [23, 32, 56, 89, 79, 12, 40, 67]
s2 = pd.Series(n, index=m)
s3 = pd.Series(n + l, index=m+m)
s3
s3 = pd.Series(n + l, index=2*m)
s3
df1 = pd.DataFrame({'month': s1, 'marks' : s2 })
df1.month = 2019
df1
df1.loc[:,'month']
df1.loc[:,'marks']
df1.rename(columns = {'month':2019,'marks':2020})








 
 