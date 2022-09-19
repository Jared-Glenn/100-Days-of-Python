import random

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

#Write your code below this line 👇

print("Welcome to Rock, Paper, Scissors! Let's play!")
player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

choice = [rock, paper, scissors]

comp_choice = random.randint(0,2)

print(choice[player_choice])
print("Computer chose:\n" + choice[comp_choice])

if player_choice == 0:
  if comp_choice == 0:
    print("It's a draw!")
  elif comp_choice == 1:
    print("You lose!")
  elif comp_choice == 2:
    print("You win!")

if player_choice == 1:
  if comp_choice == 0:
    print("You win!")
  elif comp_choice == 1:
    print("It's a draw!")
  elif comp_choice == 2:
    print("You lose!")

if player_choice == 2:
  if comp_choice == 0:
    print("You lose!")
  elif comp_choice == 1:
    print("You win!")
  elif comp_choice == 2:
    print("It's a draw!")