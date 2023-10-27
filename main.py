from tkinter import *
from PIL import Image, ImageTk
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
random_word = ""


def get_french_word():
    global random_word
    # Opens CSV as a dataframe and gets it into a list of dictionaries
    csv_dataframe = pandas.read_csv("data/french_words.csv")
    data_dict = csv_dataframe.to_dict('records')
    words_list = []
    # Gets each value of dictionary to words_list
    for dictionary in data_dict:
        words_list.append(dictionary["French"])
    canvas.delete("text")
    random_word = random.choice(words_list)

    # Word text
    canvas.create_text(400, 263, text=random_word, fill="black", font=("Arial", 60, "bold"), tags="text")
    # Language Type
    canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))


# Setup window
window = Tk()
window.title("Flash card game")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
# Create Front card
front_image = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Starting word
get_french_word()

# Create WRONG button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=get_french_word)
wrong_button.grid(column=0,row=1)


# Create RIGHT button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=get_french_word)
right_button.grid(column=1, row=1)



window.mainloop()
