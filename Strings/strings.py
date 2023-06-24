print("Multiline Strings")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#in the result, the line breaks are inserted at the same position as in the code
print("\n")

print("String as an array of strings")
a = "Hello, World!"
print(a[0])
print("\n")
print("Looping through the strings")
for x in "banana":
    print(x)

print("\n")
print("String length")
b = "Hello, World!"
print(len(b))

print("\n")
print("Checking the string")
txt = "The best things in life are free!"
print("free" in txt)

print("\n")
print("checking the string is not present in the string")
txt = "The best things in life are free!"
print("expensive" not in txt)
print("\n")
print("Slicing the string")
b = "Hello, World!"
print(b[2:5])
print("Slice from the start")
b = "Hello, World!"
print(b[:5])
print("Slice from the end")
b = "Hello, World!"
print(b[2:])
print("\n")
print("Negative Indexing")
print(b[-5:-2])

print("\n")
print("-----------MODIFYING THE STRING-----------")
print("Upper case string")
a = "Hello, World!"
print(a.upper())
print("\n")
print("Lower case string")
print(a.lower())
print("\n")
print("Remove Whitespace")
print(a.strip())
print("\n")
print("Replace String")
print(a.replace("H", "J"))
print("\n")
print("Split String")
print(a.split(","))
print("\n")
print("-----------String Concatenation---------")
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print("\n")
print("Python - Format - Strings")
print("the format() method takes the passed arguments ,formats them, and places the in the string where the placeholders {} are")
print("\n")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("\n")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#can be placed in the form of the array with numbers indexed from 0
print("---Escape characters---")
print("1.Single quotes \n""2.Backlash \n""3.New line \n""4.Carriage return \n"+"5.Tab \n""6.Backspacec\n""7.form Feed\n""8.Octal value\n""9.Hex value\n")
print("\n")
print("Python - String Methods")
