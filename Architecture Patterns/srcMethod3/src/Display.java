package src;
public class Display {

    public Display() {

    }

    public void displayText(String text) { 
        System.out.println("Displaying the Product: ");
        System.out.println(text);
    }
    public void notifyText(String text){//subscriber method, waits for nottification of product input and reacts to it
        System.out.print("Subscription Recived by Display, ");
        System.out.println(text + " was order");
    }
}
