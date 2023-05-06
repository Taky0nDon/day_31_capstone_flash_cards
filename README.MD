D A Y T H I R T Y O N E

# Overview

This is a tkinter GUI that loads a CSV file containing pairs of French words
and their English translation.

The cards flip from the French to english side after 3 seconds, but the timer
is reset every time the user marks a card known (check) or unknown (cross).

I added a couple of modifications to the way
the app behaves:
1. Instead of only removing cards that are marked known from
the deck and looping over it infinitely until they are all marked known, 
every card shown to the user is removed from the deck until the deck is empty.
2. A CSV file containing only the words that were marked unknown is saved every time the user marks a card.
3. When the deck is empty, the user is asked if they want to keep learning.

   a. If the user clicks "No", the program ends.
   
   b. If the user clicks "Yes", the program restarts with a new deck consisting only of the cards marked unknown.

# Potential Improvements
* I feel like this code is begging to be object oriented.
* Users could be allowed to create their own cards.
* Users could store multiple decks to choose from when the program starts.
* Code documentation could be improved (or made present)

# Lesson notes

## flash card program

* learn most frequently used words
* flips after 3 seconds
* green check for yes, red x for no
  * if checked, card is taken out of deck


* google sheets
  * =GOOGLETRANSLATE(CELL, FIRST_LANG, FINAL_LANG)

## STEP ONE: CREATE THE UI

* the `index` in pandas are called records
