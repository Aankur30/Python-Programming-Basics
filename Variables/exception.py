try:
    a,b=[int(x) for x in input("Enter two numbers : ").split(' ')]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Divison by zero happened")
    print("Please do not enter 0 in input")
finally:
    print("Code executed successfully")
            
    