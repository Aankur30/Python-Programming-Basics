print("hello world")

#formmatted print function
# a=int(input("Enter the first number "))
# b=int(input("Enter the second number "))
# sum=a+b
# print("the sum of two numbers is %i" %sum)

#alignment of the numbers
var="this is the sum"
print("hello %+100s"%var)#right alignment


#roots of the quadratic equation
import math

# a=int(input("Enter the coefficient of x**2 = "))
# b=int(input("Enter the coefficient of x = "))
# c=int(input("Enter the coefficient of constant = "))
# if(b**2-4*a*c==0):
#     result=-b/a;
# if((b**2-4*a*c)>0):
#     result1=int((-b+math.sqrt(b**2-(4*a*c)))/2*a)
#     print("The first root of the quadratic equation is result1 %i"%result1)
#     result2=int((-b-math.sqrt(b**2-(4*a*c)))/2*a)
#     print("The second root of the quadratic equation is %i" %result2) 
# if((b**2-(4*a*c))<0):
#     print("the rooots of the quadratic equation is imaginary")



    #the year is leap year or not
# year=int(input("Enter the year "))
# if(year%4==0 and year%100!=0):
#     print("%i is a leap year"%year)
# elif(year%400==0):
#     print("%i is a leap year"%year) 
# else:
#     print("%i is not a leap year"%year)  



    #printing the star patttern
# rows=int(input("Enter the number or rows "))
# # columns=int(input("Enter the number or columns "))
# for i in range(rows,1):
#     j=i-1
#     while j>0:
#         print(" ")
#         j=j-1
#     for k in range(0,rows-i+1):
#         print("*")

# #printing in the same line
# for i in (1, 2, 3):
#     print(str(i), end=' ')

# arr=[10,20,30,40,50,60,70,80]
# byt=bytes(arr)
# print(byt)

# lis_1=["a",1,3,4,0.8]
# lis_1.append(45)
# print(lis_1)
# num=int(input("Enter the number you want to print the table = "))
# x=1
# while(x<=10):
#     product=int(x*num)
#     print(num, "x",x, "=",product)
#     x=x+1
    
#printing the star pattern 
sum=0
for i in range(1,101):
    sum=sum+i
print("the sum of the 100 numbes is",sum)    

             