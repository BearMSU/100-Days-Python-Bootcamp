rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Generate random number between 0 and 2
import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed and invalid number. You lose!")
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0,2)
  print("Computer chose: ")
  print(game_images[computer_choice])

  # Compare choices and define logic of the game
  
  if computer_choice == 0 and user_choice == 2:
    print("You lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a tie! Try again!")
