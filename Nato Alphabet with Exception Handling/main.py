import pandas


{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {data.letter:data.code for (row, data) in data.iterrows()}


def convert_input():

    user_word = input("Please enter a single word that you would like translated to phonetic code words: ").upper()

    #Handling a KeyError where the user has entered a character that is not in the dictionary, like a number for example
    try:
        output = [nato_alphabet[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only one word containing only letters in the english alphabet are accepted. \n")
        convert_input()
    else:
        print(f"\nThe phonetic code words for that word are: {output}")

convert_input()