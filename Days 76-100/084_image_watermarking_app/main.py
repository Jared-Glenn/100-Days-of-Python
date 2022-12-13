import tkinter
from tkinter import *
from tkinter import filedialog
from watermarker import Watermarker


BACKGROUND_COLOR = "#ffedd8"

def upload_action(event=None):
    filename = filedialog.askopenfilename()
    image_entry.delete(0, END)
    image_entry.insert(0, filename)

def create_watermark():
    image = image_entry.get()
    save_name = new_file_entry.get()
    text = text_entry.get()

    color_dict = ["black", "gray", "white"]
    color = color_dict[color_entry.get()]

    x_pos = ["left", "middle", "right"]
    y_pos = ["top", "middle", "bottom"]
    x = x_pos[x_position.get()]
    y = y_pos[y_position.get()]

    font_size = int(font_size_entry.get())

    watermarker = Watermarker()
    watermarker.mark_image(image, save_name, text, color, x, y, font_size)

window = Tk()
window.title("Watermark Maker")
window.config(pady=25, padx=50, bg=BACKGROUND_COLOR)

title_label = Label(text="Watermark Generator", fg="#583101", bg=BACKGROUND_COLOR, font=("Times New Roman", 25, "bold"))
title_label.grid(column=0, row=0, columnspan=2)


# IMAGE SECTION
file_label = Label(text="Original Image File", bg=BACKGROUND_COLOR, font=("Ariel", 10))
file_label.grid(column=0, row=1, columnspan=2)

image_entry = Entry(width=60)
image_entry.grid(column=0, row=2, columnspan=2, sticky=W)

upload_button = Button(window, text="Select Image", command=upload_action)
upload_button.grid(column=2, row=2)


# SAVE SECTION
new_file_label = Label(text="New File Name", justify=LEFT, bg=BACKGROUND_COLOR, font=("Ariel", 10))
new_file_label.grid(column=0, row=3, sticky=W)

new_file_entry = Entry(width=25)
new_file_entry.grid(column=0, row=4, sticky=W)

text_label = Label(text="Watermark Text", justify=LEFT, bg=BACKGROUND_COLOR, font=("Ariel", 10), pady=5)
text_label.grid(column=1, row=3, sticky=W)

text_entry = Entry(width=25)
text_entry.grid(column=1, row=4, sticky=W)

font_size_label = Label(text="Font Size", justify=LEFT, bg=BACKGROUND_COLOR, font=("Ariel", 10), pady=5)
font_size_label.grid(column=2, row=3, sticky=W)

font_size_entry = Entry(width=25)
font_size_entry.grid(column=2, row=4, sticky=W)


# POSITION SECTION
position_label = Label(text="Position", justify=LEFT, fg="#583101", bg=BACKGROUND_COLOR, font=("Ariel", 10, "bold"), pady=5)
position_label.grid(column=0, row=5, sticky=W)

# x-position
x_position = IntVar()
x_left = Radiobutton(text="Left", justify=LEFT, value=0, bg=BACKGROUND_COLOR, variable=x_position)
x_mid = Radiobutton(text="Middle", justify=LEFT, value=1, bg=BACKGROUND_COLOR, variable=x_position)
x_right = Radiobutton(text="Right", justify=LEFT, value=2, bg=BACKGROUND_COLOR, variable=x_position)
x_left.grid(column=0, row=6, sticky=W)
x_mid.grid(column=0, row=7, sticky=W)
x_right.grid(column=0, row=8, sticky=W)

# y-position
y_position = IntVar()
y_top = Radiobutton(text="Top", justify=LEFT, value=0, bg=BACKGROUND_COLOR, variable=y_position)
y_mid = Radiobutton(text="Middle", justify=LEFT, value=1, bg=BACKGROUND_COLOR, variable=y_position)
y_bottom = Radiobutton(text="Bottom", justify=LEFT, value=2, bg=BACKGROUND_COLOR, variable=y_position)
y_top.grid(column=1, row=6, sticky=W)
y_mid.grid(column=1, row=7, sticky=W)
y_bottom.grid(column=1, row=8, sticky=W)


# COLOR
position_label = Label(text="Text Color", justify=LEFT, fg="#583101", bg=BACKGROUND_COLOR, font=("Ariel", 10, "bold"))
position_label.grid(column=2, row=5, sticky=W)

color_entry = IntVar()
black = Radiobutton(text="Black", justify=LEFT, value=0, bg=BACKGROUND_COLOR, variable=color_entry)
gray = Radiobutton(text="Gray", justify=LEFT, value=1, bg=BACKGROUND_COLOR, variable=color_entry)
white = Radiobutton(text="White", justify=LEFT, value=2, bg=BACKGROUND_COLOR, variable=color_entry)
black.grid(column=2, row=6, sticky=W)
gray.grid(column=2, row=7, sticky=W)
white.grid(column=2, row=8, sticky=W)

# CREATE BUTTON
create_button = Button(window, text="Create Watermarked Image", command=create_watermark, padx=5, pady=5)
create_button.grid(column=0, row=9, columnspan=3, pady=15)


window.mainloop()
































# from PIL import Image, ImageDraw, ImageFont
#
# im = Image.open("img/Squareroot.PNG")
# width, height = im.size
# draw = ImageDraw.Draw(im)
#
# # INPUTS
#
# text = "Testing"
#
# black_text = (0, 0, 0)
# white_text = (255, 255, 255)
# gray_text = (80, 80, 80)
#
#
#
# font = ImageFont.truetype('arial.ttf', 36)
# textwidth, textheight = draw.textsize(text, font)
#
# # Calculate the x, y coordinates of the text
# margin = 10
# left_x = margin
# right_x = width - textwidth - margin
# top_y = margin
# bottom_y = height - textheight - margin
# mid_x = (width/2) - (textwidth/2)
# mid_y = (height/2) - (textheight/2)
#
#
# # Draw watermark in the bottom right corner
# draw.text((mid_x, mid_y), text, black_text, font=font)
# rgb_im = im.convert('RGB')
#
# # Save watermarked image
# rgb_im.save('img/watermark.jpg')