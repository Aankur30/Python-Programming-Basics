class student:
    def __init__(self):
        self.name="Ankur"
        self.age=23
        self.cgpa=7.9
    def talk(self):
        print("Your name is " + self.name)
        print("Your age is " , self.age)
        print("Your cgpa is ",self.cgpa)

s1=student()
s1.talk()   
print(id(s1)) #this gives the address of the object

class student2:
    def __init__(self,n=' ',m=0):
        self.name=n
        self.marks=m
    def display(self):
        print("Hi "+self.name)
        print("Your marks ", self.marks)


s=student2()
s.display()
print("\nUsing paramerterized constructor\n")
s2=student2("Ankur",30)
s2.display()


                #class variable and instance variables
class sample:
    x=10
    @classmethod  #this is a  decorator
    def modify(cls):#with cls we have to put the decorator othewise without decorator we should call it with class name directly
        cls.x+=1#we have to put the class name or cls if decorator is provided

print("Example of class variable")
s1=sample()
s2=sample()
print("The value of x in s1 ",s1.x)
print("The value of x in s2 ",s2.x)  
#modify x in s1
s1.modify()
print("The value of x in s1 ",s1.x)
print("The value of x in s2 ",s2.x)
#with cls it gives this value as 10 not 11
print("the value of x in class is",sample.x)#class variable can be accessed using class name this is also called class namespace variable


class marks:
    n=10
    #access class var in the s1 instance namespace
    
s1=marks()
print(s1.n)
s1.n+=1# hence it is modified in an instance only not in whole class so for other instances the value of n remains the same
print(s1.n)
s2=marks()
print(s2.n)                      


class money:
    
    def __init__(self):
        self. name="Ankur"
        self.marks=23
    #mutator method
    def setName(self, name):
        self.name = name
    #accessor method
    def getName(self):
        return self.name

n=int(input("Enter the number of students "))
i=0
while i<n:
    s=money()
    name=input("Enter the name ")
    s.setName(name)
    print("hi "+s.getName())  
    i+=1          
        