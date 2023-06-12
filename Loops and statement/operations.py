a=range(0,51)
print(type(a))

#range can widely used with for loops 
for x in range(1,11):
    print("{} times".format(x))


x=["a","b","c","d","e","f"]    
count=0    
for a in x:
    print("{} :{}".format(a,count))
    count+=1

    #using the enumerate operation
print("using the enumerate operation")
y=["a","b","c","d","e"]
for a,b in enumerate(y):
        print(a)#only get the index number printed

        #using zip operation
print("using the zip operation")
a=[1,2,3,4]
b=[1,2,3,4]
c=list(zip(a,b))
print(c)#it will in the form of tuple can perform tuples unpacking 


#in method

c="a" in ["k","a","b","d","e","f","g","h","i","j","k"]
print(c)#it will give true as a output because a is present in the list can be done with numbers as well as strings also works in tuples dictionaries or lists

c="v1" in {"k1":"v1","k2":"v2","k3":"v3"}
print(callable)#gives false becaues in dictionaries only key pairs got checked 

#for checking the values we have to do 

a={"k1":"v1","k2":"v2","k3":"v3"} 
d="v1" in a.values()
print(d)#now it will give true         

#min and max values
a=[1,2,3,4,5,6,-7,8,9,10,-11,12,13,14,15,16,17]
print(min(a))      
print(max(a))

#can also work on alphabetical lists

a=["A","B","C","z","E","F","G","H","I"]
print(min(a))
print(max(a))#z is maximum because of the assci numbers

from random import shuffle #random is the main library

a=["A","B","C","z","E","F","G"]
(shuffle(a))#this shuffles the list
print(a)


from random import randint
print(randint(0,50))#gives a random random integer betweeen 0 to 49

from random import choices
print(choices(a))#it chooses a random element from the list of elements

import random
print(random.randint(0,60))#shorthand way of importing libraries