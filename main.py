from tkinter import *
from PIL import Image, ImageTk
BACKGROUND_COLOR = "#B1DDC6"

# Setup window
window = Tk()
window.title("Flash card game")

# Create canvas
canvas = Canvas(width=800, height=800, bg=BACKGROUND_COLOR)
canvas.grid(column=1, row=1)
# Create front image
front_image = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
front_label = Label(window, bg=BACKGROUND_COLOR, image=front_image)
front_label.grid(column=1, row=1, ipadx=50, ipady=50)




window.mainloop()