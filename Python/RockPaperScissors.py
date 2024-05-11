"""
A simple Rock, Paper, Scissors practice code.
Created by following a tutorial on GeeksforGeeks.
Fixed the errors in the code to produce the correct results of the game.
"""
# import random module
import random
# print instructions
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user

    choice = int(input("Enter your choice :"))

    # Loops until the user enter a valid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

        
    # Assigns a result corresponding to User input
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # prints the user's choice
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    # Using the random module, the computer produces a random choice betwen 1 and 3
    comp_choice = random.randint(1, 3)

    #An optional line to remove ties from the game
    """
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    """    

     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Scissors'
     # Printing the result.
    if result == 'DRAW':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    # Allows the user to input a lower case letter n to end game and break loop.
    ans = input().lower()
    
    #Broken while loop that is supposed to keep you in a loop until you input y or n.
    #while ans != 'y' or 'n':
    #    print("Please enter a valid choice")
        

    if ans == 'n':
        break
# Prints a thank you message when the game ends.
print("Thanks for playing!＼(^ω^ )")
