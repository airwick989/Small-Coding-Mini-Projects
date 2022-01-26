//****************************************************************************************************************
//  DeckofCards.java           Author: Ridwan Hossain (100747897)
//
//  Deck of cards class that creates a deck object and contains a list of cards pertaining to a deck, a hand, and
//  a subdeck if chosen. Furthermore, this class contains various methods pertaining to the deck, hand, subdeck,
//  and the cards contained within them
//****************************************************************************************************************

//Necessary libraries are imported
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class DeckofCards {

    private ArrayList<Card> deck;   //the deck is created as a list of Card objects
    private ArrayList<Card> hand;   //the hand is created as a list of Card objects
    private ArrayList<Card> subdeck;//the subdeck is created as a list of Card objects
    Random generator = new Random();//Produces a random number which will be useful for numerous methods


    public DeckofCards(){

        deck = new ArrayList<Card>();       //Instantiates the deck
        hand = new ArrayList<Card>();       //Instantiates the hand
        subdeck = new ArrayList<Card>();    //Instantiates the subdeck
        FillDeck(); //Fills the deck with with cards on instantiation

    }

    public void FillDeck(){ //Fills the deck with cards, in order

        String[] suitArray = {"Spades", "Hearts", "Diamonds", "Clubs"}; //An array of suits
        String[] rankArray = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}; //An array of ranks

        for(int i = 0; i < suitArray.length; i++){  //Assign a suit and rank to each card then adds it to the deck

            for(int x = 0; x < rankArray.length; x++){

                Card current = new Card(suitArray[i], rankArray[x]);
                deck.add(current);

            }

        }
    }

    public void shuffle(){  //Puts all cards in the deck and shuffles it

        Refresh();  //Puts all in the deck
        Collections.shuffle(deck);  //Shuffles the cards in the deck
        System.out.println("---------------The deck has also been shuffled--------------- \n");

    }

    public void Refresh(){  //Puts all cards back into the deck, in order, and removes all cards from your hand

        deck.removeAll(deck);   //empties deck
        FillDeck(); //refills deck in order
        hand.removeAll(hand);   //removes all cards from your hand
        System.out.println("---------------All cards have been put in the deck--------------- \n");

    }

    public void DealaCard(){    //Deals a single card to your hand

        int pick = generator.nextInt(deck.size());  //picks a random card from the deck
        hand.add(deck.get(pick));   //adds the random card to your hand
        System.out.println("The " + deck.get(pick) + " has been added to your hand \n"); //Prints the dealt card

        deck.remove(pick);  //removes the random card from the deck

    }

    public void DealaHand(int n){   //Deals a number of cards to your hand based on a parameter

        for(int i = 0; i < n; i++){ //Deals a card 'n' times
            DealaCard();
        }

    }

    public void handScore(){    //Prints the current score of your hand

        int score = 0;

        for(int i = 0; i < hand.size(); i++){   //checks every card in your hand

            Card current = hand.get(i);
            score += current.getRankVal();  //Gets the value of each card and adds it to a total

        }

        System.out.println("The score of your current hand is " + score);

    }

    int spades, hearts, dims, clubs;    //initializes counter variables for following method

    public void getHandSuits(){ //Counts the number of each suit in your hand

        //initializes counters to 0
        spades = 0;
        hearts = 0;
        dims = 0;
        clubs = 0;

        for(int i = 0; i < hand.size(); i++){   //Checks every card in your hand

            Card current = hand.get(i);

            //Adds 1 to the counter of the corresponding suit of the curent card
            if(current.getSuit().equalsIgnoreCase("Spades")){
                spades += 1;
            }
            else if(current.getSuit().equalsIgnoreCase("Hearts")){
                hearts += 1;
            }
            else if(current.getSuit().equalsIgnoreCase("Diamonds")){
                dims += 1;
            }
            else if(current.getSuit().equalsIgnoreCase("Clubs")){
                clubs += 1;
            }

        }

    }

    public void printSuitHist(){    //Prints a histogram of the suits in your hand

        getHandSuits(); //Counts the number of each suit in your hand

        System.out.println("In your hand, there are/is " + spades + " Spade(s), " + hearts + " Heart(s), " + dims +
                " Diamond(s), and " + clubs + " Club(s) \n");   //Outputs results

    }

    public void hasFlush(){ //Checks whether your hand has a flush or not

        getHandSuits(); //Counts the number of each suit in your hand

        //Checks if there is at least 5 of any suit in your hand and outputs result
        if(spades >= 5 || hearts >=5 || dims >=5 || clubs >= 5){
            System.out.println("Your hand has a flush (at least 5 cards of the same suit) \n");
        }
        else{
            System.out.println("Your hand does not have a flush (at least 5 cards of the same suit) \n");
        }

    }

    public void HasthisMany(){  //Prints the number of card in the deck and in your hand

        System.out.println("There are " + deck.size() + " card(s) in the deck");
        System.out.println("There are " + hand.size() + " card(s) in your hand \n");

    }

///////////////////////////////----Subdeck code below---////////////////////////////////////////////////////////////////

    public void subDeck(int n){ //fills the subdeck with 'n' cards containing no suit or rank

        for(int i = 0; i < n; i++){ //fills subdeck with 'n' empty cards
            subdeck.add(new Card("",""));
        }
        System.out.println("A subdeck of " + n + " cards with no suit or rank values has been created \n");

    }

    public void subDeckSet(int n, String Suit, String Rank){    //Sets the suit and rank of the 'nth' card in the subdeck

        Card holder = subdeck.get(n);   //A placeholder Card object which will be given the suit and rank desired
        holder.setSuit(Suit);   //Sets the suit of the placeholder Card object
        holder.setRank(Rank);   //Sets the rank of the placeholder Card object
        subdeck.set(n, holder); //Sets the 'nth' card in the subdeck to be equal to the placeholder Card object
        System.out.println("The card in position " + n + "(0 - " + (subdeck.size()-1) +
                ") of the subdeck has been set to a " + subdeck.get(n));

    }
}
