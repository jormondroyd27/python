# #  multiple assignment

# x, y = 10, 30
# print(x)
# print(y)

# # unpacking - all of these are the same

# # x, y = 10, 30
# # x, y = (10, 30)
# # (x, y) = 10, 30
# # (x, y) = (10, 30)

# # e.g

# z, a = "hi"
# print(z) # h
# print(a) # i

# # returning multiple variables

# def order_total(subtotal):
#     vat = 0.20
#     vat_amount = subtotal * vat
#     total = subtotal + vat_amount

#     return (total, vat_amount, vat)

# total, vat_amount, vat = order_total(10.00)

# print("Total: " + str(total))
# print("Vat amount: " + str(vat_amount))
# print("Vat: " + str(vat))

# # enumerate

# f = open("testfile.txt", "r")
# for i, line in enumerate(f):
#     print("Line " + str(i) + ": " + line)

# names = ["alice", "bob", "jim"]

# for counter, value in enumerate(names):
#     print(counter + 1, value)

# # default arguments

# def hello(name = "Jeff"):
#     print("hello " + name)
# hello()

# def circle_area(r, PI = 3.14):
#     return PI * (r ** 2)

# print(circle_area(9.5))
# print(circle_area(9.5, 3.141592))

# # keyword arguments

# # def add_result(player_1, player_1_score):
# #     #
# #     # process data
# # add_result(player_1 = "jake", player_1_score = 8)
# # add_result(player_1_score = 8, player_1 = "jake")
# # same result

# # args

# # def count_numbers(a, b, c, d, e):
# #     return a + b + c + d + e

# # print(count_numbers(1, 3, 4, 5, 6))
# # not reusable

# # using *args means any number of arguments can be taken

# # def count_numbers(*args):
# #     total = 0
# #     for num in args:
# #         total += num
# #     return total

# # print(count_numbers(1, 3, 5, 7, 5))

# def count_numbers(*args):
#     return sum(args)

# print(count_numbers(1, 3, 5, 7, 5))

# # keyword **kwargs
# # will take any keyword arguments and print them in a dictionary 

# def my_func(**kwargs):
#     print(kwargs)

# my_func(name = "jake", location = "manchester")

# # more unpacking

# numbers = [7, 3, 4, 8]
# more_numbers = [*numbers, 9, 11, 13]

# print(more_numbers)

# fruit_stock = {
#     "apples": 15,
#     "oranges": 30,
#     "pineapples": 3
#     }

# delivery = {
#     "mangos": 12,
#     "bananas": 24
# }

# latest_stock = {
#     **fruit_stock,
#     "apples": 21,
#     **delivery}

# print(latest_stock)

# def area(x, y, z):
#     return x * y * z

# data = [
#     {
#         "x": 3, 
#         "y": 12, 
#         "z": 4
#     },
#     {
#         "x": 6, 
#         "y": 9, 
#         "z": 8
#     },
#     {
#         "x": 2, 
#         "y": 15, 
#         "z": 10
#     }
# ]

# for x in data:
#     print(area(**x))


# def add_contact(**kwargs):
#     for key, value in kwargs.items():
#         print(key + " : " + value)
# contact = {
#     "fname": "Alice",
#     "lname": "Smith"
# }

# add_contact(**contact)


# 1. Create a function that returns the first and last letters of the word passed in as separate variables.


# 2. Create a function that takes the circumferance of a circle and return the radius and area.


# 3. Create a function that takes a file name and word. Search the file to find all lines that start with the given word. Test your function using the file 'austen.txt' and find all lines that begin with "Mr". Hint: is a function that returns True/False if a string ends with a value...maybe there is one that checks to see if a string "starts with"?


# 4. Create a function that will accept any number of parameters and save them all to a file, each on a new line.
# Modify your previous answer to save key/value pairs in a file:
# fname: Alice
# lname: Smith
# phone: 555-1234


# 5.  Create a function that can accept a series of numbers and a mathematical operand. Return the result of calculating the expression. E.g.:
# calculate(1, 2, 3, 4, operand = "multiply")
# calculate(65, 200, 84, 12, operand = "add")`
# Google the Python CSV library, and modify question 5 to save the data as a csv file. Make it so that you can enter as many contacts as you want and they each end up on a new row within the csv.
