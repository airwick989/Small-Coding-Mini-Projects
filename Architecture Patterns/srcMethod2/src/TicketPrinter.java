public class TicketPrinter implements View{

    public TicketPrinter() {

    }

    @Override
    public void displayProduct(Product product) {
        System.out.println("Printing the Product's info onto Ticket: " + product.toString());
    }
}
