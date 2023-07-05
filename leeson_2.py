
# BMW = {"M5":[34653653,"RTITIIW"],
# #        "R8":[3758759,"EXPENSIVE CAR"],
# #        # "I8":[37842647,"WGQGDJQ"],
# #        "R7":[2276486428,"HAAFHAG"],
# #        "R5":[282542849,"IUII"],
# #        "X5":[1767846,"RRGJGRJGR"],
# #
# # }
# # name = input('enter value 1')
# #
# # if name  in BMW:
# #        print(BMW[name])





# BOOKS = {"HARY POTER":[70008888,"PAGES"],
#       "YOUTUBE" : [1000000000,"FOLLOWERS"],
#       "FACEBOOK" : [10030303003030, "HATERS"],
#       "INSTEGRAM" : [3107371237938, "I HATE IT"],
#       "SIGMA" : [2789137987397, "SUBSCRIBERS"],
#       "CARTOONS" : [32383471764, "SJHFGJGJD"],}
# name = input('enter value 1')
#
# if name in BOOKS:
#  print(BOOKS[name])







# GM = {
#       "Lacetti": 1000,
#        "malibu" : 2000,
#         "nexia" : 750,
#
#
#
#       }
# name = input('enter value 1')
#
# if name in GM:
#     print(GM[name])
#


# name = input("enter your name ")
# surname = input("enter your surname")
# password = input("enter your password")
#
# if name =="killer" and surname == "script" and password == "tse123456":
#       print('well')
# else:
#       print("looserrr")
















# fruits = ['cherry' , 'banana']
# fruits.append('orange')
# print(fruits)

# fruits = ['cherry', 'banana', 'orange']
# fruits.clear()
# print(fruits)

# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# txt = "Hi welcome to my garden."
#
# x = txt.find("welcome")
#
# print(x)

# fruits = ["apple", "banana", "cherry"]
#
# x = fruits.copy()
#
# print(x)



# txt = "For only {price:.7f} dollars!"
# print(txt.format(price = 475579588))
# NUMBERS = [1,2,3,4,5,6,7]
# NUMBERS.reverse()
# print(NUMBERS)
# fruits = ['apple', 'banana', 'cherry']
#
# fruits.pop(1)
# print(fruits)


# fruits = ['apple', 'banana', 'cherry']

# x = fruits.index("cherry")

# cars = ['Ford', 'BMW', 'Volvo']
#
# cars.sort()

# fruits = ['apple', 'banana', 'cherry']
#
# fruits.insert(1, "orange")

# fruits = ['apple', 'banana', 'cherry']
#
# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)




import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', '253', 'New York'],
    ['Jane', '302', 'London'],
    ['Bob', '352', 'Pariss']
]

filename = 'data.csv'

# Open the file in write mode
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print(f'Data saved to {filename} successfully.')