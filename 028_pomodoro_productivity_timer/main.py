from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
count = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global count
    reps = 10
    count = 0
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), pady=15)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global count
    if reps >= 10:
        reps = 1
    elif reps == 9:
        canvas.itemconfig(timer_text, text="00:00")
        count = 0
        return
    if reps == 8:
        title_label.config(text="Break", fg=RED, font=(FONT_NAME, 45, "bold"), pady=15)
        count = LONG_BREAK_MIN * 60
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK, font=(FONT_NAME, 45, "bold"), pady=15)
        count = SHORT_BREAK_MIN * 60
    else:
        title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50, "bold"), pady=10)
        count = WORK_MIN * 60
    count_down()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down():
    global reps
    global count
    minutes = count // 60
    seconds = count % 60
    oh = ""
    if seconds < 10:
        oh = 0
    canvas.itemconfig(timer_text, text=f"{minutes}:{oh}{seconds}")
    if count >= 0:
        count -= 1
        window.after(1000, count_down)
    elif count < 0 and reps >= 10:
        canvas.itemconfig(timer_text, text="00:00")
    else:
        reps += 1
        if reps % 2 == 1:
            check_text = ""
            for _ in range(int(reps/2)):
                check_text += "✔"
            check.config(text=check_text)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"), pady=10)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), pady=23)
check.grid(column=1, row=3)




window.mainloop()

#fg = foreground
