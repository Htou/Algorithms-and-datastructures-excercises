import java.util.ArrayList;
import java.util.Scanner;

public class Fibonacci {
  private static long calc_fib(int n) {
    if (n <= 1) {
      return n;
    }

    ArrayList<Long> list = new ArrayList();

    list.add(0L);
    list.add(1L);

    for (int i = 2; i <= n; i++) {
      list.add(list.get(i - 1) + list.get(i - 2));
    }

    System.out.println(list);
    return list.get(n);
  }

  public static void main(String args[]) {
//        Scanner in = new Scanner(System.in);
//        int n = in.nextInt();
    int n = 15;

    System.out.println(calc_fib(n));
  }
}
