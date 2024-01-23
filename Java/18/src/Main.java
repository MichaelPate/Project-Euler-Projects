import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        long sum = 0;
        long rowSums = 0;
        int centerIndex = 0;
        try {
            Scanner scanner = new Scanner(new File("./input.txt"));
            while (scanner.hasNextLine()) {
                int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();


                // Try averaging each row
                int rowSum = 0;
                for (int i : numbers) {
                    rowSum += i;
                }
                rowSums += rowSum;
                System.out.println("Row Average: " + rowSum/numbers.length);


                int num1 = 0;
                int num2 = 0;

                // Try to get each

                try {
                    num1 = numbers[centerIndex];
                } catch(Exception e) {
                    num1 = 0;
                }

                try {
                    num2 = numbers[centerIndex+1];
                } catch(Exception e) {
                    num2 = 0;
                }


                // If num1 is highest, decrement centerIndex.
                // num2, dont change centerIndex.
                // num3, increment centerIndex.
                if (num1 >= num2) {
                    // Dont change centerIndex
                    sum += num1;
                    System.out.println("Number: " + num1 + "\tIndex: " + centerIndex);
                } else {
                    // Increment centerIndex
                    System.out.println("Number: " + num2 + "\tIndex: " + centerIndex);
                    centerIndex++;
                    sum += num2;
                }

            }
            System.out.println("Total Sum: " + (sum));
            System.out.println("Sum of Averages: " + rowSums);
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
