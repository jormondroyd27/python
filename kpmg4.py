# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list
shopping_list = ["apples", "cherries", "pears", "pineapple", "peaches", "mango"]
print(shopping_list)

# 2. Add "Grapes" to the list and print the list
shopping_list.append("grapes")
print(shopping_list)

# 3. Change "Pears" to "Strawberries" and print the list
shopping_list[2] = "strawberries"
print(shopping_list)

# 4. Remove "Apples" from the list and print the list
del shopping_list[0]
print(shopping_list) 

# 5. Print out the current length of the list
print(len(shopping_list))

# 6. Order the list alphabetically
shopping_list.sort()

# 7. Print out the list again
print(shopping_list)

# 8. Loop through the list you created in section A and print each item out
for x in shopping_list:
    print(x)

# 9. Print the numbers 1 to 100 (including the number 100)
for x in range(1,101):
    print(x)

# 10. Print all odd numbers from 1 to 100
for x in range(1,101):
    if x % 2 == 1:
        print(x)

# 11. The modern olympics started in 1896, print the years they have been held (bonus points to skip 1916, 1940, 1944)
for year in range(1896, 2021, 4):
    if year != 1916 and year != 1940 and year != 1944:
        print(year)

# 12. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
random = [2, 5, 6, 7, 4, 3 ,5, 10, 11]
odd = 0
even = 0
for number in random:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even: " + str(even))
print("Odd: " + str(odd))

# 13. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ["jimmy", "laila", "sam", "jack", "mia"]
for name in names:
    print("Hello " + name + ".")

# 14. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
for letter in word:
    print(letter)

# 15. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
squared = []
for x in range(3):
    number = int(input("Enter a number:\n"))
    squared.append(number**2)
print(squared)

# 16. Create a list with five names in. Write a for loop which appends Dr. to each name in the new list.
names = []
for x in range(3):
    names.append(input("What is your name?\n"))
for name in names:
    print("Dr. " + name)
print(names)

# 17. FizzBuzz – Writ;e a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz"
for x in range(1,100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)