from tkinter import *

def button_clicked():
    converted = round(float(input.get()) * 1.60934, 2)
    output.config(text=converted)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles = Label(text="  Miles ", font=("Arial", 12))
miles.grid(column=2, row=0)

equal = Label(text="is equal to  ", font=("Arial", 12))
equal.grid(column=0, row=1)

output = Label(text="0", font=("Arial", 12, "normal"))
output.grid(column=1, row=1)

kilometers = Label(text="  Km ", font=("Arial", 12))
kilometers.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# pack() - General Layout, top, left, etc.
# place() - Precise locations, x and y
# grid() - Breaks window into a grid you can place things on.


# # Label
#
# my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.config(padx=10, pady=20)
# my_label.grid(column=0, row=0)
#
# # Button
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="Click Me", command=button_clicked)
# new_button.grid(column=2, row=0)
#
# # Entry Component
#
# input = Entry(width=10)
# input.grid(column=3, row=2)





window.mainloop()
