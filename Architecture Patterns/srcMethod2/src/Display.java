public class Display implements View{

    public Display() {

    }

    @Override
    public void displayProduct(Product product) {
        System.out.println("Displaying the Product's info on Display: " + product.toString());
    }
}
