from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="MyPass Error", message="Please write a response in each field.")
        return

    is_okay = messagebox.askokcancel(title="MyPass", message=f"These are the details you entered: \nEmail: {email_input}\n"
                                                   f"Password: {password_input}\nIs this okay?")
    if is_okay:
        with open("data.txt", "a") as data:
            data.write(f"{website_input} | {email_input} | {password_input}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)

email_label = Label(text="Email/Username:", bg="white", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2, padx=5, pady=5)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "jared_glenn@yahoo.com")

password_label = Label(text="Password:", bg="white", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3, padx=5, pady=5)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky=W)
website_entry.focus()
password_button = Button(text="Generate Password", padx=3, command=random_password)
password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W, pady=5)


window.mainloop()

# columnspan = number of columns for the element to span.
