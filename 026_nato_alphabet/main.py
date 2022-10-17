import pandas

npa_df = pandas.read_csv("nato_phonetic_alphabet.csv")
npa_dict = {row.letter: row.code for (index, row) in npa_df.iterrows()}
running = True

while running:
    user_word = [letter.upper() for letter in input("What word do you want to convert?")]
    try:
        print([npa_dict[letter] for letter in user_word])
        running = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        continue
