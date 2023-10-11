import array as arr
a=arr.array('i',[1,2,3,4])
lenght=len(a)
for i in range (0,):
    print(a[i],end=" ")
print("\n")    


    
import numpy  as np  #we can give the alias of numpy as np instead
arr = np.array([1, 2, 3])
print("1 Dimension array: \n",arr)
print("\n")

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("2 Dimensional Array: \n", arr)
print("\n")

#making multi-dimensional arrays
arr1= np.array([[-1, 2, 0, 4],#5
                [4, -0.5, 6, 0],#9.5
                [2.6, 0, 7, 8],#17.6
                [3, -7, 4, 2.0]])#2
print("Initial Array: ")
print(arr1)
print ("Sum of all array elements: ", arr.sum())#can use sum() to sum all the elements of the array

arr2 = np.array([[-1, 2, 0, 4],#5
                [4, -0.5, 6, 0],#9.5
                [2.6, 0, 7, 8],#17.6
                [3, -7, 4, 2.0]])#2
print(arr1+arr2)#can add two arrays directly 

 #Multiplication of two lists
list1 = [1, 2, 3, 4 ,5, 6]
list2 = [10, 9, 8, 7, 6, 5]
# Multiplying both lists directly would give an error.Hence convert them into numpy array
# print(list1*list2)

a=np.array(list1)
b=np.array(list2)
print(a*b)


# Using the arrange function of numpy
a = np.arange(10, 1, -2)
print("\n A sequential array with a negative step: \n",a)
 
# Indexes are specified inside the np.array method.
newarr = a[np.array([3, 1, 2 ])]#we can find the index of any given array
print("\n Elements at these indices are:\n",newarr)

# NumPy array with elements from 1 to 9
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Index values can be negative.
arr = x[np.array([1, 3, -3])]#if the index is negative it counts from backwards with 1-indexed array for negative
print("\n Elements are : \n",arr)


# Arrange elements from 0 to 19
newarray= np.arange(20)
print("\n Array is:\n ",newarray)
 
# a[start:stop:step]
print("\n newarray[-8:17:1] = ",newarray[-8:17:1])
 
# The : operator means all elements till the end.
print("\n a[10:] = ",newarray[10:])

data1=[2,6,5,7]
data2=[1,5,4,6]
new_data1=np.array(data1)
new_data2=np.array(data2)
c=(new_data1>new_data2)

print(c)