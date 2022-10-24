from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import requests
from datetime import datetime
import security

# Old background #5f0f40 and select #9a031e

BACKGROUND_COLOR = "#6a4c93"
SELECT_COLOR = "#5a189a"
USERNAME = security.USERNAME
TOKEN = security.TOKEN

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


headers = {
    "X-USER-TOKEN": TOKEN
}


def new_pixel():
    chosen_date = DateEntry(window, locale="en_US").get_date()
    date = f"{chosen_date.year}{chosen_date.month}{chosen_date.day}"
    quantity = minutes_entry.get()

    graph1_config = {
        "date": date,
        "quantity": quantity,
    }

    isSuccess = False
    print(quantity, date, graph1_config)

    while not isSuccess:
        response = requests.post(url=graph_endpoint, json=graph1_config, headers=headers)
        response_son = response.json()
        if response_son["isSuccess"] == True:
            isSuccess = True
            print("Pixel Logged")



window = Tk()
window.title("> Labbits <")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

title = Canvas(width=170, height=120, bg=BACKGROUND_COLOR, highlightthickness=0)
app_logo = Image.open("images/test_tubes.png")
resize_image = app_logo.resize((30, 100))
app_logo = ImageTk.PhotoImage(resize_image)
title.create_image(85, 50, image=app_logo)
title.create_text(85, 50, text=">Labbits<", fill="white", font=("Times", 25, "bold"))
title.grid(column=0, row=0, columnspan=2)

now = datetime.now()
calendar = Calendar(window, selectmode="day", year=now.year, month=now.month, day=now.day, background=BACKGROUND_COLOR,
                    foreground="white", bordercolor="black", borderwidth=2, selectbackground=SELECT_COLOR)
calendar.grid(column=0, row=1, columnspan=2)

minutes_label = Label(text="How many minutes did you code today?", bg=BACKGROUND_COLOR, fg="white",
                      font=("Times", 20, "normal"), pady=10)
minutes_label.grid(column=0, row=2, columnspan=2)
minutes_entry = Entry(width=50, justify=CENTER)
minutes_entry.grid(column=0, row=3, columnspan=2)
input_pixel = Button(text=">Labbit!<", padx=100, command=new_pixel, font=("Times", 10, "bold"))
input_pixel.grid(column=0, row=4, columnspan=2, pady=10)




window.mainloop()