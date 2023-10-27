from tkinter import *
from PIL import Image, ImageTk


BACKGROUND_COLOR = "#B1DDC6"

# Setup window
window = Tk()
window.title("Flash card game")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

#----------- SETUP UI ------------#

# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
canvas.pack()

# Create Front card
front_image = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
canvas.create_image(400, 256, image=front_image)
canvas.pack()

# Create WRONG button
wrong_image = ImageTk.PhotoImage(Image.open("./images/wrong.png"))
canvas.create_image(200, 570, image=wrong_image)
canvas.pack(ipady=50)

# Create RIGHT button
right_button = ImageTk.PhotoImage(Image.open("./images/right.png"))
canvas.create_image(600, 570, image=right_button)
canvas.pack()

# Language
canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))


# Word
canvas.create_text(400, 263, text="WORD", fill="black", font=("Arial", 60, "bold"))


window.mainloop()
