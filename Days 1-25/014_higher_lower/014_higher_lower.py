from art import logo, vs
import random
from game_data import data
#from replit import clear

def next_comp(a):
  print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
  print(vs)
  b = random.choice(data)
  print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")
  
  return b

a = random.choice(data)
running = True
correct = None
score = 0

while running:
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  b = next_comp(a)
  if a['follower_count'] == b['follower_count']:
      while a['follower_count'] == b['follower_count']:
        #clear()
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        b = next_comp(a)
  elif a['follower_count'] > b['follower_count']:
    correct = "a"
  else:
    correct = "b"
  if input("Who has more followers? Type 'A' or 'B': ").lower() == correct:
    score += 1
  else:
    running = False

  a = b
  #clear()

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")