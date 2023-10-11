a=pow(13,11,17)
print(a)# it gives the value (13^11)%17 this is the for of this pow hence gives 4 as output

import math
a=math.fabs(-12.5)#gives the absolute value using math module
print(a)
b=complex(12,10)#this is not present in any module
print(b)

import numpy as np
y=np.conjugate(b)#this is present in numpy module
print(y)


a,b,c=11,12.3,True;
print(a,b,c)
c=a*b
print(repr(c))#converts the object to the string 

#without using format specifier in the print statement
print("the value of "+repr(a)+" and the value of b is "+repr(b)+ " gives the product c " +repr(c))#can be helpful while priniting

