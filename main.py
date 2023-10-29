from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
words_list = []

# Opens CSV as a dataframe and gets it into a list of dictionaries
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')


def french_card():
    # Gets french word
    global flip_timer
    # Cancels timer so it waits 3 seconds everytime i click a butto n
    window.after_cancel(flip_timer)
    random_dict = random.choice(to_learn)
    canvas.itemconfig(text_word, fill="black", text=random_dict["French"])
    canvas.itemconfig(text_title, fill="black", text="French")
    canvas.itemconfig(canvas_image, image=front_image)
    words_list.append(random_dict)
    flip_timer= window.after(3000, english_card)

def english_card():
    # Changes words and background to English
    global words_list
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(text_title, fill="white", text="English")
    # Gets the english word inside of words_list
    canvas.itemconfig(text_word, fill="white", text=words_list[0]["English"])
    words_list = []



# Setup window
window = Tk()
window.title("Flash card game")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, english_card)

# Create canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
text_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
text_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# Create WRONG button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=french_card)
wrong_button.grid(column=0,row=1)


# Create RIGHT button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=french_card)
right_button.grid(column=1, row=1)

french_card()

window.mainloop()
