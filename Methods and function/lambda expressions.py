#the function can be used only once in the program called lambda expression

def square(a):
    return a**2

print(square(2))
print("\n")

vals=[1,2,3,4,5,6,7,8,9]
map(square,vals)

for x in map(square,vals):#no need to put the paranthesis infront of the square function
    print(x)

    #filter function

def even(a):
    return a%2==0;

eve=[1,2,3,4,5,6,7,8,9]

lis_1=list(filter(even,eve))#only gives the answer which holds the condition true

print(lis_1)

#lambda function

def square_2(a):
    return a**2

square_1=lambda a:a**3

for x in map(square_1,vals):
      print(x)