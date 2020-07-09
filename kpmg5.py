# 1. Print 10 random numbers
# for loop
import random
for x in range(10):
    print(random.randint(1, 10))
# while loop
import random
count = 0
while count < 10:
    print(random.randint(1,10))
    count += 1


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!"
number = 0
while number != 7:
    number = int(input("Enter a number:\n"))

print("Lucky number 7!")

# 3. Rewrite Q2 so that the number being guessed is a random value from 1 to 10
import random

number = random.randint(1,10)
guess = 0

while guess != number:
    guess = int(input("Enter my random number:\n"))

print("You guessed my random number " + str(number) + "!")

# 4. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. E.g. 240cm x 80cm = 19200cm2 = 2m2
width = int(input("Enter the height in cm: \n"))
height = int(input("Enter the height in cm: \n"))
areacm2 = (width*height)
aream2 = int(areacm2/10000)
print(str(width) + "cm x " + str(height) + "cm = " + str(areacm2) + "cm2 = " + str(aream2) + "m2.")

# 5. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure" and then ask them to enter it again. Only allow them to enter the password wrong 3 times before printing "System Locked!"
attempts = 0
password = "qwerty123"

while attempts < 3:
    attempt = input("Enter your password: \n")
    if attempt == password:
        print("You have successfully logged in.")
        break
    else:
        print("Incorrect password.")
        attempts += 1
        if attempts >= 3:
            print("Password failure.")

# 6. Add up all the numbers from 1 to 500 and print the answer
count = 0
for x in range(1,501):
    count += x
print(count)

# 7. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. Find the index at which the user entered the number 99
numbers = []

for x in range(5):
    num = int(input("Input a number\n"))
    numbers.append(num)

print(numbers)

z = 0
while z < len(numbers):
    if numbers[z] == 99:
        print(z)
    z += 1

# 8. Print a multiplication table for the number 18 up to 15. E.g. 1 x 18 = 18 2 x 18 = 36
# for loop
for x in range(1,16):
    print(str(x) + " x 18 = " + str(x*18))

times_table = 18
times = 15
for x in range(1, times+1):
    value = x * times_table
    print(str(x) + " x " + str(times_table) + " = " + str(value))

# 9. Rewrite question B2 from session 4 using a while loop Print the numbers 1 to 100 (including the number 100)
# for loop
for x in range(1,101):
    print(x)
# while loop
x = 0
while x < 100:
    x += 1
    print(x)

# 11. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list
numbers = []
count = 0
while count < 5:
    user_number = int(input("Enter a number:\n"))
    numbers.append(user_number)
    numbers.append(user_number ** 2)
    count += 1
print(numbers)

# 11. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# import random 

prize_draw_entries = []
name = None

while name != "":
    name = input("Enter your name for the prize draw: \n")
    if name != "":
        prize_draw_entries.append(name)

winner = (random.choice(prize_draw_entries))
print("\nThe winner is " + winner + "!")

# 12. Create a rock, paper, scissors game which is run against computer. This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again
# rps list, score best of 3, player turn, computer turn

import random

player_score = 0
computer_score = 0

while player_score < 2 or computer_score < 2:

    moves = ["rock", "paper", "scissors"]
    made_move = False
    computer = random.choice(moves)


    while not made_move:
        player = input("\nMake your move: ")
        if player in moves:
            made_move = True



    if player == "rock":
        if computer == player:
            print("A draw: " + player)
        elif computer == "paper":
            print("You lose!")
            computer_score += 1
        elif computer == "scissors":
            print("You win!")
            player_score += 1
    elif player == "paper":
        if computer == player:
            print("A draw: " + player)
        elif computer == "scissors":
            print("You lose!")
            computer_score += 1
        elif computer == "rock":
            print("You win!")
            player_score += 1
    elif player == "scissors":    
        if computer == player:
            print("A draw: " + player)
        elif computer == "rock":
            print("You lose!")
            computer_score += 1
        elif computer == "paper":
            print("You win!")
            player_score += 1

    print("Player: " + player + "\nScore: " + str(player_score))
    print("Computer: " + computer + "\nScore: " + str(computer_score))
    if player_score == 2 or computer_score == 2:
        break

if player_score > computer_score:
    print("\nYou win the game!")
else:
    print("\nYou lose the game!")

# 13. Expand this so that its best of 3 games
