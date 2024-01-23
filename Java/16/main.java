// I ended up doing this project in python because I was having a stupid time
// summing numbers in Java

import java.text.DecimalFormat;
public class main {
    public static void main(String args[]) {
        double n = Math.pow(2, 1000);
        int s = 0;

        while (n >= 0) {
            s += (n % 10);
            n = Math.floor(n / 10);
        }

        System.out.println(s);
    }
}