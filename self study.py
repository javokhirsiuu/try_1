# s = []
#
# for x in range(1,21):
#     for j in range(1,51):
#           s.append((x,j))
# print(s)
#
#
# s1 = []
# for i in range(-11,12):
#     if i > 0:
#         s.append(i ** 2)
#     else:
#         s.append(i ** 3)
# print(s1)
#
#
# s2 = [1,2,3,1,2,4,5]
# set_set = {i for i in s }
# print(set_set)
# dicct = {i: i **10 for i in s2}
# print(dicct)
#
# import builtins
# print(dir(builtins))
#
# y = 3
# def degree(x):
#     return y ** x
#
# print(degree(5))
#
#
# # def message(number):
# #     def print_message():
# #         return 'Num' + str(number)
# #
#
#
#
#
#
#
#
# class Car():
#     def __init__(self, model, power):
#         self.power = power
#         self.model = model
#         def car(self):
#             print("jestkaya maxina " + self.power + "krutaya maxina" + self.model)
# car1 = ['bmw',247]
#
# def distance_between_points(a, b):
#     return 0
#
#
# def simple_multiplication(number):
#
#
#     for x in number:
#
#         if x % 2 == 0:
#             pass
#
#         else:
#             print(x * 9)
#
#
#
# def likes(names):
#     for i in names:
#         if names == ["James","Largus"]:
#             print("James" + "")
#
# class Hero(object):
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#     def Hero(self):
#         print("" + self.name + "" + self.age)


import csv
#
# name = "Rasul"
# lname = "abdi"
#
# with open("data.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file, delimiter=",")
#     writer.writerow([name,lname])
name = "Siu"
pname = "ms"

with open(".csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow([name,pname])