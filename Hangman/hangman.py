#HANGMAN

import random
import hangman_library  #USED TO STORE ALL THE ART AND WORDS ON ANOTHER MODULE
from os import system   #USED TO CLEAR THE TERMINAL 



chosen_word = list(hangman_library.word_list[random.randint(0,len(hangman_library.word_list))])
current = []
used_letters = []
system('cls')       #USED TO CLEAR THE TERMINAL 

print(hangman_library.logo + "\n")
print("Welcome to Hangman!\n")
print(f"Psst, the word is {chosen_word}\n")

for i in chosen_word:
    current.append("_")

lives = 6

while lives > 0:

    if len(used_letters) >= 1:
        system('cls') 
        if used == True:
            system('cls')
            print("\nYOU HAVE ALREADY GUESSED THIS LETTER, TRY ANOTHER!!\n")
    
    print(f"{hangman_library.stages[lives]}\n")
    print(current)
    print("\n")

    if len(used_letters) >= 1:
        print(f"Letters already used: {used_letters}\n")

    guess = (input("Guess a letter in the word\n\n")).lower()
    used = False

    if len(used_letters) >= 1:
        used = False
        for i in range(0, len(used_letters)):
            if guess == used_letters[i]:
                used = True

    
    if guess in chosen_word and used == False:
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:
                current[i] = chosen_word[i]
    else:
        if used == False:
            lives -= 1

    if used == False:
        used_letters.append(guess)

    print("\n")

    if "_" not in current:
        break

print(f"{hangman_library.stages[lives]}\nThe word was {chosen_word}\n")

if lives == 0:
    print("You Lost :(")
else:
    print("You Won!")

    