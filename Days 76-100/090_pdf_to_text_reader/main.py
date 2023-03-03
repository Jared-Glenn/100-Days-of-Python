import PyPDF2
import requests
from tkinter import *
from tkinter import filedialog
from security import API_KEY


api_key = API_KEY
text_str = ""


def get_text(location):
    reader = PyPDF2.PdfReader(location)

    length = (len(reader.pages))

    text_str = ""
    for page in range(length):
        new_page = reader.pages[page].extract_text()
        text_str += new_page
    
    return text_str


def get_voice(text):
    parameters = {
        "key": api_key,
        "hl": 'en-us',
        "src": text,
    }


    response = requests.get(url="http://api.voicerss.org", params=parameters)
    response.raise_for_status()

    with open('speech.mp3', 'wb') as file:
        file.write(response.content)


def upload_action(event=None):
    filename = filedialog.askopenfilename()
    pdf_entry.delete(0, END)
    pdf_entry.insert(0, filename)
    
    
def convert(event=None):
    location = pdf_entry.get()
    print(location)
    text = get_text(location)
    get_voice(text)


# ---------------------------------- TK INTER ----------------------------------------

BACKGROUND_COLOR = "#2a82e9"
TEXT_COLOR = "white"


window = Tk()
window.title('PDF Reader')
window.config(pady=10, padx=10, bg=BACKGROUND_COLOR)

title_label = Label(text='PDF Reader', fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Ariel", 20, "bold"))
title_label.grid(column=0, row=0, columnspan=3)

# PDF Upload
file_label = Label(text="PDF File", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Ariel", 10, "bold"))
file_label.grid(column=0, row=1)

pdf_entry = Entry(width=40)
pdf_entry.grid(column=1, row=1, sticky=W)

upload_button = Button(window, text="Select PDF", command=upload_action)
upload_button.grid(column=2, row=1, padx=5)

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(column=1, row=2)


window.mainloop()

