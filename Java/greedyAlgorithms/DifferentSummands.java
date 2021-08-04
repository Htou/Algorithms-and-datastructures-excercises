import java.util.*;

public class DifferentSummands {
    private static List<Integer> optimalSummands(int n) {
        List<Integer> summands = new ArrayList<Integer>();
        //write your code here
        int prizePool = n;
        if (prizePool - 3 > 2) {
            summands.add(1);
            summands.add(2);
            summands.add(prizePool - 3);
        } else if (prizePool - 2 > 2) {
            summands.add(2);
            summands.add(prizePool - 2);
        } else {
            summands.add(prizePool);
        }

        return summands;
    }
    
    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
        int n = 2;
        List<Integer> summands = optimalSummands(n);
        System.out.println(summands.size());
        for (Integer summand : summands) {
            System.out.print(summand + " ");
        }
    }
}

