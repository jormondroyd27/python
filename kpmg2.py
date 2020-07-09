# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. Print out the string: `Rectangle of width 'width' and height 'height' has an area of 'area'.
width = 4
height = 10
area = (width*height)
print('Rectangle of width: ' + str(width) + ' and height: ' + str(height) + ' has an area of: ' + str(area) + '.')

# 2. Write code that prints the length of the string, 'python'.
print(len('python'))

# 3. Print out the first and third letter of the word 'python'.
word = 'python'
print(word[0])
print(word[2])

# 4. Ask the user to enter their name, and print out "Hello, 'name'".
name = input('Enter your name.\n')
print('Hello ' + name + '.')

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = int(input('Enter your age.\n'))
age_15 = (age + 15)
print('You will be ' + str(age_15) + ' years old in 15 years time.')

# 6. Combine the two input statements above and print out the message "Hello, 'name', you are currently 'age' years old. In 15 years time you will be 'age_in_15_years_time'".
print('Hello ' + name + ', you are currently ' + str(age) + ' years old. In 15 years time you will be ' + str(age_15) + ' years old.')

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input('Enter your hometown.\n')
print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
favourite_colour = input('Enter your favourite colour.\n')
print(len(favourite_colour))

# 9. Ask the user to enter the weather and the month. Print out the string, "It is 'month' and it is 'weather' today".
month = input('Enter the month.\n')
weather = input('Enter the weather.\n')
print('It is ' + month + ' and it is ' + weather + ' today.')

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string, .
temp1 = int(input('Enter a temperature.\n'))
temp2 = int(input('Enter a temperature.\n'))
temp3 = int(input('Enter a temperature.\n'))
temp4 = int(input('Enter a temperature.\n'))
temp5 = int(input('Enter a temperature.\n'))
average_temp = ((temp1+temp2+temp3+temp4+temp5)/5)
print('The average temperature for ' + month + ' is ' + str(average_temp) + ' degrees.')


# 11. Print out the above sentence but make the month upper case.
print('The average temperature for ' + month.upper() + ' is ' + str(average_temp) + ' degrees.')

# 12. Create a variable that holds your favourite animals and print it out. Make sure the animals are all on different lines and tabbed.
favourite_animals = ['pigs', 'moths', 'dogs']
print('\t' +favourite_animals[0] + '\n\t' + favourite_animals[1] + '\n\t' + favourite_animals[2])

# 13. Ask the user to enter their name as well as a number. Print out the uppercase character at that position in the string.
number = int(input('Enter a number\n'))
print(name[number-1].upper())