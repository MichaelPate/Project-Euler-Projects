import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

public class main {
  public static void main(String args[]) {
    // Get the file into 2D array input
    int lineNum = 0;
    int[][] input = new int[20][20];
    int[] products = new int[3200];
    try {
      Scanner fileScanner = new Scanner(new File("C:\\Users\\Michael\\Documents\\Java Euler\\Problem 11\\source.txt"));
      while (fileScanner.hasNextLine()) {
        int i = 0;
        for (String t : fileScanner.nextLine().split(" ")) {
          input[lineNum][i] = Integer.parseInt(t);
          i++;
        }
        lineNum++;
      }
      fileScanner.close();
    } catch (FileNotFoundException e) {
      System.out.println("File not Found");
    }

    // Iterate through each number, getting products
    int productNumber = 0;
    for (int r = 0; r < 20; r++) {
      for (int c = 0; c < 20; c++) {
        // Look at straight up
        try {
          int p = input[r][c];
          p *= input[r-1][c];
          p *= input[r-2][c];
          p *= input[r-3][c];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at straight down
        try {
          int p = input[r][c];
          p *= input[r+1][c];
          p *= input[r+2][c];
          p *= input[r+3][c];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at straight forward
        try {
          int p = input[r][c];
          p *= input[r][c+1];
          p *= input[r][c+2];
          p *= input[r][c+3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at straight backwards
        try {
          int p = input[r][c];
          p *= input[r][c-1];
          p *= input[r][c-2];
          p *= input[r][c-3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at back up
        try {
          int p = input[r][c];
          p *= input[r+1][c-1];
          p *= input[r+2][c-2];
          p *= input[r+3][c-3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at back down
        try {
          int p = input[r][c];
          p *= input[r-1][c-1];
          p *= input[r-2][c-2];
          p *= input[r-3][c-3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at forward up
        try {
          int p = input[r][c];
          p *= input[r+1][c+1];
          p *= input[r+2][c+2];
          p *= input[r+3][c+3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;

        // Look at forward down
        try {
          int p = input[r][c];
          p *= input[r-1][c+1];
          p *= input[r-2][c+2];
          p *= input[r-3][c+3];
          products[productNumber] = p;
        } catch (ArrayIndexOutOfBoundsException e) {
          products[productNumber] = 0;
        }
        productNumber++;
      }
    }

    // Find the highest product
    int maxP = 0;
    for (int p : products) {
      if (p > maxP) {
        System.out.println(p);
        maxP = p;
      }
    }
    System.out.println(maxP);
  }
}