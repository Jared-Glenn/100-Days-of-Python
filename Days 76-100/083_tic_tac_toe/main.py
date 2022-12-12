from art import logo, board
from winner import check_winner
from computer_brain import computer_brain
import random

px = []
po = []
game_board = board


def clean_board(good_board):
    for c in good_board:
        if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            good_board = good_board.replace(c, " ")
    return good_board


print(logo, "\n\n")
num_players = input("Welcome to Tic-Tac-Toe! How many players will there be? (1 or 2) ")
if num_players == "1":
    print("Great! You will be Player X and go first!")
else:
    print("Great! Player X will go first!")

print("You may select squares according to the key below:", board, "\n")
print("If you need to see the key again, just type 'key' at any time.")

running = True
available = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player = "O"

while running:
    winner = check_winner(px, po)
    if winner > 0:
        running = False
        print(clean_board(game_board), "\n")
        continue
    if not available:
        running = False
        continue

    if player == "X":
        player = "O"
    else:
        player = "X"

    print(clean_board(game_board))

    if num_players == "1" and player == "O":
        choice = computer_brain(px, po, available)
        print(f"Player O plays on space {choice}")
    else:
        choice = input(f"\n Player {player}, choose a square: ")
        while choice not in available:
            if choice == "key":
                print(game_board)
                choice = input("\n Player {player}, choose a square: ")
            else:
                print("Please choose an available square.", clean_board(game_board))
                choice = input("\n Player {player}, choose a square: ")

    if player == "X":
        px.append(choice)
        available.remove(choice)
        game_board = game_board.replace(choice, "X")
    else:
        po.append(choice)
        available.remove(choice)
        game_board = game_board.replace(choice, "O")

if winner == 1:
    print("Player X Wins! Congratulations!")
elif winner == 2:
    print("Player O Wins! Congratulations!")
else:
    print("It's a tie!")

print("Thank you for playing!")