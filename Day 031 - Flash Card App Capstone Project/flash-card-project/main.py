from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
DELAY_MS = 3000
seen_words = []
current_translation = None
after_id = None


# #----------------- Data Setup ----------------#
# data = pd.read_csv("data/french_words.csv")
# english_to_french_dict = data.to_dict(orient="records")

#------------------- Setup words -------------- #

try:
    df = pd.read_csv('words_to_learn.csv', header=None, names=['French', 'English'])
    if df.empty:
        raise IndexError
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    print("Using french_words.csv")

except IndexError:
    df = pd.read_csv("data/french_words.csv")
    print("Was empty file. ")


english_to_french_dict = df.to_dict(orient='records')

#--------------------- Random Word ------------ #
def random_word():
    global current_translation, after_id
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(word_text, fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    current_translation = random.choice(english_to_french_dict)
    if(len(english_to_french_dict) == len(seen_words)):
        seen_words.clear()
    while current_translation in seen_words:
        current_translation = random.choice(english_to_french_dict)
    french_word = current_translation["French"]
    canvas.itemconfig(word_text, text=french_word)
    # Cancel any previous flip delay and schedule a new one
    if after_id is not None:
        window.after_cancel(after_id)
    after_id = window.after(DELAY_MS, flip_card)
    seen_words.append(current_translation)

def flip_card():
    global current_translation
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(word_text, fill="white", text=current_translation["English"])
    canvas.itemconfig(language_text, text="English", fill="white")



#--------------- Save Progress ------------ #
def remove_word():
    english_to_french_dict.remove(current_translation)
    df = pd.DataFrame(english_to_french_dict)
    df.to_csv("words_to_learn.csv", index=False, header=False)
    random_word()

#-------------------- UI Setup ---------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Add text to the canvas
word_text = canvas.create_text(
    400, 263,
    text="Your Text Here",
    font=WORD_FONT,
    fill="black"
)

language_text = canvas.create_text(
    400, 150,
    text="French",
    font=LANGUAGE_FONT,
    fill="black"
)

random_word()


right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=remove_word)
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=random_word)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)




window.mainloop()