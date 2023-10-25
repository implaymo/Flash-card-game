from tkinter import *
from PIL import Image, ImageTk
BACKGROUND_COLOR = "#B1DDC6"

# Setup window
window = Tk()
window.title("Flash card game")

# Create back image
canvas = Canvas(width=800, height=800)
back_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 400, image=back_image)
canvas.grid(column=0, row=1)
# Create front image
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 400, image=front_image)
canvas.grid(column=0, row=1, ipadx=50, ipady=50)
# Create


window.mainloop()