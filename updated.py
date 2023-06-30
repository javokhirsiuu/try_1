# import re
# import csv
#
# name = input("please enter your name:")
# email = input("please enter your email:")
# password = input("please enter password of this acc")
#
# with open("a.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file, delimiter=",")
#     writer.writerow([email,name,password])
#
# class Magazine:
#     def init(self):
#         self.name = name
#         self.email = email
#         self.passowrd = password



import re
import csv
name_entering = "java"
email_entering = "java@gmail.com"
password_entering = 121121
with open("result.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow([name_entering,email_entering,password_entering])
# name = input("please enter your name:")
a = input("""welcome to our shop
        1)entering
        2)registration
        which one will you choose""")
print(a)
if a == "1":
    name = input("please enter your name:")
    email = input('please enter your email: ')
    d = "@"
    for y in email:
        if d in y:
            print("your email is correctly written")
        else:
            break


    # email_check = email.find("@",0)


    # emailfinder = email.find("@",0)
    # for x in emailfinder:
    #     if x.find("@",0):
    #         print("you can continue")
    #     else:
    #         break
    password = input('please enter passsword')
    password_repeating = input("repeat the password")
    for x2 in password:
        if x2 == x2.isalnum():
            print("you can continue")
        else:
            break
    for x in password:
        if len(x) >= 6 and password_repeating == password:
            print("you can continue")
        else:
            break
    if name == name_entering and email == email_entering and password == password_entering:
        print(f"hello {name}")
        print("we are happy seeing you here")
    b = input(f'''from what we will start
                1)phone 1221
                2)pubg 2332
                3)kubik rubik 7777''')
    money = 700

    for x7 in b:

        if x7 == "1":
            print("it is phone it's price is 97$")
            phones_price = 97
            result = money - phones_price
            if money > phones_price:
                print(f"{result}")
                print("I hope we will you see soon")
            else:
                print("you don't have enough money")

elif x7 == "2":
    print("it is pubg it's price is 45$")
    pubgs_price = 45
            result1 = money - pubgs_price
            if money > pubgs_price:
                print(f"{result1}")
                print("I hope we will you see soon")
            else:
                print("you don't have enough money")

        elif x7 == "3":
            print("it is kubik rubik it's price is 25$")
            kubikrubiks_price = 25
            result2 = money - kubikrubiks_price
            if money > kubikrubiks_price:
                print(f"{result2}")
                print("I hope we will you see soon")
            else:
                print("you don't have enough money")
                break
        # product = input("enter products id")
        # for x3 in product:
        #     if x3 == "1221":
        #         m = ("it is phone it's price 70")
        #     elif x3 == "2332":
        #         m2 = ("it is pubg it's price 95")
        #     elif x3 == "7777":
        #         print("it is kubik rubik it is price 30 ")
        #     else:
        #         break
        elif a == "2":
            print(input("please enter you name"))
        print(input("please enter email for registration"))
        print(input("enter password for registration"))
    else:
        print("there is no option like this")
class Magazine:
    def init(self):
        self.name = name
        self.email = email
        self.passowrd = password
