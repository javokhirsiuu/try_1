import csv
import re



class MySiuushop:
    def __init__(self,email,name,password,card_number):
        self.email = email
        self.name = name
        self.password = password
        self.card_number = card_number


a = int(input("""welcome to our shop
        1)registration
        2)entering
        which one will you choose"""))

while a == 1:
    name = input("please enter your name:")
    if name.isalpha():
        print("malades you know how to write your name")

    else:
        print(" are you tupoy or something else Dont write n anything that is not letter")
        continue

    email = input('please enter your  email:')

    if "@" in email:
        print("malades you know how to write you email ")
    else:
        print("are you tupoy how you can write email without this thing")
        continue


    password = input('please enter your password:')

    if len(password) < 6:
        print("you need to write at least 6 numbers")
        continue
    elif len(password) >= 6:
        c = input("try password again")
    if c != password:
        print("100% you are tupoy you don't know how to just copy password")
        continue
    elif c == password:
        print("you password written correctly")
    if not password.isalnum():
        print("your password should be only numbers")
        continue
    else:
        print("malades you know how to write password")


    card_number = input('please enter your credit card number:')

    if len(card_number) != 16:
        print("it should be equal to 16 symbols")
        continue
    else:
        print("malades you know how to write your credit card")
        # MySiuushop.__init__(MySiuushop,email,name,password,card_number)

        money = input("please enter how much money you have")
        a1 = int(input("""from what we will start
                    1)pubg 21$
                    2)kubik rubik 70$
                    3)telefon 890$
                    4)komputer 2000$"""))

        pruducts_price1 = 21
        pruducts_price2 = 70
        pruducts_price3 = 890
        pruducts_price4 = 2000
        result1 = int(money) - int(pruducts_price1)
        result1_againpurchasing = int(result1) - int(pruducts_price2)
        result1_againpurchasing2 = result1_againpurchasing - pruducts_price3
        result = int(money) - int(pruducts_price3)
        result4 = int(money) - int(pruducts_price4)
        result3 = int(money) - int(pruducts_price2)

        if a1 == 1:
            print(f"it is pubg it's price is {pruducts_price1}$")
            c2 = input("are you buying it?:")
            if c2 == "yes":
                print("okay")
                if int(money) > int(pruducts_price1):
                    print(f'{result1}$ you have left here is your check')
                    d2 = input("thank you for purchasing do you want something else")
                    if d2 == "yes":
                        a1 = input(f"what do you want sir {name}")
                        if a1 == "3":
                            print(f"here is your check you have left this {result1_againpurchasing2}$ amount of money")
                            print("thank you for buying but now it's time to go home")
                    else:
                        print("go home")


        elif a1 == 2:
                print(f"it is kubik rubik it's price is {pruducts_price2}$")
                c2 = input("are you buying it?:")
                print(c2)

                if c2 == "yes":
                    print(f"{result3}$ you have left")
                    if a1 == 3:
                        print(f"{result1_againpurchasing2}$ here is your check we hope that we will see you again")
                        print("it's time to go home")
                else:
                    print("fuck you")


        elif a1 == 3:
                print(f"it is phone it's price is 890$")
                c2copy = input("are you buying it?:")
                print(c2copy)
                if c2copy == "yes":
                    print("okay")
                    if int(money) > int(pruducts_price3):
                        print(f'{result}$ you have left here is your check now go home and sleep there,mani botta boshimni qotirma')
                    else:
                        print("bomj you don't have money")

        elif a1 == 4:
            print(f"it is komp it's price {pruducts_price4}$")
            c2copy = input("are you buying it?:")
            print(c2copy)
            if c2copy == "yes":
                print("okay")
                if int(money) > int(pruducts_price4):
                    print(f"{result4}$ money you have left")
                    data = [name,email,password,money]

                    fieldnames = 'names2.csv'

                    with open('names2.csv', 'w', newline='') as csvfile:
                        fieldnames = ['Name', 'Password', 'Email', 'Money']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                        writer.writeheader(data)
                        writer.writerow(
                            {f'Name': f'{name}', 'Password': f'{password}', 'Email': f'{email}',
                             'Money': f'{money}'})
while a == 2:
        name_entering = input("please enter name")
        password_entering = input("please enter password")
        email_entering = input("please enter your email")
        b1 = ("please enter your name for registration")
        if not b1.isalpha():
            print("register your name correctly")
            continue
        else:
            print("your name registered succesfully")

            c1 = input("please enter your email")
            result9 = re.search("@",c1)
            if result9 == None:
                print("rewrite it")
                continue
            else:
                print("your email registered succesfully")

                d1 = input("please enter password")
                if not d1.isalnum():
                    print("write your password correctly")
                    continue
                else:
                    print("your password registered succesfully")
                    if len(d1) < 6:
                        print("at least it should be 6 symbols")
                        d1_repeat = input("try again")
                        for x in d1_repeat:
                            if x != d1:
                                print("you didn't wrote password correctly")
                                break
                            else:
                                continue
                    for x9 in b1:
                        if x9 != name_entering:
                            break
                        else:
                            print("you can continue")
                            if c1 != email_entering:
                                continue
                            else:
                                print("you can continue")
                                if d1 != password_entering:
                                    continue
                                else:
                                    print("you can continue")
                                    if x9 == name_entering and c1 == email_entering and d1 == password_entering:
                                        print("you entered succesfully")
                                    else:
                                        print("try again")
                                        continue




            while True:
                money_copy = int(input("please enter how much money you have"))
                a1_copy = int(input("""from what we will start
                            1)pubg 21$
                            2)kubik rubik 70$
                            3)telefon 890$
                            4)komputer 2000$"""))


                pruducts_price1_copy = 21
                pruducts_price2_copy = 70
                pruducts_price3_copy = 890
                pruducts_price4_copy = 2000
                result1 = int(money_copy) - int(pruducts_price1_copy)
                result1_againpurchasing_copy = int(result1) - int(pruducts_price2_copy)
                result1_againpurchasing2_copy = result1_againpurchasing_copy - pruducts_price3_copy
                result_copy = int(money_copy) - int(pruducts_price3_copy)
                result4_copy = int(money_copy) - int(pruducts_price4_copy)
                result3_copy = int(money_copy) - int(pruducts_price2_copy)

                if a1_copy == 1:
                    print(f"it is pubg it's price is {pruducts_price1_copy}$")
                    c2 = input("are you buying it?:")
                    if c2 == "yes":
                        print("okay")
                        if int(money_copy) > int(pruducts_price1_copy):
                            print(f'{result1}$ you have left here is your check')
                            d2 = input("thank you for purchasing do you want something else")
                            if d2 == "yes":
                                a1 = input(f"what do you want sir {name_entering}")

                                if a1 == "3":
                                    print(f"here is your check you have left this {result1_againpurchasing2_copy}$ amount of money")
                                    print("thank you for buying but now it's time to go home")
                            else:
                                print("go home")
                    else:
                        print("poshol von")

                elif a1_copy == 2:
                        print(f"it is kubik rubik it's price is {pruducts_price2_copy}$")
                        c2 = input("are you buying it?:")
                        print(c2)

                        if c2 == "yes":
                            print(f"{result3_copy}$ you have left")
                            if a1_copy == 3:
                                print(f"{result1_againpurchasing2_copy}$ here is your check we hope that we will see you again")
                                print("it's time to go hoe")
                        else:
                            print("fuck you")

                elif a1_copy == 3:
                        print(f"it is phone it's price is 890$")
                        c2copy = input("are you buying it?:")
                        print(c2copy)
                        if c2copy == "yes":
                            print("okay")
                            if int(money_copy) > int(pruducts_price3_copy):
                                print(f'{result_copy}$ you have left here is your check now go home and sleep there,mani botta boshimni qotirma')
                            else:
                                print("bomj you don't have money")

                elif a1_copy == 4:
                    print(f"it is komp it's price {pruducts_price4_copy}$")
                    c2copy = input("are you buying it?:")
                    print(c2copy)
                    if c2copy == "yes":
                        print("okay")
                        if int(money_copy) > int(pruducts_price4_copy):
                            print(f"{result4_copy}$ money you have left")

