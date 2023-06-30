# def name(a , b):
#     print(a * b)
#
#     name(3, 2)
#
# def funct(*args):
#
#     print(args[2])
#     funct(1, 3, 2, 5)
#     print()





# fruits = ["banana","cherry", "apple"]
# for x in fruits:
#  print(x)
#
# def fruits(*args):
#     print(args[2])


class Solution(object):
    def strStr(self, haystack, needle):
            if haystack == needle:
                return index(needle)
            else:
                return -1