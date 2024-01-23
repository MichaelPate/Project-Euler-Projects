import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

public class main {
    public static void main(String args[]) {
        double sum = 0;
        try {
            Scanner fileScanner = new Scanner(new File("C:\\Users\\Michael\\Documents\\Java Euler\\Problem 13\\input.txt"));
            while (fileScanner.hasNextLine()) {
                String t = fileScanner.nextLine();
                sum += Double.parseDouble(t);
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not Found");
        }
        System.out.println(sum);
    }
}