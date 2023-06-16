#three cup and ball game

my_list=[1,2,3,4,5,6,7,8,9]

from random import shuffle


def shuffle_list(my_list):
    from random import shuffle
    shuffle(my_list)
    return my_list

lis_2=shuffle_list(my_list);

def guess():
    guess=""
    while True:
        guess= input("What is your guess (0,1,2): ")
        if guess not in ["1","2","0"]:
            print("Please enter a valid input ")
            pass 
        else:
            break
        return int(guess)

def check(my_list,guess):
    if my_list[guess]=='o':
        print("Right answer you won !!!")
    else:
        print("Wrong answer \n Better luck next time!!")
        print(my_list)

check(my_list,guess)        

    