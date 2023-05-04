import tkinter as tk
import random as rnd
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NAME_FONT = ("Ariel", 40, "italic")
BACK = "./images/card_back.png"
FRONT = "./images/card_front.png"
WORD_FONT = ("Ariel", 60, "bold")

CHECK = "./images/right.png"
CROSS = "./images/wrong.png"

#DATAFRAME
data = pd.read_csv("./data/french_words.csv")

# FRONT OF FLASH CARD
word_number = 0
known_words_index = []

window = tk.Tk()

# todo figure out how to add a word to list when check is cicked
def mark_known():
    pass


def show_front():
    index = rnd.randint(0,101)
    while index in known_words_index:
        index = rnd.randint(0, 101)
    canvas.create_image(400, 263, image=card_front)
    canvas.create_text((400, 150), text=data.columns[0], font=LANGUAGE_NAME_FONT)
    canvas.create_text((400, 263), text=data.French[index], font=WORD_FONT)
    window.after(3000, lambda: show_back(index))
    return index


def show_back(index):
    canvas.create_image(400, 263, image=card_back)
    canvas.create_text((400, 150), text=data.columns[1], font=LANGUAGE_NAME_FONT)
    canvas.create_text((400, 263), text=data.English[index], font=WORD_FONT)
    window.after(3000, show_front)


# WINDOW
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card App")

# IMAGES
card_front = tk.PhotoImage(file=FRONT)
card_back = tk.PhotoImage(file=BACK)
check = tk.PhotoImage(file=CHECK)
cross = tk.PhotoImage(file=CROSS)

# CANVAS
canvas=tk.Canvas(width=800, height=526, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
index = show_front()
print(show_front())


# BUTTONS
check_button = tk.Button(image=check, borderwidth=0, highlightthickness=0)
cross_button = tk.Button(image=cross, borderwidth=0, highlightthickness=0)

# GRID
canvas.grid(column=0, row=0, columnspan=2)
cross_button.grid(column=0, row=1, pady=50)
check_button.grid(column=1, row=1)


window.mainloop()
