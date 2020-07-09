# 1. Write a function that prints your name
def my_name(name):
    print(name)

my_name("James")
my_name("Laila")
my_name("Sam")
my_name("Jack")
    
# 2. Write a function that accepts a name as a parameter and prints "Hello, "
def print_name(name):
    print("Hello " + name + ".")

print_name("James")
print_name("Laila")
print_name("Sam")
print_name("Jack")

# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote
# def print_name(name):
#     print("Hello " + name + ".")

list = ["Alice", "Bob", "Charlie"]

for people in list:
    print_name(people)

# 4. Write a function that prints the area of two passed in parameters
def print_area(width, height):
    print("The area with a width of " + str(width) + "cm and a height of " + str(height) + "cm = " + str(width*height/10000) + "m2.")

print_area(200,200)
print_area(400, 400)

# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list
def print_item_in_list(list):
    for item in list:
        print(item)

numbers = [1, 2, 3, 4, 5, 6]
print_item_in_list(numbers)

# 6. Put the following into a function:
# i. If they are younger than 11, print "You're too young to go to this school"
# ii. If they are between 11 and 16, print "You can can come to this school"
# iii. If they are over 16, print 'You're too old for school"
# iiii. If they are 0, print "You're not born yet!"
def age_for_school(age):
    if age < 11 and age > 0:
        print("You're too young to go to this school.")
    elif age >= 11 and age <= 16:
        print("You can go to this school.")   
    elif age > 16:
        print("You're too old for this school.")
    elif age == 0:
        print("You aren't born yet.")

age_for_school(10)
age_for_school(12)
age_for_school(17)
age_for_school(0)

# 7. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers)
def is_odd(number):
    if number % 2:
        return True

    return False

data = [1, 2, 3]        
for item in data:
    print(is_odd(item))

# 8. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'
def reverse_word(word):
    word_length = len(word)
    new_word = ""
    while word_length != 0:
        word_length -= 1
        new_word += word[word_length]
    return new_word
   
print(reverse_word("hello"))
print(reverse_word("jimmy ormondroyd"))

# 9. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g: ***** **** *** ** *
def print_stars(x):
    star = ""
    for times in range(0, x):
        star += "*"
    print(star)    

    if x > 1: 
        print_stars(x - 1)

print_stars(50)

# 10. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked"
def padlock(passcode):
    lock = "1234"
    if passcode == lock:
        return "Unlock"
    return "Locked"
print(padlock("1234"))
print(padlock("1243"))

# 11. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
def multiple_of_3_and_5(limit):
    total = 0
    for x in range(1, limit + 1):
        if x % 3 == 0:
            total += x
        elif x % 5 == 0:
            total += x
    return total

print(multiple_of_3_and_5(10))

# 12. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not
def prime_num(number):
    for x in range(2, number):
        if number % x == 0:
            return False

    return True

print(prime_num(4))
print(prime_num(11))
print(prime_num(12))

# 13. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
def reverse_word_(word):
    word_length = len(word)
    new_word = ""
    while word_length != 0:
        word_length -= 1
        new_word += word[word_length]
    return new_word

def is_pallindrome(word):
    word_reversed = reverse_word_(word)
    if word_reversed.lower() == word.lower():
        return True
    else:
        return False

print(is_pallindrome("Anna"))

# 14. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
def is_pallindrome_(word):
    new_word = word.replace(" ", "").lower()

    word_reversed = reverse_word_(new_word)
    if word_reversed == new_word:
        return True
    else:
        return False

print(is_pallindrome_("A nut for a jar of tuna"))