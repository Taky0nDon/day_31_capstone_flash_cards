import json
import tkinter as tk
from tkinter import messagebox
import random as rnd
import pandas as pd
import pathlib as pl

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NAME_FONT = ("Ariel", 40, "italic")
BACK = "./images/card_back.png"
FRONT = "./images/card_front.png"
WORD_FONT = ("Ariel", 16, "bold")
WORD_POSITION = (400, 263)

CHECK = "./images/right.png"
CROSS = "./images/wrong.png"

data_file = pl.Path("./data/glossary_terms_cards.json")

if not data_file.exists():
    data_file = "./data/french_words_original.csv"

with open(data_file) as file:
    data = json.loads(file.read())
    current_deck = data
current_card = None
shown_cards = []
finished = None
another_round = True


def redeal_deck():
    global data_file, data, current_deck
    another_round = messagebox.askyesno(
        title="Deck complete!",
        message="Do you want to keep learning?"
        "Click 'Yes' to restart with the cards you still don't know.",
    )
    if another_round:
        # data_file = "./data/words_to_learn.csv"
        # data = pd.read_csv(data_file)
        # current_deck = data.to_dict(orient="records")
        show_front()
    else:
        save_new_json()
        quit()


def word_is_known():
    global current_card, current_deck, finished
    # Deck is empty?
    if len(current_deck) == 0 and len(shown_cards) == 0:
        new_canvas = tk.Canvas()
        new_canvas.create_text(600, 263, text="You know all the words!")
        finished = True
        redeal_deck()

    else:
        current_deck.remove(current_card)
        show_front()
    # save a new CSV of the words that are in word_pairs and not in known_words


def save_new_json():
    not_learned_cards = shown_cards + [card for card in current_deck]
    with open('not_learned.json', 'w') as output_file:
        json.dump(not_learned_cards, output_file)


def show_front():
    global current_card, current_deck
    # Deck is empty?
    if len(current_deck) < 1:
        canvas.itemconfig(word, text="All words tested", fill="black")
        redeal_deck()
    else:
        current_card = rnd.choice(current_deck)
        canvas.itemconfig(card_side, image=card_back)
        canvas.itemconfig(word, text=current_card["front"], fill="black")


def show_back():
    global current_card
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(word, text=current_card["back"], fill="white")


def dont_know():
    global current_card, finished
    if finished:
        pass
    current_deck.remove(current_card)
    if current_card not in shown_cards:
        shown_cards.append(current_card)
    show_front()


window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card App")
# IMAGES
card_front = tk.PhotoImage(file=FRONT)
card_back = tk.PhotoImage(file=BACK)
check = tk.PhotoImage(file=CHECK)
cross = tk.PhotoImage(file=CROSS)

# CANVAS
canvas = tk.Canvas(
    width=800, height=526, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR
)
card_side = canvas.create_image(400, 263, image=card_front)
word = canvas.create_text(WORD_POSITION, font=WORD_FONT)

# BUTTONS
check_button = tk.Button(
    image=check, borderwidth=0, highlightthickness=0, command=word_is_known
)
cross_button = tk.Button(
    image=cross, borderwidth=0, highlightthickness=0, command=dont_know
)

# GRID
canvas.grid(column=0, row=0, columnspan=2)
cross_button.grid(column=0, row=1, pady=50)
check_button.grid(column=1, row=1)

show_front()
window.mainloop()
