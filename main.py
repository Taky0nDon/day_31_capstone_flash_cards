import tkinter as tk
import random as rnd
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NAME_FONT = ("Ariel", 40, "italic")
BACK = "./images/card_back.png"
FRONT = "./images/card_front.png"
WORD_FONT = ("Ariel", 60, "bold")
WORD_POSITION = (400, 263)

CHECK = "./images/right.png"
CROSS = "./images/wrong.png"

#DATAFRAME
data = pd.read_csv("./data/french_words.csv")

# DATA DICTIONARY
current_deck = data.to_dict(orient="records")
# a list of dictionaries where each dict
# has two keys, "French" and "English"

# FRONT OF FLASH CARD
current_card = None
shown_words = []

window = tk.Tk()

# todo figure out how to add a word to list when check is cicked

def word_is_known():
    global current_card, current_deck
    if len(current_deck) == 0 and len(shown_words) == 0:
        new_canvas = tk.Canvas()
        new_canvas.create_text(600, 263, text="You know all the words!")
    else:
        current_deck.remove(current_card)
        show_front()
    # save a new CSV of the words that are in word_pairs and not in known_words

def save_new_csv():
    unknown_words = pd.DataFrame(shown_words)
    unknown_words.to_csv("./data/french_words.CSV")

def show_front():
    global current_card, timer, current_deck, i
    current_deck = [card for card in current_deck if card not in shown_words]
    window.after_cancel(timer)
    if len(current_deck) < 1:
        canvas.itemconfig(language, text="Done", fill="black")
        canvas.itemconfig(word, text="All words tested", fill="black")
        check_button.config(command= lambda: None)
        cross_button.config(command= lambda: None)
    else:
        current_card = rnd.choice(current_deck)
        canvas.itemconfig(card_side, image=card_back)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(word, text=current_card['French'], fill="black")
        timer = window.after(3000, show_back)
#
def show_back():
    global current_card
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")

def dont_know():
    global current_card
    current_deck.remove(current_card)
    shown_words.append(current_card)
    show_front()
# WINDOW
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card App")
timer = window.after(3000, show_back)

# IMAGES
card_front = tk.PhotoImage(file=FRONT)
card_back = tk.PhotoImage(file=BACK)
check = tk.PhotoImage(file=CHECK)
cross = tk.PhotoImage(file=CROSS)

# CANVAS
canvas=tk.Canvas(width=800, height=526, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
card_side = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text((400, 150), font=LANGUAGE_NAME_FONT)
word = canvas.create_text(WORD_POSITION, font=WORD_FONT)


# BUTTONS
check_button = tk.Button(image=check, borderwidth=0, highlightthickness=0, command=word_is_known)
cross_button = tk.Button(image=cross, borderwidth=0, highlightthickness=0, command=dont_know)

# GRID
canvas.grid(column=0, row=0, columnspan=2)
cross_button.grid(column=0, row=1, pady=50)
check_button.grid(column=1, row=1)

show_front()

window.mainloop()
save_new_csv()
