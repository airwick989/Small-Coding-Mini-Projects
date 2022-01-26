import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {data.letter:data.code for (row, data) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word that you would like translated to phonetic code words: ").upper()

output = [nato_alphabet[letter] for letter in user_word]

print(f"\nThe phonetic code words for that word are: {output}")
