# Rock-Paper-Scissors Game

#Choices function
#Win condition function
#Play function

import random

def get_choices():
    player_choice = input("Choose Rock or Paper or Scissor: ")
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])
    
    return [player_choice,computer_choice]            #Using lists 

def win_condition(player,opponent):
    if player=="Rock" and opponent=="Scissor" or player =="Paper" and opponent=="Rock" or player=="Scissor" and opponent=="Paper":
        return True

def play():
    choices = get_choices()
    print(choices)

    if choices[0]==choices[1]:
        return "It is a tie"

    if win_condition(choices[0], choices[1]):
        return "You win"
    return "you lost"

print(play())
