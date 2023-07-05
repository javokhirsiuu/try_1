import re
import csv


with open("a.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow([login,name])


class Magazine:
    def __init__(self,money):
        self.money = money

    def get_productprice(self,productprice):
        self.productprice = productprice

print("welcome to our shop")
a = input("""
            1)entering
            2)registration
            3)out    
which  one will you choose=""")
print(a)
if a == "1":
    g = (input("please enter your name: "))
    v = (input("please enter your gmail: "))
    z = (input("please enter your password: "))
    c = input("is entering done")
    if len(z) >= 6:
        print(input("do password again"))
    elif len(z) < 6:
        print("you should have password more than 6 symbols")
        if c == "yes":
            l = input("""
                    1)pubg
                    2)phone
                    3)kubik rubik
                    4)book
                    5)ball
                    from what we will start,we have this tovars=""")
            print(l)
        if l == 1:
            m = input("pubg's price is 95$,do you have enough money")
            print(m)
        if m == "yes":
            print(f"{money} - {self.productprice}")
        else:
            print("good bye you don't have enough money")
elif a == "2":
    b = print(input("can you create account:"))
    print(b)
    if b == "yes":
        g = input("enter your name")
    v = input("enter your email")
    z = input("enter password")
elif b == "no":
    print("good bye")
elif a == "3":
    print("try again")