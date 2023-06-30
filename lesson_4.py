# # for x in range(1, 6+7):
# # print(x)
# # for x in range (2, 30, 6):
# # print("hello")
# # pass
#
# count = 1
# symbol = "*"
# for s in range(5):
#      for j in range(count):
#         print(symbol, end=' ')

# empty line after each row
#  count += 1 #c = c + 1
#  print("")
#
# numbers = 1
# for s in range(1, numbers + 2, 1):
#     for j in range(1, s + 2, 1):
#         print(numbers, end='')
#         numbers += 2
#         print("")
#
# # for x in range(1, 12):
# #     print(x)
# # y = list(x)
# # print(y)
#
import sticks as sticks


# numbers = [1, 2, 3, 4, 5, 6]
# while numbers:
#     s = int(input(('кой кусок вы хотите есть = ')))
#     for x in numbers:
#         if x == s:
#             print(s)
#             numbers.remove(x)
#             print(f"{x} пицца съедена")
#     print(numbers)
# #     pass

# /
#
#
def fibonnacci(c):
    a, b = 0, 1
    result = []
    for _ in range(1, c):
        x = a + b
        a = b
        b = x
        result.append(b)
    return result


print(fibonnacci(1000))
