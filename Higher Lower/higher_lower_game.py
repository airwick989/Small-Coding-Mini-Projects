#HIGHER LOWER GAME

from os import system
import higher_lower_game_art
import higher_lower_game_data
import random





def initialise():

    data = higher_lower_game_data.data

    p1 = data[random.randint(0,len(data)-1)]
    data.remove(p1)
    p2 = data[random.randint(0,len(data)-1)]
    data.remove(p2)

    game(p1, p2, 0, data)




def compare(higher, lower):
    higher_num = higher['follower_count']
    lower_num = lower['follower_count']

    if higher_num > lower_num:
        return True
    else: 
        return False




def game(p1, p2, score, list):

    system('cls')
    print(higher_lower_game_art.logo + "\n")

    if score > 0:
        print(f"You're right! Current score: {score}. \n")
    
    print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}. \n" + higher_lower_game_art.vs + "\n")
    print(f"Against B: {p2['name']}, a {p2['description']}, from {p2['country']}. \n")

    choice = (input(f"Who has more followers? Type 'A' {p1['follower_count']} or 'B' {p2['follower_count']}: ")).lower()

    while choice != 'a' and choice != 'b':
        choice = (input(f"That is not a valid option. Type 'A' or 'B': ")).lower()
    
    if choice == 'a':
        again = compare(p1, p2)
        higher = p1
    else:
        again = compare(p2, p1)
        higher = p2
    
    if again == True:
        score += 1
        new = list[random.randint(0,len(list)-1)]
        list.remove(new)
        game(higher, new, score, list)
    else:
        system('cls')
        print(higher_lower_game_art.logo + "\n")
        print(f"Sorry, that's wrong. Final score: {score} \n")

        keep_playing = (input("Would you like to play again? Type 'y' for yes or 'n' for no: ")).lower()

        while keep_playing != 'y' and keep_playing != 'n':
            keep_playing = (input("That is not a valid option. Type 'y' for yes or 'n' for no: ")).lower()

        if keep_playing == 'y':
            initialise()




initialise()