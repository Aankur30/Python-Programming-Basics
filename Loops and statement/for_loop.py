nums=[1,3,5,7,9];
for values in nums:
    print(values);
    
  
lis_2 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for x in lis_2:
   if(x%2==0):
       print(x);   
   else:
       print("odd number ={}".format(x));   


lis_3=[1,2,3,4,5,6,7,8,9];
lis_sum=0;
for x in lis_3:
    lis_sum+=x;
    print(lis_sum);

#using loop with strings
x="Hello world!";
for y in x:
    print(y);   
    #what happenps if we put x instead of y
    for y in x:
        print(x);


lis_1=[(1,2,3),(1,2,3),(1,2,3)]
for x in lis_1:
    print(x);
    #we want to print each element separately then what to do
#tuples unpacking
    for a,b,c in lis_1:
        print(b)

        
dic_1={"k2":1,"k3":2,"k4":3,"k5":5};
for x in dic_1:
    print(x);#it will only print the keys not the values for the values 

    #for values you have to do

    for i in dic_1.items():#items will give you dictionary values in tuples
        print(i);       

    for x in range(1,51):
         if(x%5==0 and x%3==0) :
            print("fizzbuzz");
         elif(x%3==0):
             print("fizz")
         elif(x%5==0):
             print("buzz")
         else:
             print(x);
     
            