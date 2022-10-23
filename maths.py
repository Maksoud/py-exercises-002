# This challenge will ask if you want to test multiplication, division, sum or subtration and will 
# choose the challenge and check the answer

import os
import random

def maths():

    validOperators = ["+", "-", "*", "/"]
    operator = ""
    attempts = 0

    # Generating random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Clear the screen
    os.system('cls')

    while operator not in validOperators:
            
        print("Press Q anytime to quit the game...\n")

        # Getting the operation operator
        operator = input("Choose an operator between +, -, * or /: ")

        # Ending the game
        if operator.lower() == 'q':

            os.system('cls')
            print("Thank you for comming. See ya!")
            exit()

        # Check if was chosen an operator
        if operator not in validOperators:

            print("Choose an operator like following examples: +, -, * or /")

        else:

            # Create a random operation
            match operator:
                case "*":
                    calc = num1 * num2
                    print(f"What's the result of {num1} * {num2}")
                case "/":
                    calc = num1 / num2
                    print(f"What's the result of {num1} / {num2}")
                case "+":
                    calc = num1 + num2
                    print(f"What's the result of {num1} + {num2}")
                case "-":
                    calc = num1 - num2
                    print(f"What's the result of {num1} - {num2}")

            # Rounded calc
            calc = round(float(calc), 2)
            
            # Default answer
            answer = -999

            # Keep asking until the answer gets right
            while float(answer) != calc:

                # Ending game
                if attempts > 5:
                    print("Don't worry, this equation was hard. Try another one!")
                    print("The right answer is " + str(calc))
                    input()
                    maths()

                # Check answers
                answer = input("Type the answer here: ")

                # Ending the game
                if answer.lower() == 'q':

                    os.system('cls')
                    print("Thank you for comming. See ya!")
                    exit()
                
                else:

                    try:

                        if float(answer) != calc:
                            print("Wrong answer! Please, try again...")
                            attempts +=1
                        else:
                            print("Congratulations! You won the game!")
                            input()
                            maths()
                            
                    except Exception:

                        print("Choose only numbers on your answer!")
                        answer = -999
                        return

# Starting the game
maths()