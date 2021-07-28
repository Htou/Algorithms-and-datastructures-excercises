import java.util.*;
import java.io.*;

public class CarFueling {
    static int computeMinRefills(int dist, int tank, int[] stops) {

        int carStops = 0;
        int carTank  = tank;

        for (int stop: stops) {
            if (stop > tank) {
                carStops += 1;
                carTank += tank;
            }
        }

        if (carTank >=dist) {
            return carStops;
        } else if (carTank == tank && carTank >= dist) {
            return carStops;
        }

        return -1;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int dist = scanner.nextInt();
//        int tank = scanner.nextInt();
//        int n = scanner.nextInt();
//        int stops[] = new int[n];
//        for (int i = 0; i < n; i++) {
//            stops[i] = scanner.nextInt();
//        }

//        int dist = 950;
//        int tank = 400;
//        int[] stops = {200, 375, 550, 750};

//        int dist = 10;
//        int tank = 3;
//        int[] stops = {1, 2, 5, 9};

        int dist = 200;
        int tank = 250;
        int[] stops = {100, 150};


        System.out.println(computeMinRefills(dist, tank, stops));
    }
}
