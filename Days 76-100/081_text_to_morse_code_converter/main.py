from tkinter import *
from converter import Converter

converter = Converter()

################################ FUNCTIONALITY ##################################


def translate():
    text_input = text_entry.get()
    morse_response = converter.text_to_morse(text_input)

    canvas.itemconfig(morse_code, text=f"{text_input} \n {morse_response}")
    text_entry.delete(0, END)
    text_entry.focus()


###################################### UI #######################################


window = Tk()
window.title("Less is Morse")
window.config(width=300, height=200, bg="#2a9d8f", padx=50, pady=20)

title_label = Label(text="Less is Morse", fg="white", bg="#2a9d8f", font=("Times New Roman", 50, "bold"), pady=10)
title_label.config(anchor=CENTER)
title_label.grid(column=1, row=0)

canvas = Canvas(width=500, height=150, bg="#2a9d8f", highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=5)

text_label = Label(text="Original Text", bg="#2a9d8f", fg="white", font=("Courier", 12, "bold"))
text_label.grid(column=0, row=1, padx=5, pady=5)
text_entry = Entry(width=61)
text_entry.grid(column=1, row=1, sticky=W)
text_button = Button(text="Translate", padx=35, command=translate)
text_button.grid(column=2, row=1, sticky=W)
text_entry.focus()

morse_code = canvas.create_text(320, 40, text="Translation will appear here", fill="white",
                                font=("Courier", 15, "bold"), justify="center")
canvas.grid(column=0, row=2, columnspan=2)

window.mainloop()

