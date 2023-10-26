from tkinter import *
from PIL import Image, ImageTk


BACKGROUND_COLOR = "#B1DDC6"

# Setup window
window = Tk()
window.title("Flash card game")
window.configure(bg=BACKGROUND_COLOR)

#----------- SETUP UI ------------#
# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, ipadx=50, ipady=50, columnspan=2)

# Create Front card
front_image = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
front_label = Label(window, bg=BACKGROUND_COLOR, image=front_image)
front_label.grid(column=0, row=0, ipadx=50, ipady=50, columnspan=2, rowspan=2)

# Create WRONG button
wrong_image = ImageTk.PhotoImage(Image.open("./images/wrong.png"))
wrong_label = Label(window, bg=BACKGROUND_COLOR, image=wrong_image)
wrong_label.grid(column=0, row=1, ipadx=50, ipady=50, rowspan=2)

# Create RIGHT button
right_button = ImageTk.PhotoImage(Image.open("./images/right.png"))
right_label = Label(window, bg=BACKGROUND_COLOR, image=right_button)
right_label.grid(column=1, row=1, ipadx=50, ipady=50, rowspan=2)


window.mainloop()
