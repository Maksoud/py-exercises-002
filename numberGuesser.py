# The computer will choose a number between 1 and 50. Choose your guess based on the hints.

import os
import random

def guessNumber():

    theNumber  = random.randint(1, 50)
    validGuess = range(1, 51)
    guess      = 0
    attempts   = 0

    # Clear the screen
    os.system('cls')

    while (guess != theNumber):

        print("Press Q anytime to quit the game...\n")

        # Get the user's guess
        guess = input("Guess a number between 1-50 ")

        # Ending the game
        if guess.lower() == 'q':
            os.system('cls')
            print("Thank you for comming. See ya!")
            quit()
        
        # Check if it's a number
        if not guess.isdigit() or int(guess) not in validGuess:
        
            os.system('cls')
            print("Wrong option! Choose only numbers!\n")
        
        else:

            # Clear the screen
            os.system('cls')
        
            # Convert to a number
            guess = int(guess)

            # Check the user's guess
            if guess < theNumber:
                print("Guess bigger...\n")
                attempts += 1
            elif guess > theNumber:
                print("Guess lower...\n")
                attempts += 1
            elif guess == theNumber:
                print("You won! In "+str(attempts)+" attempts\n")

guessNumber()