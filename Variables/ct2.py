def sum(a,b):#defining the function 
    '''This function returns the sum of two numbers'''#this is called as docstring it gives the information about the function contains only one line
    return a+b
# group of statements that function contains called as suite 

print(sum(2,3))#calling the function

def fact(n):
    prod=1;
    while n!=1:
        prod=prod*n
        n=n-1
    return prod    

for i in range(1,11):
    print("the factorial of the {} is {}".format(i, fact(i)))
    

def Isprime(n):
    
    x=1
    for i in range(2,int(n/2)+1):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x    

#all prime numbers in range
# num=int(input("Enter the number of prime numbers "))
# j=2
# c=1
# while c<=num:
#     if(Isprime(j)):
#         print(j)
#         c+=1
#     j+=1
       


def operations(a,b):
    c=a+b
    d=a-b
    return (c,d) #return the value in the form of tuple   

x=operations(2,4)
print(x)#x become tuple and stores the value

def display(str):
    return "Hai "+str

x=display("krishna")#can make function equal to an variable
print(x)

#nested functions
def display(str):
    def message():
        return "How are you? "
    return message()+ str

x=display("Ankur")#assigning even the nested function to a variable and it works
print(x)

#passing function as the parameters
def displayNew(fun):
    return "Hello" +fun

def messageNew():
    return "Ankur"

x=display(messageNew())
print(x)

x=10
print(id(x))#gives the address of the variable 

def modify(x):
    x=15#this only works with immutable objects like integers float and tuples 
    #does not work with list
    print(x,id(x))


x=10
y=modify(x)
print(y)  #this gives none 
print(x,id(x))

#Arguments of a fumction
#positional arguments
def attac(s1,s2):
    '''To join s1 and s2 and display the value'''
    s3=s1+s2
    print("Total string "+s3)

attac("New","york")

#keyword arguments
def grocery(item, price):
    '''to displayt eh given argument'''
    print('Item is  %s' % item)
    print('Price is %.2f' % price)

grocery(item='sugar', price=50.57)
grocery(price=50.77,item='sugar')

#variable length arguments
def add(farg,*args):
    '''to add given variable'''
    print('fomal arguments:', farg)
    sum=0
    for i in args:
        sum+=i
    print("the sum of all the arguments:", sum)

add(1,7,8,9,10,11,12,13,14,15,16)
add(1,9,10,11,12,13,14,15,16)
#keyword variable arguments

def display(farg,**kwargs):
    '''to display the arguments'''
    print("formal arguments is = ",farg)

    for x,y in kwargs.items():
        print('key is ={} and value is ={}'.format(x,y))

display(5,rno=10)
display(5,rno=10,name="ankur")

#global variable
a=1
def myfunction():
    b=2
    print("b=", b)
    print("a=", a)

myfunction()

b=1
def myfunction2():
    
    c=globals()['a']#can access using the global function
    print("c=", c)
    b=2 # should be used after the global variable
    print("b=", b)


myfunction2()

#lambda function

y=lambda x:x*x;
print(y(5))