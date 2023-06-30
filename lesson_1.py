# """
# #iterable-saving more than one index
# #list()
# #imutable- unchangeable
# # #mutable-changeable
#
# #int - 1
# #float - 1.6 , 6.0
# #str - "hello" , "bwx"
# #bool - True , False
# #tupl - (1,2,3,4,5, "agajgjjsdjasf" true, [yauiuteeuisitue,seruseyu])
# #dict - {'key', value,
# # 'key2' , 'value'}
#
# set - {}
# """
#
# " " " "
#
# """
# itr
#     list
#     tuple
#     set
#     dict
# """
#
# """
# imut
#             int
#             fload
#             bool
#             tuple
#             str
#
# """
# """
# mut
#           list
#           dict
#           set
# """
#
# i = 1
# f = 2.6
# b = True
# t = (1,2,3,4,5, "gdjsjaj")
# s = "why"
# l = [ 1,2,3,3,44, "kfhdsdftstitristiutitewit"]
# d = {'a':90886}
# c = {1,2,5}
# print(i,f,b,t,s,l,d,c)
#
#
#
#
#
# print("""
# + ADD
# -SUBTRACT
# *MULTIPLY
# /DIVIDE
# """)
# num1=int(input("Enter the value 1: "))
# num2=int(input("Enter the value 2: "))
    # opr=input("enter the opr")
# if opr=="+":
#     print(num1+num2)
# elif opr=="-":
#     print(num1-num2)
# elif opr=="*":
#     print(num1*num2)
# elif opr=="**":
#     print(num1**num2)
#
# elif opr=="/":
#     print(num1/num2)
# elif opr=="√":
#     print(num1/num2)
#
# else:
#     print('not working')
#
#
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for x in numbers:
#
#   if x > 500:
#      break
#
#   elif x > 150:
#        continue
#    elif x % 5 == 0:
#       print(x)
#
# a = 'JAVA'
# print(f"my name is {a}"]
a = [2,4,5,6]

# def arithmetic(a, b, opr):
#     if opr =="+":
#       print(a + b)
# s.append(a)








import csv


reg = int(input('1. Log In'
                '\n2. Log On'
                '\n3. Log Out \n__'))

global name, email, password
while reg == 2:
    name = input('Ur name:')

    if not name.isalpha():
        print('Dont write numbers or probels')
        continue
    email = input('Ur email:')
    if '@' not in email:
        print('Email must have "@"')
        continue

    password = input('Ur password:')
    if len(password) < 6:
        print('Ur password must have more than 6 symbols!')
        continue

    card = input('Ur card:')

    if len(card) != 16 :
        print('Card must include 16 numbers, no more')
        continue
    print('User is appended successfully')

    while True:
        try:
            money = int(input('how much money u want to donate:'))
        except ValueError:
            print('Only numbers')
            continue
        break
    break






with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Password','Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)



    writer.writeheader()
    writer.writerow({f'Name':f'{name}','Password':f'{password}','Email':f'{email}'})

while reg == 1:
    in_name = input('Ur name:')
    if in_name == writer.writerow(name) :
        print('Ur email:')
    else :
        print("I don't have this kind of name in my data base"
              "\n Pls, try to write ur name same as when u registrate!")
        continue
    in_email = input('')

