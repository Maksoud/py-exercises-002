# This is a world wide know game. This challenge need's to ask a position from the user and show
# graphically the results. It's necessary to inform to the players when they win. Each player needs 
# a different charactere in this game.

import os

def choose_player():

    validFunctions = ['q', 'r', 'x', 'o']
    validOptions   = range(1, 10)
    player         = ""
    roundPlayer    = 1
    listPositions  = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        
    while player not in validFunctions:

        # Clear the screen
        os.system('cls')

        print("\nPress Q anytime to quit the game...\n")

        # Ask if the user want to be the X or the O
        player = input("Do you want to start as X or O? ")

        # Clear the screen
        os.system('cls')

        # Ending the game
        if player.lower() == 'q':

            quit_game()

        # Wrong option selected
        if player not in validFunctions:

            print("\nWrong option selected. Try again\n")

            continue
        
        # Identifing chosen option
        if player.lower() == 'x':

            print("Starting game with X\n")
            roundPlayer = "X"
            
        elif player.lower() == 'o':

            print("Starting game with O\n")
            roundPlayer = "O"

        # Print the default board
        defaultBoard = {1:"   1   |   2   |   3   ",
                        2:"-----------------------",
                        3:"   4   |   5   |   6   ",
                        4:"-----------------------",
                        5:"   7   |   8   |   9   "
                       }

        for line in defaultBoard:
            print(defaultBoard[line])

        print("\n")

        # Let's play
        if player in validFunctions:

            selectedOption = 0

            while selectedOption not in validOptions:

                # Check the end of game
                count = 0

                for pos in listPositions:

                    count += 1 if listPositions[pos] == "X" or listPositions[pos] == "O" else 0

                if count == 9:

                    print("Game Over!")
                    listPositions = restart_game()
                    choose_player()

                    continue

                # Winner check
                if check_winner(listPositions):

                    listPositions = restart_game()
                    choose_player()

                    continue

                else:

                    # Inform who's the next player
                    print("It's the "+roundPlayer+" turn")

                    # Choose an option 1-9
                    selectedOption = input("Select a number between 1-9 ")

                # Clear the screen
                os.system('cls')

                print("Press Q anytime to quit the game...")

                # Ending the game
                if selectedOption.lower() == 'q':

                    quit_game()

                if selectedOption.lower() == 'r':

                    listPositions = restart_game()

                    choose_player()

                    continue

                # Check a valid option selected
                if (not selectedOption.isdigit()) or (int(selectedOption) not in validOptions):
                    
                    print("\nWrong option selected! Choose a number between 1-9\n")
                    
                    # Printing the board
                    print_board(listPositions)
                    
                    continue

                else:
                    # Parse to int
                    selectedOption = int(selectedOption)

                if (listPositions[selectedOption] != " "):

                    print("\nOption already taken! Please choose another unchosen option")
                    
                    pass

                else:

                    # Selected positions
                    listPositions[selectedOption] = roundPlayer

                    # Next time will be for the next player
                    roundPlayer = "O" if roundPlayer == "X" else "X"

                # Printing the board
                print_board(listPositions)

                # Reset selected option to keep the game alive
                selectedOption = 0

def print_board(listPositions):

    print("\n")

    printBoard = {1:"   "+listPositions[1]+"   |   "+listPositions[2]+"   |   "+listPositions[3]+"   ",
                  2:"-----------------------",
                  3:"   "+listPositions[4]+"   |   "+listPositions[5]+"   |   "+listPositions[6]+"   ",
                  4:"-----------------------",
                  5:"   "+listPositions[7]+"   |   "+listPositions[8]+"   |   "+listPositions[9]+"   "
                 }

    for line in printBoard:
        print(printBoard[line])

    print("\n")

def check_winner(listPositions):
    
    win = False

    # Win check
    if listPositions[1] == listPositions[2] and listPositions[1] == listPositions[3] and listPositions[1] != " ":
        print("Player "+listPositions[1]+" Won!")
        win = True
    if listPositions[4] == listPositions[5] and listPositions[4] == listPositions[6] and listPositions[4] != " ":
        print("Player "+listPositions[4]+" Won!")
        win = True
    if listPositions[7] == listPositions[8] and listPositions[7] == listPositions[9] and listPositions[7] != " ":
        print("Player "+listPositions[7]+" Won!")
        win = True
    if listPositions[1] == listPositions[4] and listPositions[1] == listPositions[7] and listPositions[1] != " ":
        print("Player "+listPositions[1]+" Won!")
        win = True
    if listPositions[2] == listPositions[5] and listPositions[2] == listPositions[8] and listPositions[2] != " ":
        print("Player "+listPositions[2]+" Won!")
        win = True
    if listPositions[3] == listPositions[6] and listPositions[3] == listPositions[9] and listPositions[3] != " ":
        print("Player "+listPositions[3]+" Won!")
        win = True
    if listPositions[1] == listPositions[5] and listPositions[1] == listPositions[9] and listPositions[1] != " ":
        print("Player "+listPositions[1]+" Won!")
        win = True
    if listPositions[7] == listPositions[5] and listPositions[7] == listPositions[3] and listPositions[7] != " ":
        print("Player "+listPositions[7]+" Won!")
        win = True

    return win

def restart_game():

    input("\nPress [ENTER] to play again! ")

    # Clear the screen
    os.system('cls')

    return {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

def quit_game():

    # Clear the screen
    os.system('cls')

    print("Thank you for comming. See ya!")

    quit() 
    
    
# Starting the game
choose_player()