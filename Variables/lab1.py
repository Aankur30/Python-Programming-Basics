#lamda function
y=lambda X:X*X
print(y(4))

#lamda using multiple arguments
z=lambda a,b:a*b
print(z(2,3))

class Student:
    name="Ankur"
    age=21

    def __init__(self):
        name="Satish"
        age=23
        print("name is ",name)
        print("age is ",age)
    def __init__(self,name, company):
        self.name=name
        self.company=company
    def show(self):
        print("Hello my name is "+ self.name+ "and I work in "+ self.company + ".")        
    def display(self):
        print("name is ",self.name) 
        print("age is ",self.age)   
Student1=Student("Ankur","amazon")
Student1.display()
Student2=Student("Ankur Verma ","Google")
Student2.show()


class Dog:
    animal="dog"

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

Rodger=Dog("Pug","brown")
Buzo=Dog("Bulldog","black")

print("Rodger details")
print("Rodger is a", Rodger.animal)
print("class name is ",Dog.animal)
print("Breed is ",Rodger.breed)

#class variables can be accessed using name also
print("\n Buzo Details")
print(" Buzo is a ", Buzo.animal)
print("Breed is ",Buzo.breed)
print("color is ",Buzo.color)
print("class name is ",Dog.animal)

class Man:
    __y="Man"

    def __init__(self):
        print("This is the constructor")

    def display(self):
        print(self.__y)

m1=Man()
m1.display()
# print("this is the class variable", m1.__y)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
del p1
print(p1)

