# 1)Что такое PVM (python virtual machine)?
# pvm = это вещь котороя переводит байт код в машинный код
# 2)Напиши список базовых переменных в питоне,их описание и отличие друг от друга
# tuple,list,set,dict,float,integer,string,bool они изменяемые и не изменяемые
#       mut                 # imut
#           bool                    int
#              set                 fload
#                 list              tuple
#                  dict             str
# 3)Изменяемые объекты имеют поля, которые могут быть изменены, неизменяемые объекты не имеют полей, которые могут быть изменены после создания объекта.
#  mutable  и imutable  во 2 вопросе я написал
# 4) 2 типа f" и format
# 5)in используется для проверки наличия значения в последовательности,is используется для проверки, ссылаются ли две переменные на один и тот
# пример на in и is
# su = ["apple", "banana", "cherry"]
#
# if "banana" in su:
#   print("lakaka")
# x = ["apple", "banana", "cherry"]
# y = x
# print(x is y)
# 6) локальный и глобальный
# 7)если там нету  return он возвращает None
# 1)Создать функцию, которая возвращает длину наименьшей строки
# ?
# 2)Написать функцию, которая принимает число (функция должна работать для чисел от 0 до 99) и возвращает её как строку на английском
# Пример:  name_that_number(4)   # returns "four"
# name_that_number(19)  # returns "nineteen"
# name_that_number(99)  # returns "ninety nine"
numbers =[]
# for i in range(99):
#     if i == numbers +1:
#         print(f"name_that_number(i)")
# 3) l = "you got fire"
#  x = l.split()
#  print(x)
# 4)names = []
# for i in range(10):
#     names.append(i + 4)
# if i == 7:
#     names.pop(0)
siu = ['John','cena','java','script']
names = input("Enter name 1:")
if names is siu:
     print("John")
else:
    print(-1)
