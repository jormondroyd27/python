print("Hello World")
print(2 + 2)
print(5.7 - 3.4)
print(8 * 7)
print(144 / 12)
print(67 % 12)
print((4 - 2) * 6)
print(2 + 2)
print("Hello, Jimmy")

#1. Create two variables, one that holds the width and one that holds the height of a rectangle, then, work out and store the variable in a third variable.
width = 4
height = 8
area = width * height 
print("rectangle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area))

#2 Write the code that prints the length of the string, 'python'.
print(len('python'))

#3 Print out the first and third letter of the word 'python'.
word  = "python"
print(word[0])
print(word[2])

#4 Ask the user to enter their name, and print out "Hello, <name>".

name = input("What's your name? ")
print("Hello " + name)

#5 Ask the user to enter their age, tell them how old they will be in 15 years time.

age = int(input("How old are you? "))
age_in_15_years = age + 15
print(age_in_15_years)

#6 Combine the two input statements above and print out the message "Hello, Jimmy, you are currently 26 years old. In 15 years time you will be <age_in_15_years_time>".

name = input("What's your name? ")
age = int(input("How old are you? "))
age_in_15_years = age + 15
print("Hello, " + name + " you are currently " + str(age) + ". In 15 years you will be " + str(age_in_15_years) + ".")

#7 Ask the user to enter their hometown, print it out in uppercase letters.

hometown =input("What is your hometown called? ")
print(hometown.upper())

