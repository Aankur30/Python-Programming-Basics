# python has the following data types in by default in these categories:

# 1.Text Type: str
# 2.Numerica Types:int,float,complex
# 3.Sequence types:list,tuple,range
# 4.Mapping types:dict
# 5.Set Types: set,frozenset
# 6.Boolean type:bool
# 7.Binary Types:bytes,bytearry,memoryview
# 8.None Type:noneType


x = "Hello World"
print(x)
print(type(x)) 
print("\n")

y = 1j
print(y)
print(type(y)) 
print("\n")

print("Set Data Type ")
z = {"apple", "banana", "cherry"}
print(z)
print(type(z)) 
print("\n")

print("FrozenSet Data Type ")
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 
print("\n")

print("Type conversions")
x=1;
print("convert from int to float")
a=float(x)
print(a)
print("Convert from int to complex number")
a=complex(x)
print(a)
print("WARNING: you cannot convert complex numbers into another number type")


import random
print("Random number generator...")
print(random.randrange(1,11))


