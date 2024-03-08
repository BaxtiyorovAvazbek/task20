# 1-masala
# def integer_boolean(lst):
#     result = []
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x == "1":
#             y = x.replace("1", str(True))
#             result.append(y)
#         else:
#             m = x.replace("0", str(False))
#             result.append(m)
#     return result
#
#
# print(integer_boolean("100101"))
# 2-masala
# 3-masala
# def first_and_last(lst):
#     result = []
#     i = 0
#     while i < len(lst):
#         x = list(lst)
#         x.sort()
#         result.append(x)
#         y = list(reversed(x))
#         m = "".join(y)
#         return result, m
#
#
# print(first_and_last("marmite"))
# 4-masala
# 5-masala
# def cap_to_front(lst):
#     result = []
#     result2 = []
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x == x.upper():
#             result.append(x)
#         elif x == x.lower():
#             result2.append(x)
#     return "".join(result) + "".join(result2)
#
#
# print(cap_to_front("hApPy"))
# 6-masala
# def left_digit(lst):
#     result = ""
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x.isdigit():
#             result += x
#     return result[0:1]
#
#
# print(left_digit("TrAdE2W1n95!"))
# 7-masala
# def vow_replace(lst):
#     result = []
#     y = "u"
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x in "i,e,a,o,u,oʻ":
#             m = x.replace(x, y)
#             result.append(m)
#         else:
#             result.append(x)
#     return "".join(result)
#
#
# print(vow_replace("apples and bananas"))
# 8-masala
# def letters_only(lst):
#     result = ""
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x.isalpha():
#             result += x
#     return result
#
#
# print(letters_only("R!=:~0o0./c&}9k`60=y"))
# 9-masala
# 10-masala