import java.util.*;

public class FibonacciHuge {

    private static long pisano(long m) {
        long previous = 0;
        long current = 1;
        long res = 0;

        for (int i = 0; i < m * m; i++) {
            long temporary = 0;
            temporary = current;
            current = (previous + current) % m;

            if (previous == 0 && current == 1) {
                res = i + 1;
            }

        }

        return res;
    }


    private static long getFibonacciHuge(long n, long m) {
        long pisanoPerdiod = pisano(m);

        n = n % pisanoPerdiod;
        long previous = 0;
        long current = 1;

        for(int i = 0; i < n - 1; i++) {
            long temporary = 0;
            temporary = current;
            current = (previous + current) % m;
            previous = temporary;
        }

        return current % m;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long n = scanner.nextLong();
//        long m = scanner.nextLong();
        long n = 115;
        long m = 1000;

        System.out.println(getFibonacciHuge(n, m));
    }

}