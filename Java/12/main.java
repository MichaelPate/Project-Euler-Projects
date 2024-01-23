public class main {
    public static void main(String args[]) {
        // Generate a triangle number and check its factors
        int triangleNumberIndex = 500;
        int numberOfFactors = 0;

        while (countFactors(generateTriangleSum(triangleNumberIndex)) < 500) {
            triangleNumberIndex++;
        }

        System.out.println(triangleNumberIndex);
        System.out.println(generateTriangleSum(triangleNumberIndex));
        System.out.println(countFactors(generateTriangleSum(triangleNumberIndex)));
    }

    private static int generateTriangleSum(int triangleNum) {
        int sum = 0;
        int i = 0;
        while (i <= triangleNum) {
            sum += i;
            i++;
        }
        return sum;
    }

    private static int countFactors(int num) {
        int factorCount = 0;
        for (int i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0 && i * i != num) {
                factorCount += 2;
            } else if (i * i == num) {
                factorCount++;
            }
        }

        return factorCount;
    }
}