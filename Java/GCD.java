import java.util.*;

public class GCD {
  private static long euclidGCD(long a, long b) {

    if ( b == 0) {
      return a;
    }

    return euclidGCD(b,a % b);
  }

  public static void main(String args[]) {
//    Scanner scanner = new Scanner(System.in);
//    int a = scanner.nextInt();
//    int b = scanner.nextInt();

    System.out.println(euclidGCD(235, 234436));
  }
}
