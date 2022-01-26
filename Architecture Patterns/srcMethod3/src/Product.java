package src;
public class Product {

    private String name;
    private long upcCode;
    private double price;

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", upcCode=" + upcCode +
                ", price=" + price +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public long getUpcCode() {
        return upcCode;
    }

    public void setUpcCode(int upcCode) {
        this.upcCode = upcCode;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public Product(String name, long upcCode, double price) {
        this.name = name;
        this.upcCode = upcCode;
        this.price = price;
    }
}
