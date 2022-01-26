//****************************************************************************************************************
//  CardDriver.java           Author: Ridwan Hossain (100747897)
//
//  Driver program to utilize objects and methods from the Card class and the DeckofCards class
//****************************************************************************************************************

public class CardDriver {

    public static void main(String [] args) {

        DeckofCards deck1 = new DeckofCards();  //Creates a deck object which contains 52 card objects

        deck1.shuffle();    //Shuffles the cards in the deck
        deck1.DealaHand(52); //Deals every card in the deck and reads out each one
        deck1.HasthisMany();    //Shows that the whole deck has been dealt

        deck1.shuffle();    //Puts all cards back in the deck and shuffles it
        deck1.DealaHand(5); //Deals a hand of 5 cards
        deck1.HasthisMany();    //Shows the number of cards in your hand and in the deck
        deck1.handScore();  //Shows the score of your hand
        deck1.printSuitHist();  //Prints a histogram of the suits in your hand
        deck1.hasFlush();   //Says whether your hand has a flush or not

    }

}
