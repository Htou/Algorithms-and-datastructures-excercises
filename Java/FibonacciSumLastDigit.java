import java.util.ArrayList;

public class FibonacciSumLastDigit {
    private static long getFibonacciSum(long n) {
        if (n <= 1)
            return n;

        ArrayList<Long> list = new ArrayList<Long>();

        list.add(0L);
        list.add(1L);

        long sum = 0L;

        for (int i = 2; i <= n; ++i) {
            list.add(list.get(i - 1) + list.get(i - 2));
        }

        System.out.println(list);

        for (int i = 0; i < list.size(); i++) {
            sum += list.get(i);
        }

        return sum % 10;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long n = scanner.nextLong();

        long n = 50;
        long s = getFibonacciSum(n);

        System.out.println(s);
    }
}

