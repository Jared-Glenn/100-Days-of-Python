from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password():
    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    final_pass = [random.choice(letters) for _ in range(nr_letters)]\
                 + [random.choice(symbols) for _ in range(nr_symbols)]\
                 + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(final_pass)

    password = "".join(final_pass)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    if len(website_input) == 0 or len(email_input) == 0 or (password_input) == 0:
        messagebox.showerror(title="MyPass Error", message="Please write a response in each field.")
    else:
        try:
            with open("data.json", "r") as data:
                old_data = json.load(data)
                old_data.update(new_data)
            with open("data.json", "w") as data:
                json.dump(old_data, data, indent=4)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json","w") as data:
                json.dump(new_data, data, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ------------------------ SEARCH FUNCTION ---------------------------- #

def find_password():
    website_input = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                messagebox.showinfo(title="MyPass Results",
                                    message=f"Website: {website_input}\nPassword: {data[website_input]['password']}")
                pyperclip.copy(data[website_input]['password'])
            except KeyError:
                messagebox.showerror(title="MyPass Error", message="Website not in database yet.")
    except FileNotFoundError:
        messagebox.showerror(title="MyPass Error", message="No websites in database yet."
                                                           "\nPlease add a Website and Password.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass -- Password Manager")
window.config(padx=60, pady=50, bg="white")

logo = Canvas(width=200, height=200, bg="white", highlightthickness=0) # Actual dimensions of the picture.
lock_logo = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=lock_logo) # Placement of the picture (from the center).
logo.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1, padx=5, pady=5)
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, sticky=W)
website_button = Button(text="Search", padx=35, command=find_password)
website_button.grid(column=2, row=1, sticky=W)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2, padx=5, pady=5)
email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "jared_glenn@yahoo.com")

password_label = Label(text="Password:", bg="white", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3, padx=5, pady=5)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky=W)
password_button = Button(text="Generate Password", padx=3, command=random_password)
password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W, pady=5)


window.mainloop()

# columnspan = number of columns for the element to span.
