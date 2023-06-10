x=3;
if(x>10):
    print("The value of x is greater than 10");
elif(x<2):
    print("the value of x is too small");
elif(x<5):
    print("X might be 3");
else:
    print("this is the else statement");

#nested if statements
x=int(input("Enter the number between 0 and 20 : "))
if(x<20):
      if(x<=10):
          print("The number is less than or equal to 10");
      elif(x<=10 and x<=20):
          print("The number is greater than 10");
      else:
          print("The number is mysterious");
else:
    print("This is the outer else statement glad you make it here :");          