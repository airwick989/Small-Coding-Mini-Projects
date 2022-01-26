import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Recursive {


    static int numberOfSolution = 0;
    static int SIZE = 8;
    public static List<int[]> queenPlaceList = new ArrayList<int[]>();

    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // System.out.print("Enter the size of the board: ");
        // SIZE = sc.nextInt();
        // sc.close();
        Main.startTime = System.nanoTime();
        solve(queenPlaceList, 0);
        Main.allSolutionsEndTime = System.nanoTime();
        Main.firstSolutionTimeElapsed = (Main.firstSolutionEndTime - Main.startTime);
        Main.allSolutionsTimeElapsed = (Main.allSolutionsEndTime - Main.startTime);
        System.out.println("Board size is " + SIZE);
        System.out.println("Time elapsed for first solution is " + ((double)Main.firstSolutionTimeElapsed/ Main.nanoToMilli) + " ms");
        System.out.println("Time elapsed for entire solutions is " + ((double)Main.allSolutionsTimeElapsed / Main.nanoToMilli) + " ms");
    }

    public static boolean isValid(int r, int c) {
        for (int[] cellLocation: queenPlaceList) {
            int row = cellLocation[0];
            int col = cellLocation[1];
            if (row == r || col == c || Math.abs(row - r) == Math.abs(col - c)) {
                return false;
            }
        }
        return true;
    }

    public static void printBoard() {
        int row = 0;
        int col = 0;
        while (row < SIZE) {

            boolean f = false;
            for (int[] queen: queenPlaceList) {
                int r = queen[0];
                int c = queen[1];
                if (row==r && col==c) {
                    f = true;
                    break;
                } else {
                    f = false;
                }
            }
            if (f) {
                System.out.print(Main.QUEEN);
            } else {
                System.out.print(Main.WHITE);
            }
            col++;
            if (col >= SIZE) {
                col = 0;
                row++;
                System.out.println();
            }

        }
    }

    public static boolean solve(List<int[]> queens, int row) {
        if (row == SIZE) {
            // print
            numberOfSolution++;
            if (numberOfSolution == 1) {
                Main.firstSolutionEndTime = System.nanoTime();
            }
            System.out.println("Solution #"+ numberOfSolution);
            printBoard();
            return true;
        }

        boolean check = false;
        for (int col = 0; col < SIZE; col++) {
            if (isValid(row, col)) {
                int[] loc = {row, col};
                queens.add(loc);

                check = solve(queens, row + 1) || check;

                queens.remove(loc);
            }
        }
        return check;
    }


}
