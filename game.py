# game.py

# importing random function
import random
import os
import dotenv
from dotenv import load_dotenv



load_dotenv() # invoke the function


# introduction to game
print("-------------------")
USER_NAME = os.getenv("USER_NAME", default="Player One")

print(f"PLAYER:'{USER_NAME}'")
print("-------------------")

# asking for user input


user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
user_choice = user_choice.lower()

# print(x)
print("You chose:", user_choice)

# NOTES from class: different ways to print a string 
        # can print many things in a string as long as they are seperated by commas
        # print("you chose:",x,"another string",x)

        # string concat:
        # print("you chose:" + "other string here")

        # string inerpolation / format string usage
        # print(f"you chose: {x}")



# simulating a computer input
options = ['rock', 'paper', 'scissors']

# validate the user selection
#
# stop the program (not try to determine the winner)
# ... if the user choice is invalid


if user_choice in options:
    pass
else:
        print("OOPS, please choose a valid option and try again")
        exit()

        
computer_choice = random.choice(options)
#NOTES from class
        # alternative: computer_choice = choice(options)

print(f"The computer chose: {computer_choice}")

# determining who won
#single equal sign assigns value to variable. the way it is evaluated as saying what is on the right, and store it in the left
# equality operations. is what is on the left equal to what is on the right? true or false


if user_choice == computer_choice:
        print("It's tie!")
elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
        print("Oh! The computer won, that's ok!")
# adapted from solution shared by Will in Slack
