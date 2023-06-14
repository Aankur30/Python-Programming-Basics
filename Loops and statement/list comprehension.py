word="watermelon"
lis_1=[]
for x in word:
    #   lis_1.append(x)

# print(lis_1)
 lis_2=[x for x in word ]
print(lis_2)  

#using the range function
lis_3=[x for x in range(0,11)]
print(lis_3)

#operations using the list comprehension

lis_4=[]
lis_4=[x for x in range(0,10) if x%2==0]
print(lis_4)

#perfoming various operation using the list comprehension 
#all the operation are to be performed over the first variable

lis_5=[x**2 for x in range(0,11)]#printing the square of each numbers
print(lis_5)

lis_6=[]
lis_6=[x if x%2==0 else "ODD" for x in range(0,11)]
print(lis_6)