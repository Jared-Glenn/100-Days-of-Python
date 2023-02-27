from tkinter import *
from tkinter import filedialog
from docx import Document


class Clock:
    def __init__(self):
        self.running = False
        self.counter = 0
        self.state = 0
        

    def restart_timer(self, key):
        self.counter = 0
        self.state = 0
        self.running = True
        writing_area['fg'] = "#000000"
        

    def stop_timer(self):
        self.running = False
        response = writing_area.get("1.0", 'end-1c')
        document = Document()
        document.add_heading(response)
        document.save('lost_and_found.docx')
        writing_area.delete("1.0", "end")
        writing_area.focus_set()
        writing_area['fg'] = "#000000"
        self.counter = 0
        self.state = 0
        

    def count(self):
        if self.running:
            if self.counter > 10:
                self.stop_timer()
            elif self.counter > 5:
                self.state += 1
            self.counter += 1
            
            
def keep_time():
    clock.count()
    if clock.state >= 5:
        title_label["text"] = "Let/'s start over!"
        writing_area['fg'] = "#CCCCCC"
        clock.stop_timer()
    elif clock.state == 4:
        title_label["text"] = 'Bye!'
        writing_area['fg'] = "#CCCCCC"
    elif clock.state == 3:
        title_label["text"] = 'Fading ....'
        writing_area['fg'] = "#999999"
    elif clock.state == 2:
        title_label["text"] = 'Fading ..'
        writing_area['fg'] = "#666666"
    elif clock.state == 1:
        title_label["text"] = "Uh oh! Don/'t stop!"
        writing_area['fg'] = "#333333"
    title_label["text"] = 'Keep Going!'
    window.after(1000, keep_time)


clock = Clock()
BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"


window = Tk()
window.title('Disappearing Text Editor')
window.config(pady=10, padx=10, bg=BACKGROUND_COLOR)

text = 'Disappearing Text Editor'

title_label = Label(text=text, fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Ariel", 20, "bold"))
title_label.grid(column=1, row=0, columnspan=2)


writing_area = Text(window, wrap=WORD, width=100, height=50, font=150, borderwidth=2)
writing_area.grid(column=0, row=1, columnspan=4, sticky=W)
writing_area.bind("<KeyRelease>", clock.restart_timer)

keep_time()

window.mainloop()