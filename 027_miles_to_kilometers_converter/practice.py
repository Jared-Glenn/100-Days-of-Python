from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label

my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry Component

input = Entry(width=10)
input.pack()
print(input.get())

# Text

text = Text(height=5, width=30)

text.insert(END, "Example of multi-line text entry.")
text.pack()

# Spinbox

spinbox = Spinbox(from_=0, to=10, width=5)
spinbox.pack()

# Scale

scale = Scale(from_=0, to=100)
scale.pack()


# Checkbox

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state)
checked_state.get()
checkbutton.pack()

# Radio Button

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()
