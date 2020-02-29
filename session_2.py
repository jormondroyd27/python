#1 Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

name =input("What is your name?") 
if name =="Bob":
    print("Welcome Bob!")

 #2 Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

name =input("What is your name?")
if name !="Alice":
    print("You're not Alice!")
    
#3 Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure." If they get it wrong, print "Password failure.".

password =input("Enter your password.")
if password =="qwerty123":
    print("You have successfully logged in.")
else: 
    print ("Password failure.") 

#4 Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

number = int (input("Enter a number."))
if number % 2 ==0:
    print("Even")
else:
    print ("Odd")

#5 Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe".

number=int(input("Enter a number."))
number2=int(input("Enter a number."))
if number + number2 >21:
    print("Bust") 
else:
    print ("odd")

#1 Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", print "What's up Bob!", else print "You must be Charlie".

name =input("What is your name?")
if name == "Alice":
    print ("Hello Alice")
elif name == "Bob":
    print ("What's up Bob!")
else:
    print ("You must be Charlie!")

#2 Ask the user to enter their age: i: If they are younger than 11, print "You're too young to go to this school". ii. If they are between 11 and 16, print "You can go to this school". iii. If they are over 16, print "You're too old for school." iv. If they are 0, print "You're not born yet.".

age =int(input("What is your age?"))
if age <11 and age >0:
    print ("You're too young to go to this school.")
elif age >11 and age <16:
    print ("You can come to this school.")
elif age >16:
    print ("You're too old for school.")
elif age == 0:
    print ("You're not born yet!")

#3 Ask the user to enter the name of a month. If the user enters March/April/May print <month> is in Spring, otherwise print, "I don't know". i. Expand for the rest of the year, given that Summer is June/July/August. Autumn is September/October/November. Winter is December/January/February. ii. Ensure that when an unknown month is given it print's "I don't know".

month = input("Enter the name of a month.")
if month == "March" or month == "April" or month == "May":
    print (month + " is in Spring.")
elif month == "June" or month == "July" or month == "August":
    print (month + " is in Summer.")
elif month == "September" or month == "October" or month == "November":
    print (month + " is in Autumn.")
elif month == "December" or month == "January" or month == "February":
    print (month + " is in Winter.")
else:
    print ("I don't know.")

#4 Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

number = int(input("Enter a number."))
number2 = int(input("Enter a number."))
if number % 2 == 0 and number2 % 2 == 0:
    print ("Even.")
elif number % 2 == 1 and number2 % 2 == 1:
    print ("Odd.")
else:
    print (number * number2)

#1 Create the following list of items: apples, cherries, pears, pineapple, peaches, mango.

items = ["apples", "cherries", "pears", "pineapple", "peaches", "mango"]
print(items)

#2. Add "grapes" to your list.

items.append("grapes")
print(items)

#3 Change "pears" to "strawberries".

items[2] = "strawberries"
print(items)

#4 Remove "apples" from the list.

del(items[0])
print(items)

#5 Print out the current length of your list. 

print(len(items))

#6 Print out your list.

items.sort()
print(items)

#7 Order the list alphabetically.

items.sort()

#8 Print out the list again. 

print(items)

#1 Loop through the list you created in section C and print each item out.


fruits = ["apples", "cherries", "pears", "pineapple", "peaches", "mango"]
for fruit in fruits:
    print(fruit)

#2. Print all numbers 1 to 100 including the number 100).

for number in range(101):
    print(number)

#3 Print all odd numbers from 1 to 100.

for number in range(1, 100, 2):
    print(number)

#4 The olympics started in 1896, print all the years they have been held.

for number in range(1896, 2020, 4):
    print(number)