print("Hello world!!")
# same as the above output-single line comment
print('Hello world!!')

''' this is the multi line comment
this is the second line of the multi line comment
this is the third line of the multi line comment'''

# ---------------------------------------------------------------------------------------------------

#USING THE ESCAPE SEQUENCE 
# using the escape sequences \n
print("this is the first statement \nthis is the second statement \nthis is the third statement")

# using the escape sequences \t
print("this is the first statement\tthis is the second statement\tthis is the third statement")

# using the escape sequences \b-provide backspace in the  print statement it will delete one character space from the behind
print("this is the first statement \bthis is the  second statement \bthis is the third statement")

#-------------------------------------------------------------------------------------------------------

#USING THE LEN FUNCTIONS 
a="this is a string"
print(len(a))
# length contains the length of the string it also included the gap between the string 
# can also deduce the type
print(type(a))
b= "in the python"

#-------------------------------------------------------------------------------------------------------


#CONCATENATION
c=a+" "+b
print(c)
# this will concatenate the string using the add operator

#-------------------------------------------------------------------------------------------------------


# INDEXING
val="Hello World"
print(val[0])
# in negative indexing it will start from the backwards position then either in negative indexing or in positive 0th position will be fixed
print(val[-1])

#-------------------------------------------------------------------------------------------------------


# SLICING
print(val[2:7])#this will print the string from 2nd position to the 6th position
print(val[-7:-2])
# using th thrid value in the slicing 
print(val[1:7:2])#its syntax is a[starting index:ending index:step size] the output is el(and space which is invisible)
# if the step size is n then it will skip n-1 letters and print the 

#-------------------------------------------------------------------------------------------------------
#STRING PROPERTIES AND METHODS
val="Taj MAhal"
# val[0]='R' this will give an error as the string are immutable and can be reassigned
print(val)
# we can do slicing to get the desired result
var2='R'+val[1:]
print(var2)
# we get the desired result as Raj MAhal
# we can not do reassignment  but can append the given string
val+=" "+val+" "+var2
print(val)
hello="h1"
print(hello*10)# this will print the statement 10 times

#-------------------------------------------------------------------------------------------------------
# BUILT IN FUNCTION IN THE PYTHON

x="this is a built in function in the Python Programming Language"

print(x.capitalize())# capitalize the first letter of the sentence
'''
other useful functions are 
.upper() -to convert a string into upper case same as there is .lower() to convert a string into lower case
but it didn't change the string 
'''
print(x.split())# this will convert the string into the list seperating every string 
# if we put some character in the string function box it will split the string whenever it encounters that character

#-------------------------------------------------------------------------------------------------------

# STRING PROPERTIES AND FUNCTIONS
# .FORMAT
print("this is a {}".format("cat"))
# a="this is a boy"
# print(a.format(" which is very handsome")) this will not give the desired results like this is a boy which is very handsome
# but we can do this
a="which is very handsome"
print("this is a boy {}".format(a))#this will  give the desired results like this is a boy which is very handsome
print("this is a {} {} {}".format("furry","little","cat"))
print("this is a {1} {0} {2}".format("little","furry","cat"))
# can not fill it automatically the last value if you have to give value give it to every one otherwise don't give to anyone of them
print("this is a {f} {l} {c}".format(c="cat",f="furry",l="little"))  #gives the same output as above+-

#FLOAT FORMATTING METHOD
ans=22/7
print(ans) #this will give the  most precise value
print("the answer is {a:1.5f}".format(a=ans))# here the answer is assigned in a and the 1 is the tabspace and the 5 is the precision digits 

#FSTRING METHOS
c="cat"
print(f"this is a {c}")