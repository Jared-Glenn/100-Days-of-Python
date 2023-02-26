from tkinter import *
from tkinter import filedialog


class Clock:
    def __init__(self):
        self.running = False
        self.counter = 0
        self.state = 0
        

    def restart_timer(self):
        self.counter = 0
        self.running = True
        

    def stop_timer(self):
        self.running = False
        

    def count(self):
        if self.running:
            if self.counter > 10:
                self.stop_timer()
            elif self.counter > 5:
                self.state += 1
            self.counter += 1
            window.after(1000, self.count())
            

clock = Clock()
BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"


window = Tk()
window.title('Disappearing Text Editor')
window.config(pady=10, padx=10, bg=BACKGROUND_COLOR)

text = 'Disappearing Text Editor ' +  str(clock.counter)

title_label = Label(text=text, fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Ariel", 20, "bold"))
title_label.grid(column=1, row=0, columnspan=2)


writing_area = Text(window, wrap=WORD, width=100, height=50, font=150, borderwidth=2)
writing_area.grid(column=0, row=1, columnspan=4, sticky=W)
writing_area.bind("<KeyRelease>", clock.restart_timer())

# THIS SEEMS TO BE THE PROBLEM, BUT WAS NOT AN ISSUE IN SIMILAR PROGRAMS
# INVESTIGATE FURTHER
# clock.count()

window.mainloop()