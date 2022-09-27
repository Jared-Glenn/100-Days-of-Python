from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the Secret Auction Program!")

bids = {}
running = True

while running:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))

  bids[name] = bid

  keep_going = input("Is there an additional bid? Yes or no? ").lower()

  if keep_going == "no" or keep_going == "n":
    running = False

  clear()

best_bid = 0
best_bidder = None

for key in bids:
  if bids[key] > best_bid:
    best_bid = bids[key]
    best_bidder = key

print(f"The winner of the auction is {best_bidder}, who bid ${best_bid}.")