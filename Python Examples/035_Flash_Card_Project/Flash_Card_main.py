from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# ---------------------------- DATA SETUP ------------------------------- #
try:
    script_directory = os.path.dirname(__file__)
    csv_path = os.path.join(script_directory, "data/words_to_learn.csv")
    data = pandas.read_csv(csv_path)
except FileNotFoundError:
    script_directory = os.path.dirname(__file__)
    csv_path = os.path.join(script_directory, "data/german_words.csv")
    original_data = pandas.read_csv(csv_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- CARD SETUP ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["GERMAN"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['ENGLISH']}", fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    script_directory = os.path.dirname(__file__)
    csv_path = os.path.join(script_directory, "data/words_to_learn.csv")
    data.to_csv(csv_path, index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "images/card_front.png")
front_image = PhotoImage(file=image_path)
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "images/card_back.png")
back_image = PhotoImage(file=image_path)
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "images/wrong.png")
wrong_image = PhotoImage(file=image_path)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "images/right.png")
right_image = PhotoImage(file=image_path)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
