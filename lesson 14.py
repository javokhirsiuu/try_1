# def fibonnacci(c):
#     a, b = 0, 1
#     result = []
#     for _ in range(1, c):
#         x = a + b
#         a = b
#         b = x
#         result.append(b)
#     return result
#
#
# print(fibonnacci(10))
#
#
# class First:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def second(self, a, b):
#         return a + b
#
#
# # vars = Calculator(name= "First", surname="ieroew",age=12)
# #
# # print(vars.second(a=12,b=13))
# #
# # def siuuu(self,g ,c):
# #         return g + c
# # vars = Calculator(name= "First", surname="ieroew",age=12)
# # print(vars.second(g=12,c=13))
#
#
# # class Calculate:
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #
# #     def second(self):
# #         return self.x + self.y
# #
# # ss = Calculate(x=12,y=17)
# #
# # print(ss.second())
#
# # class Siuu:
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #
# #     def lakaka(self):
# #         return self.x - self.y
# #
# # ss = Siuu(x=12,y=17)
# #
# # print(ss.lakaka())
# #
# #
# # class Siuu:
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #
# #     def lak(self):
# #         return self.x * self.y
# #
# # ss = Siuu(x=72,y=11657)
# #
# # print(ss.lak())
# #
# #
# # def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #
# # def lak(self):
# #         return self.x / self.y
# #
# # ss = Siuu(x=72,y=11657)
# #
# # print(ss.lak())
#
#
# # class Calculator:
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #     def bomb(self):
# #         return self.x + self.y
# #
# #     ss = Calculator(x=13, y=18)
# #     print(ss.bomb())
#
# class Calculate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def plus(self):
#         return self.x + self.y
#
#
#     def delen(self):
#         return self.x / self.y
#
#     def minus(self):
#         return self.x - self.y
#
#     def mult(self):
#         return self.x * self.y
#
#
# x = int(input("num 1 ="))
# y = int(input("num 2 ="))
# s = Calculate(x=x, y=y)
# operation = input("operation = ")
#
# if operation == "+":
#     print(s.plus())
# elif operation == "-":
#     print(s.minus())
# elif operation == "*":
#     print(s.mult())
# else:
#      print(s.delen())
#
#
#
import math

n = 24
x = math.sqrt(n)
y = math.sqrt(n)

if x * y == n:
    print(True)
else:
    print(False)
