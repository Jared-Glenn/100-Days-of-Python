from words import words
from random import choice


class TextBuilder:
    def __init__(self):
        self.words = words
        self.num_words = 0

    def get_words(self):
        self.num_words = 0
        text = ""
        while len(text) < 200:
            new_word = choice(self.words)
            if len(text) == 0:
                text += new_word
            else:
                text += " " + new_word

        self.num_words = (len(text) // 5)

        return text
