#many values to many variables
print("Many values to many variables")
x,y,z=12,13,14
print(x)
print(y)
print(z)
#make sure the number of variables matches the number of values or else you will get an error

#One value to multiple variables
print("One value to multiple variables")
x=y=z=34
print(x)
print(y)
print(z)

print("Unpacking a collection of variables")
fruits=["Apple","Banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
print("\n")
#The global keyword 
print("Global keyword of the variables")
def myfunc():
    global x
    x="fantastic"

myfunc()

print(x)