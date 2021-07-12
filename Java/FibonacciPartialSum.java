import java.util.*;

public class FibonacciPartialSum {
    private static long getFibonacciPartialSum(long from, long to) {

        ArrayList<Long> list = new ArrayList<Long>();

        list.add(0L);
        list.add(1L);

        long sum = 0L;

        for (int i = 2; i <= to; ++i) {
            list.add(list.get(i - 1) + list.get(i - 2));
        }



        for (long i = from; i < list.size(); i++) {
            sum += list.get((int) i);
        }

        System.out.println(list);
        return sum % 10;
    }
    
    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long from = scanner.nextLong();
//        long to = scanner.nextLong();

        long from = 10;
        long to = 10;

        System.out.println(getFibonacciPartialSum(from, to));
    }
}

