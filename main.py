from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"


# Opens CSV as a dataframe and gets it into a list of dictionaries
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')


def next_card():
    random_french_word = random.choice(to_learn)
    canvas.itemconfig(text_word, text=random_french_word["French"])
    canvas.itemconfig(text_title, text="French")


# def flip_card():
#     if wrong_button or right_button and Word French
#         canvas.itemconfig(GET ENGLISH WORD)
#     if wrong_button or right_button and Word English
#         canvas.itemconfig(GET FRENCH WORD)

# Setup window
window = Tk()
window.title("Flash card game")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Create canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_image)
text_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
text_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# Create WRONG button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=1)


# Create RIGHT button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()
