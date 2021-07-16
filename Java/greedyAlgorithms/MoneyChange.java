import java.util.Scanner;

public class MoneyChange {
    private static int getChange(int cashToChange) {
        int coin1 = 1;
        int coin5 = 5;
        int coin10 = 10;

        int totalCoins = 0;
        int totalCashLeft = cashToChange;

        while (totalCashLeft > 0) {
            if (totalCashLeft - coin10 >= 0) {
                totalCoins += 1;
                totalCashLeft -= coin10;

                System.out.println("giving you a 10coin");
                System.out.println("total coins:" + totalCoins);
                System.out.println("total cash left " + totalCashLeft);

            } else if (totalCashLeft - coin5 >= 0) {
                totalCoins += 1;
                totalCashLeft -= coin5;

                System.out.println("giving you a 5coin");
                System.out.println("total coins: " + totalCoins);
                System.out.println("total cash left " + totalCashLeft);

            } else if (totalCashLeft - coin1 >= 0) {
                totalCoins += 1;
                totalCashLeft -= 1;

                System.out.println("giving you a 1coin");
                System.out.println("total coins: " + totalCoins);
                System.out.println("total cash left: " + totalCashLeft);
            }
        }

                return totalCoins;
        }

        public static void main (String[]args){
//            Scanner scanner = new Scanner(System.in);
//            int m = scanner.nextInt();

            int cashToChange = 28;

            System.out.println("you have " + getChange(cashToChange) + " coins worth of " + cashToChange);

        }
    }
