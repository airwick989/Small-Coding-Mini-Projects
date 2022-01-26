package src;
import java.util.ArrayList;
import java.util.Random;

public class ProductDB {

    public final long START_UPC_CODE = 100000000000L;
    public final int SIZE = 10;
    private final ArrayList<Product> db;

    public ProductDB() {
        db = new ArrayList<Product>();
        for (int i = 0; i < SIZE; i++) {
            Random random = new Random();
            db.add(new Product(
                    "Product " + i,
                    START_UPC_CODE + i+1,
                    (i + 1) * random.nextInt(10)
            ));
        }
    }

    public ArrayList<Product> getDB(){
        return this.db;
    }

    public Product getProductInfo(long upcCode) {
        Product foundProduct = null;
        for (Product product: db) {
            if (upcCode == product.getUpcCode()) {
                foundProduct = product;
                break;
            }
        }
        return foundProduct;
    }
}
