import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class FractionalKnapsack {
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double valueInKnapsack = 0;

        ArrayList<Float> ratioValues = new ArrayList();

        for (int i = 0; i < values.length; i++) {
            ratioValues.add((float) values[i] / weights[i]);
        }

        ratioValues.sort(Collections.reverseOrder());

        int j = 0;


        while (j < values.length) {
            if (capacity > 0) {
                for (int k = 0; k < values.length; k++) {
                    if (((float) values[k] / weights[k]) == ratioValues.get(j)) {
                        if ((capacity - weights[k]) < 0) {
                            valueInKnapsack += (float) ratioValues.get(j) * capacity;
                            capacity = 0;
                            break;

                        } else {
                            capacity -= weights[k];
                            valueInKnapsack += values[k];
                            break;
                        }
                    }
                }
                j += 1;

            } else {
                j += 1;
            }
        }

        return valueInKnapsack ;
    }

    public static void main(String args[]) {

//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        int capacity = scanner.nextInt();

        int n = 10000;
        int capacity = 50;

        int[] values = new int[n];
        int[] weights = new int[n];

        for (int i = 0; i < n; i++) {
            values[i] = ThreadLocalRandom.current().nextInt(1, 10000 + 1);
            weights[i] = ThreadLocalRandom.current().nextInt(1, 1000 + 1);
        }

        for (int i = 0; i < n; i++) {
            System.out.println(values[i] + " " + weights[i]);
        }

//        int[] values = { 40, 60, 100, 120 };
//        int[] weights = { 40, 10, 20, 30 };
//        int capacity = 50;
//        result = 240;


        System.out.println(getOptimalValue(capacity, values, weights));

    }
}

