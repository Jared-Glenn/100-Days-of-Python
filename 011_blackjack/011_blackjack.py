from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  if input("Do you want to play a game of Blackjack? Enter 'y' or 'n': ").lower() == 'y':
    clear()
    running = True
    print(logo)
    
    player_hand = []
    computer_hand = []
    victory = None
  
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
  
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
  
  else:
    print("Thank you for playing!")
    return
  
  while running:
    print(player_hand)
    cur_score = sum(player_hand)
    comp_score = sum(computer_hand)
    print(f"Your cards: {player_hand}, current score: {cur_score}")
    print(f"Computer's first card: {computer_hand[0]}")
    if cur_score > 21:
      if 11 in player_hand:
        ind = player_hand.index(11)
        player_hand[ind] = 1
        continue
      victory = False
      running = False
    elif cur_score == 21:
      victory = True
      running = False
    else:
      if input("Type 'y' to get another card. Type 'n' to pass: ") == 'y':
        player_hand.append(random.choice(cards))
        if comp_score < 17:
          computer_hand.append(random.choice(cards))
      else:
        running = False
        if comp_score > 21:
          if 11 in computer_hand:
            ind - computer_hand.index(11)
            computer_hand[ind] = 1
            comp_score = sum(computer_hand)
            if cur_score > comp_score:
              victory = True
            elif cur_score < comp_score:
              victory = False
          else:
            victory = True
        if cur_score > comp_score:
          victory = True
        elif cur_score < comp_score:
          victory = False

  print(f"Your final hand: {player_hand}, current score: {cur_score}")
  print(f"Computer's final hand: {computer_hand}, computer's final score: {comp_score}")
  if victory == None:
    print("Draw")
  elif victory == True:
    print("You win!")
  elif victory == False:
    print("You lose.")

  blackjack()

blackjack()
