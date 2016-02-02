### generate a number and define it as a variable

import random
number_to_guess = random.randint(1,20)

guess_number = int(input("Guess the number between 1 and 20... "))

while number_to_guess != guess_number:
    if guess_number < number_to_guess:
        print("Guess a higher number")
        guess_number = int(input("Guess the number again... "))
    else:
        print("Guess a lower number")
        guess_number = int(input("Guess the number again... "))

    if number_to_guess == guess_number:
        print("Congrats! That is the Correct Number!")
        break

print(number_to_guess)
