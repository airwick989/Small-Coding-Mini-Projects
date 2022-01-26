package src;


public class TicketPrinter {
   
    public TicketPrinter() {
         
    }

    public void displayText(String text) { 
        System.out.println("Printing the Product");
        System.out.println(text);
    }

    public void notifyText(String text){//subscriber method, waits for nottification of product input and reacts to it
        System.out.print("Subscription Recived by Printer, ");
        System.out.println(text + " was order");
    }
}
