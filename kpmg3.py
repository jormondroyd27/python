# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!"
name = input('Enter your name.\n')
if name == 'bob':
    print('Welcome Bob!')

# # 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!"
elif name != 'alice':
    print("You're not Alice!")

# # 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure"
password = "qwerty123"
password_attempt = input("Enter the password\n")
if password_attempt == password:
    print("You have successfully logged in.")
else:
    print("Password failure.")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"
number = int(input("Enter a number.\n"))
if number % 2 == 0:
    print("Even.")
else:
    print("Odd.")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
number1 = int(input("Enter a number.\n"))
number2 = int(input("Enter another number.\n"))
if number1 + number2 > 21:
    print("Bust.")
else:
    print("Safe.")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
width = int(input("Enter the width.\n"))
height = int(input("Enter the height.\n"))
if width == height:
    print("This shape is a square.")
else:
    print("This shape is not a square.")

# 7. Your company has had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("Enter your current salary.\n"))
service = int(input("Enter your years of service.\n"))
bonus = int(salary * 0.1)
if service >= 3:
    print("Salary: " + str(salary) + "\nBonus: " + str(bonus))
else:
    print("No bonus.")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
whole_number = int(input("Enter a number.\n"))
if whole_number > 0:
    print(whole_number * whole_number * whole_number)
elif whole_number < 0:
    print(int(whole_number / 2))

# 9. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", print "You're not Bob! I'm Bob", else print "You must be Charlie"
name1 = input("Enter your name:\n")
if name1 == 'Alice':
    print("Hello Alice!")
elif name1 == 'Bob':
    print("You're not Bob, I'm Bob!")
else:
    print("You must be Charlie.")
 
# 10. Ask the user to enter their age
# If they are younger than 11, print "You're too young to go to this school"
# If they are between 11 and 16, print "You can can come to this school"
# If they are over 16, print 'You're too old for school"
# If they are 0, print "You're not born yet!"
age = int(input("Enter your age.\n"))
if age < 11 and age > 0:
    print("You're too young to go to this school.")
elif age >= 11 and age <= 16:
    print("You can go to this school.")   
elif age > 16:
    print("You're too old for this school.")
elif age == 0:
    print("You aren't born yet.") 

# 11. Ask the user to enter the name of a month. If the user enters March/April/May: print " is in Spring", otherwise print "I don't know"
# Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February
# Ensure that when an unknown month is given it prints "I don't know"
month = input("Enter the month.\n")
if month == "March" or month == "April" or month == "May":
    print(month + " is in Spring!")
elif month == "June" or month == "July" or month == "August":
    print(month + " is in Summer!") 
elif month == "September" or month == "October" or month == "November":
    print(month + " is in Autumn!")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter!")
else:
    print("I don't know.")

# 12. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers
number_one = int(input("Enter a number.\n"))
number_two = int(input("Enter another number.\n"))
if number_one % 2 == 0 and number_two % 2 == 0:
    print("Even.")
if number_one % 2 == 1 and number_two % 2 == 1:
    print("Odd.")    
else:
    print(str(number_one + number_two))

# # 13. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
number_three = int(input("Enter a number:\n"))
number_four = int(input("Enter another number:\n"))
if number_three > number_four:
    print(str(number_three) + " is the highest value.")
else:
    print(str(number_four) + " is the highest value.")

# 14. Your company has had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("Enter your current salary.\n"))
service = int(input("Enter your years of service.\n"))
bonus_1 = (salary * 0.1)
bonus_2 = (salary * 0.15)
bonus_3 = (salary * 0.2)
if service >= 3 and service < 5:
    print("Salary: " + str(salary) + "\nBonus: " + str(bonus_1))
elif service >= 5 and service <= 6:
    print("Salary: " + str(salary) + "\nBonus: " + str(bonus_2))
elif service >= 7:
    print("Salary: " + str(salary) + "\nBonus: " + str(bonus_3))
else:
    print("No bonus.")

# 15. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. If all three ages are the same, print that.
name1 = input("Enter your name: \n")
age1 = int(input("Enter your age: \n"))
name2 = input("Enter your name: \n")
age2 = int(input("Enter your age: \n"))
name3 = input("Enter your name: \n")
age3 = int(input("Enter your age: \n"))
# # Oldest
if age1 > age2 and age1 > age3:
    print(name1 + " is " + str(age1) + " and is the oldest.")
elif age2 > age1 and age1 > age3:
    print(name2 + " is " + str(age2) + " and is the oldest.")
elif age3 > age1 and age3 > age2:
    print(name3 + " is " + str(age3) + " and is the oldest.")
else:
    print("You are all the same age.")
# # Youngest
if age1 < age2 and age1 < age3:
    print(name1 + " is " + str(age1) + " and is the youngest.")
elif age2 < age1 and age2 < age3:
    print(name2 + " is " + str(age2) + " and is the youngest.")
elif age3 < age1 and age3 < age2:
    print(name3 + " is " + str(age3) + " and is the youngest.")
else:
    print("You are all thre same age.")

# 16. A school has following rules for their grading system:
# a. Above 80 – A
# b. 60 to 80 – B
# c. 50 to 60 – C
# d. 45 to 50 – D
# e. 25 to 45 – E
# f. Below 25 - F
# Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson1 = input("Enter the subject.\n")
marks1 = int(input("Enter the marks for this subject.\n"))

if marks1 < 25:
    print("\nSubject: " + lesson1 + "\nGrade: F\n")
elif marks1 >= 25 and marks1 < 45:
    print("\nSubject: " + lesson1 + "\nGrade: E\n")
elif marks1 >= 45 and marks1 < 50:
    print("\nSubject: " + lesson1 + "\nGrade: D\n")
elif marks1 >= 50 and marks1 < 60:
    print("\nSubject: " + lesson1 + "\nGrade: C\n")
elif marks1 >= 60 and marks1 < 80:
    print("\nSubject: " + lesson1 + "\nGrade: B\n")
elif marks1 > 80:
    print("\nSubject: " + lesson1 + "\nGrade: A\n")
else:
    print("\nGo see your teacher")

lesson2 = input("Enter the subject.")
marks2 = int(input("Enter the marks for this subject.\n"))

if marks2 < 25:
    print("\nSubject: " + lesson2 + "\nGrade: F\n")
elif marks2 >= 25 and marks2 < 45:
    print("\nSubject: " + lesson2 + "\nGrade: E\n")
elif marks2 >= 45 and marks2 < 50:
    print("\nSubject: " + lesson2 + "\nGrade: D\n")
elif marks2 >= 50 and marks2 < 60:
    print("\nSubject: " + lesson2 + "\nGrade: C\n")
elif marks2 >= 60 and marks2 < 80:
    print("\nSubject: " + lesson2 + "\nGrade: B\n")
elif marks2 > 80:
    print("\nSubject: " + lesson2 + "\nGrade: A\n")
else:
    print("\nGo see your teacher")

lesson3 = input("Enter the subject.")
marks3 = int(input("Enter the marks for this subject.\n"))

if marks3 < 25:
    print("\nSubject: " + lesson3 + "\nGrade: F\n")
elif marks3 >= 25 and marks3 < 45:
    print("\nSubject: " + lesson3 + "\nGrade: E\n")
elif marks3 >= 45 and marks3 < 50:
    print("\nSubject: " + lesson3 + "\nGrade: D\n")
elif marks3 >= 50 and marks3 < 60:
    print("\nSubject: " + lesson3 + "\nGrade: C\n")
elif marks3 >= 60 and marks3 < 80:
    print("\nSubject: " + lesson3 + "\nGrade: B\n")
elif marks3 > 80:
    print("\nSubject: " + lesson3 + "\nGrade: A\n")
else:
    print("\nGo see your teacher")