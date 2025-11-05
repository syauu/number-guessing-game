"""
program pilih random number 1-100
chances to guess based on the game level
corect guess, user win, game stop

1. welcome message
2. program choose random number
3. user select level (easy, medium, hard)
4. if wrong guess, display hint wether the number is greater or less than user's guess
5. game stop when user win or runs out of chances
"""

import random

print("Welcome to the Number Guessing Game!")
print("Difficulty Level:")
print("1. Easy (10 chances)")
print("2. Medium (6 chances)")
print("3. Hard (4 chances)")
print("")
level = int(input("Please select the difficulty level (enter number): "))
match level:
    case 1:
        chances = 10
    case 2:
        chances = 6
    case 3:
        chances = 4
print("")
print("Aight. Lets start!")
print("")

random_number = random.randint(1, 100)

while chances != 0:
    try:
        guess_number = int(input("Enter your guess: "))
        if guess_number != random_number:
            chances -= 1
            if random_number < guess_number:
                print(f"Incorrect! The number is less than {guess_number}. You have {chances} more chances.")
            elif random_number > guess_number:
                print(f"Incorrect! The number is greater than {guess_number}. You have {chances} more chances.")
        elif guess_number == random_number:
            print("")
            print("Congrats! That is correct.")
            break
    except ValueError:
        print("Please enter a whole number")

print("")
if chances == 0 and guess_number != random_number:
    print(f"You lost! The number is {random_number}")