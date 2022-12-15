from tkinter import *
from tkinter import filedialog
from text_builder import TextBuilder
from typing_clocker import TypingClocker


def read_typing(key):
    global test_text, correct, current_time, running
    response = answer_entry.get("1.0", 'end-1c')
    res_length = len(response)
    truncated_text = test_text[:res_length]
    if test_text == response:
        running = False
        wpm = str(clock.calculate_wpm(builder.num_words))
        timer_label['text'] = current_time  + "\nWell done!\nWords Per Minute:    " + wpm
        timer_label['bg'] = FINISHED_COLOR
        timer_label['font'] = ("Arial", 20, "bold")
    elif truncated_text == response:
        correct = True
    else:
        correct = False


def get_test():
    global test_text, running
    running = True
    answer_entry.delete("1.0", "end")
    answer_entry.focus_set()
    test_text = builder.get_words()
    test_words["text"] = test_text
    clock.start_timer()


def end_test():
    global running
    if not running:
        window.destroy()
    else:
        running = False
        response = answer_entry.get("1.0", 'end-1c')
        res_length = len(response)
        words = res_length // 5
        wpm = str(clock.calculate_wpm(words))
        timer_label['text'] = current_time + "\nEnded Early\nWords Per Minute (Shortened):    " + wpm
        timer_label['bg'] = FINISHED_COLOR
        timer_label['font'] = ("Arial", 20, "bold")

def keep_time():
    global correct, current_time
    current_time = str(clock.count())
    if running:
        start_test_button['text'] = "Restart Test"
        end_test_button['text'] = "End Test"
        if correct:
            timer_label['text'] = current_time
            timer_label['bg'] = BACKGROUND_COLOR
            timer_label['font'] = ("Arial", 30, "bold")
        else:
            timer_label['text'] = current_time + "\nOops! You typed a wrong letter."
            timer_label['bg'] = INCORRECT_COLOR
            timer_label['font'] = ("Arial", 20, "bold")
    else:
        start_test_button['text'] = "Start Test"
        end_test_button['text'] = "Close Program"
    window.after(1000, keep_time)


clock = TypingClocker()
builder = TextBuilder()
test_text = None
correct = True
current_time = None
running = False
BACKGROUND_COLOR = "#263159"
FONT_COLOR = "#FFFBEB"
INCORRECT_COLOR = "#9C254D"
FINISHED_COLOR = "#68B984"

window = Tk()
window.title("Typing Speed Test")
window.config(pady=25, padx=50, bg=BACKGROUND_COLOR)

title_label = Label(text="Typing Speed Test", fg=FONT_COLOR, bg=BACKGROUND_COLOR, font=("Times New Roman", 40, "bold"))
title_label.grid(column=0, row=0, columnspan=2)


# TEST SECTION
timer_label = Label(window, text="Click the Start Test button to begin", fg=FONT_COLOR,
                    bg=BACKGROUND_COLOR, font=("Arial", 30, "bold"))
timer_label.grid(column=0, row=1, columnspan=2, pady=10, sticky=NSEW)

test_words = Label(window, text="", fg=FONT_COLOR, bg=BACKGROUND_COLOR,
                   wraplength=800, font=("Arial", 18))
test_words.grid(column=0, row=2, columnspan=3, pady=10, sticky=NSEW)


answer_entry = Text(window, wrap=WORD, width=80, height=10, font=100)
answer_entry.grid(column=0, row=3, columnspan=2, sticky=W)
answer_entry.bind("<KeyRelease>", read_typing)

# BUTTON
start_test_button = Button(window, text="Start Test", bg=FINISHED_COLOR, fg=FONT_COLOR, command=get_test, padx=5, pady=5, font=("Arial", 15, "bold"))
start_test_button.grid(column=0, row=4, pady=15, padx=50, sticky=E)

end_test_button = Button(window, text="End Test", bg=INCORRECT_COLOR, fg=FONT_COLOR, command=end_test, padx=5, pady=5, font=("Arial", 15, "bold"))
end_test_button.grid(column=1, row=4, pady=15, padx=50, sticky=W)

keep_time()

window.mainloop()
