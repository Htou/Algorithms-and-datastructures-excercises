import java.util.*;

public class FibonacciLastDigit {
    private static long getFibonacciLastDigit(int n) {
        if (n <= 1) {
            return n;
        }

        ArrayList<Long> list = new ArrayList();

        list.add(0L);
        list.add(1L);

        for (int i = 2; i <= n; ++i) {
            list.add(i, (list.get(i - 1) + list.get(i - 2)) % 10);
        }

        System.out.println(list);
        return list.get(n);
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        int c = getFibonacciLastDigit(n);

        int c = 91239;
        System.out.println(getFibonacciLastDigit(c));
    }
}

