# RPS.py 
import random


def get_choices():
  player_choice = input("Enter a choice: (rock, paper, or scissors) " )
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}


  return choices


def check_win(player, computer):

  print(f"Player chose: {player}, the computer chose: {computer}") #new way
  if player == computer:
    return ("It's a tie!")

  elif player == "rock":
    if computer == "scissors":
      return ("rock beats scissors. You win! :)")
    else: 
      return ("paper beats rock. You lose. :(")

  elif player == "paper":
    if computer == "rock":
      return ("paper beats rock. You Win! :)")
    else:
      return "scissors beats paper. You lose. :("

  elif player == "scissors":
    if computer == "paper":
      return ("scissors beats paper. You win! :)")
    else:
      return ("rock beats scissors. You lose. :(")



choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)
