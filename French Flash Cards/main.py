BACKGROUND_COLOR = "#B1DDC6"
TIMER_COLOUR = "#0084ff"
from tkinter import *
import pandas
from random import choice
import os

LANGUAGE_1 = "French"
LANGUAGE_2 = "English"
ALL_WORDS_PATH = "./data/french_words.csv"
WORDS_TO_LEARN_PATH = "./data/words_to_learn.csv"
TIMER_LENGTH = 5
total_right = 0
total_wrong = 0
picked_card = None
flipped_card = None
words_to_learn = []

timer = None #We have to initialise the timer variable to make the reset (stop()) function work
#We just set it to none so it has literally no value. We just want it to exist

# ---------------------------- IMPORT AND INITIALISE CSV DATA ------------------------------- #

try:
    data = pandas.read_csv(WORDS_TO_LEARN_PATH)
    words_list = data.to_dict(orient="records") 
except FileNotFoundError:
    data = pandas.read_csv(ALL_WORDS_PATH)
    words_list = data.to_dict(orient="records") #Orients the dictionary data in such a way that one column's row's data corresponds to the same row's data in the other columns
    #It essentially turns it into a list of dictionaries, where each index of the list is a row of data from the csv
    #print it out and view it alongside the csv file to see what I mean
    #print(words_dict)
    #print(type(words_list))

LANGUAGE_1 = "French"
LANGUAGE_2 = "English"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    global flipped_card

    if count >= 0:
        main_label.config(text= str(count))
        timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(card, image= card_2)
        canvas.itemconfig(lang_text, text= LANGUAGE_2)
        canvas.itemconfig(word_text, text= flipped_card)

# ---------------------------- CREATE A NEW CARD (AND MORE) ------------------------------- #

def new_card():
    global picked_card
    global flipped_card

    try:
        picked_card = choice(words_list)
        canvas.itemconfig(card, image= card_1)
        canvas.itemconfig(lang_text, text= LANGUAGE_1)
        canvas.itemconfig(word_text, text= picked_card[LANGUAGE_1])
        flipped_card = picked_card[LANGUAGE_2]
        words_list.remove(picked_card)
        count_down(TIMER_LENGTH)
    except IndexError:
        wrong_button["state"] = "disabled"  #You can use this to disbale buttons
        right_button["state"] = "disabled"
        canvas.itemconfig(card, image= card_2)
        canvas.itemconfig(lang_text, text= "Congratulations!")
        canvas.itemconfig(word_text, font= ("Arial", 30, "bold"), text= "You've went through all the cards!")
        
        #Basically, if theres words left to learn, its gonna save them for later
        #If there aren't any left to learn, it just deletes words_to_learn.csv so it defaults to the full list
        if len(words_to_learn) > 0:
            new_data = pandas.DataFrame(words_to_learn)
            new_data.to_csv(WORDS_TO_LEARN_PATH)
        else:
            #Delete words_to_learn.csv
            if os.path.exists(WORDS_TO_LEARN_PATH):
                os.remove(WORDS_TO_LEARN_PATH)

def right():
    global total_right
    
    total_right += 1
    right_label.config(text= f"Total Right: {total_right}")
   
    window.after_cancel(timer)  #This will cancel the timer using the after_cancel() method
    new_card()

def wrong():
    global total_wrong
    
    total_wrong += 1
    wrong_label.config(text= f"Total Wrong: {total_wrong}")
    words_to_learn.append(picked_card)
    
    window.after_cancel(timer)  #This will cancel the timer using the after_cancel() method
    new_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg= BACKGROUND_COLOR)

main_label = Label(text=str(TIMER_LENGTH), bg= BACKGROUND_COLOR, font = ("Arial", 30, "bold"), fg= TIMER_COLOUR)
main_label.grid(row = 0, column = 1)

wrong_label = Label(text="Total Wrong: 0", bg= BACKGROUND_COLOR, font = ("Arial", 20))
wrong_label.grid(row = 0, column = 0, sticky= W)

right_label = Label(text="Total Right: 0", bg= BACKGROUND_COLOR, font = ("Arial", 20))
right_label.grid(row = 0, column = 2, sticky= E)

canvas = Canvas(width= 800, height= 526, highlightthickness= 0, bg= BACKGROUND_COLOR)
card_1 = PhotoImage(file= "./images/card_front.png")
card_2 = PhotoImage(file= "./images/card_back.png")
card = canvas.create_image(400, 263, image= card_1)
lang_text = canvas.create_text(400, 150, text= LANGUAGE_1, font= ("Arial", 20, "italic"))
word_text = canvas.create_text(400, 263, text= "", font= ("Arial", 40, "bold"))
canvas.grid(row=1, column= 0, columnspan= 3)
new_card()

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness= 0, command= wrong)
wrong_button.grid(row=2, column= 0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image= right_image, highlightthickness= 0, command= right)
right_button.grid(row=2, column= 2)




window.mainloop()