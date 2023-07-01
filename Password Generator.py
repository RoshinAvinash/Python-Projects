import random
import string

while True:     
    l = input("Enter the number of Lowercase letter's you want in your password (Can be from 0 to 26 including ): ")
    if  l.isdigit():
        l = int(l)
        if 24 >= l  >= 0:
            print("")
            break
        else:
            print("Wrong input, may be out of range, Please type again")
    else:
        print("Wrong input, Please type again")    

while True:
    u = input("Enter the number of Uppercase letter's you want in your password (Can be from 0 to 26 including): ")
    if  u.isdigit():
        u = int(u)
        if 24 >= u  >= 0:
            print("")
            break
        else:
            print("Wrong input, may be out of range, Please type again")
    else:
        print("Wrong input, Please type again")

while True:
    d = input("Enter the number of Digit's you want in your password (Can be from 0 to 10 including): ")
    if  d.isdigit():
        d = int(d)
        if 10 >= d  >= 0:
            print("")
            break
        else:
            print("Wrong input, may be out of range, Please type again")
    else:
        print("Wrong input, Please type again")

while True:
    s = input("Enter the number of Symbol's you want in your password (Can be from 0 to 32 including ): ")
    if  s.isdigit():
        s = int(s)
        if 32 >= s  >= 0:
            print("")
            break
        else:
            print("Wrong input, may be out of range, Please type again")
    else:
        print("Wrong input, Please type again")

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation     

a = "".join(random.sample(lowercase,l))
b = "".join(random.sample(uppercase,u))
c = "".join(random.sample(digits,d))
d = "". join(random.sample(symbols,s))

x = a+b+c+d

password = "".join(random.sample(x, len(x)))

print(f"The password is {password}")