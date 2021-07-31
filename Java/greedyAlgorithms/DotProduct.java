import java.util.*;

public class DotProduct {
    private static long maxDotProduct(int[] a, int[] b) {
        long result = 0;

        if (a.length <= 1) {
            result = a[0] * b[0];
            return result;
        }

        ArrayList<Integer> aX = new ArrayList();
        ArrayList<Integer> bX = new ArrayList();

        for (int i = 0; i < a.length; i++) {
            aX.add(a[i]);
            bX.add(b[i]);
        }

        aX.sort(Collections.reverseOrder());
        bX.sort(Collections.reverseOrder());

        for (int j = 0; j < aX.size(); j++) {
            result += (aX.get(j) * bX.get(j));
        }

        return result;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();

//        int[] a = new int[n];
//        for (int i = 0; i < n; i++) {
//            a[i] = scanner.nextInt();
//        }
//        int[] b = new int[n];
//        for (int i = 0; i < n; i++) {
//            b[i] = scanner.nextInt();
//        }

//        int[] a = {23};
//        int[] b = {39};

        int[] a = {1, 3, -5};
        int[] b = {-2, 4, 1};

        System.out.println(maxDotProduct(a, b));
    }
}



