import java.sql.SQLOutput;
import java.util.Arrays;

class FindPairSum2 {
    //Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in A[] whose sum is exactly x.

    public static void main(String[] args) {
        int[] list = {8, 7, 2, 5, 3, 1};
//        int[] list = {5, 2, 6, 8, 1, 9};
        int target = 10;
//        int target = 12;

        Arrays.sort(list);

        int low = 0;
        int high = list.length - 1;

        while (low < high) {
            if (list[low] + list[high] == target) {
                System.out.println("Pair found (" + list[low] + ", " + list[high] + ")");
            }
            if (list[low] + list[high] < target) {
                low++;
            } else {
                high--;
            }
        }
        System.out.println("Pair not found");
    }
}