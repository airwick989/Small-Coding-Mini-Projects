import java.util.Scanner;

public class MainApp {

    private  final Scanner sc;
    private  final Keyboard keyboard;
    private  final MyScanner scanner;
    private  final CashRegister cashRegister;
    private  final Display display;
    private final TicketPrinter ticketPrinter;

    public MainApp() {
        sc = new Scanner(System.in);
        display = new Display();
        ticketPrinter = new TicketPrinter();
        cashRegister = new CashRegister(display);
        keyboard = new Keyboard(cashRegister);
        scanner = new MyScanner(cashRegister);
    }

    public static void main(String[] args) {
        MainApp mainApp = new MainApp();
        mainApp.runApp();
    }

    public void runApp() {
        long proUpcCode;
        int inputChoice = 0;
        do {
            System.out.println("Choose input device: ");
            System.out.println("1 - Keyboard");
            System.out.println("2 - Scanner");
            System.out.println("3 - exit");
            inputChoice = sc.nextInt();
            if (inputChoice == 3) {
                System.exit(1);
            } else if (inputChoice == 1) {
                System.out.println("Enter product's upc code manually: ");
                proUpcCode = sc.nextLong();
                keyboard.setUpcCode(proUpcCode);
            } else if (inputChoice == 2) {
                scanner.scannedUPCCode();
            } else {
                System.out.println("Please Enter a Number between 1 and 3...");
                continue;
            }
            System.out.println("Choose how you would like to view the product info: ");
            System.out.println("1 - Display");
            System.out.println("2 - Ticket");
            inputChoice = sc.nextInt();
            if(inputChoice == 1) {
                cashRegister.setView(display);
            }
            else if (inputChoice == 2){
                cashRegister.setView(ticketPrinter);
            }
            else {
                System.out.println("Please Enter a Number between 1 and 2...");
                continue;
            }
            cashRegister.getCurrentProductInfo();
        } while (inputChoice != 0);

    }
}
