count=0
while count<5:
    print(count)
    count += 1
else:
    print("The value is now equal to 5")# this else is a statement not a loop it will not repeat itself

    x=[1,2,3,4,5,6,7,8,9,100]
    for a in x:
        pass
        #this is a comment cannot made even a comment

        for b in x:
            if b%10==0:
                break
            elif b%2==0:
                continue
            else:
                print(b)

print("end of the code")                 
