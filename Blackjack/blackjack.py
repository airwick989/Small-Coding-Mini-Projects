############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################# MY CODE ######################################

from os import system
import random
import blackjack_art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

again = True

while again:
    system('cls')
    print(blackjack_art.logo + "\n")
    print("Welcome to Blackjack!\n")

    dealer_cards = []
    your_cards = []

    dealer_score = 0
    current_score = 0

    for i in range(0, 4):
        
        card_added = cards[random.randint(0,len(cards)-1)]
        
        if i <=1:
            if card_added == 11 and dealer_score + card_added > 21:
                card_added = 1
            dealer_cards.append(card_added)
        else:
            if card_added == 11 and current_score + card_added > 21:
                card_added = 1
            your_cards.append(card_added)

        dealer_score = sum(dealer_cards)
        current_score = sum(your_cards)

    print(f"Your cards: {your_cards}, current score: {current_score} \nComputer's first card: {dealer_cards[0]} \n")

    another = True

    while another ==  True and current_score <= 21:
        check_another = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        while check_another != "y" and check_another != "n":
            check_another = (input("That is not a valid option. Please enter 'y' to get another card or 'n' to pass: ")).lower()
        
        if check_another == "n":
            another = False
        else:
            your_cards.append(cards[random.randint(0,len(cards)-1)])

        current_score = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {current_score} \nComputer's first card: {dealer_cards[0]} \n")

    if current_score > 21:
        system('cls')
        print(f"Your final hand: {your_cards}. final score: {current_score} \nComputer's final hand: {dealer_cards}, final score: {dealer_score}\n")
        print("You went bust! The computer wins!\n")
    else:
        while dealer_score <= 16:
            dealer_cards.append(random.randint(0,len(cards)-1))
            dealer_score = sum(dealer_cards)

        system('cls')
        print(f"Your final hand: {your_cards}. final score: {current_score} \nComputer's final hand: {dealer_cards}, final score: {dealer_score}\n")

        if dealer_score > 21:
            print("The computer went bust! You win!\n")
        elif dealer_score == 21 and current_score == 21:
            print("The computer got blackjack! They win! (Dealer has priority)\n")
        elif dealer_score == 21:
            print("The computer got blackjack! They win!\n")
        elif current_score == 21:
            print("You got blackjack! You win!")
        elif dealer_score == current_score:
            print("The game ended in a draw!\n")
        elif dealer_score > current_score:
            print("The computer is closer to 21! They win!\n")
        elif dealer_score < current_score:
            print("You are closer to 21! You win!\n")


    check_again = (input("Would you like to play another game of blackjack? Type 'y' for yes or 'n' for no: ")).lower()
    while check_again != "y" and check_again != "n":
        check_again = (input("That is not a valid option. Please enter 'y' to play again or 'n' to end: ")).lower()

    if check_again == "n":
        again = False
