#Steps to draw a Line Plot: 
1. Import pyplot from matplotlib as plt using the following statement 
import matplotlib.pyplot as plt 

2. Plot y versus x as lines and / or markers 

plt.plot(x, y, color, others)  

3. Set the x–axis label for the current axis 
plt.xlabel("Required Text") 

4. Set the y–axis label for the current axis 
plt.ylabel("Required Text") 

5. Set a title for the current axes 
plt.title("Required Title") 

6. Display the plot 
plt.show( ) 

#Example :
import matplotlib.pyplot as plt 
def petrolrate_lineplot( ): 
price=[65.5,68.3,75.2,66.8,70,72.5,73] 
day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"] 
plt.plot(day,price) 
plt.xlabel("Day") 
lt.ylabel("Petrol Price") 
plt.title("Petrol Rate Inflammation in a Week") 
plt.show( ) 

#Example : 
import matplotlib.pyplot as plt 
x1=[1,2,3] 
y1=[5,7,4] 
plt.plot(x1,y1,label='First Line') 
x2=[1,2,3] 
y2=[10,11,14] 
plt.plot(x2,y2,label='Second Line') 
plt.xlabel('Plot Number') 
plt.ylabel('Important Variables') 
plt.title('New Graph') 
plt.legend( ) 
plt.show( ) 
❖ The function legend( ) is used to generate legends in line graphs to explain the function or the values  underlying the different lines of graph 
Plot:
 
Jawahar Navodaya Vidyalaya, Chittoor 4 
Plotting for data generated using NumPy: 
a) arange( ): This function creates a numeric sequence with equally spaced numeric values with in an interval. The  syntax of the function is 
np.arange([start,]stop[,step,][dtype]) 
∙ The start parameter indicates the beginning value of the range, and is optional and the default value is 0 ∙ The stop parameter indicates the end of the range. The value specified for stop will not be included in  the range 
∙ The step parameter specifies the spacing between values in the sequence, It is optional and the default  step value is 1 
∙ The dtype parameter specifies the data type  
Example: >>> a1=np.arange(6) 
>>> a1 
array([0, 1, 2, 3, 4, 5]) 
>>> a2=np.arange(–2, 24, 4) 
>>> a2 
array([–2, 2, 6, 10, 14, 18, 22]) 
b) linspace( ): This function is used to create an array having evenly spaced elements. Evenly spaced elements  means the difference between successive elements will be same 
Example: >>> a1=np.linspace(2.5,5,6) 
>>> a1 
array([2.5, 3. , 3.5, 4. , 4.5, 5. ]) 
>>> a2=np.linspace(3,10,2) 
>>> a2 
array([ 3., 10.]) 
>>> a3=np.linspace(2,10,5) 
>>> a3 
array([ 2., 4., 6., 8., 10.]) 
c) Some useful NumPy functions while plotting data are as below 
Trigonometric Functions  
sin(x) 
cos(x) 
tan(x) 
arcsin(x) 
arccos(x) 
arctan(x) 
Hyperbolic Functions sinh(x) 
cosh(x) 
tanh(x) 
arcsinh(x) 
arccosh(x) 
arctanh(x) 
Rounding Functions round(a, decimals,  out) 
floor(x) 
ceil(x) 
trunc(x) 
Trigonometric sine, element–wise 
Cosine element–wise 
Computes tangent element–wise 
Inverse sine, element–wise 
Trigonometric Inverse Cosine, element–wise Trigonometric Inverse Tangent, element–wise 
Hyperbolic sine, element–wise 
Hyperbolic cosine, element–wise 
Computes hyperbolic tangene, element–wise Inverse hyperbolic sine, element–wise 
Inverse hyperbolic cosine, element–wise Inverse hyperbolic tangent, element–wise 
Round an array to the given number of decimals Return the floor of the input, element–wise Return the ceiling of the input, element–wise Return the truncated value of the input, element–wise  
Exponents and Logarithms  
exp(x) exp2(x) log(x) 
log10(x) log2(x) log1p(x) 
Calculate the exponential of all elements in the input array Calculate 2**p for all p in the input array 
Natural logarithm element–wise 
Return the base 10 logarithm of the input array, element–wise Base–2 logarithm of x 
Return the natural logarithm of one plus the input array, element–wise 
Jawahar Navodaya Vidyalaya, Chittoor 5 
Changing Line Colors, Line Width and Line Styles:  
❖ Changing Line Color: The colors that can be applied in plot are blue, cyan, green, black, magenta, red,  white, yellow. Instead of providing full name of color the following abbreviations can be used to specify  colors. Python allows other valid colors also, apart from the listed colors 
Color Abbreviation Color Name Color Abbreviation Color Name 
b blue m magenta 
c cyan r red 
g green w white 
k black y yellow 
When multiple views are generated in a single plot, python automatically displays the views in different  colors 
❖ Changing Line Width: The linewidth attribute can be provided to set required line width Linewidth = <in points> 
❖ Changing Line Style: The line styles can be changed as per the need of the user. Matplotlib allows  different line styles. The available line styles are, 
Style Abbreviation Style 
– Solid Line 
– – Dashed Line 
– . Dash Dot Line 
: Dotted Line 
To generate color along with style, the color abbreviation along with style abbreviation is to be used. In  this case, the color code only to be used and full color name must not be used. For example, to generate  red dotted line the code “r:” can be used. 
Changing Marker Type, Size and Color: To change marker type, its size and color the following additional  arguments can be provided in the plot( ) function 
marker = <valid marker type> 
markersize = <in points> 
markeredgecolor = <valid color> 
Valid marker types for plotting are, 
Marker Description Marker Description Marker Description ∙ Point Marker p Pentagon Marker ∨ Triangle_Down Marker , Pixel Marker * Star Marker ∧ Triangle_Up Marker o Circle Marker h Hexagon1 Marker < Triangle_Left Marker + Plus Marker H Hexagon2 Marker > Triangle_Right Marker x x Marker 1 Tri_Down Marker | Vertical Line Marker D Diamond Marker 2 Tri_Up Marker _ Horizontal Line Marker d Thin_Diamond Marker 3 Tri_Left Marker 
s Square Marker 4 Tri_Right Marker 
Example Program: The table shows the daily sales of three different cool drinks in a week. Day Sun Mon Tues Wed Thurs Fri Sat 
ThumsUp 330 300 450 150 400 650 425 
Maaza 515 400 500 350 300 500 375 
Bindu 450 560 610 505 490 500 415 
#Program to draw line chart for sales of three different cool drinks in a week 
import matplotlib.pyplot as plt 
def sales_lineplot( ): 
 days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'] 
 thumsup=[330,300,450,150,400,650,425] 
 maaza=[515,400,500,350,300,500,375] 
 bindu=[450,560,610,505,490,500,415] 
 plt.plot(days,thumsup,"b--",label='ThumsUp',marker="o") 
 plt.plot(days,maaza,"g-.",label='Maaza',marker="h") 
 plt.plot(days,bindu,"r:",label="Bindu",marker="*") 
 plt.xlabel("Day") 
 plt.ylabel("Quantity Sold") 
 plt.title("Cool Drink Sales in a Week") 
 plt.legend( ) 
 plt.show( )
Jawahar Navodaya Vidyalaya, Chittoor 6  
Multiple Views: To plot two lines in two different views of the same window, the subplot( ) function is to be  used 
Example Program: 
import matplotlib.pyplot as plt 
import numpy as np 
x=np.arange(0,20,2) 
y1=np.linspace(1,10,10) 
y2=np.linspace(5,14,10) 
plt.subplot(2,1,1) 
plt.plot(x,y1) 
plt.xlabel('Item(s)') 
plt.ylabel('Value(s)') 
plt.title('First Chart') 
plt.grid(True) 
plt.subplots_adjust(hspace=0.8, wspace=0.2) 
plt.subplot(2,1,2) 
plt.plot(x,y2) 
plt.xlabel('Item(s)') 
plt.ylabel('Value(s)') 
plt.title('\n\n\nSecond Chart') 
plt.show( ) 
❖ The grid( ) function generates a grid in the graph area 
❖ The subplot( ) function takes three arguments and its syntax is subplot(nrows, ncols, index) where arguments  specifies number of rows, number of columns and row / column number respectively. 
❖ The method subplots_adjust( ) is used for providing horizontal spaces (hspace) and width–wise spaces (wspace)  between two subplots so that their respective titles or any other subcomponents don’t overlap or collide with  each other. 
Plot:
 
