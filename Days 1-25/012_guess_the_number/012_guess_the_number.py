from art import logo
import random

print(logo)

print("Welcome to Guess the Number!")
if input("Choose either easy or hard: ").lower() == "hard":
  guesses = 5
else:
  guesses = 10

running = True
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(f"You have {guesses} guesses to find the right number.")

guessed = set()

while running:
  guess = int(input("Guess a number: "))

  if guesses <= 0:
    print(f"You ran out of guesses. The number was {number}. You lose.")
    running = False
    continue
  if guess in guessed:
    print(f"You've already guessed {guess}. Try another number.")
  elif guess  == number:
    print(f"You got it! The number was {guess}!")
    running = False
    continue
  elif guess > number:
    print("Too high!")
    guesses  -= 1
  elif guess < number:
    print("Too low!")
    guesses -= 1
  
  guessed.add(guess)
  print(f"You have {guesses} guesses left!")

print("Thank you for playing!")