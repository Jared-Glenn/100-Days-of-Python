from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pd.read_csv("data/words_to_learn.csv")
    language_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/top_1000_dutch_words.csv")
    language_data = data.to_dict(orient="records")
    pd.DataFrame(language_data).to_csv("data/words_to_learn.csv")


current_card = random.choice(language_data)
dutch_word = current_card["Dutch"]
print(language_data)


def learned_word():
    global language_data, current_card
    language_data.remove(current_card)
    pd.DataFrame(language_data).to_csv("data/words_to_learn.csv", index=False)
    new_card()


def new_card():
    global language_data, current_card, flip_timer
    window.after_cancel(flip_timer)
    card.itemconfig(card_direction, image=card_front)
    card.itemconfig(language, text="Dutch", fill="black")
    current_card = random.choice(language_data)
    dutch_word = current_card["Dutch"]
    card.itemconfig(word, text=dutch_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    card.itemconfig(card_direction, image=card_back)
    card.itemconfig(language, text="English", fill="white")
    english_word = current_card["English"]
    card.itemconfig(word, text=english_word, fill="white")

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) # Actual dimensions of the picture.
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_direction = card.create_image(400, 263, image=card_front) # Placement of the picture (from the center).
language = card.create_text(400, 150, text="Dutch", font=("Arial", 30, "italic"))
word = card.create_text(400, 258, text=dutch_word, font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

red_image = PhotoImage(file="images/wrong.png")
red_no = Button(text="Click me", image=red_image, highlightthickness=0, border=0, command=new_card)
red_no.grid(column=0, row=1)

green_image = PhotoImage(file="images/right.png")
green_yes = Button(text="Click me", image=green_image, highlightthickness=0, border=0, command=learned_word)
green_yes.grid(column=1, row=1)

window.mainloop()