import java.util.Arrays;

public class FindMaximumProduct2Integers {
    /*

Given an integer array, find the maximum product of two integers in it.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

Input : [1]
Output: NAß

Note: Each input can have multiple solutions. The output should match with either one of them.

*/

    public static void findMaximumPairwise(int[] list, int size) {
        if (size < 2) {
            return;
        }

        int max1 = list[0];
        int max2 = Integer.MIN_VALUE;

        int min1 = list[0];
        int min2 = Integer.MAX_VALUE;

        for (int i = 1; i < list.length; i++) {
            if (list[i] > max1) {
                max2 = max1;
                max1 = list[i];
            } else if (list[i] > max2) {
                max2 = list[i];
            }

            if (list[i] < min1) {
                min2 = min1;
                min1 = list[i];
            } else if (list[i] < min2) {
                min2 = list[i];
            }
        }


        if (max1 * max2 == min1 * min2) {
            System.out.println("Pair is " + max1 + " " + "and " + max2 + " or " + min1 + " and " + min2);
        } else if (max1 * max2 > min1 * min2) {
            System.out.println("Pair is " + max1 + " and " + max2);
        } else {
            System.out.println("Pair is " + min1 + " and " + min2);
        }


    }


    public static void main(String[] args) {
//        int[] list = {-10, -3, 5, 6, -2};
        int[] list = {-4, 3, 2, 7, -5};
        int size = list.length;

        findMaximumPairwise(list, size);
    }
}
