import random
import 007b_hangman_words
import 007c_hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = 007c_hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesses = set()

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
      print(f"You've already guessed {guess}.")
      continue

    guesses.add(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(007b_hangman_art.stages[lives])