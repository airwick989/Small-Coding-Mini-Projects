//****************************************************************************************************************
//  Card.java           Author: Ridwan Hossain (100747897)
//
//  Card class that creates Card objects and contains various methods pertaining to each Card
//****************************************************************************************************************

public class Card{

    private String suit;  //Suit of the card object
    private String rank;  //Rank of the card object

    public Card(String Suit, String Rank){  //Instantiates a Card object
        suit = Suit;    //Assigns suit based on parameter
        rank = Rank;    //Assigns suit based on parameter
    }

    public String toString(){   //Prints the rank and suit of a card
        return(rank + " of " + suit);
    }

    public void setSuit(String Suit){   //Can set the suit of a card
        suit = Suit;
    }

    public void setRank(String Rank){   //Can set the rank of a card
        rank = Rank;
    }

    public int getRankVal(){    //Returns the integer value of a card's rank

        int score = 0;

        if(rank.equalsIgnoreCase("Ace")){   //Ace = 1
            score += 1;
        }
        else if(rank.equalsIgnoreCase("2")){
            score += 2;
        }
        else if(rank.equalsIgnoreCase("3")){
            score += 3;
        }
        else if(rank.equalsIgnoreCase("4")){
            score += 4;
        }
        else if(rank.equalsIgnoreCase("5")){
            score += 5;
        }
        else if(rank.equalsIgnoreCase("6")){
            score += 6;
        }
        else if(rank.equalsIgnoreCase("7")){
            score += 7;
        }
        else if(rank.equalsIgnoreCase("8")){
            score += 8;
        }
        else if(rank.equalsIgnoreCase("9")){
            score += 9;
        }
        else{
            score += 10;    //Jack, Queen, and King ranks are given a value of 10
        }

        return score;
    }

    public String getSuit(){    //Returns the suit of a card
        return suit;
    }

}
