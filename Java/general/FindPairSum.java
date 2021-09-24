import java.util.ArrayList;

class FindPairSum {
    //Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in A[] whose sum is exactly x.

    public static void main(String[] args) {
        int[] list = {8, 7, 2, 5, 3, 1};
//        int[] list = {5, 2, 6, 8, 1, 9};
        int target = 10;
//        int target = 12;
        int pointer = 0;
        int diff = target - list[pointer];
        boolean found = false;

        while (pointer <= list.length - 1) {

            for (int i = pointer + 1; i < list.length; i++) {

                if (list[i] == diff) {
                    found = true;
                    System.out.println("Pair found" + " (" + list[pointer] + ", " + diff + ")");
                }
            }
            pointer++;
        }
        if (!found) {
            System.out.println("Pair not found");
        }
    }

}
