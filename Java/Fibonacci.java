import java.util.ArrayList;
import java.util.Scanner;

public class Fibonacci {
  private static long calc_fib(int n) {
    ArrayList<Long> list = new ArrayList();

    list.add(0L);
    list.add(1L);
      
    if (n <= 1) {
      return n;
    }

    for (int i = 1; i < n; i++) {

      list.add(list.get(i) + list.get(i - 1));
    }

    System.out.println(list);
    return list.get(n);
  }

  public static void main(String args[]) {
//        Scanner in = new Scanner(System.in);
//        int n = in.nextInt();
    int n = 50;

    System.out.println(calc_fib(n));
  }
}
