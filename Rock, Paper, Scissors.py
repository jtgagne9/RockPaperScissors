# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:27:28 2022

@author: Jackson
Description: A game of rock, paper, scissors
Inspired by the random walk game from Datacamp "Intermediate Python" course 
and video by Avery Smith on YouTube
"""
import numpy as np
player_choice = input('Rock, Paper, or Scissors? ')
win_message = "You won!"
loss_message = "You lost!"
tie_message = "It's a tie."
print("--------------------------")
print("You chose " + player_choice)
computer_choice = np.random.randint(1,4)
if computer_choice == 1:
   print("The computer chose Rock")
elif computer_choice == 2:
    print("The computer chose Paper")
else:
    print("The computer chose Scissors")
print("---------------------------------")
if (computer_choice == 1) & (player_choice == "Rock"):
    print(tie_message)
elif (computer_choice == 1) & (player_choice == "Paper"):
    print(win_message)
elif (computer_choice == 1) & (player_choice == "Scissors"):
    print(loss_message)
elif (computer_choice == 2) & (player_choice == "Rock"):
    print(loss_message)
elif (computer_choice == 2) & (player_choice == "Paper"):
    print(tie_message)
elif (computer_choice == 2) & (player_choice == "Scissors"):
    print(win_message)
elif (computer_choice == 3) & (player_choice == "Rock"):
    print(win_message)
elif (computer_choice == 3) & (player_choice == "Paper"):
    print(loss_message)
elif (computer_choice == 3) & (player_choice == "Scissors"):
    print(tie_message)      
else:
    print("Some sort of error. Try again.")