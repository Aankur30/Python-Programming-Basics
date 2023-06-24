#INDEXING AND SLICING IN THE LIST
list_1=["Cat",24,0.634,[2,"Air",["last str",23,343.4]]]

#indexing
print(list_1[2]) #this is the second element of the main list
print(list_1[3][1]) #this is the 2nd subpart of the 4th element of the main list
print(list_1[3][2]) #this is the 3rd subpart of the 4th element of the main list
print(list_1[3][2][0]) #this is the 0th part of the  3rd subpart of the 4th element of the main list

# SLICINNG
print(list_1[2:])

#METHODS ASSOC WIHT LISTS
b=[1,2,3,4,5,6]
# print(b.append(7)) this is not printing the desried result
b.append(7)
print(b)#this will print the desired result and gives the modified list not the copy 
b.insert(7,8)
print(b) #this takes two arguments where to insert and what to insert
c=[1,3,4,4]
c.clear()
print(c) #it clears the whole list gives the modified list
c.append(1)
print(c) 
a=c.pop() #returned the poped value from the end of the list
print(a) 
d=[4,3,2,1]

# print(d.reverse()) this will not work 
d.reverse()
print(d) #reverse the whole list
e=[3,7,5,1,2,8,9,3,4,5,57,3,5,7,8,1]
e.sort()
print(e) #gives the sorted list
print(len(e)) #gets the length and this will work also

#theory of the list
#1. list is ordered
#2. list is changeable it allows duplicates
#3. list can have mixed data types
#4. list can be constructed with the help of the list constructor like list(("apple","banana"))
# 5. can use del keyword for deleting the list

#we cannot copy the list simply by typing list2=list1 because list2 will only be a reference to list1 and change made in list1 will automatically also be made in list2

