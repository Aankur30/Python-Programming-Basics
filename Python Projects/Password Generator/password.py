import string 
import random
from csv import writer


def password_generator():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    # s4=string.punctuation
    pass_length=int(input("Enter the length of the password: "))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    # s.extend(list(s4))
    random.shuffle(s)
    password=("".join(s[0:pass_length]))
    print(password)

#can also add special characters to the password 
password_generator()