
# Welcome message that explains the instructions

print ("\nIn this app you will enter a number between 1 - 20."
       "\nAfter that the computer will try to guess your number!")

# Setting the variable for the number that the user will input

import random
number_to_guess = 0

# while loop that gets user input to define the number that the computer will need
# to guess checks to make sure the user enters a number between 1 and 20
# prints message giving further instructions if user doesn't input number between 1 and 20

while number_to_guess < 1 or number_to_guess >20:
    number_to_guess = int(input("\n\nEnter a number for the computer to guess: "))
    if number_to_guess > 20:
        print ("You number must be lower than or equal to 20!")
    if number_to_guess < 1:
        print ("Your number must be greater than or equal to 1!")

# the computer generates a random integer and stores it in a variable
# the computer then prints it's guess

guess_number = random.randint(1, 20)
print ("The computer's guess is", guess_number)

# while loop that checks to see if the computer's guess is equal to the user's input
# if it's not equal and the computer guess number is less than the user's input
# the computer then chooses a random number between 1 and one less than the previous guess
# other wise the computer chooses a random number between 20 and one greater than the
# previous guess. The while loop stops when the computer guess is equal to the user input
while guess_number != number_to_guess:
    if guess_number > number_to_guess:
        guess_number -= 1
        guess_number = random.randint(1, guess_number)
    else:
        guess_number += 1
        guess_number = random.randint(guess_number, 20)
    print ("The computer\'s guess is ", guess_number)

# when the while loop ends the computer displays that the computer guessed
# user input and that the game is over
print ("The computer guessed", guess_number, "and it was correct... Game Over!")