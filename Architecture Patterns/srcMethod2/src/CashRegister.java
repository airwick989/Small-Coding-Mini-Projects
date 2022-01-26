import java.util.ArrayList;
import java.util.Scanner;

public class CashRegister {

    private final ProductDB productDb;
    private long currentUpcCode;
    private View view;
    private final Scanner sc;

    public CashRegister(View view) {
        productDb = new ProductDB();
        currentUpcCode = -1;
        this.view = view;
        sc = new Scanner(System.in);
    }

    public void setView(View view){
        this.view = view;
    }

    public void setCurrentProductUPC(long upcCode) {
        currentUpcCode = upcCode;
    }

    public long processScanner(){
        Product choice = null;
        int inputChoice = -1;
        ArrayList<Product> db = productDb.getDB();

        while(inputChoice == -1){
            System.out.println("Please select a product to scan:");
            int i = 0;
            for (Product product : db) {
                System.out.println(i + "- " + product.getName());
                i++;
            }
            inputChoice = sc.nextInt();
            if(inputChoice >= 0 && inputChoice <= 9){
                choice = db.get(inputChoice);
            }
            else {
                inputChoice = -1;
                System.out.println("Please Enter a Number between 1 and 10...");
                continue;
            }
        }

        long upc = choice.getUpcCode();

        return upc;
    }

    public void getCurrentProductInfo() {
        Product pro = null;
        if (currentUpcCode != -1) {
            pro = productDb.getProductInfo(currentUpcCode);
        }
        if (pro != null) {
            view.displayProduct(pro);
        } else {
            System.out.println("Product with given UPC Code " + currentUpcCode + " could not found in the ProductDB!");
        }
    }
}
