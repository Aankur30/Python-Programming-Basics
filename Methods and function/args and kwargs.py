def find_sum(a,b,c=0,d=0):
    return sum((a,b))

# print(find_sum(10,20))

def sum_1(*args):
    return sum(args)

print(sum_1(1,2,3,4,5,6,7,8))


def maximum(*data):
    return max(data)

print(max(12,2,3,4,5,5,5))


def fruits(**kwargs):
    print("My favourite food is {}".format(kwargs["food"]))



fruits(fruit="Apple",drink="Cola", food="Orange")


def value_1(*args, **kwargs):
    a=sum(args)
    print("I like {} amount of {}".format(a,kwargs["fruit"]))
    #give first all the arguments related to the args first then the kwargs otherwise it will be an error

value_1(1,2,3,4,5,6,7,8,9,food="banana",fruit="orange")