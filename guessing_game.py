# generate a random number between 1 and 20 and
# define it as a variable called "number_to_guess"

import random
number_to_guess = random.randint(1,20)

#  Print a welcome message and the user to guess an integer between 1 and 20

print("Welcome to the Number Guessing Game!")
guess_number = int(input("Guess the number between 1 and 20... "))


# A While loop checks to see if the user's guess equals the number to guess.
# If the user's guess is less than the number to guess the app tells the user
# to guess a higher number and asks for another guess.

while number_to_guess != guess_number:
    if guess_number < number_to_guess:
        print("Guess a higher number")
        guess_number = int(input("Guess the number again... "))

# If the user's guess is not less than or equal to the number to guess
# the app tells the user to Guess a lower number and asks for another guess.

    else:
        print("Guess a lower number")
        guess_number = int(input("Guess the number again... "))


# If the user's guess is equal to the number to guess
# the app ends and tells the user that their guess was correct and then
# displays what the number to guess was.

    if number_to_guess == guess_number:
        print("Congrats! That is the Correct Number! The number was " + str(number_to_guess))


