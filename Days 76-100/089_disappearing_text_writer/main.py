from tkinter import *
from tkinter import filedialog


BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"

window = Tk()
window.title('Disappearing Text Editor')
window.config(pady=25, padx=50, bg=BACKGROUND_COLOR)


title_label = Label(text="Disappearing Text Editor", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Ariel", 30, "bold"))
title_label.grid(column=1, row=0, columnspan=2)

window.mainloop()