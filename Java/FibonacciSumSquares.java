import java.util.*;

public class FibonacciSumSquares {
    private static long getFibonacciSumSquares(long n) {
        if (n <= 1)
            return n;

        ArrayList<Long> list = new ArrayList<Long>();
        ArrayList<Long> sumOfSquares = new ArrayList<Long>();

        list.add(0L);
        list.add(1L);
        
        long sum = ((list.get(0) * list.get(0)) + (list.get(1) * list.get(1)));

        for (int i = 2; i <= n; ++i) {
            list.add(list.get(i - 1) + list.get(i - 2));
            sum += (list.get(i) * list.get(i));
            sumOfSquares.add(sum);
        }

        System.out.println(list);
        System.out.println(sumOfSquares);
        return sum % 10;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long n = scanner.nextLong();

        long n = 7;

        long s = getFibonacciSumSquares(n);
        System.out.println(s);
    }
}

