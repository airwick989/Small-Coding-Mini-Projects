import java.util.ArrayList;
import java.util.List;
// import java.util.Scanner;

public class Main {
    // size fo the chess board
    final static int SIZE = 8;

    static long startTime = System.nanoTime();
    static long firstSolutionEndTime;
    static long firstSolutionTimeElapsed;
    static long allSolutionsEndTime;
    static long allSolutionsTimeElapsed;
    final static long nanoToMilli = 1000000;
    

    final static String QUEEN = "\uD83D\uDC51";
    final static String WHITE = "⬜";
    final static String BLACK = "⬛";

    // final static String QUEEN = "Q";
    // final static String WHITE = "0";
    // final static String BLACK = "0";

    // holds location of queenPlaceList on the board
    // index of this array represents row index of the queen placed
    // value at that index represents column index of the queen placed
    // ex. if a queen placed at 0,4 on a 8 by 8 board
    // queenPlaceList array would looks like queenPlaceList = [4]

    public static List<Integer> queenPlaceList = new ArrayList<>();

    // holds number of solution for size by size board
    public static int numOfSolutions = 0;


    public static void main(String[] args) {
        // Scanner scanner = new Scanner(System.in);
        // System.out.println("Enter the size of chess board: ");
        // size = scanner.nextInt();
        startTime = System.nanoTime();
        extracted();
        allSolutionsEndTime = System.nanoTime();
        firstSolutionTimeElapsed = (firstSolutionEndTime - startTime);
        allSolutionsTimeElapsed = (allSolutionsEndTime - startTime);
        System.out.println("Board size is " + SIZE);
        System.out.println("Time elapsed for first solution is " + ((double)firstSolutionTimeElapsed / nanoToMilli) + " ms");
        System.out.println("Time elapsed for entire solutions is " + ((double)allSolutionsTimeElapsed / nanoToMilli) + " ms");
    }

    private static void extracted() {
        findSolutions();
    }

    /**
     * Checks the given cell location in every direction if it is safe to place queen
     *
     * @param row   the row index of cell location
     * @param col   the column index of cell location
     * @return      true if it is valid to place queen in every direction such as horizontally, vertically, diagonally otherwise false
     */
    public static boolean isValid(int row, int col) {
        // loop through every queenPlaceList placed so far
        for (int r = 0; r < queenPlaceList.size(); r++) {
            int c = queenPlaceList.get(r);
            // check diagonally, horizontally and vertically
            if (Math.abs(r - row) == Math.abs(c - col) || r == row || c == col) {
                return false;
            }
        }
        return true;
    }

    /**
     * prints the board with relevant pieces
     */
    public static void printBoard() {
        System.out.println("Solution #" + numOfSolutions);
        for (int row = 0; row < SIZE ; row++) {
            for (int col = 0; col < SIZE; col++) {
                if (queenPlaceList.get(row) == col) {
                    System.out.print(QUEEN);
                } else {
                    System.out.print(WHITE);
                    // if (row % 2 == 0) {
                    //     if (col % 2 == 0) {
                    //         System.out.print(WHITE);
                    //     } else {
                    //         System.out.print(BLACK);
                    //     }
                    // } else {
                    //     if (col % 2 == 0) {
                    //         System.out.print(BLACK);
                    //     } else {
                    //         System.out.print(WHITE);
                    //     }
                    // }
                }
            }
            System.out.println();
        }
    }

    /**
     * Brute force every possible solution on the size by size board
     */
    public static void findSolutions() {
        // keep track of the solutions.
        numOfSolutions = 0;
        // initialize row index and column index
        int row = 0, col = 0;
        // set queenPlaceList to empty array
        queenPlaceList = new ArrayList<>();

        // infinite loop that only terminates if the backtrack is done and for every possible solution
        // !(col >= SIZE && row == 0)
        while (col < SIZE || row != 0) {

            // checks if the column is in boundary (SIZE) and if it is safe to place queen at cell location (row , col)
            while (col < SIZE && !(isValid(row, col))) {
                // if it is not safe and col is in boundary (SIZE) then increment column by 1
                col = col + 1;
            }

            // based on above while loop if safe cell location found then it would also be in boundary(SIZE)
            // and following if block will be executed
            if (col < SIZE) {
                // safe cell location found
                // add the column index to array of location of queenPlaceList
                queenPlaceList.add(col);

                // if the row index reached the boundary(SIZE)
                // that means column is also in boundary(SIZE)
                // then solution is found and backtrack starts by removing last queen
                // otherwise go the next row and first column
                // (!(row + 1 < SIZE && row + 1 != SIZE))
                if (row + 1 >= SIZE) {
                    numOfSolutions = numOfSolutions + 1;
                    if (numOfSolutions == 1) {
                        firstSolutionEndTime = System.nanoTime();
                    }
                    printBoard();
                    // remove the last queen from array of queenPlaceList
                    queenPlaceList.remove(queenPlaceList.size() - 1);
                    // this will allow to execute the next if block
                    col = SIZE;
                } else {
                    // go to next row first column
                    col = 0;
                    row = row + 1;
                }
            }

            // column index reached the boundary(SIZE)
            // there is no possible cell location in this row that we can place queen.
            if (col >= SIZE) {

                // if the backtrack finished going down row and coming up back to the first row and also placing correct queenPlaceList
                // terminate the solution, column reached the boundary and we are back on first row
                // if (row == 0) {
                //     allSolutionsEndTime = System.nanoTime();
                //     return; // no possible combination left
                // }

                // remove the last queen and try next column previous row
                col = queenPlaceList.remove(queenPlaceList.size() - 1) + 1;
                row = row - 1;
            }
        }
        
    }

}
