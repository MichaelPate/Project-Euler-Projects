public class main {
    public static void main(String args[]) {
        long routeCount = 1;

        // must move down by 20, and right by 20, so find all combinations
        for (int i = 0; i < 20; i++) {
            routeCount *= 40-i;
            routeCount /= i+1;
        }

        System.out.println(routeCount);
    }
}