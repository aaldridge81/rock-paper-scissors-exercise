# game.py

# importing random function

import random

# introduction to game
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking for user input


user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

# print(x)
print("You chose:", user_choice)


# can print many things in a string as long as they are seperated by commas
# print("you chose:",x,"another string",x)

# string concat:
# print("you chose:" + "other string here")

# string inerpolation / format string usage
# print(f"you chose: {x}")



# simulating a computer input

#computer_choice = "paper"


options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)



print(f"The computer chose: {computer_choice}")









# print("The computer chose: 'paper'")







exit()












# determining who won
print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")