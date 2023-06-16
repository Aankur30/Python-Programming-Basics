price=[("chair",200),("Table",500),("Car",2000)]
for a,b in price:
    print(a);
    print(b);#tuple unpacking 


Objects=[("chair",200),("Table",500),("Car",2000)]
def max_price(work):
    max=0;
    for x,y in Objects:
        if(max<y):
            max=y 
    return ("costly",max)    

print(max_price(Objects));