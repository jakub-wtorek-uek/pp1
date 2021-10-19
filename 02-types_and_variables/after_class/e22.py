# 22.	Write a program that enables the user to face the computer. The computer throws a dice.
# The user then tries to guess the number from a dice by entering a number from 1 to 6 from the keyboard.
# If the user has guessed the number from the dice, the computer displays True.

from random import randint

computer_roll = randint(1, 6)
user_guess = int(input("Take your guess: "))

while user_guess != computer_roll:
    print("Your guess was wrong!")
    user_guess = int(input("Try again: "))

print(True)


